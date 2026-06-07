# PRD — Marketplace de Esquadrões para Claude Code

- **Data:** 2026-06-06
- **Autor:** Anderson de Oliveira Venturini
- **Repositório alvo:** `andersonoliveiraventurini/esquadrao-classe-a`
- **Fonte:** `ohmyjahh/xquads-squads`
- **Referência de formato:** `mwguerra/claude-code-plugins`
- **Status:** ✅ Implementado (2026-06-06) — 13 plugins gerados, validados e publicados.

---

## 1. Visão Geral

O repositório `xquads-squads` contém **13 "squads"** (equipes de agentes de IA) no formato
BMad/AIOS — cada squad é uma pasta com `agents/`, `tasks/`, `workflows/`, `squad.yaml`,
`checklists/`, `data/` e `config/`. Esse formato **não é instalável** como plugin do
Claude Code.

O objetivo deste projeto é **empacotar cada squad como um plugin nativo do Claude Code** e
publicar tudo como um **marketplace** neste repositório, espelhando a estrutura do
marketplace do `mwguerra/claude-code-plugins`. Assim o Anderson poderá instalar qualquer
esquadrão em seus projetos e consultá-lo via skill/comando para melhorar seus trabalhos sob
demanda.

### 1.1 Problema

- As squads existem mas em formato proprietário (BMad/AIOS), não consumível pelo Claude Code.
- Não há `marketplace.json` nem `plugin.json`, então `/plugin install` não funciona.
- O ponto de entrada original (`@copy-chief`, `*comando`) é a sintaxe AIOS, não a do Claude.

### 1.2 Resultado esperado

- `/plugin marketplace add andersonoliveiraventurini/esquadrao-classe-a` registra o marketplace.
- `/plugin install <squad>@esquadrao-classe-a` instala um esquadrão.
- Em qualquer projeto, ao invocar a skill/comando do esquadrão, o Claude diagnostica o
  pedido, assume a persona do especialista certo, executa a task adequada e entrega o
  resultado com checagem de qualidade.

---

## 2. Decisões Aprovadas

| Tema | Decisão |
|------|---------|
| **Arquitetura de conversão** | **Híbrido** — cada squad = 1 plugin; orquestrador vira SKILL + comando; `agents/tasks/workflows/data` copiados **verbatim** dentro da skill. |
| **Escopo** | **Todos os 13 squads.** |
| **Idioma da FONTE** | **Manter como está** (conteúdo PT/EN misto preservado verbatim). |
| **Idioma do conteúdo SINTETIZADO** | **PT-BR** (SKILL.md + comandos), com identificadores/nomes próprios/paths verbatim, descrições **discriminativas** e **palavras-chave em inglês semeadas** em cada `description` para robustez de ativação. *(Veredito do Board — §2.1)* |
| **Comandos órfãos** | **Classificar e omitir por padrão** (opção c). Não autorar tasks faltantes. Registrar omissões em nota `KNOWN-GAPS` por SKILL.md. *(Veredito do Board — §2.1)* |
| **Licenciamento/atribuição** | Preservar `author` + `license` em todo plugin gerado; manter privado; flagar 1 squad de licença ambígua (claude-code-mastery). *(Veredito do Board — §2.2)* |
| **Identidade** | **Dados do git** — marketplace `esquadrao-classe-a`, owner Anderson de Oliveira Venturini, email `anderson.oliveira.venturini@gmail.com`. |

### 2.1 Deliberação do Board of Advisors (DEC-001)

As duas decisões táticas abaixo foram submetidas ao Board (Intelligence, Business, Life,
Security) com **convergência 4/4 em confiança ALTA** e risco BAIXO.

**Decisão 1 — Comandos órfãos → Opção (c): classificar, depois OMITIR por padrão.**
- Os orquestradores referenciam arquivos de task inexistentes. Scan dos 13 squads:
  **7 squads limpos** (advisory-board, brand-squad, cybersecurity, design-squad,
  hormozi-squad, storytelling, traffic-masters); órfãos concentrados em copy-master (2),
  copy-squad (2), movement (6), data-squad (20), c-level-squad (24), claude-code-mastery (~50).
- **Achado crítico:** muitas "órfãs" (sobretudo no claude-code-mastery) são **nomes de
  arquivo de OUTPUT que o agente gera em runtime, não inputs faltando.** Tratá-las como
  "faltando" é erro de categoria.
