# Changelog — curación del dataset piloto

**Archivo generado:** `data/processed/pilot_questions_curated.json`
**Archivo fuente:** `data/raw/pilot/pilot_questions.json` (30 ítems, **no modificado**, se conserva como registro histórico)
**Schema de validación:** `data/raw/question_schema.json`
**Rúbrica aplicada:** `docs/question_quality_rubric.md` (QQR v1.0)
**Revisión humana:** `docs/pilot-evaluation/spanish_psychology_llm_pilot_evaluation_human_review.xlsx`
**Fecha:** 2026-09-05

**Resultado:** 30 ítems → **28 ítems**. Validación en verde (`scripts/validate_dataset.py`, exit code 0), 0 IDs duplicados.

> **Trazabilidad de decisiones:** la plantilla de revisión humana se ha incorporado al
> repositorio en `docs/pilot-evaluation/` (ver sección 0). Las decisiones se citan por **ID de
> ítem**, que es el identificador que usa la propia plantilla: su hoja `Evaluación piloto`
> indexa por `ID` y no define identificadores de decisión separados.

---

## 0. Incorporación de la plantilla de revisión humana

Se añade al repositorio el fichero
`docs/pilot-evaluation/spanish_psychology_llm_pilot_evaluation_human_review.xlsx`,
que contiene las decisiones finales del revisor para los 30 ítems del piloto. Hasta ahora
las decisiones estaban recogidas solo en el enunciado del encargo; con el fichero en el repo
la curación queda auditable contra su fuente.

Estructura: hoja `Evaluación piloto` (30 filas, una por ítem, con gates G1-G8, criterios
Q1-Q9, totales, `Decisión sugerida`, `Decisión final` y `Notas`), más las hojas
`Instrucciones` y `Resumen`. Recuento oficial de la hoja `Resumen`: **20 ACCEPT, 10 REVISE,
0 REJECT**, media de Q Total 15,6.

### Cómo se leen las discrepancias de `Difficulty` en esta plantilla

Es el punto crítico para interpretar el fichero, y afecta directamente a la sección 5.
La columna `Difficulty` de la plantilla **no es el veredicto del revisor**: reproduce el
metadato del ítem tal como se revisó, y en varias filas está desfasada respecto al JSON.
El veredicto real está en la puntuación **Q6** y en el texto de `Notas`, donde el revisor
indica de forma explícita **sobre qué valor puntuó Q6**.

Filas con discrepancia entre la columna `Difficulty` y el JSON:

| ID | Columna `Difficulty` | JSON raw | Q6 | Base declarada en `Notas` | Demanda real según el revisor |
|---|---|---|---|---|---|
| PSY-009 | `medium` | `hard` | 1 | «la demanda real es media» | **medium** |
| PSY-017 | `hard` | `medium` | 2 | «Q6 puntuado sobre 'medium'» | **medium** |
| PSY-019 | `medium` | `hard` | 2 | «Q6 puntuado sobre 'hard'» | **hard** |
| PSY-025 | `medium` | `easy` | 2 | «Q6 puntuado sobre 'easy'» | **easy** |
| PSY-028 | `medium` | `hard` | 2 | «Q6 puntuado sobre 'hard'» | **hard** |
| PSY-030 | `medium` | `hard` | 2 | no la declara | sin determinar |

PSY-021 no aparece aquí porque columna y JSON coinciden (`hard`), pero sus `Notas` sí
corrigen la demanda a `medium` (ver sección 3).

Consecuencia: en PSY-019, PSY-025 y PSY-028 el revisor puntuó sobre el valor que ya tiene el
JSON, de modo que **el JSON es correcto y la columna es la desfasada**; no requieren cambio.
PSY-030 es el único caso donde la base de Q6 no está declarada y la discrepancia queda sin
resolver; no se ha modificado y se documenta en la sección 7.

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

## 5. PSY-017 — resuelto: **no requería cambio**

Este era el único punto que quedó pendiente en la curación anterior, por no estar disponible
entonces la plantilla de revisión. Con el fichero ya en el repositorio, queda resuelto.

**Verificación realizada.** Fila de PSY-017 en la hoja `Evaluación piloto`:

- columna `Difficulty`: **`hard`**
- `Q6`: **2**
- `Decisión final`: `REVISE` (por Q3=1, Q7=1 y Q8=1, no por la dificultad)
- `Notas`, textualmente: *«Discrepancia de metadatos: JSON 'medium', plantilla 'hard';
  **Q6 puntuado sobre 'medium'**.»*

**Conclusión: se mantiene `medium`. No se aplica ningún cambio.**

