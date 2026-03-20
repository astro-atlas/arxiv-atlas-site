"""Patch Astro .astro pages to replace internal <a href="/..."> links to papers/concepts with <WikiLink> component.
This is conservative: it only replaces absolute internal links starting with /papers/ or /concepts/ and adds the import frontmatter.
Run from project root: PYTHONPATH=projects/arxiv-atlas python3 projects/arxiv-atlas/tools/patch_astro_links.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES_DIR = ROOT / 'src' / 'pages'
IMPORT_SHALLOW = "import WikiLink from '../components/WikiLink.astro';\n"
IMPORT_DEEP = "import WikiLink from '../../components/WikiLink.astro';\n"

LINK_PATTERN = re.compile(r'<a\s+([^>]*?)href=("|\')(?P<href>/(?:papers|concepts|pages)/[^"\']+)("|\')(.*?)>(?P<label>.*?)</a>', re.IGNORECASE|re.DOTALL)


def ensure_frontmatter(text, depth):
    imp = IMPORT_DEEP if depth >= 2 else IMPORT_SHALLOW
    if text.lstrip().startswith('---'):
        # insert import into the frontmatter block (after the first '---' block start)
        parts = text.split('---', 2)
        # parts[0] is before first ---, parts[1] = frontmatter content, parts[2] = rest
        if len(parts) >= 3:
            front = parts[1]
            rest = parts[2]
            if "import WikiLink" in front:
                return text
            new_front = front + '\n' + imp
            return '---' + new_front + '---' + rest
    else:
        # create frontmatter
        return '---\n' + imp + '---\n' + text
    return text


def replace_links(text):
    def repl(m):
        href = m.group('href')
        label = m.group('label').strip()
        # Skip links with nested HTML (spans, divs, etc.) — WikiLink text is plain string
        if '<' in label:
            return m.group(0)
        slug = href.lstrip('/').rstrip('/')
        # Escape double quotes in label
        label = label.replace('"', '\\"')
        return f'<WikiLink slug="{slug}" text="{label}" />'
    return LINK_PATTERN.sub(repl, text)


def process_file(p: Path):
    text = p.read_text()
    new_text = replace_links(text)
    if new_text != text:
        # Compute depth: how many dirs deep from PAGES_DIR
        rel = p.relative_to(PAGES_DIR)
        depth = len(rel.parts) - 1  # e.g. pages/Foo.astro = depth 1, concepts/bar.astro = depth 1
        new_text = ensure_frontmatter(new_text, depth)
        p.write_text(new_text)
        print('Patched', p)


def main():
    for f in PAGES_DIR.rglob('*.astro'):
        process_file(f)
    print('Done')

if __name__ == '__main__':
    main()