- **Regra:** para cada ref órfã, classificar em **(i) input genuíno faltando** vs
  **(ii) output de runtime**. OMITIR do SKILL.md apenas os comandos que resolvem para (i);
  MANTER os (ii). **Não autorar** tasks especulativas (rejeitado pelos 4 conselhos).
  Registrar cada omissão numa nota `KNOWN-GAPS` por SKILL.md → backlog sob demanda
  (escrever uma task só quando o uso real travar nela). Ambíguo → omitir e logar.

**Decisão 2 — Idioma do conteúdo sintetizado → PT-BR.**
- SKILL.md + comandos em PT-BR; identificadores/nomes próprios/file paths/command names
  **verbatim**.
- Descrições **discriminativas** (o que faz ESTE squad disparar vs os outros) para evitar
  colisão de trigger entre 13 squads parecidos.
- **Semear palavras-chave em inglês** em cada `description` para ativação robusta
  independente do idioma do prompt.
- Rejeitado "espelhar idioma da fonte" (branching por squad sem benefício).

### 2.2 Licenciamento e Atribuição (achado do Security Council, verificado)

- **Não existe arquivo `LICENSE/COPYING/NOTICE`** no root do upstream.
- **12/13 squads declaram `license: MIT` + `author: "Synkra AIOS"`** no manifesto →
  grant MIT informal porém real para esses 12.
- **1 squad de licença AMBÍGUA:** `claude-code-mastery` (usa `config.yaml`, sem campo `license`). Os outros 12 declaram `license: MIT`.
  - ✅ **RESOLVIDO (2026-06-06):** o `claude-code-mastery` foi **reconstruído** a partir de `TheDecipherist/claude-code-mastery` (MIT) — material de referência MIT creditado + personas/orquestração autorais. Agora **todos os 13 squads são MIT** e não há nenhum `UNLICENSED` no `marketplace.json`.
- **Ações obrigatórias:**
  1. Preservar `author` + `license` em cada `plugin.json`/SKILL.md gerado (compliance MIT).
  2. Adicionar um `NOTICE`/seção de atribuição no README raiz creditando `Synkra AIOS` /
     `ohmyjahh/xquads-squads`.
  3. Manter o marketplace **privado/local**; **não publicar nem compartilhar** — sobretudo
     o squad ambíguo — sem confirmar a proveniência.
- Risco para uso privado single-user com atribuição preservada: **BAIXO**.

> Persistência: o `.board/board.db` não foi gravado nesta sessão (`sqlite3` ausente na
> máquina). A decisão DEC-001 fica registrada aqui no PRD como fonte de verdade.

---

## 3. Inventário da Fonte

13 squads. Totais aproximados: **177 agents, 135 tasks, 28 workflows.**

| Squad | agents | tasks | workflows | data | checklists | manifesto |
|-------|:--:|:--:|:--:|:--:|:--:|--|
| advisory-board | 11 | 7 | 2 | ✓ | ✓ | squad.yaml |
| brand-squad | 15 | 9 | 2 | ✓ | ✓ | squad.yaml |
| c-level-squad | 6 | 7 | 2 | ✓ | ✓ | squad.yaml |
| **claude-code-mastery** | 8 | 26 | 3 | ✓ | ✓ | **config.yaml** + `scripts/` + `templates/` |
| copy-master | 33 | 15 | 4 | ✓ | ✓ | squad.yaml |
| copy-squad | 23 | 13 | 2 | ✓ | ✓ | squad.yaml |
| cybersecurity | 15 | 9 | 2 | ✓ | ✓ | squad.yaml |
| data-squad | 7 | 7 | 2 | ✓ | ✓ | squad.yaml |
| design-squad | 8 | 8 | 2 | ✓ | ✓ | squad.yaml |
| hormozi-squad | 16 | 10 | 2 | ✓ | ✓ | squad.yaml |
| movement | 7 | 7 | 1 | ✓ | ✓ | squad.yaml |
| storytelling | 12 | 8 | 2 | ✓ | ✓ | squad.yaml |
| traffic-masters | 16 | 9 | 2 | ✓ | ✓ | squad.yaml |

**Caso especial:** `claude-code-mastery` não tem `squad.yaml` (usa `config.yaml`) e possui as
pastas extras `scripts/` e `templates/`. Tratamento dedicado na implementação (ler metadados
do `config.yaml`; copiar `scripts/` e `templates/` para os resources da skill).

---

## 4. Arquitetura

