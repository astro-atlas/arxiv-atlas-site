"""Minimal SQLite access layer for ArXiv Atlas.
Plain sqlite3 (no ORM) with basic helpers for sub-agents and export script.
"""
import sqlite3
import json
import time
from contextlib import contextmanager
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "arxiv.db"
SCHEMA_SQL = Path(__file__).resolve().parent / "db_schema.sql"

# Simple retry params for busy DB
RETRY_SLEEP = 0.1
RETRY_COUNT = 10


def migrate():
    """Apply starter schema if DB missing/tables missing."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DB_PATH.exists():
        DB_PATH.touch()
    with sqlite_conn() as conn:
        sql = SCHEMA_SQL.read_text()
        conn.executescript(sql)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.commit()


@contextmanager
def sqlite_conn():
    for attempt in range(RETRY_COUNT):
        try:
            conn = sqlite3.connect(str(DB_PATH), timeout=30)
            conn.row_factory = sqlite3.Row
            # Enforce foreign keys
            conn.execute("PRAGMA foreign_keys = ON;")
            yield conn
            conn.close()
            return
        except sqlite3.OperationalError as e:
            if 'database is locked' in str(e).lower() and attempt < RETRY_COUNT - 1:
                time.sleep(RETRY_SLEEP)
                continue
            raise


# Papers helpers

def claim_paper_for_processing(arxiv_id):
    """Atomically insert or set status=processing and return paper row id."""
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("BEGIN IMMEDIATE")
        cur.execute(
            "SELECT id, status FROM papers WHERE arxiv_id = ?",
            (arxiv_id,)
        )
        row = cur.fetchone()
        if row is None:
            cur.execute(
                "INSERT INTO papers (arxiv_id, status, created_at, updated_at) VALUES (?, 'processing', datetime('now'), datetime('now'))",
                (arxiv_id,)
            )
            paper_id = cur.lastrowid
        else:
            paper_id = row[0]
            cur.execute(
                "UPDATE papers SET status='processing', updated_at=datetime('now') WHERE id = ?",
                (paper_id,)
            )
        conn.commit()
        return paper_id


def finish_paper(arxiv_id, title=None, authors=None, abstract=None, doi=None, submitted_date=None, processed_date=None, summary_path=None, metadata=None, score=None, status='done'):
    """Update paper record when processing finishes."""
    metadata_json = json.dumps(metadata or {})
    with sqlite_conn() as conn:
        conn.execute(
            "UPDATE papers SET title = COALESCE(?, title), authors = COALESCE(?, authors), abstract = COALESCE(?, abstract), doi = COALESCE(?, doi), submitted_date = COALESCE(?, submitted_date), processed_date = COALESCE(?, processed_date), summary_path = COALESCE(?, summary_path), metadata_json = COALESCE(?, metadata_json), score = COALESCE(?, score), status = ?, updated_at = datetime('now') WHERE arxiv_id = ?",
            (title, authors, abstract, doi, submitted_date, processed_date, summary_path, metadata_json, score, status, arxiv_id)
        )
        conn.commit()


# Pages helpers

def create_or_get_page(page_slug, title=None, page_type=None, source_paper_id=None, path=None, metadata=None):
    metadata_json = json.dumps(metadata or {})
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id FROM pages WHERE page_slug = ?", (page_slug,))
        row = cur.fetchone()
        if row:
            return row[0]
        cur.execute(
            "INSERT INTO pages (page_slug, title, page_type, source_paper_id, path, metadata_json, created_date, updated_date) VALUES (?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))",
            (page_slug, title, page_type, source_paper_id, path, metadata_json)
        )
        conn.commit()
        return cur.lastrowid


def link_paper_page(paper_id, page_id, role='mentions'):
    with sqlite_conn() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO paper_page_links (paper_id, page_id, role) VALUES (?, ?, ?)",
            (paper_id, page_id, role)
        )
        conn.commit()


def add_page_link(source_page_id, target_page_slug, link_text=None):
    """Insert a directed link from source page to target slug (stub-safe)."""
    with sqlite_conn() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO page_links (source_page_id, target_page_slug, link_text) VALUES (?, ?, ?)",
            (source_page_id, target_page_slug, link_text)
        )
        conn.commit()


def set_page_tags(page_id, tags):
    """Replace all tags for a page. tags is a list of strings."""
    with sqlite_conn() as conn:
        conn.execute("DELETE FROM page_tags WHERE page_id = ?", (page_id,))
        for tag in tags:
            conn.execute(
                "INSERT OR IGNORE INTO page_tags (page_id, tag) VALUES (?, ?)",
                (page_id, tag)
            )
        conn.commit()


def get_page_tags(page_id):
    """Return list of tag strings for a page."""
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT tag FROM page_tags WHERE page_id = ? ORDER BY tag", (page_id,))
        return [r['tag'] for r in cur.fetchall()]


def log_processing(paper_id, attempt, status, message=None):
    """Append a row to processing_log."""
    with sqlite_conn() as conn:
        conn.execute(
            "INSERT INTO processing_log (paper_id, attempt, status, message) VALUES (?, ?, ?, ?)",
            (paper_id, attempt, status, message)
        )
        conn.commit()


# Query helpers used by export

def recent_papers(limit=20):
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, arxiv_id, title, authors, processed_date, status, summary_path FROM papers WHERE status = 'done' ORDER BY processed_date DESC LIMIT ?", (limit,))
        return [dict(r) for r in cur.fetchall()]


def stats():
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT status, COUNT(*) as cnt FROM papers GROUP BY status")
        by_status = {r['status']: r['cnt'] for r in cur.fetchall()}
        cur.execute("SELECT COUNT(*) as total FROM papers")
        total = cur.fetchone()['total']
        cur.execute("SELECT COUNT(*) as pages FROM pages")
        pages = cur.fetchone()['pages']
        return {'total_papers': total, 'papers_by_status': by_status, 'total_pages': pages}


def all_papers_index():
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, arxiv_id, title, authors, processed_date, status, summary_path FROM papers ORDER BY processed_date DESC")
        return [dict(r) for r in cur.fetchall()]


def all_pages_index():
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, page_slug, title, page_type, path, created_date FROM pages ORDER BY created_date DESC")
        return [dict(r) for r in cur.fetchall()]


def paper_pages(limit=None):
    """Return paper pages joined with papers table for rich metadata."""
    with sqlite_conn() as conn:
        cur = conn.cursor()
        q = """
            SELECT p.page_slug, p.title AS page_title, p.path, p.created_date,
                   pa.arxiv_id, pa.title AS paper_title, pa.authors,
                   pa.processed_date, pa.status
            FROM pages p
            LEFT JOIN papers pa ON p.source_paper_id = pa.id
            WHERE p.page_type = 'paper'
            ORDER BY p.created_date DESC
        """
        if limit:
            q += f" LIMIT {int(limit)}"
        cur.execute(q)
        return [dict(r) for r in cur.fetchall()]


def daily_summary_pages():
    """Return all daily summary pages."""
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT page_slug, title, path, created_date
            FROM pages WHERE page_type = 'daily_summary'
            ORDER BY created_date DESC
        """)
        return [dict(r) for r in cur.fetchall()]


def all_page_tags():
    """Return {page_slug: [tags]} for all pages that have tags."""
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT p.page_slug, pt.tag
            FROM page_tags pt
            JOIN pages p ON pt.page_id = p.id
            ORDER BY p.page_slug, pt.tag
        """)
        result = {}
        for r in cur.fetchall():
            result.setdefault(r['page_slug'], []).append(r['tag'])
        return result


def stub_links():
    """Return target slugs that are linked-to but don't exist as pages."""
    with sqlite_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT pl.target_page_slug
            FROM page_links pl
            LEFT JOIN pages p ON pl.target_page_slug = p.page_slug
            WHERE p.page_slug IS NULL
            ORDER BY pl.target_page_slug
        """)
        return [r['target_page_slug'] for r in cur.fetchall()]


if __name__ == '__main__':
    print('Running migrate() and printing stats')
    migrate()
    print(stats())