El razonamiento importa, porque la lectura ingenua lleva a lo contrario. Tomar sin más el
`hard` de la columna `Difficulty` habría contradicho al propio revisor: éste detectó la
discrepancia, declaró que puntuaba **sobre `medium`**, y le asignó **Q6 = 2**, que en la
sección 6 de la rúbrica significa «la dificultad asignada refleja con exactitud la demanda
cognitiva del ítem». Es decir, el revisor validó `medium` de forma explícita; el `hard` de la
columna es el metadato desfasado de esa fila, exactamente el mismo fenómeno descrito en la
sección 0.

Esto invierte, solo para este ítem, el supuesto de partida del encargo («la plantilla usó el
valor correcto, el JSON tiene el desfasado»): en PSY-017 el desfasado es el de la plantilla.
El JSON ya tenía el valor correcto.

---

## 6. Corroboración de las decisiones previas con la plantilla

Al disponer ya del fichero, se han contrastado las decisiones aplicadas en las secciones 1-4,
que se habían tomado únicamente a partir del enunciado del encargo. Todas quedan respaldadas
por las `Notas` del revisor:

| Decisión | Respaldo textual en la plantilla |
|---|---|
| Eliminar **PSY-018** | «Q7=1: solapa con PSY-022, que aplica la misma lógica de evidencia insuficiente al caso concreto de n=20; conviene decidir cuál conserva ese rol.» |
| Eliminar **PSY-020** | «Q7=0: es sustancialmente redundante con PSY-009 […] y su escenario sueño-ansiedad es exactamente el que PSY-026 usa […]. Recomendación: rediseñar escenario y demanda, **o eliminarlo**.» |
| Reescribir **PSY-004** | «Q3=0: definir el efecto Stroop y el conflicto tinta/palabra es trivial […]. RUBRIC_ISSUE: la sección 6 de la rúbrica prohíbe ACCEPT con Q3=0, pero la fórmula de 'Decisión sugerida' no implementa esa regla». `Decisión final`: `REVISE`. |
| **PSY-009** `hard`→`medium` | «Q6=1: el JSON lo marca 'hard' y la plantilla 'medium' […]; **la demanda real es media**.» |
| **PSY-021** `hard`→`medium` | «Q6=1: etiquetado 'hard', pero la demanda es una distinción conceptual (confianza vs exactitud), **más propia de 'medium'**.» |
| **PSY-021** cambio de fuente | «Q8=1: Koriat (1997) trata juicios de aprendizaje durante el estudio, no memoria autobiográfica; […] existen fuentes más directas sobre la relación confianza-exactitud.» |

Ninguna decisión previa ha tenido que revertirse.

---

## 7. Cuestiones abiertas detectadas en la plantilla (fuera del alcance de esta curación)

No se ha actuado sobre ninguna de ellas; se documentan porque afectan al dataset y requieren
decisión humana.

1. **PSY-030 — discrepancia de `difficulty` sin resolver.** Columna `Difficulty` = `medium`,
   JSON = `hard`. Es la única fila cuyas `Notas` registran la discrepancia pero **no declaran
   sobre qué valor se puntuó Q6**, por lo que no puede resolverse como se resolvió PSY-017.
   El JSON se ha dejado en `hard`.

2. **Cuatro ítems `REVISE` siguen en el dataset curado sin remediar:** PSY-006, PSY-024,
   PSY-025 y PSY-026. La curación abordó los otros seis `REVISE` (PSY-004 reescrito, PSY-018 y
   PSY-020 eliminados, PSY-009, PSY-017 y PSY-021 revisados). Motivos registrados por el
   revisor: sobrerrepresentación de la teoría de la autodeterminación en PSY-006 (cuatro ítems
   del piloto usan ese marco, en tensión con la sección 11), solapamiento parcial en PSY-024 y
   PSY-026, y criterios de evaluación poco operativos en PSY-025 (Q4=1).

3. **`RUBRIC_ISSUE` recurrentes señalados por el revisor**, que afectan a la rúbrica y no a
   ítems concretos: la fórmula de `Decisión sugerida` no implementa el veto de la sección 6
   (devolvió ACCEPT para PSY-004 con Q3=0), el tratamiento de `Q8=NA` en el umbral, y la
   frontera no operativizada entre las dimensiones `reasoning`, `uncertainty` y
   `critical_analysis` (señalada en PSY-009, G3=REVISE).

---

## 8. Ítems no modificados

El resto del dataset se conserva **sin cambios**, incluidos los 20 ACCEPT originales y
específicamente PSY-006, PSY-010, PSY-017, PSY-024, PSY-025, PSY-026, PSY-029 y PSY-030.
Se verificó por comparación campo a campo que los únicos ítems con diferencias respecto al raw
son **PSY-004, PSY-009 y PSY-021**.
