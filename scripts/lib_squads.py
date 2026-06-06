"""Biblioteca compartilhada do build do marketplace Esquadrão Clase A."""
from pathlib import Path
import yaml

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "xquads-squads-src"

# Ordem de processamento: limpos primeiro, depois com órfãs, especial por último.
CLEAN = ["advisory-board", "brand-squad", "cybersecurity", "design-squad",
         "hormozi-squad", "storytelling", "traffic-masters"]
ORPHAN = ["copy-master", "copy-squad", "movement", "data-squad", "c-level-squad"]
SPECIAL = ["claude-code-mastery"]
SQUADS = CLEAN + ORPHAN + SPECIAL

PACKAGER = {"name": "Anderson de Oliveira Venturini",
            "email": "anderson.oliveira.venturini@gmail.com"}

MARKETPLACE = "esquadrao-clase-a"

# Rebrand: remove a marca da fonte para o projeto ter identidade própria.
# (A atribuição MIT ao autor original fica centralizada no NOTICE/README.)
REBRAND = [
    ("Synkra AIOS", "Esquadrão Clase A"),
    ("Synkra", "Esquadrão Clase A"),
    ("xQuads", "Esquadrão Clase A"),
    ("XQuads", "Esquadrão Clase A"),
    ("Xquads", "Esquadrão Clase A"),
]


def transform_text(s: str) -> str:
    for a, b in REBRAND:
        s = s.replace(a, b)
    return s


def read_manifest(squad_dir: Path) -> dict:
    sy, cy = squad_dir / "squad.yaml", squad_dir / "config.yaml"
    if sy.exists():
        d = yaml.safe_load(sy.read_text(encoding="utf-8")) or {}
        return {
            "name": d.get("name", squad_dir.name),
            "version": str(d.get("version", "1.0.0")),
            "description": (d.get("description") or "").strip(),
            "author": d.get("author", "autor original"),
            "license": d.get("license", "UNLICENSED"),
            "keywords": d.get("tags") or [],
            "short_title": d.get("short-title") or d.get("short_title") or "",
        }
    d = yaml.safe_load(cy.read_text(encoding="utf-8")) or {}
    sq = d.get("squad", {}) or {}
    return {
        "name": sq.get("name", squad_dir.name),
        "version": str(sq.get("version", "1.0.0")),
        "description": (sq.get("description") or "").strip().replace("\n", " "),
        "author": d.get("author") or sq.get("created_by", "autor original"),
        "license": sq.get("license", "UNLICENSED"),
        "keywords": sq.get("keywords") or [],
        "short_title": sq.get("display_name", ""),
    }
