"""Generate links.json by reading page_links from DB and scanning src/pages for existing pages."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
SRC_PAGES = ROOT / 'src' / 'pages'
OUT = ROOT / 'src' / 'data' / 'links.json'


def normalize_slug(s):
    """Canonical slug: lowercase, spaces/hyphens → underscores, strip slashes."""
    if s is None:
        return s
    s = s.strip()
    s = s.lstrip('/').rstrip('/')
    s = s.replace(' ', '_').replace('-', '_').lower()
    return s


def scan_disk_pages():
    # Gather page slugs from files under src/pages, normalized
    slugs = set()
    for p in SRC_PAGES.rglob('*.astro'):
        rel = p.relative_to(SRC_PAGES).with_suffix('')
        slug = str(rel).replace('\\', '/').lower()
        slugs.add(normalize_slug(slug))
    return slugs


def build_link_map():
    slugs_on_disk = scan_disk_pages()
    pages = db_access.all_pages_index()
    page_map = {normalize_slug(p['page_slug']): p for p in pages}

    # gather page_links from DB
    import sqlite3
    conn = sqlite3.connect(str(db_access.DB_PATH))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT source_page_id, target_page_slug, link_text FROM page_links')
    rows = cur.fetchall()
    links_by_source = {}
    for r in rows:
        sid = r['source_page_id']
        target_norm = normalize_slug(r['target_page_slug'])
        links_by_source.setdefault(sid, []).append({'target': target_norm, 'text': r['link_text']})

    # reverse map: target -> list of sources
    linked_from = {}
    for sid, items in links_by_source.items():
        source_slug = None
        # find source slug from pages
        for slug, p in page_map.items():
            if p['id'] == sid:
                source_slug = slug
                break
        for it in items:
            linked_from.setdefault(it['target'], []).append({'source': source_slug, 'text': it['text']})

    # assemble final map
    link_map = {}
    for slug, p in page_map.items():
        exists = slug in slugs_on_disk
        outgoing = [{'target': it['target'], 'text': it['text'], 'exists': (it['target'] in slugs_on_disk)} for it in links_by_source.get(p['id'], [])]
        incoming = linked_from.get(slug, [])
        link_map[slug] = {
            'title': p.get('title'),
            'exists': exists,
            'links_to': outgoing,
            'linked_from': incoming,
            'path': p.get('path')
        }

    # also include targets that are referred-to but not in pages table
    for target, sources in linked_from.items():
        if target not in link_map:
            link_map[target] = {
                'title': None,
                'exists': (target in slugs_on_disk),
                'links_to': [],
                'linked_from': sources,
                'path': None
            }
    return link_map


def main():
    db_access.migrate()
    lm = build_link_map()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(lm, indent=2, ensure_ascii=False))
    print('Wrote', OUT)

if __name__ == '__main__':
    main()
