# Task: Criar Skill

**Responsável:** Forge (`agents/skill-smith.md`)
**Recursos MIT:** `reference/skills/commit-messages/SKILL.md`, `reference/skills/security-audit/SKILL.md`, `reference/GUIDE.md` (Parte 5)

## Objetivo
Empacotar uma expertise recorrente numa skill (`SKILL.md`) que o Claude aciona automaticamente no contexto certo, com progressive disclosure.

## Entradas
- A expertise/processo a empacotar.
- Os sinais de ativação (palavras e situações em que deve disparar).

## Passos
1. **Validar o critério** — a expertise é recorrente mas vale para <20% das conversas? Se for universal, é CLAUDE.md (handoff a Ledger).
2. **Criar a pasta** `skills/<nome>/SKILL.md`.
3. **Frontmatter** — `name` e `description` discriminativa, descrevendo *quando ativar* (espelhar `reference/skills/security-audit/SKILL.md` e `.../commit-messages/SKILL.md`).
4. **Corpo** — seção "When to Use", processo passo a passo e exemplos.
5. **Progressive disclosure** — manter o `SKILL.md` enxuto; mover detalhes pesados para arquivos de apoio carregados sob demanda.
6. **Testar o gatilho** — a `description` cobre as frases reais do usuário?

## Saída
- `skills/<nome>/SKILL.md` que dispara no momento certo.

## Critérios de qualidade
- [ ] `description` lista sinais de ativação, não só a função.
- [ ] Skill em vez de CLAUDE.md quando aplica a <20% das conversas.
- [ ] Conteúdo pesado isolado em arquivos de apoio.
- [ ] Forma alinhada às skills de referência MIT.
