# AGENTS.md — Esquadrão Classe A

This repository is a **marketplace of agent squads** packaged as Agent Skills, usable across
**Claude Code**, **opencode**, and **Codex**.

## What's here

- **13 squads**, each a team of specialist AI agents with an orchestrator that routes requests.
- Cross-tool skills live in [`.agents/skills/<squad>/`](./.agents/skills) — the directory read
  natively by **opencode** and **Codex**.
- Claude Code plugin packaging lives in each top-level `<squad>/` folder, listed in
  [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json).

## Using a squad (any tool)

Each squad's `SKILL.md` is an **orchestrator**: it diagnoses the request, routes to the right
specialist, reads that specialist's persona file (`agents/<name>.md`), runs the matching task
(`tasks/<name>.md`), and quality-checks the output. Resources are bundled inside each skill
folder and referenced relative to its `SKILL.md`.

Squads (skill names): `advisory-board`, `c-level-squad`, `hormozi-squad`, `copy-master`,
`copy-squad`, `brand-squad`, `storytelling`, `traffic-masters`, `design-squad`, `data-squad`,
`cybersecurity`, `movement`, `claude-code-mastery`.

## Maintaining this repo

- Source of truth for content: `xquads-squads-src/` (gitignored clone of `ohmyjahh/xquads-squads`).
- Regenerate: `python scripts/build_marketplace.py` (Claude plugins + marketplace.json), then
  `python scripts/build_agents_skills.py` (mirror to `.agents/skills/`).
- Install for opencode/Codex globally: `python scripts/install_skills.py`.
- Do NOT re-run `build_marketplace.py` blindly after differentiating orchestrators — it recopies
  resources from source and would revert the renamed orchestrator personas. See
  [`docs/PRD-marketplace-esquadroes.md`](./docs/PRD-marketplace-esquadroes.md).

## License

Squad content mostly MIT (original author: Synkra AIOS). See [`NOTICE`](./NOTICE).
`claude-code-mastery` has an ambiguous upstream license — do not redistribute publicly.
