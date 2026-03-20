# ArXiv Fetcher STATUS

## Purpose
Automated fetcher that pulls new arXiv papers (astro-ph.GA), normalizes metadata, and queues them for sub-agent processing.

## Current State
- [ ] Fetching automation (not implemented)
- [ ] Scheduler (cron/GitHub Actions) for periodic runs
- [ ] Rate limiting and retry logic
- [ ] Deduplication checks against DB

## Next actions
- Implement fetcher script and tests
- Add GitHub Action to run weekly and commit exported JSON + site rebuild
- Track fetcher failures in db.processing_log
