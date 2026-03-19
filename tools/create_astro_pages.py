#!/usr/bin/env python3
"""
Create page files for all papers in the database.
Uses the analysis files from data/temp/ as source content.

Supports two output formats:
  --format astro  (default, legacy) → src/pages/pages/{id}.astro
  --format mdx                      → src/content/pages/{id}.mdx  (content collection)
"""

import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access as db

def escape_for_template(text):
    """Escape characters for Astro template literals"""
    # First escape backslashes
    text = text.replace('\\', '\\\\')
    # Escape template literal special chars
    text = text.replace('`', '\\`')
    text = text.replace('$', '\\$')
    # Escape curly braces for JSX by doubling them
    text = text.replace('{', '{{')
    text = text.replace('}', '}}')
    # Escape HTML entities
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    return text

def create_paper_page(arxiv_id, title, authors, abstract, analysis_file):
    """Create an .astro page for a paper (legacy format)"""
    
    if not Path(analysis_file).exists():
        print(f"  Warning: Analysis file not found: {analysis_file}")
        return False
    
    content = Path(analysis_file).read_text()
    
    # Extract key sections
    contents_match = re.search(r'# Contents\n(.*?)(?:\n## Citations|\n# Analysis|$)', content, re.DOTALL)
    contents = contents_match.group(1).strip() if contents_match else ""
    
    citations_match = re.search(r'## Citations\n(.*?)(?:\n##|\n#|$)', content, re.DOTALL)
    citations = citations_match.group(1).strip() if citations_match else ""
    
    analysis_match = re.search(r'# Analysis\n(.*?)(?:\n---|\Z)', content, re.DOTALL)
    analysis = analysis_match.group(1).strip() if analysis_match else ""
    
    # Escape for template
    title_escaped = title.replace('"', '\\"')
    contents_html = escape_for_template(contents)
    citations_html = escape_for_template(citations)
    analysis_html = escape_for_template(analysis)
    abstract_html = escape_for_template(abstract)
    
    # Build content using string concatenation
    parts = []
    parts.append('---')
    parts.append("import Base from '../../layouts/Base.astro';")
    parts.append("import Sidebar from '../../components/Sidebar.astro';")
    parts.append('const title = "' + title_escaped + ' - ArXiv Atlas";')
    parts.append('---')
    parts.append('')
    parts.append('<Base title={title}>')
    parts.append('  <Sidebar />')
    parts.append('  <main class="page-main">')
    parts.append('    <h1 class="page-title">' + title + '</h1>')
    parts.append('')
    parts.append('    <div class="infobox">')
    parts.append('      <h3 class="infobox-title">Paper Details</h3>')
    parts.append('      <table>')
    parts.append('        <tr>')
    parts.append('          <th>Authors:</th>')
    parts.append('          <td>' + authors + '</td>')
    parts.append('        </tr>')
    parts.append('        <tr>')
    parts.append('          <th>arXiv ID:</th>')
    parts.append('          <td><a href="https://arxiv.org/abs/' + arxiv_id + '">' + arxiv_id + '</a></td>')
    parts.append('        </tr>')
    parts.append('      </table>')
    parts.append('    </div>')
    parts.append('')
    parts.append('    <h2 id="abstract">Abstract</h2>')
    parts.append('    <Fragment set:html={`' + abstract_html + '`} />')
    parts.append('')
    parts.append('    <h2 id="contents">Contents</h2>')
    parts.append('    <Fragment set:html={`' + contents_html + '`} />')
    parts.append('')
    parts.append('    <h2 id="references">References</h2>')
    parts.append('    <Fragment set:html={`' + citations_html + '`} />')
    parts.append('')
    parts.append('    <h2 id="analysis">Analysis</h2>')
    parts.append('    <Fragment set:html={`' + analysis_html + '`} />')
    parts.append('  </main>')
    parts.append('</Base>')
    
    return '\n'.join(parts)


