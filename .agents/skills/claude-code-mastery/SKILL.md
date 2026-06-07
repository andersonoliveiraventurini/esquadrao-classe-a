---
name: claude-code-mastery
description: Acione para maestria no PRÓPRIO Claude Code — escrever CLAUDE.md, desenhar hooks de enforcement, integrar servidores MCP, criar skills e slash commands, e endurecer segredos/permissões. Use quando o assunto for configurar, automatizar ou orquestrar o Claude Code em si, não construir features de uma app comum. Keywords: claude-code, hooks, mcp, skills, slash-commands, enforcement
---
# Esquadrão: Maestria em Claude Code
> Conteúdo de referência (templates, hooks, comandos, skills e guia) adaptado de **TheDecipherist/claude-code-mastery** (licença MIT) — ver `LICENSE-thedecipherist`. Personas e orquestração: autoria própria.

## Propósito
Domínio prático do próprio Claude Code: o `CLAUDE.md` como gatekeeper de segurança e blueprint de scaffolding, hooks de enforcement determinístico, servidores MCP e documentação viva (Context7), skills reutilizáveis, slash commands e hardening de segredos/permissões. Acione-me quando a tarefa for **configurar, automatizar ou orquestrar o Claude Code** — e não quando for desenvolver uma feature de produto comum. Todo o conhecimento de domínio é ancorado no material MIT em `reference/`.

## Como me usar
1. **Diagnosticar** — classifique o pedido em um domínio (CLAUDE.md/config, hooks, MCP, skills, slash commands, segurança, integração). Comece por Vega (`agents/claude-mastery-chief.md`) se não souber a quem perguntar.
2. **Rotear** — escolha o especialista pela tabela de Roteamento.
3. **Carregar a persona** — leia `agents/<x>.md` e assuma aquela voz e foco.
4. **Executar a task** — leia `tasks/<x>.md` e siga os passos.
5. **Usar os recursos** — apoie-se nos arquivos MIT em `reference/` (guia, hooks, comandos, templates, skills).

## Roteamento (por domínio)
| Domínio | Sinais / palavras-chave | Especialista |
|---------|-------------------------|--------------|
| CLAUDE.md & config | CLAUDE.md, settings.json, permissões, memory hierarchy, scaffolding | Ledger — `agents/config-curator.md` |
| Hooks & automação | hook, PreToolUse/PostToolUse/Stop, exit code 2, formatar, bloquear | Grommet — `agents/hooks-architect.md` |
| MCP & ferramentas | mcp, server, context7, tool discovery, stdio/sse/http | Relay — `agents/mcp-integrator.md` |
| Skills | skill, SKILL.md, progressive disclosure, expertise reutilizável | Forge — `agents/skill-smith.md` |
| Slash commands | /review, /pr, /test, /explain, $ARGUMENTS, comando explícito | Quill — `agents/command-author.md` |
| Segurança & enforcement | segredo, .env, rm -rf, deny list, auditoria, hardening | Bastion — `agents/security-warden.md` |
| Integração de projeto | integrar, onboarding, brownfield, dotfiles sync, instalar setup | Span — `agents/project-onboarder.md` |

## Especialistas
| Especialista | Quando usar | Arquivo |
|--------------|-------------|---------|
| Vega (orquestrador) | Triagem, roteamento e perguntas cross-cutting; ponto de entrada | `agents/claude-mastery-chief.md` |
| Grommet — hooks-architect | Criar/depurar hooks e pipelines de enforcement determinístico | `agents/hooks-architect.md` |
| Relay — mcp-integrator | Servidores MCP, Context7, tradeoffs de contexto | `agents/mcp-integrator.md` |
| Ledger — config-curator | CLAUDE.md, settings.json, permissões, hierarquia de memória | `agents/config-curator.md` |
| Forge — skill-smith | Criar skills (SKILL.md) com progressive disclosure | `agents/skill-smith.md` |
| Quill — command-author | Criar slash commands explícitos | `agents/command-author.md` |
| Bastion — security-warden | Bloqueio de segredos, deny list, auditoria, defesa em profundidade | `agents/security-warden.md` |
| Span — project-onboarder | Integração/onboarding do Claude Code em projetos | `agents/project-onboarder.md` |

## Tasks
| Task | Quando usar | Arquivo |
|------|-------------|---------|
| Gerar/otimizar CLAUDE.md | Escrever o CLAUDE.md global ou de projeto | `tasks/gerar-claude-md.md` |
| Configurar hooks | Instalar e fazer wiring dos hooks de enforcement | `tasks/configurar-hooks.md` |
| Criar slash command | Autorar um comando `/...` explícito | `tasks/criar-slash-command.md` |
| Criar skill | Empacotar expertise numa skill que dispara sozinha | `tasks/criar-skill.md` |
| Auditar segurança | Endurecer segredos/permissões em defesa em profundidade | `tasks/auditar-seguranca.md` |
| Integrar MCP | Conectar servidores MCP sem desperdiçar contexto | `tasks/integrar-mcp.md` |

## Recursos de referência (MIT)
Em `reference/` (adaptado de TheDecipherist, licença MIT — ver `LICENSE-thedecipherist`):
- `reference/GUIDE.md` — guia completo (CLAUDE.md, MCP, Context7, skills, chats de propósito único, hooks, LSP). Use como base de qualquer recomendação.
- `reference/CLAUDE.md` — exemplo de CLAUDE.md descrevendo o próprio repositório de referência.
- `reference/hooks/` — hooks prontos: `block-secrets.py`, `block-dangerous-commands.sh`, `after-edit.sh`, `end-of-turn.sh`, `notify.sh`. Use ao configurar enforcement.
- `reference/commands/` — slash commands prontos: `review.md`, `pr.md`, `test.md`, `explain.md` (+ README). Use como molde ao criar comandos.
- `reference/templates/` — `global-claude.md`, `project-claude.md`, `settings.json` (+ `.gitignore`). Use ao gerar CLAUDE.md e settings.
- `reference/skills/` — skills prontas: `commit-messages/SKILL.md`, `security-audit/SKILL.md`. Use como molde ao criar skills e na auditoria de segurança.

## Checklist de qualidade
- [ ] Domínio diagnosticado e roteado ao especialista certo.
- [ ] Persona assumida lendo `agents/<x>.md`.
- [ ] Task executada conforme `tasks/<x>.md`.
- [ ] Recomendações ancoradas num arquivo específico de `reference/` (citado).
- [ ] Defesa em profundidade considerada quando há segredos/permissões.
- [ ] Higiene de contexto respeitada ("Uma Tarefa, Um Chat").
- [ ] Crédito MIT preservado (`LICENSE-thedecipherist`) ao reutilizar recursos.
