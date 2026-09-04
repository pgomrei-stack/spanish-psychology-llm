#!/usr/bin/env python3
"""Valida data/raw/pilot/pilot_questions.json contra data/raw/question_schema.json.

Comprueba:
  - Conformidad con el JSON Schema (Draft 2020-12).
  - Higiene de codificación: ausencia de BOM y de mojibake típico de UTF-8
    mal decodificado como Latin-1/CP1252 (secuencias "Ã©", "Ã³", etc.).
  - IDs duplicados (bloqueante).
  - Equilibrio de dimensiones (aviso, no bloqueante).

Uso:
    python3 scripts/validate_dataset.py \
        [--schema data/raw/question_schema.json] \
        [--data data/raw/pilot/pilot_questions.json]

Código de salida: 0 si todo pasa, 1 si hay al menos un error bloqueante.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCHEMA = REPO_ROOT / "data" / "raw" / "question_schema.json"
DEFAULT_DATA = REPO_ROOT / "data" / "raw" / "pilot" / "pilot_questions.json"

MOJIBAKE_PATTERN = re.compile(
    r"Ã[\x80-\xBF]|Â[\x80-\xBF]|â\x80[\x90-\x9F]"
)
BOM = b"\xef\xbb\xbf"


def check_encoding_hygiene(path: Path) -> list[str]:
    errors = []
    raw = path.read_bytes()

    if raw.startswith(BOM):
        errors.append(f"[encoding] {path.name}: el archivo empieza con BOM UTF-8 (EF BB BF).")

    text = raw.decode("utf-8")
    mojibake_lines = [
        lineno
        for lineno, line in enumerate(text.splitlines(), start=1)
        if MOJIBAKE_PATTERN.search(line)
    ]
    if mojibake_lines:
        preview = ", ".join(str(n) for n in mojibake_lines[:10])
        more = "..." if len(mojibake_lines) > 10 else ""
        errors.append(
            f"[encoding] {path.name}: mojibake detectado en {len(mojibake_lines)} línea(s) "
            f"(p.ej. líneas {preview}{more})."
        )

    return errors


def check_schema_conformance(schema: dict, data: list) -> list[str]:
    errors = []
    validator = Draft202012Validator(schema)

    if not isinstance(data, list):
        return [f"[schema] El dataset raíz debe ser un array, se encontró {type(data).__name__}."]

    for idx, item in enumerate(data):
        item_id = item.get("id", f"<sin id, índice {idx}>") if isinstance(item, dict) else f"<índice {idx}>"
        for err in sorted(validator.iter_errors(item), key=lambda e: list(e.path)):
            path = "/".join(str(p) for p in err.path) or "<raíz del ítem>"
            errors.append(f"[schema] {item_id} ({path}): {err.message}")

    return errors


def check_duplicate_ids(data: list) -> list[str]:
    errors = []
    ids = [item.get("id") for item in data if isinstance(item, dict) and "id" in item]
    counts = Counter(ids)
    duplicates = [id_ for id_, count in counts.items() if count > 1]
    if duplicates:
        errors.append(f"[ids] IDs duplicados: {', '.join(sorted(duplicates))}")
    return errors


def check_dimension_balance(data: list) -> list[str]:
    warnings = []
    dims = Counter(item.get("dimension") for item in data if isinstance(item, dict))
    if not dims:
        return warnings

    total = sum(dims.values())
    avg = total / len(dims)
    for dim, count in sorted(dims.items()):
        deviation = abs(count - avg) / avg if avg else 0
        if deviation > 0.25:
            warnings.append(
                f"[balance] Dimensión '{dim}': {count} ítems, se desvía "
                f">25% de la media ({avg:.1f}) entre las {len(dims)} dimensiones."
            )
    return warnings


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    args = parser.parse_args()

    schema = json.loads(args.schema.read_text(encoding="utf-8"))

    blocking_errors: list[str] = []
    blocking_errors += check_encoding_hygiene(args.data)

    # Decodifica con utf-8-sig (tolera un BOM inicial, ya reportado arriba si existe)
    # para poder seguir validando el resto del archivo en vez de abortar.
    try:
        data = json.loads(args.data.read_bytes().decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"Validando {_display_path(args.data)} contra {_display_path(args.schema)}\n")
        print(f"ERRORES (1):\n  - [parse] {args.data.name}: no se pudo interpretar como JSON UTF-8: {exc}\n")
        print("RESULTADO: FALLO")
        return 1

    blocking_errors += check_schema_conformance(schema, data)
    blocking_errors += check_duplicate_ids(data)

    warnings = check_dimension_balance(data)

    print(f"Validando {_display_path(args.data)} contra {_display_path(args.schema)}")
    print(f"Ítems evaluados: {len(data)}\n")

    if blocking_errors:
        print(f"ERRORES ({len(blocking_errors)}):")
        for e in blocking_errors:
            print(f"  - {e}")
        print()
    else:
        print("Sin errores bloqueantes.\n")

    if warnings:
        print(f"AVISOS ({len(warnings)}, no bloqueantes):")
        for w in warnings:
            print(f"  - {w}")
        print()

    if blocking_errors:
        print("RESULTADO: FALLO")
        return 1

    print("RESULTADO: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
