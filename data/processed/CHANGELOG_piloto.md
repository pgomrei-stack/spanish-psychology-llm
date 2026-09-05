# Changelog — curación del dataset piloto

**Archivo generado:** `data/processed/pilot_questions_curated.json`
**Archivo fuente:** `data/raw/pilot/pilot_questions.json` (30 ítems, **no modificado**, se conserva como registro histórico)
**Schema de validación:** `data/raw/question_schema.json`
**Rúbrica aplicada:** `docs/question_quality_rubric.md` (QQR v1.0)
**Fecha:** 2026-09-05

**Resultado:** 30 ítems → **28 ítems**. Validación en verde (`scripts/validate_dataset.py`, exit code 0), 0 IDs duplicados.

> **Nota sobre la trazabilidad de decisiones:** la plantilla de revisión humana
> `spanish_psychology_llm_pilot_evaluation_human_review.xlsx` no está presente en el
> repositorio ni en el entorno de trabajo. Las decisiones se citan por **ID de ítem**, que es
> el identificador disponible; no ha sido posible referenciar los identificadores internos de
> decisión de esa plantilla. Esto afecta además a una corrección que ha quedado pendiente
> (ver sección 4).

---

## 1. Ítems eliminados por redundancia (Q7)

| ID | Dimensión | Motivo |
|---|---|---|
| **PSY-018** | `critical_analysis` | Solapa con **PSY-022** sin aportar una demanda cognitiva distinta. Ambos evalúan por qué un único resultado estadísticamente significativo no basta para dar por establecido un efecto; el revisor confirmó que no añade perspectiva adicional. |
| **PSY-020** | `uncertainty` | Redundante simultáneamente con **PSY-009** (correlación → causalidad en un caso aplicado) y con **PSY-026** (comunicar esa misma distinción). Constituye una tercera instancia del mismo patrón de inferencia, lo que la sección 9 de la rúbrica señala explícitamente como redundancia estructural a controlar. |

Efecto sobre el equilibrio de dimensiones: `knowledge` 6, `reasoning` 6, `critical_analysis` 5, `uncertainty` 5, `communication` 6. Ninguna dimensión se desvía más de un 25 % de la media, por lo que el validador no emite aviso de desequilibrio.

---

## 2. Ítem reescrito

### PSY-004 — atención y efecto Stroop

**Problema detectado (revisión humana):** el enunciado original ("¿Qué es el efecto Stroop y qué conflicto básico se produce en la tarea clásica?") era pura recuperación de definición y resultaba trivial para cualquier LLM competente actual → **Q3 (potencial discriminativo) = 0**. La sección 6 de la rúbrica prohíbe `ACCEPT` con un 0 en cualquier criterio esencial (Q1, Q2, Q3, Q4), de modo que el ítem no podía aceptarse tal cual.

**Rediseño aplicado.** Se mantienen `id`, `dimension` (`knowledge`) y `topic`. El ítem deja de pedir una definición y pasa a exigir dos cosas encadenadas:

1. explicar **a qué se atribuye la asimetría** del efecto (la palabra interfiere en la denominación del color, pero el color apenas interfiere en la lectura);
2. **predecir y justificar** qué le ocurre a la magnitud de la interferencia si se degrada visualmente la palabra manteniendo identificable el color.

Esto sigue la vía recomendada en las secciones 7.1 y 10 de la rúbrica para elevar la exigencia de un ítem de conocimiento: no mediante vocabulario más complejo, sino aumentando la demanda cognitiva (interpretación de un hallazgo establecido + aplicación del principio a una variante del paradigma).

**Campos actualizados:** `question`, `expected_answer`, `evaluation_criteria`, `critical_errors`, `notes`, y `difficulty` (`easy` → `medium`, justificado porque la demanda pasa a ser de aplicación y explicación con integración de un número limitado de conceptos, que es la definición de `medium` en la sección 6).

**Fuente:** se conserva MacLeod (1991), *Psychological Bulletin*, 109(2), 163-203 — la revisión integradora de referencia sobre el efecto Stroop, que respalda tanto la asimetría como sus moduladores.

**Estructura de `evaluation_criteria`:** se mantiene el esquema de niveles 3/2/1 usado por los otros 27 ítems, por coherencia interna del dataset.

#### Re-evaluación contra la QQR v1.0

**Gates obligatorios (sección 4):**

| Gate | Resultado | Comentario |
|---|---|---|
| G1 Error científico | Pasa | La asimetría y la dirección de la predicción son consistentes con la literatura establecida; el `expected_answer` admite formulaciones alternativas sin imponer una teoría mecanística. |
| G2 Ambigüedad sustantiva | Pasa | La tarea está explícitamente segmentada: explicar, predecir, justificar. |
| G3 Desalineación constructo-pregunta | Pasa | Lo que determina el acierto es conocer el principio de automaticidad relativa y sus moduladores; la predicción se deriva de ese conocimiento. |
| G4 Respuesta no evaluable | Pasa | Criterios observables y discretos. |
| G5 Inferencia injustificada incrustada | Pasa | La asimetría que se da por supuesta es un hallazgo establecido, no una conclusión no justificada. |
| G6 Tarea clínica inapropiada | N/A | |
| G7 Dependencia cultural | Pasa | |
| G8 Fallo técnico/schema | Pasa | Validado contra el schema. |

**Criterios de calidad (sección 5):**

