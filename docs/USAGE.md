# Usage Guide — Esquadrão Classe A

**🌐 Language:** **English** · [Português](./USAGE.pt-BR.md)

A practical guide to getting the most out of the squads in Claude Code.

## 1. Concept

Each **squad** is a plugin with:
- an **orchestrator** (the `SKILL.md` skill) that understands your request and decides who solves it;
- several **specialists** (personas in `agents/`) that the orchestrator "wears" to do the work;
- **tasks** (executable steps in `tasks/`) and **workflows** (multi-step flows).

You never need to memorize specialist names: describe the problem and the orchestrator routes it.

## 2. Three ways to invoke

1. **Natural (recommended):** just ask. The skill activates from context.
   > "I need to rewrite my course's sales page; the audience is cold."
2. **Dedicated command:** `/<squad> <request>`.
   > `/copy-squad rewrite my sales page for a cold audience`
3. **Specific specialist:** if you already know who you want, ask by name.
   > "Use Eugene Schwartz's approach to diagnose the awareness level."

## 3. Examples by squad

| You want… | Squad | Example request |
|---|---|---|
| A headline / VSL / email / sales letter | `copy-squad` or `copy-master` | `/copy-squad 10 headlines for an English-course ad` |
| To decide something strategic (partner, investment, pivot) | `advisory-board` | `/advisory-board is it worth taking an investor for 30%?` |
| Executive perspective (CEO/CTO/CFO/CMO) | `c-level-squad` | `/c-level-squad how should I structure next year's product roadmap?` |
| To build an irresistible offer | `hormozi-squad` | `/hormozi-squad turn my service into a Grand Slam Offer` |
| To position/name a brand | `brand-squad` | `/brand-squad archetype and tone of voice for a specialty coffee brand` |
| To structure a narrative | `storytelling` | `/storytelling story arc for the launch video` |
| To fix a paid-traffic campaign | `traffic-masters` | `/traffic-masters my CPA doubled this week, what should I investigate?` |
| Product/UX design | `design-squad` | `/design-squad onboarding flow for a fintech app` |
| Data analysis / BI | `data-squad` | `/data-squad how do I model churn with the data I have?` |
| Security/audit | `cybersecurity` | `/cybersecurity hardening checklist for my Laravel API` |
| To build a movement/community | `movement` | `/movement plan to launch a community around my cause` |
| To master Claude Code itself | `claude-code-mastery` | `/claude-code-mastery create hooks to run tests on save` |

## 4. A typical session flow

1. **Ask.** The orchestrator diagnoses and tells you which specialist will act.
2. **Refine.** Answer the diagnostic questions (audience, objective, constraints).
3. **Receive the work**, already run through the squad's quality check.
4. **Iterate.** Ask a second specialist for another opinion, or run a full workflow.

## 5. Tips

- **Combine squads:** copy + traffic + design cover an entire launch.
- **Workflows** deliver end-to-end projects (e.g., `copy-squad` has a "full copy project"):
  ask to "run the full workflow".
- **Quality:** for extra rigor, ask to "review against the squad's checklist".
- **KNOWN-GAPS:** some squads have orchestrator commands from the original without a ready
  task — they are documented at the end of each `SKILL.md`. Ask anyway and the specialist
  will handle it.

## 6. Updating/rebuilding

The marketplace is reproducible from the source (see `README.md` › "How the marketplace is
built"). To update when the source changes: re-clone `xquads-squads-src/`, run
`scripts/classify_orphans.py` and `scripts/build_marketplace.py`, and review the `SKILL.md` files.
