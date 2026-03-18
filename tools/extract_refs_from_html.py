#!/usr/bin/env python3
"""
Extract references from arXiv HTML pages and update Citations sections in analysis files.
"""

import re
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

def fetch_arxiv_html(arxiv_id):
    """Fetch HTML version of arXiv paper"""
    url = f"https://arxiv.org/html/{arxiv_id}"
    
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8')
        return html
    except (HTTPError, URLError) as e:
        return None

def extract_references_from_html(html):
    """Extract references section from arXiv HTML"""
    match = re.search(r'<section[^>]*class="ltx_bibliography"[^>]*>(.*?)</section>', html, re.DOTALL)
    if match:
        return match.group(1)
    return None

def parse_html_references(refs_html):
    """Parse references from HTML"""
    bibitem_pattern = r'<li[^>]*id="([^"]*)"[^>]*class="[^"]*ltx_bibitem[^"]*"[^>]*>(.*?)</li>'
    bibitems = re.findall(bibitem_pattern, refs_html, re.DOTALL)
    
    references = []
    
    for bib_id, bibitem in bibitems:
        ref = parse_single_html_ref(bibitem)
        if ref:
            references.append(ref)
    
    return references

def parse_single_html_ref(bibitem_html):
    """Parse a single bibliography item from HTML"""
    
    # Extract DOI (look for dx.doi.org or doi.org links)
    doi_match = re.search(r'href="https://(?:dx\.)?doi\.org/(10\.\d{4,}/[^"]+)"', bibitem_html)
    doi = doi_match.group(1) if doi_match else None
    
    # Extract arXiv ID (appears as plain text like "1307.6212" in ltx_bib_external)
    arxiv_match = re.search(r'<span class="ltx_text ltx_bib_external">(\d{4}\.\d{4,5})</span>', bibitem_html)
    arxiv_id = arxiv_match.group(1) if arxiv_match else None
    
    # Extract title (in ltx_bib_title)
    title_match = re.search(r'<span class="ltx_text ltx_bib_title">([^<]+)</span>', bibitem_html)
    title = title_match.group(1) if title_match else ""
    
    # Extract author names (in ltx_tag_bibitem, before year)
    author_match = re.search(r'ltx_tag_bibitem">([^(]+?)(?:\(| \d)', bibitem_html)
    if author_match:
        authors_str = author_match.group(1).strip()
        # Get first author
        first_author_match = re.search(r'([A-Z][a-z]+(?:\s+[A-Z]\.?)*)', authors_str)
        author = first_author_match.group(1) if first_author_match else authors_str[:30]
    else:
        author = "Unknown"
    
    # Extract year
    year_match = re.search(r'\((\d{4})\)', bibitem_html)
    year = year_match.group(1) if year_match else None
    
    # Clean plain text for summary
    text = re.sub(r'<[^>]+>', '', bibitem_html)
    text = re.sub(r'\s+', ' ', text).strip()
    
    return {
        'text': text[:150],
        'title': title[:100] if title else text[:100],
        'arxiv_id': arxiv_id,
        'doi': doi,
        'year': year,
        'author': author,
    }

def format_citation(ref, pages_dir):
    """Format reference as citation entry"""
    if ref['doi']:
        ref_id = f"https://doi.org/{ref['doi']}"
    elif ref['arxiv_id']:
        ref_id = f"arXiv:{ref['arxiv_id']}"
    else:
        return None
    
    author = ref['author']
    year = ref['year'] if ref['year'] else "n.d."
    title = ref['title'] if ref['title'] else "untitled"
    
    # Check if page exists
    if ref['arxiv_id']:
        pagelink = f"/pages/{ref['arxiv_id']}"
        page_file = pages_dir / f"{ref['arxiv_id']}.astro"
        exists = page_file.exists()
    else:
        pagelink = ""
        exists = False
    
    exists_str = "true" if exists else "false"
    pagelink_str = f"[pagelink: {pagelink}]" if pagelink else "[pagelink: ]"
    
    entry = f"- {ref_id} {author} ({year}) [{title}]: {ref['text']} {pagelink_str} [exists: {exists_str}]"
    
    return entry

def update_citations_in_file(md_file, references, pages_dir):
    """Update the Citations section in an analysis file"""
    content = md_file.read_text()
    
    # Find Citations section
    match = re.search(r'(## Citations\n)(.*?)(\n##|\n#|$)', content, re.DOTALL)
    if not match:
        print(f"  Warning: No Citations section found")
        return False
    
    # Format all citations
    citations = []
    for ref in references:
        citation = format_citation(ref, pages_dir)
        if citation:
            citations.append(citation)
    
    if not citations:
        print(f"  Warning: No citations to add")
        return False
    
    # Build new Citations section
    new_section = match.group(1) + '\n'.join(citations) + '\n'
    
    # Replace in content
    new_content = content[:match.start()] + new_section + match.group(3) + content[match.end():]
    
    # Write back
    md_file.write_text(new_content)
    
    return True

def main():
    base_dir = Path(__file__).parent.parent
    temp_dir = base_dir / "data" / "temp"
    pages_dir = base_dir / "src" / "pages" / "pages"
    
    analysis_files = sorted(temp_dir.glob("*.md"))
    
    print(f"Processing {len(analysis_files)} papers\n")
    
    success_count = 0
    skipped_count = 0
    
    for md_file in analysis_files:
        arxiv_id = md_file.stem
        print(f"{arxiv_id}... ", end='', flush=True)
        
        # Fetch HTML
        html = fetch_arxiv_html(arxiv_id)
        if not html:
            print(f"✗ (no HTML)")
            skipped_count += 1
            continue
        
        # Extract references
        refs_html = extract_references_from_html(html)
        if not refs_html:
            print(f"✗ (no refs)")
            skipped_count += 1
            continue
        
        # Parse references
        references = parse_html_references(refs_html)
        
        arxiv_refs = [r for r in references if r['arxiv_id']]
        doi_refs = [r for r in references if r['doi']]
        
        # Update file
        if update_citations_in_file(md_file, references, pages_dir):
            print(f"✓ ({len(references)} refs: {len(arxiv_refs)} arXiv, {len(doi_refs)} DOI)")
            success_count += 1
        else:
            print(f"✗ (update failed)")
            skipped_count += 1
        
        time.sleep(0.5)  # Rate limiting
    
    print(f"\n{'='*70}")
    print(f"✓ Successfully updated {success_count} files")
    print(f"✗ Skipped {skipped_count} files")
    print(f"\nTotal citations extracted from {success_count} papers")

if __name__ == "__main__":
    main()
