# Esquadrão Classe A 🎖️

**🌐 Language:** **English** · [Português](./README.pt-BR.md)

**A plugin marketplace for [Claude Code](https://claude.com/claude-code).**
Each plugin is a **squad** — a team of specialist AI agents led by an **orchestrator**
that diagnoses your request, routes it to the right specialist, and delivers the work
with a quality check.

**13 squads** · **177 specialist agents** · **135 tasks** · **28 workflows**, all
invocable as Claude Code skills.

> **Private/personal project.** Content adapted from the open-source project
> [`ohmyjahh/xquads-squads`](https://github.com/ohmyjahh/xquads-squads) (original author:
> Synkra AIOS). Credits and license in [`NOTICE`](./NOTICE). Marketplace format inspired by
> [`mwguerra/claude-code-plugins`](https://github.com/mwguerra/claude-code-plugins).

---

## 🚀 Installation

In Claude Code, register the marketplace and install the squads you want:

```bash
# 1. Register the marketplace (once)
/plugin marketplace add andersonoliveiraventurini/esquadrao-classe-a

# 2. Install a squad
/plugin install copy-squad@esquadrao-classe-a

# 3. (optional) install the ones you care about
/plugin install advisory-board@esquadrao-classe-a
/plugin install traffic-masters@esquadrao-classe-a
```

> Tip: to test locally from a clone of the repo, run `/plugin marketplace add .` at the
> project root.

---

## 🧭 How to use

After installing, just ask naturally — the squad's skill activates on its own from context —
or call the dedicated command:

```bash
/copy-squad I need a headline for an English-course ad
/advisory-board should I accept an investor who wants 30% of the company?
/traffic-masters my Meta campaign has a high CPA, what should I investigate?
```

The orchestrator then:
1. **Diagnoses** the request (type of work, context, objective).
2. **Routes** to the right specialist(s).
3. **Adopts the persona** of the specialist (by reading the agent file) and **runs the task**.
4. **Checks quality** before delivering.

> The synthesized orchestration layer (each squad's `SKILL.md`) is written in **Brazilian
> Portuguese** to maximize skill-activation accuracy for the author's prompts. The squads
> understand and respond in any language — feel free to prompt in English.

---

## 🎯 The 13 Squads

| Squad | Focus | Agents | Install |
|-------|-------|:------:|---------|
| `advisory-board` | Mentor council for strategic business & life decisions | 11 | `/plugin install advisory-board@esquadrao-classe-a` |
| `c-level-squad` | Executive C-level council (CEO/CTO/CFO/CMO…) | 6 | `/plugin install c-level-squad@esquadrao-classe-a` |
| `hormozi-squad` | Irresistible offers, monetization & scaling (Hormozi-style) | 16 | `/plugin install hormozi-squad@esquadrao-classe-a` |
| `copy-master` | Elite copywriting — 32 legendary copywriters | 33 | `/plugin install copy-master@esquadrao-classe-a` |
| `copy-squad` | Direct-response copywriting — 22 copywriters | 23 | `/plugin install copy-squad@esquadrao-classe-a` |
| `brand-squad` | Branding, identity & market positioning | 15 | `/plugin install brand-squad@esquadrao-classe-a` |
| `storytelling` | Narrative, scriptwriting & story-driven communication | 12 | `/plugin install storytelling@esquadrao-classe-a` |
| `traffic-masters` | Paid traffic & performance media (Meta/Google Ads) | 16 | `/plugin install traffic-masters@esquadrao-classe-a` |
| `design-squad` | Product design, UX/UI & visual systems | 8 | `/plugin install design-squad@esquadrao-classe-a` |
| `data-squad` | Data, BI, analytics & data-driven growth | 7 | `/plugin install data-squad@esquadrao-classe-a` |
| `cybersecurity` | Offensive/defensive security, audits & incident response | 15 | `/plugin install cybersecurity@esquadrao-classe-a` |
| `movement` | Building movements, causes & communities | 7 | `/plugin install movement@esquadrao-classe-a` |
| `claude-code-mastery` ⚠️ | Mastering Claude Code itself (hooks, skills, MCP, subagents) | 8 | `/plugin install claude-code-mastery@esquadrao-classe-a` |

⚠️ `claude-code-mastery` has an **ambiguous license** upstream (no MIT declaration). Use it for
personal purposes; **do not redistribute publicly** without confirming provenance. See
[`NOTICE`](./NOTICE).

---

## 🗂️ Plugin structure

```
<squad>/
├── .claude-plugin/plugin.json        # plugin manifest
├── commands/<squad>.md               # slash command that activates the skill
└── skills/<squad>/
    ├── SKILL.md                      # orchestrator (routing + catalog)
    ├── agents/                       # specialist personas
    ├── tasks/                        # executable tasks
    ├── workflows/                    # multi-agent flows
    ├── checklists/                   # quality criteria
    └── data/                         # supporting data (frameworks, catalogs)
```

The root has `.claude-plugin/marketplace.json` listing all 13 plugins.

---

## 🛠️ How the marketplace is built (reproducible)

Content is generated from the source by scripts in [`scripts/`](./scripts):

```bash
python -m pip install --user pyyaml
cd scripts
python classify_orphans.py     # orphan-reference report -> docs/relatorio-orfas.md
python build_marketplace.py    # scaffold all 13 plugins + marketplace.json
```

- `lib_squads.py` — squad list, manifest reader, and rebrand map.
- `classify_orphans.py` — classifies references to non-existent tasks (missing input vs runtime output).
- `build_marketplace.py` — copies resources (with rebrand), generates `plugin.json`, commands and `marketplace.json`.

The `SKILL.md` files (PT-BR orchestration layer) are authored on top of that scaffold.

---

## 📚 Documentation

- [`docs/USAGE.md`](./docs/USAGE.md) — practical usage guide (English) · [Português](./docs/USAGE.pt-BR.md)
- [`docs/PRD-marketplace-esquadroes.md`](./docs/PRD-marketplace-esquadroes.md) — requirements & decisions (PT).
- [`docs/superpowers/plans/2026-06-06-marketplace-esquadroes.md`](./docs/superpowers/plans/2026-06-06-marketplace-esquadroes.md) — implementation plan (PT).
- [`docs/relatorio-orfas.md`](./docs/relatorio-orfas.md) — orphan-reference QA report.

---

## ⚖️ License & credits

Squad content: mostly **MIT** (original author **Synkra AIOS**) — see [`NOTICE`](./NOTICE).
Adaptation layer (orchestration, commands, marketplace identity): Anderson de Oliveira Venturini.
