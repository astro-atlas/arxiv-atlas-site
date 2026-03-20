#!/usr/bin/env python3
"""
Generate Daily Summary Page

Runs AFTER all papers for a given date are processed.

Stage 7: Sonnet reads all pages tagged for the date, identifies 3-4 key themes,
groups papers, creates a summary page, updates DB and indices.

Usage:
  python generate_daily_summary.py --date 2026-03-16
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

def log(msg: str, level: str = "INFO"):
    """Simple logging"""
    print(f"[{level}] {msg}", file=sys.stderr)

def load_json(path: str) -> Any:
    """Load JSON file"""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def save_json(path: str, data: Any):
    """Save JSON file"""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

# ============================================================================
# STEP 1: Fetch Papers for Date
# ============================================================================

def fetch_papers_for_date(date_str: str) -> list:
    """
    Fetch all papers processed on a given date from the database.
    
    Args:
        date_str: Date in format "YYYY-MM-DD" (e.g., "2026-03-16")
    
    Returns:
        List of {arxiv_id, title, processing_date}
    """
    log(f"Fetching papers processed on {date_str}", "INFO")
    with db_access.sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, arxiv_id, title, processed_date FROM papers WHERE DATE(processed_date) = ? AND status = 'done' ORDER BY processed_date",
            (date_str,)
        )
        papers = [dict(r) for r in cur.fetchall()]
    log(f"Found {len(papers)} papers for {date_str}", "INFO")
    return papers

# ============================================================================
# STEP 2: Read Pages & Extract Content (Sonnet)
# ============================================================================

def read_pages_for_papers(arxiv_ids: list) -> dict:
    """
    Read all concept and paper pages related to papers processed today.
    
    Args:
        arxiv_ids: List of arxiv_ids processed today
    
    Returns:
        {arxiv_id: {title, concepts, summary, url}}
    """
    log(f"Reading pages for {len(arxiv_ids)} papers", "INFO")
    
    # In real implementation:
    # - Query page_links table for papers matching arxiv_ids
    # - Read each concept page from disk
    # - Ask Sonnet: "Summarize this concept page briefly (2-3 sentences)"
    # - Collect all content
    
    papers_content = {}
    
    log(f"Read content for {len(papers_content)} papers", "INFO")
    return papers_content

# ============================================================================
# STEP 3: Generate Summary with Sonnet
# ============================================================================

def generate_summary_themes(papers_content: dict) -> dict:
    """
    Ask Sonnet to identify 3-4 key research themes from the day's papers.
    
    Args:
        papers_content: {arxiv_id: {title, concepts, summary, url}}
    
    Returns:
        {
            themes: [
                {name: "Theme Name", papers: [{arxiv_id, title, summary_sentence}], concepts: [...]},
                ...
            ],
            overall_summary: "2-3 sentence summary of the day"
        }
    """
    log("Generating summary themes with Sonnet", "INFO")
    
    # In real implementation:
    # - Assemble prompt: "Here are today's papers and their key concepts. Group them into 3-4 themes."
    # - Send to Sonnet
    # - Parse structured response
    
    # For now, placeholder:
    result = {
        "themes": [],
        "overall_summary": "Summary to be generated"
    }
    
    log(f"Generated {len(result['themes'])} themes", "INFO")
    return result

# ============================================================================
# STEP 4: Create .astro Page
# ============================================================================

def create_astro_page(date_str: str, summary_data: dict) -> str:
    """
    Create the daily summary .astro page.
    
    Args:
        date_str: "YYYY-MM-DD"
        summary_data: {themes: [...], overall_summary: "..."}
    
    Returns:
        File path where page was written
    """
    log(f"Creating .astro page for {date_str}", "INFO")
    
    # Convert date format: 2026-03-16 → 2026_03_16
    date_slug = date_str.replace("-", "_")
    file_path = f"src/pages/pages/daily_{date_slug}.astro"
    
    # Build themes section
    themes_html = ""
    for theme in summary_data.get("themes", []):
        theme_name = theme.get("name", "Unknown Theme")
        papers = theme.get("papers", [])
        
        papers_html = ""
        for paper in papers:
            arxiv_id = paper.get("arxiv_id", "")
            title = paper.get("title", "Untitled")
            summary_sentence = paper.get("summary_sentence", "")
            # NOTE: In real implementation, use WikiLink for the paper
            papers_html += f"""    <div class="theme-paper">
      <strong><a href="/pages/{arxiv_id.replace('.', '-')}/">{title}</a></strong>
      <p>{summary_sentence}</p>
    </div>
"""
        
        themes_html += f"""  <div class="theme-section">
    <h3>{theme_name}</h3>
{papers_html}  </div>
"""
    
    # Create .astro template
    astro_content = f"""---
