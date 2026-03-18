#!/usr/bin/env python3
"""
Ingest analysis files from data/papers/*.md into the database.
Creates paper records, page records, and citation links.

Expected analysis file format (from SUBAGENT_PARSE_WORKFLOW.md):

    # Metadata
    * **Title:** ...
    * **Authors:** ...
    * **arXiv ID:** 2603.XXXXX
    * **DOI:** ...
    * **Submitted date:** ...
    * **Abstract:** ...

    # Contents
    ## [Section]
    ### Key claims
    ...

    ## Citations
    * [DOI] [First author] [main concept]: statement [pagelink] [x]
    ...

    ## Analysis
    ...
"""

import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access as db


def strip_bold(s):
    """Remove markdown bold markers from a string."""
    return s.replace('**', '').strip()


def parse_analysis_file(md_file):
    """Parse an analysis markdown file and extract structured data."""
    content = md_file.read_text()

    # --- Extract metadata section ---
    metadata = {}
    metadata_match = re.search(r'#\s*Metadata\n(.*?)(?:\n#|\Z)', content, re.DOTALL)
    if metadata_match:
        meta_text = metadata_match.group(1)
        for line in meta_text.split('\n'):
            line = line.strip()
            if line.startswith('-') or line.startswith('*'):
                # Strip leading bullet character
                line = line[1:].strip()
                # Remove bold markers before splitting on ':'
                line = strip_bold(line)
                parts = line.split(':', 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if value:
                        metadata[key] = value

    # --- Extract citations ---
    # Workflow format: * [DOI] [First author] [main concept]: statement [pagelink] [x]
    # The last bracket pair is the pagelink; [x] means page exists, [] means missing.
    citations = []
    citations_match = re.search(r'##\s*Citations\n(.*?)(?:\n##|\n#|\Z)', content, re.DOTALL)
    if citations_match:
        cites_text = citations_match.group(1)
        for line in cites_text.split('\n'):
            line = line.strip()
            if not (line.startswith('-') or line.startswith('*')):
                continue
            # Look for [pagelink] [...] at the end of the line.
            # The second-to-last bracket pair is the pagelink slug.
            brackets = re.findall(r'\[([^\]]*)\]', line)
            if len(brackets) >= 2:
                pagelink = brackets[-2].strip()
                if pagelink:
                    citations.append(pagelink)

    # --- Extract arxiv_id from metadata (more reliable than filename) ---
    arxiv_id = metadata.get('arXiv ID', '').strip()

    return {
        'arxiv_id': arxiv_id,
        'metadata': metadata,
        'citations': citations,
        'full_path': str(md_file),
    }


def ingest_paper(md_file):
    """Ingest a single paper analysis file."""
    data = parse_analysis_file(md_file)
    arxiv_id = data['arxiv_id']

    # Fall back to filename stem if metadata didn't contain an arXiv ID
    if not arxiv_id:
        arxiv_id = md_file.stem

    print(f"  Ingesting {arxiv_id}...", end=' ', flush=True)

    # Claim paper for processing
    paper_id = db.claim_paper_for_processing(arxiv_id)

    # Extract metadata
    meta = data['metadata']
    title = meta.get('Title', 'Untitled')
    authors = meta.get('Authors', 'Unknown')
    abstract = meta.get('Abstract', '')
    doi = meta.get('DOI', None)
    submitted = meta.get('Submitted date', meta.get('Submitted', None))

    # Finish paper record
    db.finish_paper(
        arxiv_id=arxiv_id,
        title=title,
        authors=authors,
        abstract=abstract,
        doi=doi,
        submitted_date=submitted,
        processed_date=datetime.now().isoformat(),
        summary_path=data['full_path'],
        status='done'
    )

    # Create page for this paper
    page_slug = f"pages/{arxiv_id}"
    page_id = db.create_or_get_page(
        page_slug=page_slug,
        title=title,
        page_type='paper',
        source_paper_id=paper_id,
        path=f'src/pages/pages/{arxiv_id}.astro'
    )

    # Link paper to its page
    db.link_paper_page(paper_id, page_id, role='primary')

    # Record citation links (referenced papers)
    for cited_slug in data['citations']:
        db.add_page_link(page_id, cited_slug, link_text=None)

    print(f"✓ (paper_id={paper_id}, page_id={page_id}, {len(data['citations'])} citations)")

    return paper_id, page_id


def main():
    base_dir = Path(__file__).parent.parent
    papers_dir = base_dir / "data" / "papers"

    # Initialize database
    print("Initializing database...")
    db.migrate()

    # Get all analysis files (skip date-tracking files like YYYY-MM-DD_analyzed.md)
    analysis_files = [
        f for f in sorted(papers_dir.glob("*.md"))
        if not re.match(r'\d{4}-\d{2}-\d{2}_analyzed\.md$', f.name)
    ]

    print(f"\nFound {len(analysis_files)} analysis files to ingest\n")
    print("=" * 70)

    success_count = 0
    failed_count = 0

    for md_file in analysis_files:
        try:
            ingest_paper(md_file)
            success_count += 1
        except Exception as e:
            print(f"✗ Error: {e}")
            failed_count += 1

    print("=" * 70)
    print(f"\n✓ Successfully ingested {success_count} papers")
    if failed_count > 0:
        print(f"✗ Failed to ingest {failed_count} papers")

    # Print database stats
    print("\nDatabase statistics:")
    stats = db.stats()
    print(f"  Total papers: {stats['total_papers']}")
    print(f"  Total pages: {stats['total_pages']}")
    print(f"  Papers by status: {stats['papers_by_status']}")


if __name__ == "__main__":
    main()
