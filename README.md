# Esquadrão Clase A 🎖️

**Marketplace de plugins para o [Claude Code](https://claude.com/claude-code).**
Cada plugin é um **esquadrão** — um time de agentes de IA especialistas, com um
**orquestrador** que diagnostica o seu pedido, roteia para o especialista certo e
entrega o trabalho com checagem de qualidade.

São **13 esquadrões** · **177 agentes especialistas** · **135 tasks** · **28 workflows**,
todos invocáveis por skill no Claude Code.

> Projeto **privado/pessoal**. Conteúdo adaptado do projeto open-source
> [`ohmyjahh/xquads-squads`](https://github.com/ohmyjahh/xquads-squads) (autor original:
> Synkra AIOS). Créditos e licença em [`NOTICE`](./NOTICE). Formato de marketplace
> inspirado em [`mwguerra/claude-code-plugins`](https://github.com/mwguerra/claude-code-plugins).

---

## 🚀 Instalação

No Claude Code, registre o marketplace e instale os esquadrões que quiser:

```bash
# 1. Registrar o marketplace (uma vez)
/plugin marketplace add andersonoliveiraventurini/esquadrao-clase-a

# 2. Instalar um esquadrão
/plugin install copy-squad@esquadrao-clase-a

# 3. (opcional) instalar todos os que interessam
/plugin install advisory-board@esquadrao-clase-a
/plugin install traffic-masters@esquadrao-clase-a
```

> Dica: para testar localmente a partir de um clone do repo, use
> `/plugin marketplace add .` na raiz do projeto.

---

## 🧭 Como usar

Depois de instalar, é só pedir naturalmente — a skill do esquadrão ativa sozinha pelo
contexto — ou chamar o comando dedicado:

```bash
/copy-squad preciso de uma headline para um anúncio de curso de inglês
/advisory-board devo aceitar um sócio investidor que pede 30% da empresa?
/traffic-masters minha campanha no Meta está com CPA alto, o que investigar?
```

O orquestrador então:
1. **Diagnostica** o pedido (tipo de trabalho, contexto, objetivo).
2. **Roteia** para o(s) especialista(s) certo(s).
3. **Assume a persona** do especialista (lendo o arquivo do agente) e **executa a task**.
4. **Checa a qualidade** antes de entregar.

---

## 🎯 Os 13 Esquadrões

| Esquadrão | Foco | Agentes | Instalar |
|-----------|------|:------:|----------|
| `advisory-board` | Conselho de mentores para decisões estratégicas de negócio e vida | 11 | `/plugin install advisory-board@esquadrao-clase-a` |
| `c-level-squad` | Conselho executivo C-level (CEO/CTO/CFO/CMO…) | 6 | `/plugin install c-level-squad@esquadrao-clase-a` |
| `hormozi-squad` | Ofertas irresistíveis, monetização e escala (estilo Hormozi) | 16 | `/plugin install hormozi-squad@esquadrao-clase-a` |
| `copy-master` | Copywriting de elite — 32 copywriters lendários | 33 | `/plugin install copy-master@esquadrao-clase-a` |
| `copy-squad` | Copywriting direct-response — 22 copywriters | 23 | `/plugin install copy-squad@esquadrao-clase-a` |
| `brand-squad` | Branding, identidade e posicionamento de marca | 15 | `/plugin install brand-squad@esquadrao-clase-a` |
| `storytelling` | Narrativa, roteiro e comunicação por histórias | 12 | `/plugin install storytelling@esquadrao-clase-a` |
| `traffic-masters` | Tráfego pago e mídia de performance (Meta/Google Ads) | 16 | `/plugin install traffic-masters@esquadrao-clase-a` |
| `design-squad` | Design de produto, UX/UI e sistemas visuais | 8 | `/plugin install design-squad@esquadrao-clase-a` |
| `data-squad` | Dados, BI, analytics e crescimento orientado a dados | 7 | `/plugin install data-squad@esquadrao-clase-a` |
| `cybersecurity` | Segurança ofensiva/defensiva, auditoria e resposta a incidentes | 15 | `/plugin install cybersecurity@esquadrao-clase-a` |
| `movement` | Construção de movimentos, causas e comunidades | 7 | `/plugin install movement@esquadrao-clase-a` |
| `claude-code-mastery` ⚠️ | Maestria no próprio Claude Code (hooks, skills, MCP, subagents) | 8 | `/plugin install claude-code-mastery@esquadrao-clase-a` |

⚠️ `claude-code-mastery` tem **licença ambígua** na origem (sem declaração MIT). Use para
fins pessoais; **não redistribua publicamente** sem confirmar a proveniência. Detalhes no
[`NOTICE`](./NOTICE).

---

## 🗂️ Estrutura de um plugin

```
<esquadrão>/
├── .claude-plugin/plugin.json        # manifesto do plugin
├── commands/<esquadrão>.md           # slash command que ativa a skill
└── skills/<esquadrão>/
    ├── SKILL.md                      # orquestrador (roteamento + catálogo)
    ├── agents/                       # personas especialistas
    ├── tasks/                        # tarefas executáveis
    ├── workflows/                    # fluxos multi-agente
    ├── checklists/                   # critérios de qualidade
    └── data/                         # bases de apoio (frameworks, catálogos)
```

A raiz tem `.claude-plugin/marketplace.json` listando os 13 plugins.

---

## 🛠️ Como o marketplace é construído (reprodutível)

O conteúdo é gerado a partir da fonte por scripts em [`scripts/`](./scripts):

```bash
python -m pip install --user pyyaml
cd scripts
python classify_orphans.py     # relatório de refs órfãs -> docs/relatorio-orfas.md
python build_marketplace.py    # scaffold dos 13 plugins + marketplace.json
```

- `lib_squads.py` — lista de esquadrões, leitor de manifesto e rebrand.
- `classify_orphans.py` — classifica refs de tasks inexistentes (input faltando × output de runtime).
- `build_marketplace.py` — copia resources (com rebrand), gera `plugin.json`, comandos e `marketplace.json`.

Os arquivos `SKILL.md` (camada de orquestração em PT-BR) são autorados sobre esse scaffold.

---

## 📚 Documentação

- [`docs/PRD-marketplace-esquadroes.md`](./docs/PRD-marketplace-esquadroes.md) — requisitos e decisões.
- [`docs/superpowers/plans/2026-06-06-marketplace-esquadroes.md`](./docs/superpowers/plans/2026-06-06-marketplace-esquadroes.md) — plano de implementação.
- [`docs/relatorio-orfas.md`](./docs/relatorio-orfas.md) — QA das referências órfãs.
- [`docs/GUIA-DE-USO.md`](./docs/GUIA-DE-USO.md) — guia prático de uso dos esquadrões.

---

## ⚖️ Licença e créditos

Conteúdo dos squads: majoritariamente **MIT** (autor original **Synkra AIOS**) — ver
[`NOTICE`](./NOTICE). Camada de adaptação (orquestração, comandos, identidade do
marketplace): Anderson de Oliveira Venturini.
