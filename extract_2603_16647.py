import sys, json, re
from pathlib import Path
pdf_path = Path('/tmp/2603.16647.pdf')
output_bib = Path('/home/node/.openclaw/workspace/projects/arxiv-atlas/data/papers/2603.16647_bibliography.json')
output_bib.parent.mkdir(parents=True, exist_ok=True)
text = ''
# Try PyPDF2, then pdfplumber
try:
    import PyPDF2
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for p in reader.pages:
            try:
                text += p.extract_text() + '\n'
            except Exception:
                pass
    method='PyPDF2'
except Exception as e1:
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            for p in pdf.pages:
                text += p.extract_text() + '\n'
        method='pdfplumber'
    except Exception as e2:
        print(json.dumps({'ok':False,'error':'No PDF libs available','details':str(e1)+'; '+str(e2)}))
        sys.exit(0)
# Basic metadata extraction
title=''
authors=''
abstract=''
# Try to find title as first long line
lines = [l.strip() for l in text.splitlines() if l.strip()]
if lines:
    title = lines[0]
    # look for abstract
    joined = '\n'.join(lines[:200])
    m = re.search(r'Abstract\s*[:\n]\s*(.+?)(?=\n\s*(1\.|Introduction|I\.|Introduction:))', joined, re.S|re.I)
    if m:
        abstract = m.group(1).strip()
# Extract references section: find 'References' or 'REFERENCES'
refs=''
m = re.search(r'\nREFERENCES\n(.+)$', text, re.S|re.I)
if not m:
    m = re.search(r'\nReferences\n(.+)$', text, re.S|re.I)
if m:
    refs = m.group(1).strip()
else:
    # try find 'Acknowledgements' and take text between
    m2 = re.search(r'\nAcknowledgments?\n(.+?)(\n[A-Z][a-z]+|$)', text, re.S)
    if m2:
        # take after that
        after = text.split(m2.group(0))[-1]
        refs = after
# Split references heuristically by lines that start with [number] or digit.
ref_items = []
if refs:
    candidates = re.split(r'\n\s*(\[?\d+\]?\.?\s+)', refs)
    if len(candidates)>1:
        # reassemble
        cur=''
        for part in candidates:
            if re.match(r'\[?\d+\]?\.?\s+', part):
                if cur:
                    ref_items.append(cur.strip())
                cur=''
            else:
                cur += part
        if cur:
            ref_items.append(cur.strip())
    else:
        # fallback split by double newlines
        ref_items = [r.strip() for r in refs.split('\n\n') if r.strip()]
# For each ref, try to extract DOI and first author and title (very heuristic)
bib = []
for r in ref_items:
    doi_match = re.search(r'(10\.\d{4,9}/[^\s,;\)]+)', r)
    doi = doi_match.group(1) if doi_match else None
    # first author: up to comma
    first_author = None
    m = re.match(r'\s*([^,\n]+),', r)
    if m:
        first_author = m.group(1).strip()
    # title in quotes or between year and journal
    title_match = re.search(r'"([^"]{5,})"', r)
    if not title_match:
        # look for patterns: Author (Year). Title. Journal
        m2 = re.search(r'\)\.\s*([^\.\n]{10,200})\.', r)
        title_match = m2
    title_text = title_match.group(1).strip() if title_match and hasattr(title_match,'group') else None
    bib.append({'raw':r, 'doi':doi, 'first_author':first_author, 'title':title_text})
# Save bibliography
with open(output_bib, 'w') as f:
    json.dump({'source_method':method, 'title':title, 'abstract':abstract, 'bibliography':bib}, f, indent=2)
# Extract main sections headings
sections = {}
for sec in ['Introduction','Methods','Methodology','Results','Discussion','Conclusion','Conclusions']:
    m = re.search(r'\n\s*'+sec+'\s*\n(.+?)(\n[A-Z][a-z]+\s*\n|$)', text, re.S)
    if m:
        sections[sec]=m.group(1).strip()[:2000]
# Output summary
out = {'ok':True, 'method':method, 'title':title, 'abstract_present':bool(abstract), 'num_references':len(bib), 'bib_path':str(output_bib), 'sections_found':list(sections.keys())}
print(json.dumps(out))
