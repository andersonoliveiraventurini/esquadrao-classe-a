"""Cria o plugin-bundle 'esquadrao-completo' — um único plugin do Claude Code que
empacota os 13 esquadrões (skills + comandos). Permite instalar tudo com UM comando:

    /plugin install esquadrao-completo@esquadrao-classe-a

Também registra o bundle no marketplace.json (sem regenerar o resto)."""
import json
import shutil
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_squads import SQUADS, REPO, PACKAGER

BUNDLE = "esquadrao-completo"


def build():
    dest = REPO / BUNDLE
    # limpa skills/commands antigos do bundle (mantém idempotência)
    for sub in ("skills", "commands"):
        if (dest / sub).exists():
            shutil.rmtree(dest / sub)
    (dest / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (dest / "skills").mkdir(parents=True, exist_ok=True)
    (dest / "commands").mkdir(parents=True, exist_ok=True)

    kw = set()
    for s in SQUADS:
        # skill (SKILL.md + resources) com o estado atual (já diferenciado)
        shutil.copytree(REPO / s / "skills" / s, dest / "skills" / s)
        # comando
        shutil.copy2(REPO / s / "commands" / f"{s}.md", dest / "commands" / f"{s}.md")
        pj = json.load(open(REPO / s / ".claude-plugin" / "plugin.json", encoding="utf-8"))
        kw.update(pj.get("keywords", [])[:3])

    plugin = {
        "name": BUNDLE,
        "version": "1.0.0",
        "description": ("Pacote completo: instala os 13 esquadrões de uma vez "
                        "(177 agentes especialistas). Use este plugin único em vez de "
                        "instalar squad por squad."),
        "license": "MIT",
        "author": PACKAGER,
        "keywords": sorted(kw)[:25],
        "metadata": {"bundles": SQUADS, "adapted_from": "ohmyjahh/xquads-squads",
                     "note": "claude-code-mastery tem licença ambígua — ver NOTICE"},
    }
    (dest / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(plugin, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # registra no marketplace.json (sem regenerar os demais)
    mp_path = REPO / ".claude-plugin" / "marketplace.json"
    mp = json.load(open(mp_path, encoding="utf-8"))
    entry = {"name": BUNDLE, "source": f"./{BUNDLE}", "version": "1.0.0",
             "description": plugin["description"], "keywords": plugin["keywords"],
             "license": "MIT"}
    mp["plugins"] = [p for p in mp["plugins"] if p["name"] != BUNDLE]
    mp["plugins"].insert(0, entry)  # bundle em primeiro
    mp_path.write_text(json.dumps(mp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    nsk = len(list((dest / "skills").iterdir()))
    print(f"OK: bundle '{BUNDLE}' com {nsk} skills + comandos; registrado no marketplace.json")


if __name__ == "__main__":
    build()
