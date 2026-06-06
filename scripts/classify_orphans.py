"""Escaneia refs de task órfãs e classifica input-faltando vs output-runtime."""
import re
from pathlib import Path
from lib_squads import SQUADS, SRC, REPO

TASK_REF = re.compile(r'([a-z0-9][a-z0-9_-]*\.md)')
OUTPUT_HINT = re.compile(r'\b(creates?|outputs?|saves?|destino|produces?|gera|generates?|persiste|saida|saída)\b', re.I)
INPUT_HINT = re.compile(r'\b(task|executes?|runs?|executa|reads?|uses?|invoca|chama|entrada)\b', re.I)
IGNORE = {"readme.md", "changelog.md", "notice.md", "license.md"}


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
    for k in list(runtime):
        if k in missing:
            runtime.pop(k)
    return missing, runtime


def main():
    out = ["# Relatório de Refs Órfãs\n\n",
           "Gerado por `scripts/classify_orphans.py`.\n\n",
           "- `(i) input faltando` → **OMITIR** do SKILL.md + registrar em KNOWN-GAPS.\n",
           "- `(ii) output runtime` → **MANTER** (é arquivo que o agente gera, não um gap).\n"]
    totals = []
    for s in SQUADS:
        miss, rt = classify(s)
        totals.append((s, len(miss), len(rt)))
        out.append(f"\n## {s}\n\n")
        out.append(f"**input faltando (omitir): {len(miss)}**\n")
        for k, ctx in sorted(miss.items()):
            out.append(f"- `{k}` — {ctx[:110]}\n")
        out.append(f"\n**output runtime (manter): {len(rt)}**\n")
        for k, ctx in sorted(rt.items()):
            out.append(f"- `{k}` — {ctx[:110]}\n")
    out.append("\n## Resumo\n\n| Squad | input faltando | output runtime |\n|---|---|---|\n")
    for s, m, r in totals:
        out.append(f"| {s} | {m} | {r} |\n")
    (REPO / "docs" / "relatorio-orfas.md").write_text("".join(out), encoding="utf-8")
    print("OK -> docs/relatorio-orfas.md")
    for s, m, r in totals:
        print(f"  {s:22} input-faltando={m:2}  output-runtime={r}")


if __name__ == "__main__":
    main()
