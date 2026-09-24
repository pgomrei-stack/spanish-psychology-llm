# Ítems nuevos (PSY-031 a PSY-172)

**Estado:** pendientes de revisión con la QQR v1.0. No forman parte todavía del benchmark.

- **Fuente:** `docs/new-items-evaluation/spanish_psychology_llm_new_items_evaluation.xlsx`
  (plantilla de evaluación con el contenido de los ítems; las columnas de revisión
  G1-G8, Q1-Q9 y las decisiones están vacías).
- **Archivo generado:** `new_items_questions.json` (142 ítems), producido con:

  ```bash
  python3 scripts/import_items_from_xlsx.py \
      --xlsx docs/new-items-evaluation/spanish_psychology_llm_new_items_evaluation.xlsx \
      --out data/raw/new_items/new_items_questions.json
  ```

- **Validación:** `python3 scripts/validate_dataset.py --data data/raw/new_items/new_items_questions.json`
  → sin errores bloqueantes; un aviso de equilibrio (`knowledge`: 14 ítems frente a una media de 28,4).

La columna `Generator_Notes` de la plantilla se guarda en el campo `notes`. El resto de campos se
corresponden uno a uno con el schema.

Como con el piloto, este archivo raw no se modifica tras la revisión: las decisiones del revisor se
aplicarán en un dataset curado aparte en `data/processed/`.
