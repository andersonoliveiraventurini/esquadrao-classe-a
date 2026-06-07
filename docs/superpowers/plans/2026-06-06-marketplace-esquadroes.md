# Marketplace de Esquadrões — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Empacotar os 13 "squads" de `ohmyjahh/xquads-squads` como 13 plugins instaláveis num marketplace do Claude Code no repo `esquadrao-classe-a`.

**Architecture:** Arquitetura Híbrida — cada squad vira 1 plugin com `.claude-plugin/plugin.json`, um `commands/<squad>.md` e uma skill `skills/<squad>/SKILL.md` (cérebro orquestrador, sintetizado em PT-BR). Os `agents/tasks/workflows/data/checklists/config` originais são copiados **verbatim** para dentro da pasta da skill. Um script Python determinístico faz cópia + manifestos; a síntese do SKILL.md é feita por squad. Decisões do Board (DEC-001) aplicadas: classificar-e-omitir comandos órfãos, PT-BR + keywords EN, preservar atribuição/licença.

**Tech Stack:** Python 3.12 (`pip --user pyyaml`), `git`. Sem Node. Fonte clonada em `xquads-squads-src/` (gitignored).

**Referências:** `docs/PRD-marketplace-esquadroes.md` (spec). Formato alvo: `mwguerra/claude-code-plugins`.

**Os 13 squads:**
- **Limpos (7)** — sem órfãs: `advisory-board`, `brand-squad`, `cybersecurity`, `design-squad`, `hormozi-squad`, `storytelling`, `traffic-masters`.
- **Com órfãs (5)**: `copy-master`, `copy-squad`, `movement`, `data-squad`, `c-level-squad`.
- **Especial (1)**: `claude-code-mastery` (usa `config.yaml`, tem `scripts/` + `templates/`, ~50 refs que são majoritariamente outputs de runtime).

---

## File Structure

| Arquivo | Responsabilidade |
|---------|------------------|
| `scripts/lib_squads.py` | Constantes (lista de squads, paths) + leitor de manifesto (`squad.yaml`/`config.yaml`). |
| `scripts/classify_orphans.py` | Escaneia refs órfãs, classifica input-faltando vs output-runtime, gera `docs/relatorio-orfas.md`. |
| `scripts/build_marketplace.py` | Scaffold determinístico: copia resources, gera `plugin.json`, `commands/<squad>.md` e `.claude-plugin/marketplace.json`. |
| `<squad>/.claude-plugin/plugin.json` | Manifesto do plugin (gerado). |
| `<squad>/commands/<squad>.md` | Slash command que ativa a skill (gerado). |
| `<squad>/skills/<squad>/SKILL.md` | Orquestrador sintetizado em PT-BR (autoria por squad). |
| `<squad>/skills/<squad>/{agents,tasks,...}` | Resources verbatim (copiados). |
| `.claude-plugin/marketplace.json` | Manifesto do marketplace (gerado). |
| `README.md` | Instalação + tabela de esquadrões + Atribuição/Créditos. |
| `docs/relatorio-orfas.md` | Relatório de QA das refs órfãs (gerado). |

---

## Task 1: Preparar ambiente e dependências

**Files:**
- Create: `scripts/lib_squads.py`

- [ ] **Step 1: Confirmar fonte e instalar pyyaml**

Run:
```bash
test -d xquads-squads-src && echo "FONTE OK" || git clone --depth 1 https://github.com/ohmyjahh/xquads-squads.git xquads-squads-src
python -m pip install --user pyyaml
python -c "import yaml; print('pyyaml', yaml.__version__)"
```
Expected: `FONTE OK` e `pyyaml <versão>`. (Sem sudo — `--user` instala no perfil.)

- [ ] **Step 2: Criar `scripts/lib_squads.py`**

