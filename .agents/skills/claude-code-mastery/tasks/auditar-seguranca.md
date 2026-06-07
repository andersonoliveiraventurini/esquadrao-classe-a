# Task: Auditar Segurança & Enforcement

**Responsável:** Bastion (`agents/security-warden.md`)
**Recursos MIT:** `reference/skills/security-audit/SKILL.md`, `reference/hooks/block-secrets.py`, `reference/hooks/block-dangerous-commands.sh`, `reference/templates/settings.json`, `reference/GUIDE.md` (Partes 1 e 7)

## Objetivo
Verificar e endurecer o setup com defesa em profundidade — impedir vazamento de segredos e operações destrutivas.

## Entradas
- Projeto/setup alvo e seu `settings.json`, `.gitignore` e `CLAUDE.md` atuais.

## Passos
1. **Camada 1 — comportamental** — confirmar regras "NEVER EVER DO" no CLAUDE.md global (segredos, `.env`). Ver `reference/GUIDE.md` Parte 1.
2. **Camada 2 — acesso** — validar `permissions.deny` no `settings.json` (`Read(./.env*)`, `Read(./secrets/**)`, `Bash(rm:-rf)`, `Bash(curl:*)`) espelhando `reference/templates/settings.json`.
3. **Camada 3 — git** — garantir `.env*` e segredos no `.gitignore`.
4. **Camada 4 — enforcement** — confirmar `block-secrets.py` e `block-dangerous-commands.sh` instalados e ativos (exit 2). Wiring com Grommet.
5. **Auditoria de código** — rodar o roteiro de `reference/skills/security-audit/SKILL.md`: grep de padrões de segredo, checagem de `.gitignore`, histórico git, dependências.
6. **Testar** — disparar condições de risco e confirmar bloqueio + mensagem clara.

## Saída
- Relatório de auditoria com gaps por camada e correções aplicadas.

## Critérios de qualidade
- [ ] As 4 camadas de defesa presentes e testadas.
- [ ] Hooks de bloqueio retornam exit 2 com motivo.
- [ ] Nenhum segredo rastreável em código ou histórico.
- [ ] Deny/allow list coerente com o stack do projeto.
