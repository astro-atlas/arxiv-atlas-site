#!/usr/bin/env python3
"""
Bulk-convert .astro pages in src/pages/pages/ to .mdx in src/content/pages/.

For each .astro file (except _template.astro and [slug].astro):
1. Extract the title from `const title = "..."` in frontmatter
2. Detect pageType from filename (arxiv ID pattern → paper, else concept)
3. Detect status from `const status = '...'`
4. Extract HTML content between <main class="page-main"> and </main>
5. Write .mdx with YAML frontmatter + WikiLink import + content

Run from project root:
    python3 tools/convert_astro_to_mdx.py
    python3 tools/convert_astro_to_mdx.py --dry-run   # preview only
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src' / 'pages' / 'pages'
DEST = ROOT / 'src' / 'content' / 'pages'

# arXiv ID pattern: digits, dot, digits (e.g. 2603.16183)
ARXIV_RE = re.compile(r'^\d{4}[.\-]\d{4,5}$')


def extract_title(frontmatter: str) -> str:
    """Extract title from const title = "..." or const title = '...'"""
    m = re.search(r'const\s+title\s*=\s*["\'](.+?)\s*-\s*ArXiv Atlas["\']', frontmatter)
    if m:
        return m.group(1).strip()
    # Fallback: grab whatever is in the title string
    m = re.search(r'const\s+title\s*=\s*["\'](.+?)["\']', frontmatter)
    if m:
        return m.group(1).strip()
    return 'Untitled'


def extract_status(frontmatter: str) -> str:
    m = re.search(r"const\s+status\s*=\s*['\"](\w+)['\"]", frontmatter)
    return m.group(1) if m else 'done'


def detect_page_type(stem: str) -> str:
    if ARXIV_RE.match(stem):
        return 'paper'
    if stem.startswith('portal-'):
        return 'portal'
    if stem.startswith('daily_') or stem.startswith('daily-'):
        return 'daily_summary'
    return 'concept'


def extract_main_content(html: str) -> str:
    """Extract everything between <main class="page-main"> and the closing </main>."""
    # Find opening tag
    start_pattern = re.compile(r'<main\s+class="page-main"\s*>')
    m = start_pattern.search(html)
    if not m:
        return ''
    start = m.end()

    # Find the matching </main> — take the last one in case of nesting
    # In practice there's exactly one <main> so just find </main> from the end
    end = html.rfind('</main>')
    if end == -1 or end <= start:
        return ''

    content = html[start:end]

    # Strip leading/trailing whitespace but preserve internal formatting
    lines = content.split('\n')
    # Remove common leading indentation (usually 4 spaces from the .astro template)
    if lines:
        # Find minimum indentation of non-empty lines
        indents = [len(line) - len(line.lstrip()) for line in lines if line.strip()]
        min_indent = min(indents) if indents else 0
        if min_indent > 0:
            lines = [line[min_indent:] if len(line) >= min_indent else line for line in lines]

    return '\n'.join(lines).strip()


def needs_wikilink(content: str) -> bool:
    return 'WikiLink' in content or '<WikiLink' in content


def convert_file(astro_path: Path, dry_run: bool = False) -> bool:
    text = astro_path.read_text()

    # Split frontmatter from template
    parts = text.split('---', 2)
    if len(parts) < 3:
        print(f'  SKIP {astro_path.name}: no frontmatter')
        return False

    frontmatter = parts[1]
    template = parts[2]

    title = extract_title(frontmatter)
    status = extract_status(frontmatter)
    page_type = detect_page_type(astro_path.stem)
    content = extract_main_content(template)

    if not content:
        print(f'  SKIP {astro_path.name}: no <main> content found')
        return False

    # Escape any bare { or } in content that aren't part of JSX expressions
    # MDX treats { } as JSX expressions. We need to be careful here.
    # Actually, the content uses {expressions} for Astro template syntax which
    # MDX also supports, so we should leave them as-is.

    # Build MDX
    mdx_lines = []
    mdx_lines.append('---')
    # Escape quotes in title for YAML
    yaml_title = title.replace('"', '\\"')
    mdx_lines.append(f'title: "{yaml_title}"')
    mdx_lines.append(f'pageType: {page_type}')
    mdx_lines.append(f'status: {status}')
    mdx_lines.append('---')
    mdx_lines.append('')
    if needs_wikilink(content):
        mdx_lines.append('import WikiLink from "../../components/WikiLink.astro";')
        mdx_lines.append('')
    mdx_lines.append(content)
    mdx_lines.append('')

    mdx_text = '\n'.join(mdx_lines)

    dest_path = DEST / (astro_path.stem + '.mdx')

    if dry_run:
        print(f'  {astro_path.name} → {dest_path.name}  (title="{title}", type={page_type}, status={status}, {len(content)} chars)')
    else:
        dest_path.write_text(mdx_text)
        print(f'  ✓ {astro_path.name} → {dest_path.name}')

    return True


def main():
    dry_run = '--dry-run' in sys.argv

    DEST.mkdir(parents=True, exist_ok=True)

    astro_files = sorted(SRC.glob('*.astro'))
    # Skip template and dynamic route
    skip = {'_template.astro', '[slug].astro'}
    astro_files = [f for f in astro_files if f.name not in skip]

    print(f'Converting {len(astro_files)} .astro files to .mdx\n')
    if dry_run:
        print('DRY RUN — no files will be written\n')

    success = 0
    failed = 0
    for f in astro_files:
        if convert_file(f, dry_run=dry_run):
            success += 1
        else:
            failed += 1

    print(f'\n{"=" * 60}')
    print(f'✓ Converted: {success}')
    if failed:
        print(f'✗ Skipped: {failed}')
    if not dry_run:
        print(f'\nMDX files written to: {DEST}')
        print(f'You can now delete the .astro originals from: {SRC}')


if __name__ == '__main__':
    main()