```python
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "xquads-squads-src"

# Ordem: limpos primeiro, depois com órfãs, especial por último.
CLEAN = ["advisory-board", "brand-squad", "cybersecurity", "design-squad",
         "hormozi-squad", "storytelling", "traffic-masters"]
ORPHAN = ["copy-master", "copy-squad", "movement", "data-squad", "c-level-squad"]
SPECIAL = ["claude-code-mastery"]
SQUADS = CLEAN + ORPHAN + SPECIAL

PACKAGER = {"name": "Anderson de Oliveira Venturini",
            "email": "anderson.oliveira.venturini@gmail.com"}

def read_manifest(squad_dir: Path) -> dict:
    sy, cy = squad_dir / "squad.yaml", squad_dir / "config.yaml"
    if sy.exists():
        d = yaml.safe_load(sy.read_text(encoding="utf-8")) or {}
        return {
            "name": d.get("name", squad_dir.name),
            "version": str(d.get("version", "1.0.0")),
            "description": (d.get("description") or "").strip(),
            "author": d.get("author", "Synkra AIOS"),
            "license": d.get("license", "UNLICENSED"),
            "keywords": d.get("tags") or [],
        }
    d = yaml.safe_load(cy.read_text(encoding="utf-8")) or {}
    sq = d.get("squad", {}) or {}
    return {
        "name": sq.get("name", squad_dir.name),
        "version": str(sq.get("version", "1.0.0")),
        "description": (sq.get("description") or "").strip().replace("\n", " "),
        "author": d.get("author") or sq.get("created_by", "Synkra AIOS"),
        "license": sq.get("license", "UNLICENSED"),
        "keywords": sq.get("keywords") or [],
    }
```

- [ ] **Step 3: Verificar o leitor**

Run:
```bash
python -c "from scripts.lib_squads import SQUADS, SRC, read_manifest; print(len(SQUADS)); [print(s, read_manifest(SRC/s)['license']) for s in SQUADS]"
```
Expected: `13` e uma linha por squad; `claude-code-mastery` e (no máximo) mais um com `UNLICENSED`, o resto `MIT`.

- [ ] **Step 4: Commit**

```bash
git add scripts/lib_squads.py
git commit -m "feat: add squad metadata library for marketplace build"
```

---

## Task 2: Classificador de comandos órfãos

**Files:**
- Create: `scripts/classify_orphans.py`
- Create (gerado): `docs/relatorio-orfas.md`

- [ ] **Step 1: Criar `scripts/classify_orphans.py`**

