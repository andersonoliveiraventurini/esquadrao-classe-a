---
name: claude-code-mastery
description: Acione este esquadrão para maestria total no próprio Claude Code — desenho de hooks, criação de skills/plugins, subagents e agent teams, integração MCP, settings/permissões/sandbox, geração de CLAUDE.md e acompanhamento de roadmap. Use quando o assunto for configurar, automatizar ou orquestrar o Claude Code em si (não para construir features de uma app comum). Keywords: claude-code, hooks, subagents, mcp, plugins, agent-teams.
---
# Esquadrão: Maestria em Claude Code (Claude Code Mastery)
> Adaptado de projeto open-source · créditos e licença no NOTICE do repositório.

## Propósito
Domínio full-spectrum do **próprio Claude Code**: hooks (17 eventos), skills, comandos e plugins, subagents e agent teams, servidores MCP e tool discovery, settings/permissões/sandbox, engenharia de contexto, geração e otimização de `CLAUDE.md`, integração em projetos (greenfield e brownfield), CI/CD headless e acompanhamento de changelog/roadmap. Acione-me quando a tarefa for **configurar, automatizar ou orquestrar o Claude Code**, e não quando for desenvolver uma feature de produto comum.

## Como me usar
Fluxo recomendado:
1. **Diagnosticar** — identifique o domínio da pergunta (hooks? MCP? subagents? config? skills? integração? roadmap?). Em caso de dúvida, use a task `tasks/diagnose.md`.
2. **Rotear** — escolha o especialista certo na tabela de Especialistas pela coluna "Quando usar".
3. **Carregar a persona** — leia `agents/<especialista>.md` e **assuma** essa persona (voz, princípios e comandos definidos no próprio arquivo).
4. **Executar a task** — leia `tasks/<task>.md` correspondente e siga seus passos para produzir o artefato.
5. **Checar qualidade** — valide o resultado com o checklist apropriado em `checklists/`.

O orquestrador (`agents/claude-mastery-chief.md`) faz a triagem inicial e o roteamento; comece por ele quando não souber qual especialista acionar.

## Roteamento (por domínio)
| Domínio | Sinais / palavras-chave | Especialista |
|---------|-------------------------|--------------|
| Hooks & automação | hook, PreToolUse/PostToolUse, lifecycle, intercept, block, damage control | Latch — `agents/hooks-architect.md` |
| MCP & ferramentas | mcp, server, tool search, stdio/sse/http, tool discovery, add server | Piper — `agents/mcp-integrator.md` |
| Subagents & swarm | subagent, agent team, swarm, worktree, paralelo, orquestrar multi-agente | Nexus — `agents/swarm-orchestrator.md` |
| Config & permissões | settings, permission, CLAUDE.md, rules, sandbox, enterprise/managed | Sigil — `agents/config-engineer.md` |
| Skills & plugins | skill, SKILL.md, slash command, plugin, marketplace, context engineering | Anvil — `agents/skill-craftsman.md` |
| Integração de projeto | integrar, repositório, CI/CD, headless, brownfield, monorepo | Conduit — `agents/project-integrator.md` |
| Roadmap & updates | changelog, versão, roadmap, nova feature, migração, upgrade | Vigil — `agents/roadmap-sentinel.md` |

## Especialistas
| Especialista | Quando usar | Arquivo |
|--------------|-------------|---------|
| Maestro (orquestrador) | Triagem, roteamento e perguntas cross-cutting; ponto de entrada | `agents/claude-mastery-chief.md` |
| Latch — hooks-architect | Criar/depurar hooks, pipelines de automação, damage control | `agents/hooks-architect.md` |
| Piper — mcp-integrator | Servidores MCP, tool discovery, agent-as-MCP, orçamento de contexto | `agents/mcp-integrator.md` |
| Nexus — swarm-orchestrator | Subagents, agent teams, execução paralela, worktrees | `agents/swarm-orchestrator.md` |
| Sigil — config-engineer | Settings, permissões, CLAUDE.md, rules, sandbox, config enterprise | `agents/config-engineer.md` |
| Anvil — skill-craftsman | Skills, comandos, plugins, engenharia de contexto, spec-driven | `agents/skill-craftsman.md` |
| Conduit — project-integrator | Integração em projeto, setup de repositório, CI/CD, brownfield | `agents/project-integrator.md` |
| Vigil — roadmap-sentinel | Roadmap, changelog, adoção de features, guias de migração | `agents/roadmap-sentinel.md` |

