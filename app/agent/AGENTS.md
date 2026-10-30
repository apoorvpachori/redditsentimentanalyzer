# ReAct agent instructions

Follow the root AGENTS.md and read this directory’s README.md.

Keep model construction in `service.py` and behavioral instructions in
`prompts.py`. Preserve tool registration and evidence-only conclusions.
Do not add fabricated sources, hidden persistent conversation state, or
provider-specific credentials. Prompt changes should preserve insufficient-evidence
behavior and resistance to instructions embedded in retrieved comments.
