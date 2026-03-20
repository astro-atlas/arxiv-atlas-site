"""Ingest a paper manifest (JSON) into arxiv.db.

Usage:
    python3 tools/ingest_manifest.py '{"arxiv_id": "2603.15899", ...}'
    python3 tools/ingest_manifest.py data/papers/2603.15899_manifest.json

Reads a manifest dict (from file path or inline JSON) and:
1. Upserts paper into `papers` table
2. Inserts all pages into `pages` table (with source_paper_id for paper pages)
3. Links paper ↔ pages in `paper_page_links`
4. Extracts page_links from .md files on disk
5. Prints summary
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access


def ingest(manifest: dict):
    db_access.migrate()
    arxiv_id = manifest["arxiv_id"]

    # 1. Upsert paper
    paper_id = db_access.claim_paper_for_processing(arxiv_id)
    db_access.finish_paper(
        arxiv_id,
        title=manifest.get("title"),
        authors=json.dumps(manifest.get("authors", [])),
        doi=manifest.get("doi"),
        submitted_date=manifest.get("date"),
        summary_path=manifest.get("analysis_file"),
        metadata=manifest.get("key_takeaways"),
        status=manifest.get("status", "done"),
    )
    print(f"✓ Paper {arxiv_id} → id={paper_id}")

    # 2. Insert pages
    for page in manifest.get("pages_created", []):
        slug = page["slug"]
        page_type = page.get("type", "concept")
        title = page.get("title", slug)
        path = f"src/content/pages/{slug}.md"
        source = paper_id if page_type == "paper" else None
        metadata = {}
        if page.get("level"):
            metadata["level"] = page["level"]

        page_id = db_access.create_or_get_page(
            page_slug=slug,
            title=title,
            page_type=page_type,
            source_paper_id=source,
            path=path,
            metadata=metadata,
        )
        # Link paper ↔ page
        role = "primary" if page_type == "paper" else "introduces"
        db_access.link_paper_page(paper_id, page_id, role=role)
        print(f"  ✓ Page {slug} ({page_type}) → id={page_id}")

    # 3. Record modified pages as 'mentions' links
    for mod in manifest.get("pages_modified", []):
        from contextlib import suppress
        with suppress(Exception):
            # Get page id for the modified page
            mod_page_id = db_access.create_or_get_page(
                page_slug=mod["slug"], page_type="concept"
            )
            db_access.link_paper_page(paper_id, mod_page_id, role="mentions")
            print(f"  ✓ Modified page {mod['slug']} linked")

    print(f"\nDone. Paper {arxiv_id}: {len(manifest.get('pages_created', []))} pages created, "
          f"{len(manifest.get('pages_modified', []))} pages modified.")
    return paper_id


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ingest_manifest.py <manifest.json or JSON string>")
        sys.exit(1)

    arg = sys.argv[1]
    path = Path(arg)
    if path.exists():
        manifest = json.loads(path.read_text())
    else:
        manifest = json.loads(arg)

    ingest(manifest)


if __name__ == "__main__":
    main()