### 4.1 Raiz do marketplace (este repositório)

```
esquadrao-classe-a/
├── .claude-plugin/
│   └── marketplace.json        # lista os 13 plugins
├── README.md                   # o que é + como instalar cada esquadrão
├── docs/
│   └── PRD-marketplace-esquadroes.md
├── advisory-board/             # ┐
├── brand-squad/                # │
├── c-level-squad/              # │
├── claude-code-mastery/        # │ 13 pastas de plugin
├── copy-master/                # │  (uma por squad)
├── ...                         # │
└── traffic-masters/            # ┘
```

### 4.2 Estrutura de cada plugin (padrão Híbrido)

```
<squad-name>/
├── .claude-plugin/
│   └── plugin.json             # GERADO a partir de squad.yaml/config.yaml
├── commands/
│   └── <squad-name>.md         # /<squad-name>  → instrui o Claude a usar a skill
└── skills/
    └── <squad-name>/
        ├── SKILL.md            # SINTETIZADO: cérebro orquestrador
        ├── agents/             # copiado VERBATIM da fonte
        ├── tasks/              # copiado VERBATIM
        ├── workflows/          # copiado VERBATIM
        ├── data/               # copiado VERBATIM
        ├── checklists/         # copiado VERBATIM
        ├── config/             # copiado VERBATIM (se existir)
        └── README.md           # README original do squad
```

**Por que os resources ficam dentro da pasta da skill:** skills do Claude Code usam
*progressive disclosure* — o `SKILL.md` é carregado e referencia arquivos vizinhos por
caminho relativo (`agents/eugene-schwartz.md`), carregados sob demanda. Mantendo tudo dentro
de `skills/<squad>/`, as referências são relativas e auto-contidas (sem depender de
`${CLAUDE_PLUGIN_ROOT}`).

### 4.3 Conteúdo do `marketplace.json`

```json
{
  "name": "esquadrao-classe-a",
  "owner": {
    "name": "Anderson de Oliveira Venturini",
    "email": "anderson.oliveira.venturini@gmail.com"
  },
  "metadata": {
    "description": "Esquadrões de agentes de IA (squads) empacotados como plugins do Claude Code.",
    "version": "1.0.0"
  },
  "plugins": [
    { "name": "copy-squad", "source": "./copy-squad", "version": "1.0.0",
      "description": "...", "keywords": ["..."] }
    /* ...13 entradas, descrição/keywords derivadas de cada squad.yaml... */
  ]
}
```

### 4.4 Conteúdo do `plugin.json` (por squad)

Derivado de `squad.yaml` (ou `config.yaml`):

```json
{
  "name": "copy-squad",
  "version": "1.0.0",
  "description": "<description do squad.yaml>",
  "license": "MIT",
  "author": { "name": "Anderson de Oliveira Venturini",
              "email": "anderson.oliveira.venturini@gmail.com" },
  "keywords": ["<tags do squad.yaml>"]
}
```

> Atribuição: o `README.md` de cada plugin e o README raiz creditam a fonte original
> (`ohmyjahh/xquads-squads`, "Synkra AIOS") e o formato de referência (`mwguerra`).

### 4.5 Conteúdo do `SKILL.md` (o único arquivo sintetizado por squad)

Frontmatter (em **PT-BR**, com `description` **discriminativa** + palavras-chave EN semeadas):
```yaml
---
name: <squad-name>
description: Use quando o usuário precisar de <domínio ESPECÍFICO do squad> — consultar o
  esquadrão para criar, revisar ou melhorar <tipo de trabalho>. Roteia para o especialista
  certo. <keywords EN: copywriting, sales copy, headline, ...>
---
```
- A `description` deve ser **discriminativa**: deixar claro o que dispara ESTE squad e não
  os outros 13 (evita colisão de trigger).
- Semear de 3 a 6 **palavras-chave em inglês** ao final da `description` para ativação robusta.
- Atribuição: incluir `author: Synkra AIOS` / fonte em comentário ou rodapé do SKILL.md.

Corpo (em **PT-BR**, adaptado do orquestrador + `squad.yaml` + README; identificadores e
nomes de arquivo **verbatim**):
1. **Propósito do esquadrão** e arquitetura de tiers.
2. **Lógica de roteamento** — como diagnosticar o pedido e escolher o especialista
   (preserva o `routing_logic`/`awareness_routing` do orquestrador).
