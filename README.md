# ArXiv Atlas — site

This repository contains only the static site for ArXiv Atlas (extracted from a larger workspace). Build instructions:

1. cd projects/arxiv-atlas
2. npm ci
3. npm run build

The site builds into projects/arxiv-atlas/dist which the provided Actions workflow publishes to GitHub Pages.

If you need the full workspace, it still exists in the original repo `astro-atlas/arxiv-atlas`.
