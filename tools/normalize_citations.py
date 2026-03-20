#!/usr/bin/env python3
"""
Normalize citations in analysis files:
- Extract reference lists from arXiv papers
- Look up DOIs where possible
- Add pagelinks for cited papers
- Mark exists: true/false based on wiki page presence
"""

import re
import sys
from pathlib import Path

def extract_arxiv_id(text):
    """Extract arXiv ID from various formats"""
    patterns = [
        r'arXiv:(\d{4}\.\d{4,5})',
        r'(\d{4}\.\d{4,5})',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None

def check_page_exists(arxiv_id, pages_dir):
    """Check if a wiki page exists for this paper"""
    slug = arxiv_id.replace('.', '-')
    page_file = pages_dir / f"{slug}.md"
    return page_file.exists()

def normalize_file(filepath, pages_dir):
    """Normalize citations in a single analysis file"""
    print(f"Processing {filepath.name}...")
    
    content = filepath.read_text()
    
    # Extract the paper's own arXiv ID
    paper_id = filepath.stem
    
    # Find all arXiv references in the file
    arxiv_refs = set(re.findall(r'arXiv:(\d{4}\.\d{4,5})', content))
    
    print(f"  Found {len(arxiv_refs)} unique arXiv references")
    
    # For now, just report what we found
    # Full implementation would:
    # 1. Query ADS for each reference to get DOI
    # 2. Check if wiki page exists
    # 3. Update citation format
    
    for ref in sorted(arxiv_refs):
        exists = check_page_exists(ref, pages_dir)
        status = "✓" if exists else "✗"
        print(f"    {ref} {status}")
    
    return len(arxiv_refs)

def main():
    base_dir = Path(__file__).parent.parent
    temp_dir = base_dir / "data" / "temp"
    pages_dir = base_dir / "src" / "pages" / "pages"
    
    if not temp_dir.exists():
        print(f"Error: {temp_dir} does not exist")
        sys.exit(1)
    
    analysis_files = sorted(temp_dir.glob("*.md"))
    
    if not analysis_files:
        print(f"No .md files found in {temp_dir}")
        sys.exit(0)
    
    print(f"Found {len(analysis_files)} analysis files\n")
    
    total_refs = 0
    for filepath in analysis_files:
        refs = normalize_file(filepath, pages_dir)
        total_refs += refs
    
    print(f"\nTotal references found: {total_refs}")
    print(f"\nNote: ADS lookup not yet implemented (papers too new)")
    print("Citations are currently in format: (arXiv:XXXX.XXXXX)")

if __name__ == "__main__":
    main()
