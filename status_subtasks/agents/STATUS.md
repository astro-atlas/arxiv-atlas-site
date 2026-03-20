# Agents STATUS

## Purpose
Sub-agent templates and orchestration for per-paper analysis: fetch HTML/pdf, analyze content, create/update pages, and return summary.

## Current State
- [x] Decision to spawn per-paper sub-agents recorded in memory
- [ ] Template sub-agent task needs implementation
- [ ] Orchestration: how to retry/fan-out/constrain resource use

## Next actions
- Implement template sub-agent script
- Add monitoring and logs for sub-agent runs
- Integrate sub-agents with db_access helpers to claim and finish papers
