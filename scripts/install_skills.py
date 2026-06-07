"""Instala os 13 esquadrões como Agent Skills para opencode e Codex.

Uso:
    python install_skills.py                  # global: ~/.agents/skills/ (opencode + Codex)
    python install_skills.py --dest CAMINHO   # num projeto: CAMINHO/.agents/skills/
    python install_skills.py --list           # só lista o que seria instalado

~/.agents/skills/ é lido nativamente por opencode (global) e por Codex (escopo de usuário),
então uma única instalação cobre as duas ferramentas em todos os seus projetos.
"""
import argparse
import shutil
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_squads import SQUADS, REPO

SRC_ROOT = REPO / ".agents" / "skills"


def install(dest_root: Path):
    dest_root.mkdir(parents=True, exist_ok=True)
    n = 0
    for s in SQUADS:
        src = SRC_ROOT / s
        if not (src / "SKILL.md").exists():
            print(f"  AVISO: {s} ausente em .agents/skills — rode build_agents_skills.py antes")
            continue
        target = dest_root / s
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(src, target)
        n += 1
        print(f"  instalado: {s}")
    print(f"\nOK: {n} esquadroes -> {dest_root}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", help="raiz de um projeto (instala em <dest>/.agents/skills/)")
    ap.add_argument("--list", action="store_true", help="apenas lista os esquadroes")
    args = ap.parse_args()
    if not SRC_ROOT.exists():
        print("ERRO: .agents/skills/ nao existe. Rode: python build_agents_skills.py")
        sys.exit(1)
    if args.list:
        for s in SQUADS:
            print(" ", s)
        return
    if args.dest:
        dest = Path(args.dest).expanduser().resolve() / ".agents" / "skills"
    else:
        dest = Path.home() / ".agents" / "skills"
    install(dest)


if __name__ == "__main__":
    main()
