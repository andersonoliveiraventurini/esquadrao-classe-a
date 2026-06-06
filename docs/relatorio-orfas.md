# Relatório de Refs Órfãs

Gerado por `scripts/classify_orphans.py`.

- `(i) input faltando` → **OMITIR** do SKILL.md + registrar em KNOWN-GAPS.
- `(ii) output runtime` → **MANTER** (é arquivo que o agente gera, não um gap).

## advisory-board

**input faltando (omitir): 0**

**output runtime (manter): 0**

## brand-squad

**input faltando (omitir): 0**

**output runtime (manter): 0**

## cybersecurity

**input faltando (omitir): 0**

**output runtime (manter): 0**

## design-squad

**input faltando (omitir): 0**

**output runtime (manter): 0**

## hormozi-squad

**input faltando (omitir): 0**

**output runtime (manter): 0**

## storytelling

**input faltando (omitir): 0**

**output runtime (manter): 0**

## traffic-masters

**input faltando (omitir): 0**

**output runtime (manter): 0**

## copy-master

**input faltando (omitir): 2**
- `compare-approaches.md` — task: compare-approaches.md
- `create-copy-brief.md` — task: create-copy-brief.md

**output runtime (manter): 0**

## copy-squad

**input faltando (omitir): 2**
- `compare-approaches.md` — task: compare-approaches.md
- `create-copy-brief.md` — task: create-copy-brief.md

**output runtime (manter): 0**

## movement

**input faltando (omitir): 0**

**output runtime (manter): 0**

## data-squad

**input faltando (omitir): 2**
- `multi-specialist-report.md` — task: multi-specialist-report.md
- `route-data-question.md` — task: route-data-question.md

**output runtime (manter): 0**

## c-level-squad

**input faltando (omitir): 0**

**output runtime (manter): 0**

## claude-code-mastery

**input faltando (omitir): 21**
- `agent-authority.md` — reference: ".claude/settings.json (deny/allow rules), .claude/rules/agent-authority.md"
- `api-docs.md` — +-- api-docs.md    # Detailed reference loaded on demand
- `api-rules.md` — 1. Extract API rules to `.claude/rules/api-rules.md` with `paths: ["src/api/**"]`
- `architecture.md` — 3. Move framework docs to `@docs/architecture.md` import
- `backend.md` — - .claude/rules/backend.md with `paths: ["packages/backend/**"]`
- `claude-md-fullstack.md` — - claude-md-fullstack.md
- `claude-md-library.md` — - claude-md-library.md
- `claude-md-microservices.md` — - claude-md-microservices.md
- `claude-md-mobile.md` — - claude-md-mobile.md
- `claude-md-monorepo.md` — - claude-md-monorepo.md
- `constitution.md` — - ".aios-core/constitution.md"
- `frontend.md` — - .claude/rules/frontend.md with `paths: ["packages/frontend/**"]`
- `git-instructions.md` — - "@docs/git-instructions.md"
- `local.md` — local: "./CLAUDE.local.md (gitignored)"
- `my-project-instructions.md` — home: "@~/.claude/my-project-instructions.md"
- `ontext.md` — - Project-Context.md: Persistent context file for technology stack, conventions, patterns
- `personal-rules.md` — - "@~/.claude/personal-rules.md"
- `review.md` — A file at .claude/commands/review.md and a skill at .claude/skills/review/SKILL.md
- `template.md` — +-- template.md        # Template for Claude to fill in
- `test-rules.md` — 2. Extract test rules to `.claude/rules/test-rules.md` with `paths: ["tests/**"]`
- `update-knowledge.md` — - Example: update-knowledge.md -> .aios-core/development/tasks/update-knowledge.md

**output runtime (manter): 8**
- `create-agent.md` — - Example: create-agent.md → .aios-core/development/tasks/create-agent.md
- `create-doc.md` — - Example: create-doc.md -> .aios-core/development/tasks/create-doc.md
- `create-hook.md` — - Example: create-hook.md -> .aios-core/development/tasks/create-hook.md
- `create-skill.md` — - Example: create-skill.md -> .aios-core/development/tasks/create-skill.md
- `pr-body.md` — --output-format json | jq -r '.result' > pr-body.md
- `sample.md` — |   +-- sample.md      # Example output showing expected format
- `security-reviewer.md` — Save to `.claude/agents/security-reviewer.md`:
- `staging.md` — namespacing: "Nested directories create namespaced commands (e.g., deploy/staging.md -> /deploy:staging)"

## Resumo

| Squad | input faltando | output runtime |
|---|---|---|
| advisory-board | 0 | 0 |
| brand-squad | 0 | 0 |
| cybersecurity | 0 | 0 |
| design-squad | 0 | 0 |
| hormozi-squad | 0 | 0 |
| storytelling | 0 | 0 |
| traffic-masters | 0 | 0 |
| copy-master | 2 | 0 |
| copy-squad | 2 | 0 |
| movement | 0 | 0 |
| data-squad | 2 | 0 |
| c-level-squad | 0 | 0 |
| claude-code-mastery | 21 | 8 |
