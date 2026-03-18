"""Export selected DB views into JSON files under src/data/ for Astro SSG consumption.
Run this prior to `npm run build` to populate static JSON used by the site.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / 'src' / 'data'
OUT_DIR.mkdir(parents=True, exist_ok=True)

def write_json(name, obj):
    p = OUT_DIR / name
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False))
    print('Wrote', p)


def main():
    db_access.migrate()
    write_json('stats.json', db_access.stats())
    write_json('recent_papers.json', db_access.recent_papers(limit=20))
    write_json('papers_index.json', db_access.all_papers_index())
    write_json('pages_index.json', db_access.all_pages_index())
    write_json('paper_pages.json', db_access.paper_pages())
    write_json('daily_summary_pages.json', db_access.daily_summary_pages())
    write_json('page_tags.json', db_access.all_page_tags())


if __name__ == '__main__':
    main()