def create_paper_mdx(arxiv_id, title, authors, abstract, analysis_file):
    """Create an .mdx page for a paper (content collection format).
    
    MDX files live in src/content/pages/ and are rendered by
    src/pages/pages/[slug].astro via getStaticPaths().
    Content goes inside <main class="page-main"> automatically.
    """
    if not Path(analysis_file).exists():
        print(f"  Warning: Analysis file not found: {analysis_file}")
        return False

    content = Path(analysis_file).read_text()

    contents_match = re.search(r'# Contents\n(.*?)(?:\n## Citations|\n# Analysis|$)', content, re.DOTALL)
    contents = contents_match.group(1).strip() if contents_match else ""

    citations_match = re.search(r'## Citations\n(.*?)(?:\n##|\n#|$)', content, re.DOTALL)
    citations = citations_match.group(1).strip() if citations_match else ""

    analysis_match = re.search(r'# Analysis\n(.*?)(?:\n---|\Z)', content, re.DOTALL)
    analysis = analysis_match.group(1).strip() if analysis_match else ""

    title_escaped = title.replace('"', '\\"')

    parts = []
    parts.append('---')
    parts.append(f'title: "{title_escaped}"')
    parts.append('pageType: paper')
    parts.append('status: done')
    parts.append('---')
    parts.append('')
    parts.append('import WikiLink from "../../components/WikiLink.astro";')
    parts.append('')
    parts.append(f'<h1 class="page-title">{title}</h1>')
    parts.append('')
    parts.append('<div class="infobox">')
    parts.append('  <h3 class="infobox-title">Paper Details</h3>')
    parts.append('  <table>')
    parts.append('    <tr><th>Authors:</th><td>' + authors + '</td></tr>')
    parts.append(f'    <tr><th>arXiv ID:</th><td><a href="https://arxiv.org/abs/{arxiv_id}">{arxiv_id}</a></td></tr>')
    parts.append('  </table>')
    parts.append('</div>')
    parts.append('')
    parts.append('## Abstract')
    parts.append('')
    parts.append(abstract)
    parts.append('')
    parts.append('## Contents')
    parts.append('')
    parts.append(contents)
    parts.append('')
    parts.append('## References')
    parts.append('')
    parts.append(citations)
    parts.append('')
    parts.append('## Analysis')
    parts.append('')
    parts.append(analysis)

    return '\n'.join(parts)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Create page files from analysis data')
    parser.add_argument('--format', choices=['astro', 'mdx'], default='astro',
                        help='Output format: astro (legacy) or mdx (content collection)')
    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent
    temp_dir = base_dir / "data" / "temp"

    if args.format == 'mdx':
        out_dir = base_dir / "src" / "content" / "pages"
        ext = '.mdx'
        create_fn = create_paper_mdx
    else:
        out_dir = base_dir / "src" / "pages" / "pages"
        ext = '.astro'
        create_fn = create_paper_page

    out_dir.mkdir(parents=True, exist_ok=True)
    
    with db.sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id, p.arxiv_id, p.title, p.authors, p.abstract, p.summary_path
            FROM papers p
            WHERE p.status = 'done'
            ORDER BY p.processed_date DESC
        """)
        papers = cur.fetchall()
    
    print(f"Creating {ext} files for {len(papers)} papers\n")
    
    created_count = 0
    
    for paper in papers:
        arxiv_id = paper['arxiv_id']
        title = paper['title'] or "Untitled"
        authors = paper['authors'] or "Unknown"
        abstract = paper['abstract'] or ""
        
        analysis_file = temp_dir / f"{arxiv_id}.md"
        
        if not analysis_file.exists():
            print(f"✗ {arxiv_id}: Analysis file not found")
            continue
        
        slug = arxiv_id.replace('.', '-')
        out_path = out_dir / f"{slug}{ext}"
        page_content = create_fn(arxiv_id, title, authors, abstract, analysis_file)
        
        if page_content:
            out_path.write_text(page_content)
            print(f"✓ {arxiv_id}")
            created_count += 1
    
    print(f"\n{'='*70}")
    print(f"✓ Created {created_count} {ext} files in {out_dir}")

if __name__ == "__main__":
    main()