```python
import re
from pathlib import Path
from lib_squads import SQUADS, SRC, REPO

TASK_REF = re.compile(r'([a-z0-9][a-z0-9_-]*\.md)')
OUTPUT_HINT = re.compile(r'\b(creates?|outputs?|saves?|destino|produces?|gera|generates?|persiste)\b', re.I)
INPUT_HINT = re.compile(r'\b(task|executes?|runs?|executa|reads?|uses?|invoca|chama)\b', re.I)
IGNORE = {"readme.md", "changelog.md"}

def existing_md(squad_dir: Path) -> set:
    out = set()
    for sub in ("tasks", "agents", "workflows", "checklists"):
        d = squad_dir / sub
        if d.is_dir():
            out |= {p.name for p in d.glob("*.md")}
    return out

def classify(squad: str):
    sd = SRC / squad
    have = existing_md(sd)
    missing, runtime = {}, {}
    files = list((sd / "agents").glob("*.md"))
    for mf in ("squad.yaml", "config.yaml"):
        if (sd / mf).exists():
            files.append(sd / mf)
    files += list((sd / "workflows").glob("*.yaml"))
    for f in files:
        for ln in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            for m in TASK_REF.finditer(ln):
                ref = m.group(1)
                if ref in have or ref.lower() in IGNORE:
                    continue
                if OUTPUT_HINT.search(ln) and not INPUT_HINT.search(ln):
                    runtime.setdefault(ref, ln.strip())
                else:
                    missing.setdefault(ref, ln.strip())
    for k in list(runtime):          # ambíguo (em ambos) => trata como faltando
        if k in missing:
            runtime.pop(k)
    return missing, runtime

def main():
    lines = ["# Relatório de Refs Órfãs\n",
             "Gerado por `scripts/classify_orphans.py`. ",
             "`(i) input faltando` → OMITIR do SKILL.md + KNOWN-GAPS. ",
             "`(ii) output runtime` → MANTER (não é gap).\n"]
    for s in SQUADS:
        miss, rt = classify(s)
        lines.append(f"\n## {s}\n")
        lines.append(f"- input faltando (omitir): **{len(miss)}**\n")
        for k, ctx in sorted(miss.items()):
            lines.append(f"  - `{k}` — {ctx[:100]}\n")
        lines.append(f"- output runtime (manter): **{len(rt)}**\n")
        for k, ctx in sorted(rt.items()):
            lines.append(f"  - `{k}` — {ctx[:100]}\n")
    (REPO / "docs" / "relatorio-orfas.md").write_text("".join(lines), encoding="utf-8")
    print("OK -> docs/relatorio-orfas.md")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Rodar o classificador**

Run:
```bash
cd scripts && python classify_orphans.py && cd ..
```
Expected: `OK -> docs/relatorio-orfas.md`.

- [ ] **Step 3: Validar buckets contra a expectativa**

Run:
```bash
grep -E '^## |input faltando|output runtime' docs/relatorio-orfas.md
```
Expected: os 7 squads limpos com `input faltando: 0`; `copy-master`/`copy-squad` com ~2 faltando; `claude-code-mastery` com a maioria em `output runtime`. Revisar visualmente os itens listados — se algum `output runtime` parecer um input real, anotar para tratar na síntese.

- [ ] **Step 4: Commit**

```bash
git add scripts/classify_orphans.py docs/relatorio-orfas.md
git commit -m "feat: add orphan-reference classifier and QA report"
```

---

## Task 3: Script de scaffold + manifestos (piloto em 1 squad)

**Files:**
- Create: `scripts/build_marketplace.py`

- [ ] **Step 1: Criar `scripts/build_marketplace.py`**

```python
import json, shutil, sys
from pathlib import Path
from lib_squads import SQUADS, SRC, REPO, PACKAGER, read_manifest

RES_DIRS = ["agents", "tasks", "workflows", "data", "checklists", "config", "scripts", "templates"]
RES_FILES = ["README.md"]

