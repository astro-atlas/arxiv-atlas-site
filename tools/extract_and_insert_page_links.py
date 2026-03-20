"""Extract links from .astro pages (WikiLink components and internal anchors) and insert into page_links table.
Conservative: looks for <WikiLink slug="..." and href="/..." patterns.
Run: PYTHONPATH=projects/arxiv-atlas python3 projects/arxiv-atlas/tools/extract_and_insert_page_links.py
"""
import re
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
SRC_PAGES = ROOT / 'src' / 'pages'

WIKILINK_RE = re.compile(r'WikiLink\s+[^>]*slug=\"([^\"]+)\"', re.IGNORECASE)
HREF_RE = re.compile(r'href=\"(/(?:papers|concepts|pages)/[^\"]+)\"', re.IGNORECASE)


def normalize_slug(s):
    if not s:
        return None
    s = s.strip()
    s = s.lstrip('/').rstrip('/')
    s = s.replace(' ', '-').replace('_', '-').lower()
    # remove leading 'pages/' if present to keep consistent (we store slugs as e.g. pages/...) - keep full path
    return s


def insert_link(conn, source_id, target_slug, link_text=None):
    cur = conn.cursor()
    cur.execute('INSERT OR IGNORE INTO page_links (source_page_id, target_page_slug, link_text) VALUES (?, ?, ?)', (source_id, target_slug, link_text))


def find_page_id(conn, slug):
    cur = conn.cursor()
    cur.execute('SELECT id FROM pages WHERE page_slug = ?', (slug,))
    r = cur.fetchone()
    return r[0] if r else None


def main():
    db_access.migrate()
    conn = sqlite3.connect(str(db_access.DB_PATH))
    conn.row_factory = sqlite3.Row
    count = 0
    for p in SRC_PAGES.rglob('*.astro'):
        text = p.read_text()
        # compute slug used in pages table
        rel = p.relative_to(SRC_PAGES).with_suffix('')
        source_slug = str(rel).replace('\\', '/').lower()
        cur = conn.cursor()
        cur.execute('SELECT id FROM pages WHERE page_slug = ?', (source_slug,))
        row = cur.fetchone()
        if not row:
            # ensure page exists
            pid = db_access.create_or_get_page(source_slug, title=p.stem, page_type='page', path=str(p))
        else:
            pid = row['id']
        # find WikiLink components
        for m in WIKILINK_RE.finditer(text):
            target_raw = m.group(1)
            target = normalize_slug(target_raw)
            if target:
                insert_link(conn, pid, target, link_text=None)
                count += 1
        # find hrefs
        for m in HREF_RE.finditer(text):
            target_raw = m.group(1)
            target = normalize_slug(target_raw)
            if target:
                insert_link(conn, pid, target, link_text=None)
                count += 1
    conn.commit()
    conn.close()
    print('Inserted/ensured', count, 'links (INSERT OR IGNORE used)')

if __name__ == '__main__':
    main()
