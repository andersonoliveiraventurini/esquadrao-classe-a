# Task: Configurar Hooks

**Responsável:** Grommet (`agents/hooks-architect.md`)
**Recursos MIT:** `reference/hooks/` (todos), `reference/templates/settings.json`, `reference/GUIDE.md` (Parte 7)

## Objetivo
Instalar e fazer o wiring de hooks determinísticos que garantem comportamento onde o CLAUDE.md falha.

## Entradas
- Quais garantias o projeto precisa (bloquear segredos? bloquear comandos perigosos? formatar pós-edição? quality gate no fim do turno? notificações?).

## Passos
1. **Mapear necessidades por evento** usando a tabela da Parte 7: `PreToolUse`, `PostToolUse`, `Stop`, `Notification`.
2. **Selecionar hooks** em `reference/hooks/`:
   - `block-secrets.py` (PreToolUse / Read|Edit|Write)
   - `block-dangerous-commands.sh` (PreToolUse / Bash)
   - `after-edit.sh` (PostToolUse / Edit|Write)
   - `end-of-turn.sh` (Stop)
   - `notify.sh` (Notification)
3. **Instalar** — copiar para `~/.claude/hooks/` e `chmod +x` nos `.sh`.
4. **Fazer o wiring** — espelhar o bloco `hooks` de `reference/templates/settings.json` no `settings.json` alvo.
5. **Conferir exit codes** — `0` permite, `1` erro ao usuário, `2` bloqueia e devolve stderr ao Claude.
6. **Testar** — disparar cada condição e validar o comportamento (especialmente exit 2 com mensagem clara).

## Saída
- `settings.json` com hooks ativos e testados.

## Critérios de qualidade
- [ ] Cada hook mapeado ao evento e matcher corretos.
- [ ] Hooks pesados no `Stop`, não no `PostToolUse`.
- [ ] Fail-open (exit 0) em erro inesperado.
- [ ] Mensagem de bloqueio explica o porquê.