def build_plugin(name: str) -> dict:
    src, dest = SRC / name, REPO / name
    skill = dest / "skills" / name
    (dest / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (dest / "commands").mkdir(parents=True, exist_ok=True)
    skill.mkdir(parents=True, exist_ok=True)
    for d in RES_DIRS:
        if (src / d).is_dir():
            shutil.copytree(src / d, skill / d, dirs_exist_ok=True)
    for f in RES_FILES:
        if (src / f).is_file():
            shutil.copy2(src / f, skill / f)
    mf = read_manifest(src)
    plugin = {
        "name": name,
        "version": mf["version"],
        "description": mf["description"],
        "license": mf["license"],
        "author": {"name": mf["author"]},          # preserva atribuição original (MIT)
        "keywords": mf["keywords"],
        "metadata": {"source": "ohmyjahh/xquads-squads", "packaged_by": PACKAGER["name"]},
    }
    (dest / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(plugin, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cmd = (f"---\ndescription: Ativa o esquadrão {name} e roteia para o especialista certo.\n---\n"
           f"Use a skill `{name}` para atender este pedido: $ARGUMENTS\n\n"
           f"Diagnostique a necessidade, roteie para o especialista adequado do esquadrão,\n"
           f"execute a task correspondente e entregue o resultado com checagem de qualidade.\n")
    (dest / "commands" / f"{name}.md").write_text(cmd, encoding="utf-8")
    return plugin

def build_marketplace(plugins: list):
    mp = {
        "name": "esquadrao-classe-a",
        "owner": PACKAGER,
        "metadata": {
            "description": "Esquadrões de agentes de IA empacotados como plugins do Claude Code.",
            "version": "1.0.0",
            "source": "ohmyjahh/xquads-squads",
        },
        "plugins": [{
            "name": p["name"], "source": f"./{p['name']}", "version": p["version"],
            "description": p["description"], "keywords": p["keywords"], "license": p["license"],
        } for p in plugins],
    }
    (REPO / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (REPO / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps(mp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    targets = sys.argv[1:] or SQUADS
    built = [build_plugin(s) for s in targets]
    if set(targets) == set(SQUADS) or "--marketplace" in sys.argv:
        all_plugins = [build_plugin(s) for s in SQUADS]  # idempotente
        build_marketplace(all_plugins)
        print(f"marketplace.json com {len(all_plugins)} plugins")
    print("plugins:", ", ".join(p["name"] for p in built))

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Rodar o scaffold só no piloto `advisory-board`**

Run:
```bash
cd scripts && python build_marketplace.py advisory-board && cd ..
```
Expected: `plugins: advisory-board`.

- [ ] **Step 3: Verificar a estrutura gerada e a contagem de resources**

Run:
```bash
find advisory-board -type f | sort
echo "--- agents na fonte vs destino ---"
echo "fonte:   $(ls xquads-squads-src/advisory-board/agents | wc -l)"
echo "destino: $(ls advisory-board/skills/advisory-board/agents | wc -l)"
python -c "import json; d=json.load(open('advisory-board/.claude-plugin/plugin.json',encoding='utf-8')); print(d['name'], d['license'], d['author'])"
```
Expected: `plugin.json` + `commands/advisory-board.md` + `skills/advisory-board/{agents,tasks,workflows,data,checklists,...}`; contagem de agents igual (11); `license` = `MIT`, `author` = `Synkra AIOS`.

- [ ] **Step 4: Commit**

```bash
git add scripts/build_marketplace.py advisory-board/
git commit -m "feat: add marketplace build script; scaffold advisory-board plugin"
```

---

## Task 4: Sintetizar o SKILL.md do piloto (`advisory-board`)

**Files:**
- Create: `advisory-board/skills/advisory-board/SKILL.md`

- [ ] **Step 1: Ler as fontes do orquestrador**

Run:
```bash
sed -n '1,80p' xquads-squads-src/advisory-board/agents/*chair*.md 2>/dev/null || ls xquads-squads-src/advisory-board/agents
cat xquads-squads-src/advisory-board/squad.yaml
sed -n '1,40p' xquads-squads-src/advisory-board/README.md
```
Identificar: agente orquestrador, lógica de roteamento, lista de especialistas, lista de tasks.

- [ ] **Step 2: Escrever `advisory-board/skills/advisory-board/SKILL.md`** seguindo o template (PT-BR):

```markdown
---
name: advisory-board
description: Use quando o usuário precisar de aconselhamento estratégico de negócios/vida de um conselho de mentores (ex.: decisões de escala, cultura, investimento, founder counsel). Roteia para o mentor certo. Keywords: advisory board, mentorship, strategy, decision-making, founder advice.
---

# Esquadrão: Advisory Board

> Fonte: `ohmyjahh/xquads-squads` · Autor original: Synkra AIOS · Licença: MIT

## Propósito
[2-3 frases do README/squad.yaml — o que o esquadrão faz.]

## Como me usar (fluxo)
1. **Diagnosticar** o pedido do usuário (tipo de decisão, contexto, urgência).
2. **Rotear** para o(s) especialista(s) certo(s) usando a tabela abaixo.
3. **Carregar a persona**: ler `agents/<nome>.md` e assumir aquela voz/framework.
4. **Executar a task**: ler `tasks/<task>.md` e seguir suas fases.
5. **Checar qualidade** com `checklists/` antes de entregar.

## Lógica de roteamento
[Resumir o routing do agente orquestrador — quando usar cada mentor.]

## Especialistas (personas)
| Mentor | Quando usar | Arquivo |
|--------|-------------|---------|
| [nome] | [foco]      | `agents/[arquivo].md` |
[... uma linha por agente real em agents/ ...]

## Tasks disponíveis
| Task | Quando usar | Arquivo |
|------|-------------|---------|
| [nome] | [objetivo] | `tasks/[arquivo].md` |
[... APENAS tasks com arquivo real ...]

## Workflows
[Listar workflows/*.yaml e quando rodar cada um.]

## Checklist de qualidade
Antes de entregar, validar contra `checklists/output-quality.md`.
```

> Regras: descrição **discriminativa** + 3-6 keywords EN; identificadores e nomes de arquivo **verbatim**; listar só tasks/comandos com arquivo existente. `advisory-board` é limpo → **sem seção KNOWN-GAPS**.

- [ ] **Step 3: Validar o SKILL.md**

Run:
```bash
python - <<'PY'
import re, pathlib
p = pathlib.Path("advisory-board/skills/advisory-board/SKILL.md")
t = p.read_text(encoding="utf-8")
assert t.startswith("---"), "sem frontmatter"
assert re.search(r'^name:\s*advisory-board\s*$', t, re.M), "name errado"
assert re.search(r'^description:\s*.+', t, re.M), "sem description"
# toda task referenciada existe?
base = pathlib.Path("advisory-board/skills/advisory-board")
refs = set(re.findall(r'`(?:tasks|agents)/([a-z0-9_-]+\.md)`', t))
for r in refs:
    hit = (base/"tasks"/r).exists() or (base/"agents"/r).exists()
    assert hit, f"ref inexistente no SKILL.md: {r}"
print("SKILL.md OK -", len(refs), "refs resolvem")
PY
```
Expected: `SKILL.md OK - N refs resolvem`.

- [ ] **Step 4: Commit**

```bash
git add advisory-board/skills/advisory-board/SKILL.md
git commit -m "feat(advisory-board): synthesize orchestrator SKILL.md (PT-BR)"
```

---

## Task 5: Scaffold de todos os 13 squads + marketplace.json

**Files:**
- Create: `<cada-squad>/...` (12 restantes) + `.claude-plugin/marketplace.json`

- [ ] **Step 1: Rodar o build completo**

Run:
```bash
cd scripts && python build_marketplace.py && cd ..
```
Expected: `marketplace.json com 13 plugins` e a lista dos 13.

- [ ] **Step 2: Validar marketplace.json e contagem de plugins**

Run:
```bash
python - <<'PY'
import json, pathlib
mp = json.load(open(".claude-plugin/marketplace.json", encoding="utf-8"))
assert mp["name"] == "esquadrao-classe-a"
names = [p["name"] for p in mp["plugins"]]
assert len(names) == 13, names
for n in names:
    assert pathlib.Path(n, ".claude-plugin", "plugin.json").exists(), n
    assert pathlib.Path(n, "commands", f"{n}.md").exists(), n
    assert pathlib.Path(n, "skills", n).is_dir(), n
amb = [p["name"] for p in mp["plugins"] if p["license"] == "UNLICENSED"]
print("OK 13 plugins; licença ambígua:", amb)
PY
```
Expected: `OK 13 plugins; licença ambígua: ['claude-code-mastery', ...]` (1 ou 2 nomes).

- [ ] **Step 3: Verificar contagem de resources de todos os squads (não-perda)**

Run:
```bash
for s in advisory-board brand-squad cybersecurity design-squad hormozi-squad storytelling traffic-masters copy-master copy-squad movement data-squad c-level-squad claude-code-mastery; do
  a=$(ls xquads-squads-src/$s/agents 2>/dev/null | wc -l)
  b=$(ls $s/skills/$s/agents 2>/dev/null | wc -l)
  [ "$a" = "$b" ] && echo "OK  $s agents=$a" || echo "DIFF $s fonte=$a destino=$b"
done
```
Expected: todas as linhas `OK`.

- [ ] **Step 4: Commit**

```bash
git add .claude-plugin/ brand-squad/ cybersecurity/ design-squad/ hormozi-squad/ storytelling/ traffic-masters/ copy-master/ copy-squad/ movement/ data-squad/ c-level-squad/ claude-code-mastery/
git commit -m "feat: scaffold all 13 squad plugins and generate marketplace.json"
```

---

## Task 6: Sintetizar SKILL.md dos 6 squads limpos restantes

**Files:**
- Create: `SKILL.md` em `brand-squad`, `cybersecurity`, `design-squad`, `hormozi-squad`, `storytelling`, `traffic-masters`.

> Sem órfãs → **sem KNOWN-GAPS**. Repetir o procedimento da Task 4 para cada squad.
> Recomendado: 1 subagente por squad (respeitar máx. 3 simultâneos).

- [ ] **Step 1: Para CADA squad da lista, ler as fontes**

Run (exemplo `brand-squad`):
```bash
S=brand-squad; cat xquads-squads-src/$S/squad.yaml; ls xquads-squads-src/$S/agents xquads-squads-src/$S/tasks; sed -n '1,40p' xquads-squads-src/$S/README.md
```

- [ ] **Step 2: Escrever `<S>/skills/<S>/SKILL.md`** seguindo o mesmo template da Task 4 Step 2, em PT-BR, com description discriminativa + keywords EN, listando todos os agents reais e todas as tasks reais.

- [ ] **Step 3: Validar cada SKILL.md** com o mesmo script de validação da Task 4 Step 3 (trocar o caminho do squad). Expected: `SKILL.md OK`.

- [ ] **Step 4: Commit (um por squad ou em lote)**

```bash
git add brand-squad/skills cybersecurity/skills design-squad/skills hormozi-squad/skills storytelling/skills traffic-masters/skills
git commit -m "feat: synthesize SKILL.md for 6 clean squads (PT-BR)"
```

---

## Task 7: Sintetizar SKILL.md dos 5 squads com órfãs (omissão + KNOWN-GAPS)

**Files:**
- Create: `SKILL.md` em `copy-master`, `copy-squad`, `movement`, `data-squad`, `c-level-squad`.

- [ ] **Step 1: Para cada squad, consultar o bucket no relatório**

Run (exemplo `copy-master`):
```bash
S=copy-master; awk "/^## $S$/,/^## /" docs/relatorio-orfas.md
```
Anotar quais refs são `input faltando` (omitir) e quais são `output runtime` (manter).

- [ ] **Step 2: Escrever `<S>/skills/<S>/SKILL.md`** como na Task 4, MAS:
  - Na tabela de tasks, **listar só tasks com arquivo real** (não incluir as `input faltando`).
  - Comandos do orquestrador que apontavam para `input faltando` → **não expor**.
  - Adicionar ao final a seção:

```markdown
## KNOWN-GAPS
Comandos do orquestrador original cuja task não existe na fonte (omitidos até haver demanda real):
- `*<comando>` → `<arquivo-faltando>.md` — escrever a task sob demanda quando um fluxo travar nela.
```

- [ ] **Step 3: Validar** com o script da Task 4 Step 3 (todas as refs listadas devem resolver). Expected: `SKILL.md OK`.

- [ ] **Step 4: Commit**

```bash
git add copy-master/skills copy-squad/skills movement/skills data-squad/skills c-level-squad/skills
git commit -m "feat: synthesize SKILL.md for 5 squads with orphan handling + KNOWN-GAPS"
```

---

## Task 8: Squad especial `claude-code-mastery`

**Files:**
- Create: `claude-code-mastery/skills/claude-code-mastery/SKILL.md`

- [ ] **Step 1: Confirmar que `scripts/` e `templates/` foram copiados**

Run:
```bash
ls claude-code-mastery/skills/claude-code-mastery/ | tr '\n' ' '; echo
test -d claude-code-mastery/skills/claude-code-mastery/scripts && echo "scripts OK"
test -d claude-code-mastery/skills/claude-code-mastery/templates && echo "templates OK"
python -c "import json; d=json.load(open('claude-code-mastery/.claude-plugin/plugin.json',encoding='utf-8')); print('license=',d['license'])"
```
Expected: `scripts OK`, `templates OK`, `license= UNLICENSED` (ambíguo).

- [ ] **Step 2: Consultar o bucket de órfãs (maioria deve ser output runtime)**

Run:
```bash
awk '/^## claude-code-mastery$/,0' docs/relatorio-orfas.md | head -60
```
Revisar: confirmar que itens tipo `claude-md-go.md`, `api-docs.md`, `architecture.md` estão como `output runtime` (manter, não são gaps).

- [ ] **Step 3: Escrever o SKILL.md** (template da Task 4) usando `config.yaml` (campo `squad.entry_agent: claude-mastery-chief`) como orquestrador. Listar agents/tasks reais; KNOWN-GAPS só para `input faltando` genuínos (se houver). Mencionar que o squad gera arquivos de output em runtime (não são tasks ausentes).

- [ ] **Step 4: Validar e commit**

Run o script de validação (Task 4 Step 3) para este squad. Depois:
```bash
git add claude-code-mastery/skills
git commit -m "feat(claude-code-mastery): synthesize SKILL.md (config.yaml orchestrator)"
```

---

## Task 9: README raiz com instalação e atribuição

**Files:**
- Create: `README.md`
- Create: `NOTICE`

- [ ] **Step 1: Escrever `NOTICE`**

```text
Este marketplace empacota os "squads" do projeto ohmyjahh/xquads-squads.
Autor original do conteúdo dos squads: Synkra AIOS.
Squads com `license: MIT` declarada no manifesto de origem mantêm a licença MIT.
Squads sem declaração de licença (ex.: claude-code-mastery) são de licença AMBÍGUA
e NÃO devem ser redistribuídos sem confirmação de proveniência com o autor original.
Empacotamento e camada sintetizada (SKILL.md/comandos): Anderson de Oliveira Venturini.
```

- [ ] **Step 2: Escrever `README.md`** com:
  - Título + 1 parágrafo do que é.
  - **Instalação:**
    ```
    /plugin marketplace add andersonoliveiraventurini/esquadrao-classe-a
    /plugin install copy-squad@esquadrao-classe-a
    ```
  - Tabela dos 13 esquadrões: nome do plugin · domínio · comando de install. Gerar a tabela a partir do marketplace.json:
    ```bash
    python - <<'PY'
    import json
    mp = json.load(open(".claude-plugin/marketplace.json", encoding="utf-8"))
    print("| Esquadrão | Descrição | Instalar |")
    print("|-----------|-----------|----------|")
    for p in mp["plugins"]:
        d = p["description"][:80].replace("|", "/")
        print(f"| `{p['name']}` | {d}… | `/plugin install {p['name']}@esquadrao-classe-a` |")
    PY
    ```
    (Colar a saída no README.)
  - Seção **Atribuição/Créditos**: link para `ohmyjahh/xquads-squads`, Synkra AIOS, formato inspirado em `mwguerra/claude-code-plugins`.
  - Aviso de licença: marketplace **privado**; não publicar os squads ambíguos sem licença.

- [ ] **Step 3: Commit**

```bash
git add README.md NOTICE
git commit -m "docs: add root README (install + squad table) and NOTICE (attribution)"
```

---

## Task 10: Validação final (critérios de aceite do PRD §6)

- [ ] **Step 1: Validação automatizada completa**

Run:
```bash
python - <<'PY'
import json, re, pathlib
mp = json.load(open(".claude-plugin/marketplace.json", encoding="utf-8"))
plugins = mp["plugins"]
assert len(plugins) == 13, len(plugins)
for p in plugins:
    n = p["name"]
    pj = json.load(open(f"{n}/.claude-plugin/plugin.json", encoding="utf-8"))
    assert pj["name"] == n
    assert "author" in pj and "license" in pj
    skill = pathlib.Path(n, "skills", n, "SKILL.md")
    assert skill.exists(), f"sem SKILL.md: {n}"
    t = skill.read_text(encoding="utf-8")
    assert re.search(rf'^name:\s*{re.escape(n)}\s*$', t, re.M), f"name: {n}"
    assert re.search(r'^description:\s*.+', t, re.M), f"description: {n}"
    base = pathlib.Path(n, "skills", n)
    for r in set(re.findall(r'`(?:tasks|agents)/([a-z0-9_-]+\.md)`', t)):
        assert (base/"tasks"/r).exists() or (base/"agents"/r).exists(), f"{n}: ref {r}"
    cmd = pathlib.Path(n, "commands", f"{n}.md")
    assert cmd.exists() and cmd.read_text(encoding="utf-8").startswith("---"), f"command: {n}"
print("TODOS OS 13 PLUGINS VÁLIDOS")
PY
```
Expected: `TODOS OS 13 PLUGINS VÁLIDOS`.

- [ ] **Step 2: Confirmar que a fonte não está versionada**

Run:
```bash
git status --porcelain | grep xquads-squads-src && echo "ERRO: fonte versionada" || echo "OK: fonte ignorada"
```
Expected: `OK: fonte ignorada`.

- [ ] **Step 3: (Manual) Testar instalação real no Claude Code**

No Claude Code:
```
/plugin marketplace add .
/plugin install advisory-board@esquadrao-classe-a
```
Depois invocar a skill com um pedido de teste e confirmar que ela roteia para um especialista e lê o arquivo do agente. Validar também `copy-squad` (squad com órfãs) e `claude-code-mastery` (especial).

- [ ] **Step 4: Spot-test de colisão de trigger**

Dar 3 prompts ambíguos (ex.: "preciso de uma headline", "quero rever minha estratégia de cultura", "configurar hooks do Claude Code") e confirmar que ativam, respectivamente, `copy-squad`/`copy-master`, `advisory-board`/`c-level-squad`, `claude-code-mastery` — sem colisão grosseira. Ajustar descriptions se houver colisão.

---

## Task 11: Push final

- [ ] **Step 1: Revisar o log e push**

Run:
```bash
git log --oneline -15
git push -u origin main
```
Expected: histórico com os commits do marketplace; push aceito.

> Lembrete (regra do usuário): commits sem co-autoria do Claude; conventional commits; testes/validação verdes antes do push.

---

## Self-Review (cobertura do spec)

- ✅ Arquitetura Híbrida (PRD §4.2) → Tasks 3-8.
- ✅ 13 squads, ordem limpos→órfãos→especial (PRD §3) → Tasks 5-8.
- ✅ marketplace.json + plugin.json com atribuição (PRD §4.3/§4.4/§2.2) → Tasks 3,5,9.
- ✅ SKILL.md PT-BR + discriminativa + keywords EN (PRD §2.1/§4.5) → Tasks 4,6,7,8.
- ✅ Classificar-e-omitir órfãs + KNOWN-GAPS (PRD §2.1/§4.7) → Tasks 2,7,8.
- ✅ Licença/atribuição: preservar author+license, NOTICE, flag ambíguos (PRD §2.2/§4.8) → Tasks 3,9.
- ✅ claude-code-mastery especial (PRD §3) → Task 8.
- ✅ Fonte não versionada (PRD §6) → `.gitignore` + Task 10 Step 2.
- ✅ Critérios de aceite (PRD §6) → Task 10.