import Base from '../../layouts/Base.astro';
import Sidebar from '../../components/Sidebar.astro';
import WikiLink from '../../components/WikiLink.astro';

const title = "Daily summary — {date_str} — ArXiv Atlas";
---
<Base title={{title}}>
  <Sidebar />
  <main class="page-main">
    <h1 class="page-title">Daily summary — {date_str}</h1>
    
    <div class="paper-meta">
      <p><strong>Date:</strong> {date_str}</p>
    </div>
    
    <div class="daily-overview">
      <p>{summary_data.get('overall_summary', 'Summary to be generated')}</p>
    </div>
    
    <h2>Key research themes</h2>
{themes_html}
    
    <h2>References</h2>
    <p>All papers and concepts discussed in this summary are linked to their respective wiki pages. See the theme sections above for detailed references.</p>
  </main>
</Base>
"""
    
    # Write file
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(astro_content)
    
    log(f"Created {file_path}", "INFO")
    return file_path

# ============================================================================
# STEP 5: Update Database
# ============================================================================

def update_database(date_str: str, file_path: str):
    """
    Insert or update the daily summary page row in data/arxiv.db.
    
    Args:
        date_str: "YYYY-MM-DD"
        file_path: Path to .astro file
    """
    log(f"Updating database for {date_str}", "INFO")
    date_slug = date_str.replace("-", "_")
    page_slug = f"pages/daily_{date_slug}"
    title = f"Daily summary \u2014 {date_str}"
    db_access.create_or_get_page(
        page_slug,
        title=title,
        page_type='daily_summary',
        path=file_path
    )
    log(f"Upserted page row for {page_slug}", "INFO")

# ============================================================================
# STEP 6: Update Indices
# ============================================================================

def update_indices(date_str: str, file_path: str):
    """
    Regenerate src/data JSON exports from the DB so the site picks up the new
    daily summary page. Delegates to export_for_site.py.

    Args:
        date_str: "YYYY-MM-DD"
        file_path: Path to .astro file (unused; kept for interface compat)
    """
    log(f"Regenerating src/data exports for {date_str}", "INFO")
    import subprocess
    export_script = Path(__file__).resolve().parent / 'export_for_site.py'
    subprocess.check_call([sys.executable, str(export_script)])
    log(f"src/data exports updated", "INFO")

# ============================================================================
# Orchestrator
# ============================================================================

def generate_daily_summary(date_str: str) -> dict:
    """
    Generate daily summary page for a given date.
    
    Args:
        date_str: Date in format "YYYY-MM-DD" (e.g., "2026-03-16")
    
    Returns:
        {date, success, file_path, errors}
    """
    
    log(f"Starting daily summary generation for {date_str}", "INFO")
    
    try:
        # Step 1: Fetch papers
        papers = fetch_papers_for_date(date_str)
        arxiv_ids = [p["arxiv_id"] for p in papers]
        
        if not arxiv_ids:
            log(f"No papers found for {date_str}", "WARN")
            return {
                "date": date_str,
                "success": False,
                "file_path": None,
                "errors": ["No papers found for this date"]
            }
        
        # Step 2: Read pages
        papers_content = read_pages_for_papers(arxiv_ids)
        
        # Step 3: Generate summary (Sonnet)
        summary_data = generate_summary_themes(papers_content)
        
        # Step 4: Create .astro page
        file_path = create_astro_page(date_str, summary_data)
        
        # Step 5: Update database
        update_database(date_str, file_path)
        
        # Step 6: Update indices
        update_indices(date_str, file_path)
        
        result = {
            "date": date_str,
            "success": True,
            "file_path": file_path,
            "papers_processed": len(arxiv_ids),
            "themes_identified": len(summary_data.get("themes", [])),
            "errors": []
        }
        
        log(f"Daily summary complete for {date_str}", "INFO")
        return result
        
    except Exception as e:
        log(f"Daily summary failed for {date_str}: {e}", "ERROR")
        return {
            "date": date_str,
            "success": False,
            "file_path": None,
            "errors": [str(e)]
        }

# ============================================================================
# CLI
# ============================================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_daily_summary.py --date YYYY-MM-DD")
        sys.exit(1)
    
    date_str = None
    if "--date" in sys.argv:
        date_str = sys.argv[sys.argv.index("--date") + 1]
    
    if not date_str:
        print("Usage: generate_daily_summary.py --date YYYY-MM-DD")
        sys.exit(1)
    
    result = generate_daily_summary(date_str)
    
    # Output JSON for sub-agent to capture
    print(json.dumps(result, indent=2))
    
    sys.exit(0 if result["success"] else 1)