3. **Catálogo de especialistas** — tabela: nome → quando usar → arquivo
   (`agents/<nome>.md`). Instrução: "leia o arquivo do agente e assuma aquela persona".
4. **Catálogo de tasks** — tabela: task → quando usar → arquivo (`tasks/<task>.md`).
   Instrução: "leia e siga a task". **Listar apenas tasks com arquivo real** (pós-classificação
   de órfãs §4.7).
5. **Workflows** — quando rodar um workflow multi-agente (`workflows/*.yaml`).
6. **Checklist de qualidade** — referência a `checklists/` antes de entregar.
7. **Ponto de entrada "melhorar meu trabalho"** — fluxo: diagnosticar → rotear →
   carregar persona + task → produzir → revisar.
8. **Seção `KNOWN-GAPS`** — lista os comandos órfãos omitidos (input genuíno faltando), como
   backlog sob demanda. Comandos cuja ref é output de runtime **não** entram aqui (não são gaps).

### 4.6 Conteúdo do comando `commands/<squad-name>.md`

```markdown
---
description: Ativa o esquadrão <Squad Name> para <domínio>.
---
Use a skill `<squad-name>` para atender este pedido: $ARGUMENTS

Diagnostique a necessidade, roteie para o especialista adequado do esquadrão,
execute a task correspondente e entregue o resultado com checagem de qualidade.
```

### 4.7 Classificação de comandos órfãos (pré-requisito do SKILL.md)

Antes de sintetizar cada SKILL.md, rodar o **classificador de refs órfãs**:

1. Para cada squad, extrair as refs de task citadas nos `commands:` do agente orquestrador
   (e em outros agents) e verificar se o arquivo existe em `tasks/`.
2. Para cada ref **inexistente**, classificar:
   - **(i) input genuíno faltando** — uma task que o orquestrador esperaria *ler/executar*.
     → **OMITIR** o comando do SKILL.md + registrar em `KNOWN-GAPS`.
   - **(ii) output de runtime** — nome de arquivo que o agente *gera* durante a execução
     (ex.: `claude-md-go.md`, `api-docs.md`, `architecture.md`). → **MANTER** (não é gap).
3. Emitir um relatório `docs/relatorio-orfas.md` com os buckets por squad (artefato de QA).
4. Ambíguo → tratar como (i) e omitir (regra do Board: não deliberar por arquivo).

### 4.8 Licenciamento e atribuição (ver §2.2)

- `plugin.json` de cada squad herda `license` (`MIT` quando declarado na fonte) e credita o
  autor original via campo dedicado ou no README do plugin.
- Marketplace marca o squad de licença ambígua (ex.: chave `"license": "UNLICENSED"` +
  nota) e o README raiz instrui a **não redistribuí-los** sem confirmar proveniência.
- README raiz inclui seção **Atribuição/Créditos**: `Synkra AIOS` / `ohmyjahh/xquads-squads`.

---

## 5. Estratégia de Implementação

Pipeline determinístico (cópia/scaffold) + síntese por squad (SKILL.md).

1. **Preparar fonte:** clonar `xquads-squads` para um diretório temporário **fora** do
   versionamento do repo (já em `.gitignore` como `xquads-squads-src/`). Garantir que a
   fonte não seja commitada.
2. **Classificar órfãs (§4.7):** rodar o classificador nos 13 squads, gerar
   `docs/relatorio-orfas.md` (buckets input-faltando vs output-runtime + lista KNOWN-GAPS).
   Identificar o squad de licença ambígua: claude-code-mastery (§2.2).
3. **Scaffold determinístico (script):** para cada squad, criar a árvore de pastas, copiar
   `agents/tasks/workflows/data/checklists/config/README.md` verbatim para
   `skills/<squad>/`, e gerar `plugin.json` a partir do `squad.yaml`/`config.yaml`
   (preservando `author` + `license`).
4. **Síntese do SKILL.md (por squad), em PT-BR:** ler orquestrador + `squad.yaml` + README e
   escrever o `SKILL.md` conforme §4.5, aplicando a omissão de órfãs + `KNOWN-GAPS`.
   **Ordem:** começar pelos **7 squads limpos** (validação rápida), depois os 7 com órfãs.
   Processar em lotes (máx. 3 agentes simultâneos — regra do usuário) se paralelizar.
