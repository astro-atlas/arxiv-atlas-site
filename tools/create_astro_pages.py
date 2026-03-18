#!/usr/bin/env python3
"""
Create .astro files for all papers in the database.
Uses the analysis files from data/temp/ as source content.
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
    """Create an .astro page for a paper"""
    
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

def main():
    base_dir = Path(__file__).parent.parent
    pages_dir = base_dir / "src" / "pages" / "pages"
    temp_dir = base_dir / "data" / "temp"
    
    with db.sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT p.id, p.arxiv_id, p.title, p.authors, p.abstract, p.summary_path
            FROM papers p
            WHERE p.status = 'done'
            ORDER BY p.processed_date DESC
        """)
        papers = cur.fetchall()
    
    print(f"Creating .astro files for {len(papers)} papers\n")
    
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
        
        astro_path = pages_dir / f"{arxiv_id}.astro"
        astro_content = create_paper_page(arxiv_id, title, authors, abstract, analysis_file)
        
        if astro_content:
            astro_path.write_text(astro_content)
            print(f"✓ {arxiv_id}")
            created_count += 1
    
    print(f"\n{'='*70}")
    print(f"✓ Created {created_count} .astro files in {pages_dir}")

if __name__ == "__main__":
    main()
