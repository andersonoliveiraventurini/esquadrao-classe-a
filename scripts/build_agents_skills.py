"""Espelha cada esquadrão para .agents/skills/<squad>/ — o formato lido nativamente
por opencode E Codex (e por ~/.agents/skills global em ambos).

Copia o estado ATUAL de <squad>/skills/<squad>/ (SKILL.md + resources + orquestradores
já diferenciados). NÃO recopia da fonte (não reverte a diferenciação)."""
import shutil
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_squads import SQUADS, REPO


def main():
    dest_root = REPO / ".agents" / "skills"
    if dest_root.exists():
        shutil.rmtree(dest_root)
    dest_root.mkdir(parents=True)
    for n in SQUADS:
        src = REPO / n / "skills" / n
        if not (src / "SKILL.md").exists():
            print(f"  AVISO: {n} sem SKILL.md — pulado")
            continue
        shutil.copytree(src, dest_root / n)
        nag = len(list((dest_root / n / "agents").glob("*.md")))
        print(f"  {n:22} -> .agents/skills/{n}/ (SKILL.md + {nag} agents)")
    print(f"\nOK: {len(list(dest_root.iterdir()))} skills em .agents/skills/")


if __name__ == "__main__":
    main()
