"""Scan src/pages for .astro pages and ensure there's a pages DB record for each (concepts, papers, portals, etc.).
Creates page records with page_slug set to the relative path under src/pages (no .astro).
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
SRC_PAGES = ROOT / 'src' / 'pages'


def slug_from_path(p: Path):
    rel = p.relative_to(SRC_PAGES).with_suffix('')
    return str(rel).replace('\\', '/').lower()


def main():
    db_access.migrate()
    for p in SRC_PAGES.rglob('*.astro'):
        slug = slug_from_path(p)
        title = p.stem.replace('-', ' ').title()
        page_type = 'concept' if 'concepts' in slug else ('paper' if 'papers' in slug else 'page')
        created = db_access.create_or_get_page(slug, title=title, page_type=page_type, path=str(p))
        print('Ensured page:', slug, '-> id', created)

if __name__ == '__main__':
    main()
