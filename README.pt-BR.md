# Esquadrão Classe A 🎖️

**🌐 Idioma:** [English](./README.md) · **Português**

**Marketplace de plugins para o [Claude Code](https://claude.com/claude-code).**
Cada plugin é um **esquadrão** — um time de agentes de IA especialistas, com um
**orquestrador** que diagnostica o seu pedido, roteia para o especialista certo e
entrega o trabalho com checagem de qualidade.

São **13 esquadrões** · **177 agentes especialistas** · **135 tasks** · **28 workflows**,
todos invocáveis por skill no Claude Code.

> *"Se você tem um problema… se nenhuma IA genérica resolve… e se você conseguir instalá-los… talvez possa convocar o Esquadrão Classe A."* 🎬

> Projeto **privado/pessoal**. Conteúdo adaptado do projeto open-source
> [`ohmyjahh/xquads-squads`](https://github.com/ohmyjahh/xquads-squads) (autor original:
> Synkra AIOS). Créditos e licença em [`NOTICE`](./NOTICE). Formato de marketplace
> inspirado em [`mwguerra/claude-code-plugins`](https://github.com/mwguerra/claude-code-plugins).

---

## 🎬 Sobre o nome

**Esquadrão Classe A** é o título brasileiro de **The A-Team** (*Esquadrão Classe A*) — a
série dos anos 80 sobre um time de especialistas que você chama quando tem um problema e
ninguém mais pode ajudar.

É essa a ideia: em vez de uma IA generalista, você ganha um *time* de especialistas que
convoca sob demanda — e um orquestrador que escolhe o certo para cada tarefa. Como diria o
Hannibal: **"Adoro quando um plano dá certo."**

---

## 🚀 Instalação

No Claude Code, registre o marketplace:

```bash
/plugin marketplace add andersonoliveiraventurini/esquadrao-classe-a
```

**Instalar tudo de uma vez (recomendado)** — um único plugin-bundle com os 13 esquadrões:

```bash
/plugin install esquadrao-completo@esquadrao-classe-a
```

**Ou instalar esquadrões individuais** — escolha só os que quiser:

```bash
/plugin install copy-squad@esquadrao-classe-a
/plugin install advisory-board@esquadrao-classe-a
/plugin install traffic-masters@esquadrao-classe-a
```

> Escolha **uma** abordagem: instale o `esquadrao-completo` (tudo) **ou** os esquadrões
> individuais — instalar os dois carregaria cada esquadrão em duplicidade.

> Dica: para testar localmente a partir de um clone do repo, use
> `/plugin marketplace add .` na raiz do projeto.

### Usar no opencode e no Codex

Os esquadrões também são entregues como **Agent Skills padrão** em
[`.agents/skills/`](./.agents/skills) — o diretório lido nativamente pelo **opencode** e pelo **Codex**.

**Opção A — global (recomendado; funciona em todo projeto, nas duas ferramentas):**

```bash
git clone https://github.com/andersonoliveiraventurini/esquadrao-classe-a.git
cd esquadrao-classe-a
python scripts/install_skills.py        # copia os 13 esquadrões para ~/.agents/skills/
```

`~/.agents/skills/` é lido pelo opencode (escopo global) e pelo Codex (escopo de usuário),
então uma única instalação habilita os esquadrões em qualquer lugar.

**Opção B — por projeto:**

```bash
python scripts/install_skills.py --dest /caminho/do/seu/projeto   # -> <projeto>/.agents/skills/
```

Ou copie as pastas que quiser de `.agents/skills/` para o `.agents/skills/` do seu projeto
(também funciona em `.opencode/skills/` ou `.claude/skills/`).

**Como invocar:**
- **opencode** — peça naturalmente (a skill ativa pela descrição) ou referencie-a.
- **Codex** — digite `$<esquadrão>` (ex.: `$copy-squad`), use `/skills`, ou deixe casar implicitamente.

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

> A camada de orquestração sintetizada (o `SKILL.md` de cada esquadrão) é escrita em
> **português brasileiro** para maximizar a precisão de ativação das skills nos seus prompts.
> Os esquadrões entendem e respondem em qualquer idioma.

---

## 🎯 Os 13 Esquadrões

| Esquadrão | Foco | Agentes | Instalar |
|-----------|------|:------:|----------|
| `advisory-board` | Conselho de mentores para decisões estratégicas de negócio e vida | 11 | `/plugin install advisory-board@esquadrao-classe-a` |
| `c-level-squad` | Conselho executivo C-level (CEO/CTO/CFO/CMO…) | 6 | `/plugin install c-level-squad@esquadrao-classe-a` |
| `hormozi-squad` | Ofertas irresistíveis, monetização e escala (estilo Hormozi) | 16 | `/plugin install hormozi-squad@esquadrao-classe-a` |
| `copy-master` | Copywriting de elite — 32 copywriters lendários | 33 | `/plugin install copy-master@esquadrao-classe-a` |
| `copy-squad` | Copywriting direct-response — 22 copywriters | 23 | `/plugin install copy-squad@esquadrao-classe-a` |
| `brand-squad` | Branding, identidade e posicionamento de marca | 15 | `/plugin install brand-squad@esquadrao-classe-a` |
| `storytelling` | Narrativa, roteiro e comunicação por histórias | 12 | `/plugin install storytelling@esquadrao-classe-a` |
| `traffic-masters` | Tráfego pago e mídia de performance (Meta/Google Ads) | 16 | `/plugin install traffic-masters@esquadrao-classe-a` |
| `design-squad` | Design de produto, UX/UI e sistemas visuais | 8 | `/plugin install design-squad@esquadrao-classe-a` |
| `data-squad` | Dados, BI, analytics e crescimento orientado a dados | 7 | `/plugin install data-squad@esquadrao-classe-a` |
| `cybersecurity` | Segurança ofensiva/defensiva, auditoria e resposta a incidentes | 15 | `/plugin install cybersecurity@esquadrao-classe-a` |
| `movement` | Construção de movimentos, causas e comunidades | 7 | `/plugin install movement@esquadrao-classe-a` |
| `claude-code-mastery` | Maestria no próprio Claude Code — CLAUDE.md, hooks, MCP, skills, slash commands | 8 | `/plugin install claude-code-mastery@esquadrao-classe-a` |

ℹ️ `claude-code-mastery` empacota material de referência com **licença MIT** (templates, hooks,
comandos, skills, guia) de [`TheDecipherist/claude-code-mastery`](https://github.com/TheDecipherist/claude-code-mastery);
as personas especialistas e a orquestração são autoria própria. Detalhes no [`NOTICE`](./NOTICE).

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

- [`docs/USAGE.pt-BR.md`](./docs/USAGE.pt-BR.md) — guia prático de uso · [English](./docs/USAGE.md)
- [`docs/PRD-marketplace-esquadroes.md`](./docs/PRD-marketplace-esquadroes.md) — requisitos e decisões.
- [`docs/superpowers/plans/2026-06-06-marketplace-esquadroes.md`](./docs/superpowers/plans/2026-06-06-marketplace-esquadroes.md) — plano de implementação.
- [`docs/relatorio-orfas.md`](./docs/relatorio-orfas.md) — QA das referências órfãs.

---

## ⚖️ Licença e créditos

Conteúdo dos squads: majoritariamente **MIT** (autor original **Synkra AIOS**) — ver
[`NOTICE`](./NOTICE). Camada de adaptação (orquestração, comandos, identidade do
marketplace): Anderson de Oliveira Venturini.
