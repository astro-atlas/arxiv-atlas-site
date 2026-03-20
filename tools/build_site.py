"""Top-level build script: export DB -> generate links -> run npm build (if available).
Run this locally or in CI before publishing to GitHub Pages.
"""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import db_access

ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / 'tools' / 'export_for_site.py'
GEN = ROOT / 'tools' / 'generate_links.py'


def run(cmd, cwd=ROOT):
    print('Running:', ' '.join(cmd))
    subprocess.check_call(cmd, cwd=str(cwd))


def main():
    db_access.migrate()
    run(['python3', str(EXPORT)])
    run(['python3', str(GEN)])
    # try to run npm build if available
    try:
        run(['npm', 'run', 'build'])
    except Exception as e:
        print('npm run build failed or not available; export + links.json completed:', e)

if __name__ == '__main__':
    main()
