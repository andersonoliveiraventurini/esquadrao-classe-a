# Task: Integrar Servidores MCP

**Responsável:** Relay (`agents/mcp-integrator.md`)
**Recursos MIT:** `reference/GUIDE.md` (Partes 3 e 4)

## Objetivo
Conectar o Claude Code às ferramentas externas certas via MCP, sem desperdiçar contexto.

## Entradas
- Integrações desejadas (DB, browser, docs, cloud, workflow).
- Frequência de uso de cada uma (pontual vs repetido).

## Passos
1. **Mapear necessidades** — listar as integrações e seu padrão de uso.
2. **MCP vs alternativa** — aplicar a tabela de tradeoffs (Parte 3): uso pontual → CLI/`curl`; uso repetido na mesma conversa → MCP.
3. **Escolher servidores** do catálogo recomendado (Parte 3): Core dev (Context7, GitHub, Filesystem, Sequential Thinking), Bancos, Docs/RAG, Browser/Testes, Cloud, Workflow.
4. **Instalar** — `claude mcp add <nome> -- <comando>`. Para docs vivas: `claude mcp add context7 -- npx -y @upstash/context7-mcp@latest` (Parte 4).
5. **Validar** — `claude mcp list` e um teste real da tool.
6. **Documentar** — registrar os servidores no `CLAUDE.md` do projeto (handoff a Ledger).

## Saída
- Servidores MCP instalados, validados e documentados.

## Critérios de qualidade
- [ ] Cada servidor justificado pelo padrão de uso (repetido).
- [ ] Integrações pontuais resolvidas por CLI, não MCP.
- [ ] `claude mcp list` confirma os servidores ativos.
- [ ] Servidores documentados no CLAUDE.md do projeto.
