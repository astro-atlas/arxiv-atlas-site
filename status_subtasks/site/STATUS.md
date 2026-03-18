# Site STATUS

## Purpose
Astro static site that presents the ArXiv Atlas content on GitHub Pages.

## Current State
- [x] Migration to Astro SSG complete
- [x] Templates, components, and pages in place
- [x] JSON export integration (export_for_site.py) writes to src/data/

## Next actions
- Add npm script: "build:site": "python tools/export_for_site.py && npm run build"
- Add GitHub Action to run weekly: export -> build -> commit/publish to gh-pages
- Visual tests for regressions (optional)
