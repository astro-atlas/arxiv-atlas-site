"""Scan src/pages and src/content/pages for page files and ensure there's a pages DB record for each.
Creates page records with page_slug set to the relative path under src/pages (no extension).
Supports both .astro (legacy) and .mdx (content collection) files.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
SRC_PAGES = ROOT / 'src' / 'pages'
CONTENT_PAGES = ROOT / 'src' / 'content' / 'pages'


def slug_from_path(p: Path):
    rel = p.relative_to(SRC_PAGES).with_suffix('')
    return str(rel).replace('\\', '/').lower()


def main():
    db_access.migrate()

    # Scan .astro files under src/pages/
    for p in SRC_PAGES.rglob('*.astro'):
        if p.stem.startswith(('_', '[')):
            continue
        slug = slug_from_path(p)
        title = p.stem.replace('-', ' ').title()
        page_type = 'concept' if 'concepts' in slug else ('paper' if 'papers' in slug else 'page')
        created = db_access.create_or_get_page(slug, title=title, page_type=page_type, path=str(p))
        print('Ensured page:', slug, '-> id', created)

    # Scan .mdx files under src/content/pages/
    if CONTENT_PAGES.exists():
        for p in CONTENT_PAGES.rglob('*.mdx'):
            slug = 'pages/' + p.stem.lower()
            title = p.stem.replace('-', ' ').title()
            page_type = 'page'
            created = db_access.create_or_get_page(slug, title=title, page_type=page_type, path=str(p))
            print('Ensured page (mdx):', slug, '-> id', created)

if __name__ == '__main__':
    main()
