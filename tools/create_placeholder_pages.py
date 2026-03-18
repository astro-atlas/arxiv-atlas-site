"""Create placeholder page records in DB for targets referenced in page_links but missing a pages record.
Marks placeholders with metadata_json={'placeholder': true} and leaves path NULL so generate_links can set exists based on disk.
"""
import sqlite3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access
import json

DB = db_access.DB_PATH


def normalize_slug(s):
    if not s:
        return None
    s = s.strip()
    s = s.lstrip('/').rstrip('/')
    s = s.replace(' ', '-').replace('_', '-').lower()
    return s


def main():
    db_access.migrate()
    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT target_page_slug FROM page_links')
    rows = cur.fetchall()
    created = 0
    for r in rows:
        raw = r['target_page_slug']
        slug = normalize_slug(raw)
        if not slug:
            continue
        # Check if pages record exists
        cur.execute('SELECT id, path FROM pages WHERE page_slug = ?', (slug,))
        if cur.fetchone():
            continue
        # create placeholder page record
        metadata = json.dumps({'placeholder': True})
        title = slug.split('/')[-1].replace('-', ' ').title()
        cur.execute('INSERT INTO pages (page_slug, title, page_type, source_paper_id, path, counters_json, metadata_json, created_date, updated_date) VALUES (?, ?, ?, NULL, NULL, NULL, ?, datetime(\'now\'), datetime(\'now\'))', (slug, title, 'concept', metadata))
        created += 1
    conn.commit()
    conn.close()
    print('Created', created, 'placeholder pages')

if __name__ == '__main__':
    main()
