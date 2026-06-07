# Task: Criar Slash Command

**Responsável:** Quill (`agents/command-author.md`)
**Recursos MIT:** `reference/commands/` (`review.md`, `pr.md`, `test.md`, `explain.md`), `reference/commands/README.md`, `reference/GUIDE.md` (Parte 5)

## Objetivo
Criar um slash command explícito (`/...`) com um roteiro determinístico que o usuário invoca sob demanda.

## Entradas
- Nome e propósito do comando.
- Formas de invocação e flags necessárias.
- Escopo: por projeto (`.claude/commands/`) ou global (`~/.claude/commands/`).

## Passos
1. **Confirmar que deve ser explícito** — se a ação deve disparar sozinha, é skill (handoff a Forge, `agents/skill-smith.md`).
2. **Escolher um análogo** em `reference/commands/` para usar de molde (`review.md` para checklists, `pr.md` para fluxo git, `test.md` para `$ARGUMENTS`/flags, `explain.md` para análise).
3. **Frontmatter** — escrever `description` clara (aparece na lista de comandos).
4. **Definir Input** — explicitar invocações e flags via `$ARGUMENTS`.
5. **Roteiro numerado** — passos determinísticos com os comandos shell/git exatos.
6. **Instalar** — copiar para `.claude/commands/` (projeto) ou `~/.claude/commands/` (global), conforme `reference/commands/README.md`.
7. **Testar** a invocação real do comando.

## Saída
- Arquivo `<comando>.md` instalado e funcional.

## Critérios de qualidade
- [ ] `description` descreve o que o comando faz.
- [ ] Passos determinísticos e reproduzíveis.
- [ ] Flags via `$ARGUMENTS` quando há variações.
- [ ] Comandos shell sensíveis revisados com Bastion.
