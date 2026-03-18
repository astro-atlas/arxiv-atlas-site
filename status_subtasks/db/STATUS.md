# DB STATUS

## Purpose
Store canonical records of papers, pages, and links; serve as authoritative source for weekly site exports.

## Current State
- [x] Starter SQLite schema created (db_schema.sql)
- [x] db_access.py access layer implemented (plain sqlite3)
- [x] WAL mode enabled and basic retry on busy
- [x] Seeded DB with existing analyzed papers

## Next actions
- Add backup/export policy (e.g., commit DB weekly, or export SQL dump)
- Add migrations/upgrade process for schema changes
- Consider Postgres if concurrency grows
