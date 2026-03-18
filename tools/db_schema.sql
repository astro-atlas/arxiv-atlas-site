-- Starter schema for ArXiv Atlas SQLite database
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS meta (
  key TEXT PRIMARY KEY,
  value TEXT
);

CREATE TABLE IF NOT EXISTS papers (
  id INTEGER PRIMARY KEY,
  arxiv_id TEXT UNIQUE,
  title TEXT,
  authors TEXT,
  abstract TEXT,
  doi TEXT,
  submitted_date DATE,
  processed_date DATETIME,
  status TEXT DEFAULT 'pending',
  summary_path TEXT,
  metadata_json TEXT,
  score REAL,
  created_at DATETIME DEFAULT (datetime('now')),
  updated_at DATETIME DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_papers_arxiv_id ON papers(arxiv_id);
CREATE INDEX IF NOT EXISTS idx_papers_status ON papers(status);

CREATE TABLE IF NOT EXISTS pages (
  id INTEGER PRIMARY KEY,
  page_slug TEXT UNIQUE,
  title TEXT,
  page_type TEXT,
  source_paper_id INTEGER,
  path TEXT,
  counters_json TEXT,
  metadata_json TEXT,
  created_date DATETIME DEFAULT (datetime('now')),
  updated_date DATETIME DEFAULT (datetime('now')),
  FOREIGN KEY(source_paper_id) REFERENCES papers(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_pages_type ON pages(page_type);

CREATE TABLE IF NOT EXISTS paper_page_links (
  paper_id INTEGER,
  page_id INTEGER,
  role TEXT,
  PRIMARY KEY (paper_id, page_id),
  FOREIGN KEY(paper_id) REFERENCES papers(id) ON DELETE CASCADE,
  FOREIGN KEY(page_id) REFERENCES pages(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS processing_log (
  id INTEGER PRIMARY KEY,
  paper_id INTEGER,
  attempt INTEGER,
  status TEXT,
  message TEXT,
  created_at DATETIME DEFAULT (datetime('now')),
  FOREIGN KEY(paper_id) REFERENCES papers(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS page_links (
  id INTEGER PRIMARY KEY,
  source_page_id INTEGER NOT NULL,
  target_page_slug TEXT NOT NULL,
  link_text TEXT,
  created_at DATETIME DEFAULT (datetime('now')),
  FOREIGN KEY(source_page_id) REFERENCES pages(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_page_links_source ON page_links(source_page_id);
CREATE INDEX IF NOT EXISTS idx_page_links_target ON page_links(target_page_slug);

CREATE TABLE IF NOT EXISTS page_tags (
  page_id INTEGER NOT NULL,
  tag TEXT NOT NULL,
  PRIMARY KEY (page_id, tag),
  FOREIGN KEY(page_id) REFERENCES pages(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_page_tags_tag ON page_tags(tag);

-- schema version
CREATE TABLE IF NOT EXISTS migrations (
  version INTEGER PRIMARY KEY,
  applied_at DATETIME DEFAULT (datetime('now'))
);
