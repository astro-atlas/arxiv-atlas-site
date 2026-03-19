Key takeaways block — pipeline spec

Purpose

Every paper analysis must include a prominent "Key takeaways" block (displayed as a highlighted box on the paper page) that summarizes the paper's main scientific results, field-level implications, and broader context. This block is intended for quick-scanning by readers and to drive follow-up priorities.

Format (required)

- Location: Insert immediately after the frontmatter and abstract in data/papers/[arxiv-id].md and the generated paper .astro page.
- Content sections (in order):
  1. Main results — 3–6 bullet points (concise, science-first)
  2. Implications — 1 short paragraph about field-level implications, with an eye to galaxy evolution
  3. Other works -  1 short paragraph about how this paper compares to similar results / where this paper falls in a broader field context 

Rendering

- On the website, render this block as a visually highlighted box with heading "Key takeaways" and include links to recommended follow-ups and related concept pages.

Generation

- Subagents (Sonnet/Opus) must produce this block as part of their output files: data/papers/[arxiv-id]_keytakeaways.md or include the section inside data/papers/[arxiv-id].md under the heading "Key takeaways".

Retroactive updates

- For already-processed papers, generate Key takeaways by synthesizing from existing analysis outputs without re-running full parse unless critical data is missing.

Quality controls

- Every bullet in Main results must be traceable to at least one citation in the paper analysis; add inline references when possible.
- Avoid speculative language; when speculative, label it explicitly ("speculative").

Maintenance

- Keep this spec in instructions/KEY_TAKEAWAYS_SPEC.md and version when changed.