5. **Gerar comandos:** um `commands/<squad>.md` por plugin (§4.6), em PT-BR.
6. **Gerar `marketplace.json`** com as 13 entradas (§4.3), marcando o ambíguo (claude-code-mastery).
7. **Tratar `claude-code-mastery`** (caso especial §3 — `config.yaml` + `scripts/` + `templates/`).
8. **README raiz** com instruções de instalação, tabela dos 13 esquadrões e seção
   **Atribuição/Créditos** (§4.8). Adicionar `NOTICE` se aplicável.
9. **Validação** (§6).
10. **Commit + push** (conventional commits, sem co-autoria do Claude — regra do usuário).

---

## 6. Critérios de Aceite / Validação

- [ ] `.claude-plugin/marketplace.json` é JSON válido e lista exatamente os 13 plugins.
- [ ] Cada plugin tem `.claude-plugin/plugin.json` válido com `name` igual ao da pasta e ao
      do `marketplace.json`, **preservando `author` + `license` da fonte** (§2.2).
- [ ] Cada plugin tem `skills/<squad>/SKILL.md` com frontmatter `name` + `description`
      **em PT-BR, discriminativa, com keywords EN semeadas** (§2.1).
- [ ] Cada plugin tem `commands/<squad>.md` com frontmatter `description` (PT-BR).
- [ ] Todos os `agents/tasks/workflows/data/checklists` originais estão presentes e idênticos
      à fonte (contagem por squad confere com §3).
- [ ] **Todo comando/task listado no SKILL.md resolve para um arquivo existente** (zero refs
      input-faltando expostas); órfãs do tipo (i) omitidas e registradas em `KNOWN-GAPS`.
- [ ] `docs/relatorio-orfas.md` existe com os buckets por squad (§4.7).
- [ ] Os 7 squads limpos não têm seção `KNOWN-GAPS` (nada a omitir).
- [ ] O squad de licença ambígua (claude-code-mastery) está marcado no `marketplace.json` e citados no README
      raiz com aviso de não-redistribuição (§2.2/§4.8).
- [ ] README raiz tem seção **Atribuição/Créditos** (`Synkra AIOS` / `ohmyjahh/xquads-squads`).
- [ ] `claude-code-mastery` inclui `scripts/` e `templates/` e tem `plugin.json` derivado do
      `config.yaml`.
- [ ] Diretório-fonte temporário **não** está versionado.
- [ ] README raiz documenta `marketplace add` + `plugin install`.
- [ ] (Manual) `/plugin marketplace add .` + `/plugin install copy-squad@esquadrao-classe-a`
      instala e a skill responde a um pedido de teste.

---

## 7. Riscos e Mitigações

| Risco | Severidade | Mitigação |
|-------|:--:|-----------|
| **Licenciamento:** sem `LICENSE` no root; 1 squad (claude-code-mastery) sem declaração MIT. Redistribuir = risco de copyright. | **Alta se público** / Baixa se privado | Preservar `author`+`license`; manter privado/local; flagar o ambíguo; **não publicar** sem confirmar proveniência (§2.2). |
| Classificar ref de **output de runtime** como "task faltando" e omitir um comando válido. | Média | Classificador §4.7 com bucket (i)/(ii); revisão do `relatorio-orfas.md` antes de sintetizar. |
| Formato AIOS dos agents (`*comandos`, ACTIVATION-NOTICE) não mapeia 1:1 para Claude. | Baixa | Resources verbatim; o SKILL.md traduz o ponto de entrada para a sintaxe do Claude. |
| `claude-code-mastery` quebra o pipeline uniforme. | Baixa | Branch dedicado no script para `config.yaml` + pastas extras. |
| Volume (177 agents) torna o SKILL.md gigante. | Baixa | SKILL.md lista/roteia (catálogo enxuto); conteúdo pesado fica nos arquivos de agente, lidos sob demanda. |
| **Colisão de trigger** entre 13 skills parecidas (PT-BR). | Média | Descrições discriminativas + keywords EN semeadas (§2.1); spot-test de roteamento na validação. |
| Fonte commitada por engano. | Baixa | `.gitignore` + checagem no critério de aceite. |
| Conflito de nomes de comando entre plugins. | Baixa | Comando = nome do squad (único). Prefixos derivam do nome do plugin. |

---

## 8. Fora de Escopo

- Reescrever/normalizar o conteúdo dos agents/tasks (idioma mantido).
- Conversão nativa total (cada agent → subagent, cada task → comando).
- Publicação automatizada / CI do marketplace.
- Tradução de conteúdo.