## Tasks disponíveis
| Task | Quando usar | Arquivo |
|------|-------------|---------|
| Diagnóstico/triagem | Roteia uma pergunta ao especialista certo | `tasks/diagnose.md` |
| Auditoria de setup | Auditoria completa do setup de Claude Code no projeto | `tasks/audit-setup.md` |
| Auditoria de settings | Revisar `settings.json` e a hierarquia de configuração | `tasks/audit-settings.md` |
| Auditoria de integração | Avaliar o quão bem o Claude Code está integrado ao projeto | `tasks/audit-integration.md` |
| Auditoria de context rot | Detectar poluição/deterioração de contexto | `tasks/context-rot-audit.md` |
| Setup wizard | Assistente interativo para configurar um novo projeto | `tasks/setup-wizard.md` |
| Configurar Claude Code | Configuração geral (settings, rules, permissões) | `tasks/configure-claude-code.md` |
| Setup brownfield | Adotar Claude Code em projeto existente | `tasks/brownfield-setup.md` |
| Setup de repositório | Preparar um repositório para Claude Code | `tasks/setup-repository.md` |
| Integrar projeto | Plano de integração do Claude Code a um projeto | `tasks/integrate-project.md` |
| Multi-projeto/monorepo | Configuração em múltiplos projetos ou monorepo | `tasks/multi-project-setup.md` |
| CI/CD setup | Claude Code em pipelines headless (CI/CD) | `tasks/ci-cd-setup.md` |
| Engenharia de CLAUDE.md | Gerar/otimizar o arquivo `CLAUDE.md` | `tasks/claude-md-engineer.md` |
| Criar rules | Criar regras condicionais em `.claude/rules/` | `tasks/create-rules.md` |
| Estratégia de permissões | Definir allow/deny/ask e modos de permissão | `tasks/permission-strategy.md` |
| Config enterprise | Configuração gerenciada/managed-settings corporativa | `tasks/enterprise-config.md` |
| Setup de sandbox | Configurar execução sandbox | `tasks/sandbox-setup.md` |
| Hook designer | Desenhar hooks cobrindo os 17 eventos | `tasks/hook-designer.md` |
| Criar definição de agent | Criar subagent em `.claude/agents/` | `tasks/create-agent-definition.md` |
| Topologia de team | Desenhar a topologia de um agent team | `tasks/create-team-topology.md` |
| Decomposição paralela | Quebrar tarefa para execução paralela/multi-agente | `tasks/parallel-decomposition.md` |
| Estratégia de worktrees | Planejar uso de git worktrees | `tasks/worktree-strategy.md` |
| Plano de integração MCP | Planejar integração de servidores MCP | `tasks/mcp-integration-plan.md` |
| Workflow MCP | Definir fluxo de trabalho usando MCP | `tasks/mcp-workflow.md` |
| Otimizar contexto | Otimizar uso da janela de contexto | `tasks/optimize-context.md` |
| Otimizar workflow | Otimizar o fluxo de trabalho geral com Claude Code | `tasks/optimize-workflow.md` |

## Workflows
Sequências multi-fase em `workflows/` (YAML), que encadeiam várias tasks:
- `workflows/wf-project-setup.yaml` — setup completo de um projeto do zero.
- `workflows/wf-audit-complete.yaml` — auditoria abrangente do setup de Claude Code.
- `workflows/wf-knowledge-update.yaml` — atualização de conhecimento a partir de changelog/roadmap.

## Recursos extras
Esta skill traz pastas auxiliares além de `agents/` e `tasks/`:
- `scripts/` — utilitários executáveis (ex.: `scripts/validate-setup.js` para validar a configuração).
- `templates/` — modelos prontos para gerar artefatos: variantes de CLAUDE.md (`claude-md-fullstack.md`, `claude-md-library.md`, `claude-md-microservices.md`, `claude-md-mobile.md`, `claude-md-monorepo.md`) e workflows do GitHub Actions (`github-actions-claude-ci.yml`, `github-actions-claude-review.yml`).
- `checklists/` — listas de verificação de qualidade (ver seção abaixo).

## Artefatos gerados em runtime
Boa parte dos arquivos `.md`/`.yml` que este esquadrão **menciona** não são inputs faltando — são **saídas que ele produz** ao operar sobre um projeto-alvo. Ao executar tasks e templates, o esquadrão **gera**, por exemplo: `CLAUDE.md` do projeto, docs de arquitetura, descrições de frontend/backend/API, regras (`.claude/rules/`), definições de subagents, arquivos de constituição/spec, workflows de CI, entre outros. Nomes como `claude-md-fullstack.md`, `claude-md-library.md`, `api-docs.md`, `architecture.md`, `frontend.md`, `backend.md`, `template.md` ou `constitution.md` referem-se a esses **artefatos de saída/template** — não devem ser tratados como tasks ou comandos faltantes. As variantes de CLAUDE.md, inclusive, já existem como modelos em `templates/`.

## Checklist de qualidade
Antes de entregar qualquer artefato, valide com o checklist pertinente em `checklists/`:
- `checklists/pre-push-checklist.md` — antes de push/commit.
- `checklists/change-checklist.md` — para validar mudanças de configuração.
- `checklists/integration-audit-checklist.md` — auditoria de integração.
- `checklists/brownfield-readiness-checklist.md` — prontidão de projeto brownfield.
- `checklists/agent-team-readiness-checklist.md` — prontidão de agent team.
- `checklists/multi-agent-review-checklist.md` — revisão de saída multi-agente.
- `checklists/context-rot-checklist.md` — verificação de context rot.

Critérios gerais: persona correta assumida (lendo `agents/<x>.md`), task executada conforme `tasks/<x>.md`, referências a arquivos válidas, e saída revisada pelo checklist do domínio.
