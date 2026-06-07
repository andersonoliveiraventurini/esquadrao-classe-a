# Esquadrão: Maestria em Claude Code

Esquadrão do marketplace **Esquadrão Classe A** para dominar o próprio Claude Code: escrever `CLAUDE.md`, desenhar hooks de enforcement, integrar servidores MCP, criar skills e slash commands, e endurecer segredos/permissões.

## Estrutura
- `SKILL.md` — orquestrador (PT-BR): propósito, roteamento, especialistas, tasks e recursos.
- `agents/` — 8 personas (1 orquestrador + 7 especialistas), de autoria própria.
- `tasks/` — 6 procedimentos atômicos, cada um apontando para os recursos MIT em `reference/`.
- `reference/` — recursos de referência (guia, hooks, comandos, templates, skills) adaptados da fonte MIT.
- `LICENSE-thedecipherist` — licença MIT original preservada.

## Créditos e licença
Os **recursos de referência** em `reference/` (`GUIDE.md`, `CLAUDE.md`, `hooks/`, `commands/`, `templates/` e `skills/`) são adaptados de **[TheDecipherist/claude-code-mastery](https://github.com/TheDecipherist/claude-code-mastery)**, distribuído sob a **licença MIT** (Copyright (c) 2025 TheDecipherist). O texto integral da licença está preservado em `LICENSE-thedecipherist`, conforme exigido pelo MIT.

As **personas** (`agents/`), a **orquestração** (`SKILL.md`) e as **tasks** (`tasks/`) são de **autoria própria**, escritas do zero para este esquadrão — não são derivadas de personas de outros projetos. Elas apenas referenciam e ancoram-se no material MIT em `reference/`.

## Uso rápido
Comece por `SKILL.md`. Diagnostique o domínio do seu pedido, carregue a persona em `agents/<x>.md`, execute a task correspondente em `tasks/<x>.md` e apoie-se nos recursos MIT em `reference/`.
