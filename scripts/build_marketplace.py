"""Scaffold determinístico: copia resources (com rebrand), gera plugin.json,
commands/<squad>.md e .claude-plugin/marketplace.json."""
import json
import shutil
import sys
from pathlib import Path
from lib_squads import (SQUADS, SRC, REPO, PACKAGER, MARKETPLACE,
                        read_manifest, transform_text)

RES_DIRS = ["agents", "tasks", "workflows", "data", "checklists", "config", "scripts", "templates"]
RES_FILES = ["README.md"]
TEXT_EXT = {".md", ".yaml", ".yml", ".txt", ".json"}


def copy_tree_transformed(src: Path, dst: Path):
    """Copia recursivamente aplicando rebrand em arquivos de texto."""
    for p in src.rglob("*"):
        rel = p.relative_to(src)
        target = dst / rel
        if p.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        if p.suffix.lower() in TEXT_EXT:
            try:
                txt = p.read_text(encoding="utf-8")
                target.write_text(transform_text(txt), encoding="utf-8")
                continue
            except UnicodeDecodeError:
                pass
        shutil.copy2(p, target)


def build_plugin(name: str) -> dict:
    src, dest = SRC / name, REPO / name
    skill = dest / "skills" / name
    (dest / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (dest / "commands").mkdir(parents=True, exist_ok=True)
    skill.mkdir(parents=True, exist_ok=True)
    for d in RES_DIRS:
        if (src / d).is_dir():
            copy_tree_transformed(src / d, skill / d)
    for f in RES_FILES:
        if (src / f).is_file():
            (skill / f).write_text(transform_text((src / f).read_text(encoding="utf-8")), encoding="utf-8")
    mf = read_manifest(src)
    plugin = {
        "name": name,
        "version": mf["version"],
        "description": mf["description"],
        "license": mf["license"],
        "author": PACKAGER,
        "keywords": mf["keywords"],
        "metadata": {
            "adapted_from": "ohmyjahh/xquads-squads",
            "original_author": "Synkra AIOS",
        },
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
        "name": MARKETPLACE,
        "owner": PACKAGER,
        "metadata": {
            "description": "Esquadrões de agentes de IA especialistas para o Claude Code.",
            "version": "1.0.0",
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
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    targets = args or SQUADS
    built = [build_plugin(s) for s in targets]
    if not args or "--marketplace" in sys.argv:
        all_plugins = [build_plugin(s) for s in SQUADS]
        build_marketplace(all_plugins)
        print(f"marketplace.json com {len(all_plugins)} plugins")
    print("plugins gerados:", ", ".join(p["name"] for p in built))


if __name__ == "__main__":
    main()