| Criterio | Antes | Ahora |
|---|---|---|
| Q1 Validez de constructo | 2 | 2 |
| Q2 Precisión científica | 2 | 2 |
| Q3 Potencial discriminativo | **0** | **2** |
| Q4 Evaluabilidad | 2 | 2 |
| Q5 Claridad | 2 | 2 |
| Q6 Adecuación de la dificultad | 2 | 2 (con `medium`) |
| Q7 No redundancia | 2 | 2 |
| Q8 Calidad de la fuente | 2 | 2 |
| Q9 Adecuación lingüística | 2 | 2 |
| **Total** | — | **18 → ACCEPT** |

**Objetivo cumplido: Q3 = 2 ≥ 1**, y ningún criterio esencial en 0.

*Matiz honesto sobre Q3:* un revisor conservador podría puntuarlo **1** en lugar de 2, argumentando que un modelo frontera resolverá la parte de la asimetría por recuperación directa (es contenido de manual) y que solo la justificación de la predicción discrimina de verdad. Incluso con esa lectura más estricta el ítem suma 17 → `ACCEPT` y cumple el requisito Q3 ≥ 1. La diferencia entre 1 y 2 no altera la decisión.

---

## 3. Metadatos corregidos

| ID | Campo | Antes | Ahora | Motivo |
|---|---|---|---|---|
| **PSY-009** | `difficulty` | `hard` | `medium` | La tarea consiste en aplicar la distinción asociación/causalidad a un caso y enumerar explicaciones alternativas: es aplicación e interpretación, no evaluación de evidencia conflictiva ni integración de múltiples marcos. Encaja en `medium` según la sección 6. El JSON arrastraba el valor desfasado; la plantilla ya usaba el correcto. |
| **PSY-021** | `difficulty` | `hard` | `medium` | Distinguir confianza subjetiva de exactitud objetiva y explicar por qué un recuerdo vívido puede contener errores es una demanda de explicación e interpretación conceptual, no de razonamiento bajo evidencia conflictiva. |
| **PSY-021** | `source` | Koriat (1997) | Talarico & Rubin (2003) | Ver sección 4. |
| **PSY-021** | `notes` | — | actualizado | Ajustado para reflejar qué respalda exactamente la nueva fuente. |

---

## 4. Sustitución de fuente en PSY-021

**Problema (Q8):** la fuente citada era Koriat, A. (1997), *Monitoring one's own knowledge during study: A cue-utilization approach to judgments of learning*, JEP:General, 126(4), 349-370. Ese trabajo trata sobre **juicios de aprendizaje (JOLs) durante el estudio de material de laboratorio**, no sobre memoria autobiográfica. Sostiene el principio genérico de que los juicios metacognitivos no equivalen a exactitud, pero **no respalda directamente** la afirmación concreta del ítem sobre confianza y exactitud en el recuerdo autobiográfico. Según la sección 5, una fuente que no sostiene la afirmación para la que se cita puntúa 0 en Q8.

**Fuente nueva:**

> Talarico, J. M., & Rubin, D. C. (2003). Confidence, not consistency, characterizes flashbulb memories. *Psychological Science*, 14, 455-461. DOI: `10.1111/1467-9280.02453`

**Por qué encaja:** es un estudio longitudinal de recuerdos autobiográficos (memorias "flashbulb" del 11-S frente a sucesos cotidianos) que muestra precisamente la disociación que el ítem evalúa: la **consistencia** del recuerdo decae con el tiempo igual en ambos tipos, mientras que la **vividez y la creencia en la propia exactitud** se mantienen elevadas solo en los flashbulb. Es decir, alta confianza sin la exactitud correspondiente — el núcleo conceptual de PSY-021.

**Verificación del DOI:** confirmado por dos vías independientes. El DOI resuelve en el sitio del editor (SAGE, que publica *Psychological Science*) en `journals.sagepub.com/doi/10.1111/1467-9280.02453`, y los datos bibliográficos coinciden en múltiples registros secundarios. No se pudo consultar Crossref ni OpenAlex directamente porque el proxy de red del entorno bloquea esos dominios; por esa misma razón **no se ha incluido el número de fascículo** en la cita, al no haber podido confirmarlo en una fuente autorizada. Se cita volumen y páginas, que sí están confirmados.

---

## 5. Corrección pendiente (no aplicada)

**PSY-017 — `difficulty`.** La instrucción era verificar en
`spanish_psychology_llm_pilot_evaluation_human_review.xlsx` qué demanda real declaró el
revisor y aplicarla. **Ese archivo no existe en el repositorio ni en el entorno**, por lo que
no hay forma de comprobar el valor declarado sin inventarlo.

El ítem figura actualmente como `medium` y se ha dejado **sin tocar**. Nótese que `medium` es
plausible por sí mismo (detectar el absolutismo de "siempre" y matizar la relación entre
recompensas externas y motivación intrínseca es interpretación y explicación), pero eso es una
valoración propia, **no** la verificación pedida. Queda pendiente de confirmar cuando la
plantilla esté disponible.

---

## 6. Ítems no modificados

El resto del dataset se conserva **sin cambios**, incluidos los 20 ACCEPT originales y
específicamente PSY-006, PSY-010, PSY-017 (contenido), PSY-024, PSY-025, PSY-026 y PSY-029.
Se verificó por comparación campo a campo que los únicos ítems con diferencias respecto al raw
son PSY-004, PSY-009 y PSY-021.
