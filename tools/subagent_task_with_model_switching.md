# Model Switching Architecture — DEPRECATED

**⚠️ This file described an intended architecture that does NOT work as designed.**

## What Was Wrong

The original design assumed subagents could call `sessions_send()` to invoke different models (GPT, Sonnet, Opus) within a single subagent session. **This is incorrect.**

**Subagents do NOT have access to:**
- `sessions_send`
- `sessions_spawn`
- `sessions_list`
- `sessions_history`
- `subagents`

Subagents only have: `read`, `write`, `edit`, `exec`, `process`, `web_fetch`, `web_search`, `image`.

## How Model Switching Actually Works

The **main agent (orchestrator)** handles all model switching by spawning separate subagents for each pipeline step:

1. **Spawn GPT subagent** → Steps 1 & 2: Fetch paper, extract tarball/bib, write metadata
2. **Spawn Sonnet subagent** → Step 3: Section-by-section analysis with citations and concepts
3. **Spawn GPT subagent** → Steps 4 & 5: Check wiki connections, recommend pages
4. **Spawn Opus subagent** → Steps 6 & 7: Critical analysis and key takeaways
5. **Spawn Opus subagent** → Step 8: Write wiki pages

Data passes between steps via the filesystem (`data/papers/[arxiv-id].md` and temp files).

The orchestrator reads each subagent's output, verifies quality, and spawns the next step.

## Reference

See `instructions/SUBAGENT_PARSE_WORKFLOW.md` for the canonical step-by-step workflow.
See `instructions/ARXIV_WORKFLOW.md` for the main agent's orchestration flow.

---
_Updated 2026-03-18: Corrected after testing confirmed subagents lack session tools._
