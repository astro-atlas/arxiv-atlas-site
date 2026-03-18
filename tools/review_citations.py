#!/usr/bin/env python3
"""
Review citations in analysis files and prepare for ADS resolution later.
For now, just audit what's present and check consistency.
"""

import re
from pathlib import Path
from collections import defaultdict

def extract_citations(content):
    """Extract all citation patterns from content"""
    citations = {
        'arxiv': set(re.findall(r'arXiv:(\d{4}\.\d{4,5})', content)),
        'doi': set(re.findall(r'10\.\d{4,}/[\w\.\-]+', content)),
        'years': set(re.findall(r'\b(19\d{2}|20\d{2})\b', content)),
    }
    return citations

def check_citation_section(content):
    """Check if Citations section is properly formatted"""
    if '## Citations' not in content:
        return False, "Missing Citations section"
    
    # Extract Citations section
    match = re.search(r'## Citations\n(.*?)\n##', content, re.DOTALL)
    if not match:
        match = re.search(r'## Citations\n(.*?)\n#', content, re.DOTALL)
    if not match:
        return False, "Citations section not parseable"
    
    citations_text = match.group(1).strip()
    
    if not citations_text or citations_text == "None" or "No citations" in citations_text:
        return True, "Empty (OK for single-paper analysis)"
    
    # Check format: should have [DOI/arXiv] [Author] [concept]: statement [pagelink] [exists]
    lines = [l.strip() for l in citations_text.split('\n') if l.strip() and not l.strip().startswith('-')]
    
    has_proper_format = any('[pagelink' in l and '[exists' in l for l in lines)
    
    if has_proper_format:
        return True, f"{len(lines)} citations with proper format"
    else:
        return False, f"{len(lines)} citations but missing pagelink/exists markers"

def analyze_file(filepath):
    """Analyze a single analysis file"""
    content = filepath.read_text()
    
    # Extract citations
    cites = extract_citations(content)
    
    # Check citation section
    section_ok, section_msg = check_citation_section(content)
    
    # Check processing log
    has_log = '**Processing log:**' in content
    has_sonnet = '✅ Sonnet (via sessions_send)' in content
    has_opus = '✅ Opus (via sessions_send)' in content
    
    return {
        'file': filepath.name,
        'arxiv_refs': len(cites['arxiv']),
        'doi_refs': len(cites['doi']),
        'years_mentioned': len(cites['years']),
        'citation_section_ok': section_ok,
        'citation_section_msg': section_msg,
        'has_processing_log': has_log,
        'has_sonnet': has_sonnet,
        'has_opus': has_opus,
    }

def main():
    base_dir = Path(__file__).parent.parent
    temp_dir = base_dir / "data" / "temp"
    
    analysis_files = sorted(temp_dir.glob("*.md"))
    
    print(f"Reviewing {len(analysis_files)} analysis files\n")
    print("=" * 80)
    
    results = []
    for filepath in analysis_files:
        result = analyze_file(filepath)
        results.append(result)
    
    # Summary by status
    print("\n📊 Processing Log Status:")
    for r in results:
        status = "✅" if (r['has_sonnet'] and r['has_opus']) else "⚠️"
        print(f"  {status} {r['file']}: Sonnet={r['has_sonnet']}, Opus={r['has_opus']}")
    
    print("\n📚 Citation Sections:")
    for r in results:
        status = "✅" if r['citation_section_ok'] else "⚠️"
        print(f"  {status} {r['file']}: {r['citation_section_msg']}")
    
    print("\n📈 Reference Statistics:")
    total_arxiv = sum(r['arxiv_refs'] for r in results)
    total_doi = sum(r['doi_refs'] for r in results)
    print(f"  Total arXiv references: {total_arxiv}")
    print(f"  Total DOI references: {total_doi}")
    print(f"  Average refs per paper: {total_arxiv / len(results):.1f} arXiv, {total_doi / len(results):.1f} DOI")
    
    # Files needing attention
    needs_attention = [r for r in results if not (r['has_sonnet'] and r['has_opus'] and r['citation_section_ok'])]
    
    if needs_attention:
        print(f"\n⚠️  {len(needs_attention)} files need attention:")
        for r in needs_attention:
            issues = []
            if not r['has_sonnet']:
                issues.append("missing Sonnet")
            if not r['has_opus']:
                issues.append("missing Opus")
            if not r['citation_section_ok']:
                issues.append("citation format")
            print(f"    {r['file']}: {', '.join(issues)}")
    else:
        print(f"\n✅ All files have proper processing logs and citation sections!")
    
    print("\n" + "=" * 80)
    print("\n💡 Next steps:")
    print("  1. Files are ready for ingestion (ADS resolution can come later)")
    print("  2. Citations use arXiv IDs (DOIs will be added when papers are published)")
    print("  3. Run tools/db_access.py to insert papers into database")

if __name__ == "__main__":
    main()
