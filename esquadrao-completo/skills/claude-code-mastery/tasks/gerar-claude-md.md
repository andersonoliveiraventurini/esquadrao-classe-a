# Task: Gerar/Otimizar CLAUDE.md

**Responsável:** Ledger (`agents/config-curator.md`)
**Recursos MIT:** `reference/templates/global-claude.md`, `reference/templates/project-claude.md`, `reference/CLAUDE.md`, `reference/GUIDE.md` (Partes 1 e 2)

## Objetivo
Produzir um `CLAUDE.md` (global e/ou de projeto) que sirva ao mesmo tempo de gatekeeper de segurança e de blueprint de scaffolding.

## Entradas
- Nível alvo: global (`~/.claude/CLAUDE.md`) ou projeto (`./CLAUDE.md`).
- Stack do projeto, contas (GitHub/Docker) e regras inegociáveis do time.

## Passos
1. **Escolher o template** em `reference/templates/`: `global-claude.md` para o nível global, `project-claude.md` para o projeto.
2. **Identidade & contas** (global) — preencher contas usadas em todos os projetos (Parte 1 do guia).
3. **Gatekeeper "NEVER EVER DO"** — adicionar as regras absolutas (nunca publicar segredos, nunca commitar `.env`). Ver `reference/GUIDE.md` Parte 1.
4. **Scaffolding** (Parte 2) — definir arquivos obrigatórios, estrutura padrão e requisitos de runtime para novos projetos.
5. **Projeto** — partir de `project-claude.md` e descrever arquitetura, comandos e regras do time.
6. **Posicionar na hierarquia** — confirmar o nível certo (enterprise/global/projeto/local) e evitar duplicação.

## Saída
- `CLAUDE.md` pronto, no nível correto, alinhado à defesa em profundidade.

## Critérios de qualidade
- [ ] Regras de gatekeeper presentes (segredos/`.env`).
- [ ] Padrões de scaffolding definidos (se global).
- [ ] Sem regras duplicadas entre níveis.
- [ ] Instruções de <20% das conversas movidas para skills (handoff a Forge).
