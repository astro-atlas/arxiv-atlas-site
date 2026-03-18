#!/usr/bin/env python3
"""
Extract references from arXiv papers and populate Citations sections.
Downloads PDFs, extracts bibliography, parses citations, checks wiki presence.
"""

import re
import sys
import subprocess
from pathlib import Path
import urllib.request
import time

def download_pdf(arxiv_id, pdf_dir):
    """Download PDF for an arXiv paper"""
    pdf_path = pdf_dir / f"{arxiv_id}.pdf"
    
    if pdf_path.exists():
        print(f"  PDF already exists: {pdf_path.name}")
        return pdf_path
    
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(f"  Downloading {url}...")
    
    try:
        urllib.request.urlretrieve(url, pdf_path)
        time.sleep(0.5)  # Rate limiting
        return pdf_path
    except Exception as e:
        print(f"  Error downloading: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext"""
    try:
        result = subprocess.run(
            ['pdftotext', str(pdf_path), '-'],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout
        else:
            print(f"  pdftotext error: {result.stderr}")
            return None
    except FileNotFoundError:
        print("  pdftotext not found, trying Python extraction...")
        # Fallback: try PyPDF2 if available
        try:
            import PyPDF2
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except ImportError:
            print("  PyPDF2 not available")
            return None

def extract_references_section(text):
    """Extract the References/Bibliography section from paper text"""
    # Common patterns for references section start
    patterns = [
        r'\nReferences\n',
        r'\nBIBLIOGRAPHY\n',
        r'\nREFERENCES\n',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Get everything after this point
            refs_start = match.end()
            refs_text = text[refs_start:]
            
            # Try to find where references end (often Appendix or acknowledgments)
            end_patterns = [
                r'\nAppendix',
                r'\nACKNOWLEDGMENTS',
                r'\nACKNOWLEDGEMENTS',
            ]
            
            for end_pattern in end_patterns:
                end_match = re.search(end_pattern, refs_text, re.IGNORECASE)
                if end_match:
                    refs_text = refs_text[:end_match.start()]
                    break
            
            return refs_text.strip()
    
    return None

def parse_references(refs_text):
    """Parse individual references from the references section"""
    # This is a simplified parser - real citation parsing is complex
    # We'll extract arXiv IDs and DOIs where present
    
    references = []
    
    # Split on numbered references (common format: [1], [2], etc.)
    # Or author names at start of line
    lines = refs_text.split('\n')
    
    current_ref = []
    for line in lines:
        line = line.strip()
        if not line:
            if current_ref:
                ref_text = ' '.join(current_ref)
                parsed = parse_single_reference(ref_text)
                if parsed:
                    references.append(parsed)
                current_ref = []
        else:
            current_ref.append(line)
    
    # Don't forget last reference
    if current_ref:
        ref_text = ' '.join(current_ref)
        parsed = parse_single_reference(ref_text)
        if parsed:
            references.append(parsed)
    
    return references

def parse_single_reference(ref_text):
    """Parse a single reference to extract key information"""
    parsed = {
        'text': ref_text,
        'arxiv_id': None,
        'doi': None,
        'authors': None,
        'year': None,
    }
    
    # Extract arXiv ID
    arxiv_match = re.search(r'arXiv[:\s]*(\d{4}\.\d{4,5})', ref_text, re.IGNORECASE)
    if arxiv_match:
        parsed['arxiv_id'] = arxiv_match.group(1)
    
    # Extract DOI
    doi_match = re.search(r'doi[:\s]*(10\.\d{4,}/[\w\.\-/]+)', ref_text, re.IGNORECASE)
    if not doi_match:
        doi_match = re.search(r'(10\.\d{4,}/[\w\.\-/]+)', ref_text)
    if doi_match:
        parsed['doi'] = doi_match.group(1)
    
    # Extract year (4 digits, typically in parentheses or after a comma)
    year_match = re.search(r'\(?(19\d{2}|20\d{2})\)?', ref_text)
    if year_match:
        parsed['year'] = year_match.group(1)
    
    # Extract first author (very basic: first capitalized word before comma or year)
    author_match = re.search(r'^[^\d]*?([A-Z][a-z]+(?:\s+[A-Z]\.)?)(?:,|\s+et\s+al|\s+\()', ref_text)
    if author_match:
        parsed['authors'] = author_match.group(1)
    
    return parsed

def format_citation_entry(ref, pages_dir):
    """Format a reference as a citation entry with pagelink and exists markers"""
    # Determine reference identifier (prefer DOI, then arXiv)
    if ref['doi']:
        ref_id = f"https://doi.org/{ref['doi']}"
    elif ref['arxiv_id']:
        ref_id = f"arXiv:{ref['arxiv_id']}"
    else:
        return None  # Skip references without identifiable IDs
    
    # Determine author
    author = ref['authors'] if ref['authors'] else "Unknown"
    
    # Determine pagelink
    if ref['arxiv_id']:
        pagelink = f"/pages/{ref['arxiv_id']}"
        page_file = pages_dir / f"{ref['arxiv_id']}.astro"
        exists = page_file.exists()
    else:
        pagelink = ""
        exists = False
    
    # Extract a short concept/topic from the reference text (first few words after author/year)
    concept = "citation"  # Default
    
    # Format: [DOI/arXiv] [Author] [concept]: statement [pagelink] [exists]
    exists_str = "true" if exists else "false"
    pagelink_str = f"[pagelink: {pagelink}]" if pagelink else "[pagelink: ]"
    
    entry = f"{ref_id} {author} [{concept}]: {ref['text'][:100]}... {pagelink_str} [exists: {exists_str}]"
    
    return entry

def main():
    base_dir = Path(__file__).parent.parent
    temp_dir = base_dir / "data" / "temp"
    pdf_dir = base_dir / "data" / "pdfs"
    pages_dir = base_dir / "src" / "pages" / "pages"
    
    # Create PDF directory
    pdf_dir.mkdir(exist_ok=True)
    
    # Get all analysis files
    analysis_files = sorted(temp_dir.glob("*.md"))
    
    print(f"Processing {len(analysis_files)} papers\n")
    
    for md_file in analysis_files[:3]:  # Start with first 3 as test
        arxiv_id = md_file.stem
        print(f"\n{'='*60}")
        print(f"Processing {arxiv_id}")
        print('='*60)
        
        # Download PDF
        pdf_path = download_pdf(arxiv_id, pdf_dir)
        if not pdf_path:
            print(f"  Skipping (PDF download failed)")
            continue
        
        # Extract text
        print(f"  Extracting text from PDF...")
        text = extract_text_from_pdf(pdf_path)
        if not text:
            print(f"  Skipping (text extraction failed)")
            continue
        
        # Extract references section
        print(f"  Extracting references section...")
        refs_text = extract_references_section(text)
        if not refs_text:
            print(f"  Skipping (no references section found)")
            continue
        
        print(f"  Found references section ({len(refs_text)} chars)")
        
        # Parse references
        print(f"  Parsing individual references...")
        references = parse_references(refs_text)
        print(f"  Found {len(references)} references")
        
        # Show sample
        arxiv_refs = [r for r in references if r['arxiv_id']]
        doi_refs = [r for r in references if r['doi']]
        print(f"    - {len(arxiv_refs)} with arXiv IDs")
        print(f"    - {len(doi_refs)} with DOIs")
        
        if references:
            print(f"\n  Sample references:")
            for ref in references[:3]:
                print(f"    • {ref['authors']} ({ref['year']}): arXiv={ref['arxiv_id']}, DOI={ref['doi']}")

if __name__ == "__main__":
    main()
