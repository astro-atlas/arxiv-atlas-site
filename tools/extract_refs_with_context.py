#!/usr/bin/env python3
"""
Extract references from arXiv HTML with citation context.
Finds where each reference is cited in the body text and extracts clean context.
"""

import re
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from collections import defaultdict
import html

def fetch_arxiv_html(arxiv_id):
    """Fetch HTML version of arXiv paper"""
    url = f"https://arxiv.org/html/{arxiv_id}"
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req, timeout=30) as response:
            return response.read().decode('utf-8')
    except (HTTPError, URLError):
        return None

def extract_references_from_html(html_content):
    """Extract references section from arXiv HTML"""
    match = re.search(r'<section[^>]*class="ltx_bibliography"[^>]*>(.*?)</section>', html_content, re.DOTALL)
    return match.group(1) if match else None

def parse_html_references(refs_html):
    """Parse references and build id→metadata map"""
    bibitem_pattern = r'<li[^>]*id="([^"]*)"[^>]*class="[^"]*ltx_bibitem[^"]*"[^>]*>(.*?)</li>'
    bibitems = re.findall(bibitem_pattern, refs_html, re.DOTALL)
    
    ref_map = {}
    for bib_id, bibitem in bibitems:
        ref = parse_single_html_ref(bibitem)
        if ref:
            ref_map[bib_id] = ref
    
    return ref_map

def parse_single_html_ref(bibitem_html):
    """Parse a single bibliography item"""
    doi_match = re.search(r'href="https://(?:dx\.)?doi\.org/(10\.\d{4,}/[^"]+)"', bibitem_html)
    doi = doi_match.group(1) if doi_match else None
    
    arxiv_match = re.search(r'<span class="ltx_text ltx_bib_external">(\d{4}\.\d{4,5})</span>', bibitem_html)
    arxiv_id = arxiv_match.group(1) if arxiv_match else None
    
    title_match = re.search(r'<span class="ltx_text ltx_bib_title">([^<]+)</span>', bibitem_html)
    title = title_match.group(1) if title_match else ""
    
    author_match = re.search(r'ltx_tag_bibitem">([^(]+?)(?:\(| \d)', bibitem_html)
    if author_match:
        authors_str = author_match.group(1).strip()
        first_author_match = re.search(r'([A-Z][a-z]+(?:\s+[A-Z]\.?)*)', authors_str)
        author = first_author_match.group(1) if first_author_match else authors_str[:30]
    else:
        author = "Unknown"
    
    year_match = re.search(r'\((\d{4})\)', bibitem_html)
    year = year_match.group(1) if year_match else None
    
    return {
        'title': title[:80] if title else "",
        'arxiv_id': arxiv_id,
        'doi': doi,
        'year': year,
        'author': author,
    }

def clean_html_text(text):
    """Remove HTML tags and decode entities"""
    # Remove tags
    text = re.sub(r'<[^>]+>', ' ', text)
    # Decode HTML entities
    text = html.unescape(text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_citation_contexts(html_content, ref_map):
    """
    Find where each reference is cited and extract surrounding context.
    In arXiv HTML, citations are links like <a href="#bib.bibXX">Year</a>
    """
    citation_contexts = defaultdict(list)
    
    # Extract just the body (exclude bibliography)
    body_match = re.search(r'<body[^>]*>(.*?)<section[^>]*class="ltx_bibliography"', html_content, re.DOTALL)
    if not body_match:
        return citation_contexts
    
    body_html = body_match.group(1)
    
    # Find all paragraphs and their citation links
    # Better approach: find paragraphs, then find citations within them
    paragraph_pattern = r'<p[^>]*>(.*?)</p>'
    
    for para_match in re.finditer(paragraph_pattern, body_html, re.DOTALL):
        para_html = para_match.group(1)
        para_text = clean_html_text(para_html)
        
        # Find citations in this paragraph
        citation_pattern = r'<a[^>]*href="#(bib\.[^"]+)"[^>]*>([^<]+)</a>'
        
        for cite_match in re.finditer(citation_pattern, para_html):
            bib_id = cite_match.group(1)
            
            if bib_id in ref_map:
                # Use the paragraph text as context (limit to reasonable length)
                context = para_text[:200] if len(para_text) > 200 else para_text
                citation_contexts[bib_id].append(context)
    
    return citation_contexts

def format_citation_with_context(ref, contexts, pages_dir):
    """Format reference with contextual summary from how it's cited"""
    if ref['doi']:
        ref_id = f"https://doi.org/{ref['doi']}"
    elif ref['arxiv_id']:
        ref_id = f"arXiv:{ref['arxiv_id']}"
    else:
        return None
    
    author = ref['author']
    year = ref['year'] if ref['year'] else "n.d."
    
    # Create summary from first context where this reference appears
    if contexts and len(contexts[0]) > 20:
        summary = contexts[0]
        # Truncate if too long
        if len(summary) > 150:
            summary = summary[:147] + "..."
    else:
        # Fallback to title if no good context
        summary = ref['title'] if ref['title'] else "Referenced in paper"
    
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
    
    entry = f"- {ref_id} {author} ({year}): {summary} {pagelink_str} [exists: {exists_str}]"
    return entry

def update_citations_in_file(md_file, ref_map, citation_contexts, pages_dir):
    """Update Citations section with contextual summaries"""
    content = md_file.read_text()
    
    match = re.search(r'(## Citations\n)(.*?)(\n##|\n#|$)', content, re.DOTALL)
    if not match:
        return False
    
    citations = []
    for bib_id, ref in ref_map.items():
        contexts = citation_contexts.get(bib_id, [])
        citation = format_citation_with_context(ref, contexts, pages_dir)
        if citation:
            citations.append(citation)
    
    if not citations:
        return False
    
    new_section = match.group(1) + '\n'.join(citations) + '\n'
    new_content = content[:match.start()] + new_section + match.group(3) + content[match.end():]
    
    md_file.write_text(new_content)
    return True

def main():
    base_dir = Path(__file__).parent.parent
    temp_dir = base_dir / "data" / "temp"
    pages_dir = base_dir / "src" / "pages" / "pages"
    
    analysis_files = sorted(temp_dir.glob("*.md"))
    
    print(f"Extracting citation contexts for {len(analysis_files)} papers\n")
    
    success_count = 0
    skipped_count = 0
    
    for md_file in analysis_files:
        arxiv_id = md_file.stem
        print(f"{arxiv_id}... ", end='', flush=True)
        
        html_content = fetch_arxiv_html(arxiv_id)
        if not html_content:
            print(f"✗ (no HTML)")
            skipped_count += 1
            continue
        
        refs_html = extract_references_from_html(html_content)
        if not refs_html:
            print(f"✗ (no refs)")
            skipped_count += 1
            continue
        
        ref_map = parse_html_references(refs_html)
        citation_contexts = extract_citation_contexts(html_content, ref_map)
        
        refs_with_context = sum(1 for bib_id in ref_map if citation_contexts.get(bib_id))
        
        if update_citations_in_file(md_file, ref_map, citation_contexts, pages_dir):
            print(f"✓ ({len(ref_map)} refs, {refs_with_context} with context)")
            success_count += 1
        else:
            print(f"✗ (update failed)")
            skipped_count += 1
        
        time.sleep(0.5)
    
    print(f"\n{'='*70}")
    print(f"✓ Successfully updated {success_count} files with citation contexts")
    print(f"✗ Skipped {skipped_count} files")

if __name__ == "__main__":
    main()
