# Changelog — generación de ítems nuevos (`new_items_draft.json`)

**Archivo generado:** `data/processed/new_items_draft.json`
**Schema de validación:** `data/raw/question_schema.json`
**Rúbrica aplicada:** `docs/question_quality_rubric.md` (QQR v1.0)
**Referencia de calidad y lista de exclusión:** `data/processed/pilot_questions_curated.json` (28 ítems validados)
**Fecha:** 2026-09-05

---

## Pasada 1 — dimensión `knowledge`, 14 ítems (PSY-031 a PSY-044)

Primera pasada sobre este archivo: no existía previamente, por lo que el acumulado tras esta
pasada es de **14 ítems**. No se ha modificado ningún archivo del piloto.

**Validación:** `python3 scripts/validate_dataset.py --data data/processed/new_items_draft.json`
→ `RESULTADO: OK`, exit code 0, 0 IDs duplicados, sin colisión con los IDs del piloto
(máximo previo `PSY-030`).

Validado también el conjunto combinado piloto + draft (42 ítems): sin errores bloqueantes. El
validador emite avisos de equilibrio de dimensiones, consecuencia esperada de escalar una única
dimensión en una sola pasada (`knowledge` pasa de 6 a 20 ítems). No son bloqueantes y se
reabsorberán al escalar el resto de dimensiones.

### Distribución

| Dificultad | N | IDs |
|---|---|---|
| `easy` | 2 | PSY-031, PSY-032 |
| `medium` | 5 | PSY-033 a PSY-037 |
| `hard` | 7 | PSY-038 a PSY-044 |

Los dos ítems `easy` miden errores conceptuales extendidos (equiparar esquizofrenia con
identidades múltiples; tipologías de dominancia hemisférica), no recuerdo trivial, conforme al
encargo y a la sección 7.1 de la rúbrica.

### Cobertura temática y control de redundancia (Q7)

Ningún marco teórico del piloto se reutiliza salvo un caso, declarado explícitamente en el
propio ítem:

- **PSY-040 (extinción y contexto)** reincide en el campo del condicionamiento, ya presente en
  PSY-007 (refuerzo operante, `reasoning`) y PSY-025 (condicionamiento clásico,
  `communication`). Se declara en su campo `notes`: la capacidad evaluada —extinción como
  aprendizaje nuevo y dependiente del contexto, más predicción justificada de un fenómeno de
  recuperación— no está cubierta por ninguno de los dos, que evalúan respectivamente aplicación
  funcional de la distinción refuerzo-castigo y traducción a lenguaje llano.

En particular **no se reutiliza la teoría de la autodeterminación**, señalada por el revisor del
piloto como sobrerrepresentada (cuatro ítems) en tensión con la sección 11 de la rúbrica.

Subcampos incorporados: psicopatología, neurociencia, emoción (2), lenguaje y cognición,
psicología social (2), inteligencia, psicología de la salud, psicometría (2), genética de la
conducta, aprendizaje asociativo, desarrollo cognitivo. Ninguno domina el lote.

Ningún escenario, caso o dato numérico del piloto reaparece: los ítems son conceptuales o
describen paradigmas experimentales que el piloto no utiliza.

---

## Autoevaluación (QQR v1.0)

### Gates obligatorios

Los 14 ítems pasan los ocho gates. Puntos que requerían comprobación específica:

| Gate | Ítems implicados | Resultado |
|---|---|---|
| G3 (desalineación constructo-pregunta) | PSY-043, PSY-044 | Pasan. Ambos podrían confundirse con `critical_analysis`, pero piden **informar** del estatus de la evidencia o de la relación entre dos teorías, no evaluar una afirmación ajena. La sección 7.1 incluye expresamente «interpretación de hallazgos establecidos» y «relaciones entre constructos» dentro de `knowledge`. |
| G5 (inferencia injustificada incrustada) | PSY-041, PSY-044 | Pasan. Los hallazgos que el enunciado da por supuestos (discrepancia entre paradigmas; menor cambio de actitud con incentivo grande) son resultados establecidos, no conclusiones no justificadas. PSY-041 está construido además para no premiar la adhesión a ninguna de las dos tradiciones. |
| G6 (tarea clínica inapropiada) | PSY-031, PSY-040, PSY-042 | Pasan. Ninguno pide diagnosticar, evaluar ni tratar a una persona: se pregunta por constructos nosológicos, por un principio general del aprendizaje y por propiedades métricas de instrumentos. |
| G7 (dependencia cultural) | Todos | Pasan. Ningún ítem depende de conocimiento cultural específicamente español. |

### Criterios de calidad

Umbral de aceptación: 16/18 (88,9 %). Ningún ítem puntúa 0 en Q1, Q2, Q3 o Q4.

| ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Total | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSY-031 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-032 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-033 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-034 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-035 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-036 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-037 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-038 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-039 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-040 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-041 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-042 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-043 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-044 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |

Media: **17,79 / 18**. Mínimo: 17. Ningún ítem por debajo del umbral.

### Matices honestos sobre las puntuaciones

Se declaran las lecturas alternativas más estrictas que un revisor conservador podría aplicar,
con su efecto sobre la decisión.

1. **Q3 = 1 en PSY-031, PSY-032 y PSY-033.** Es una puntuación deliberadamente conservadora: los
   tres son ítems de distinción conceptual y una parte sustancial de la respuesta es recuperable
   por un modelo competente. Se han diseñado con un elemento que sí discrimina —el sentido de
   «escisión», la sobrecorrección que niega toda lateralización, y la separación entre malestar
   personal y preocupación empática con sus consecuencias motivacionales distintas—, pero no se
   les atribuye Q3 = 2. Con 17/18 la decisión es ACCEPT en los tres casos, y el mínimo Q3 ≥ 1 de
   la sección 6 se cumple.
2. **Q7 en PSY-040.** Un revisor podría puntuar 1 por proximidad temática al campo del
   condicionamiento, ya presente en el piloto. Incluso así el ítem suma 17 → ACCEPT. La
   reincidencia está declarada en su campo `notes`, como exige el encargo.
3. **Q3 en PSY-037.** En su primera redacción el ítem se autoevaluó en Q3 = 1: la respuesta
   «depende de la controlabilidad» es alcanzable por recuperación. Se reescribió antes de
   incluirlo, añadiendo al enunciado la exigencia del criterio funcional de clasificación —que
   una misma conducta cambia de categoría según su función en el contexto—, que es el elemento
   que un modelo mediocre omite. La puntuación de la versión incluida es Q3 = 2.
4. **Q8 y verificación de fuentes.** Se puntúa Q8 = 2 cuando la fuente citada sostiene
   directamente la afirmación del ítem, criterio de la sección 5. En cinco ítems (PSY-034,
   PSY-041, PSY-042, PSY-043, PSY-044) se han **omitido deliberadamente los DOI** por no haber
   podido confirmarlos en una fuente autorizada desde este entorno de ejecución; se citan los
   datos bibliográficos que sí son verificables y la omisión queda anotada en el campo `notes`
   del ítem correspondiente. Es el mismo criterio de prudencia aplicado en la curación del
   piloto con PSY-021 (sección 4 de `CHANGELOG_piloto.md`). **El paso de verificación de
   fuentes del flujo de trabajo (sección 12 de la rúbrica) debe cerrar este punto antes de la
   inclusión en el dataset final.**
5. **Separación entre generación y validación.** La sección 12 de la rúbrica establece que el
   modelo generador no es la autoridad final sobre la validez de sus propios ítems. Esta
   autoevaluación es el filtro previo exigido por el encargo, no un sustituto de la revisión
   humana.

---

## Ítems descartados durante la generación

No se incluyen borradores a la espera de revisión: los candidatos que no habrían alcanzado
ACCEPT o que introducían redundancia se descartaron antes de escribirse por completo.

| Candidato | Motivo del descarte |
|---|---|
| Refuerzo negativo frente a castigo (`easy`) | Redundancia directa con PSY-007, cuyo enunciado ya pide «diferencia este proceso de un castigo». Q7 = 0. |
| Regresión a la media en la evaluación de tratamientos | Solapa con PSY-024 (`uncertainty`), que ya aborda la atribución de una mejoría a la intervención en presencia de causas concurrentes. |
| Efecto de la prueba o práctica de recuperación | Proximidad cognitiva con PSY-003 y PSY-008 (espaciamiento), y el piloto ya está muy cargado de memoria: seis ítems sobre el dominio, en tensión con la sección 11. |
| Inferencia inversa en neuroimagen | Solapa parcialmente con PSY-012 (qué puede inferirse de datos neuropsicológicos). |

Dos candidatos válidos se aplazaron por **redundancia estructural** (sección 9, patrón de
pregunta repetido), no por calidad: el lote ya contiene dos ítems con la estructura «qué afirma
la hipótesis / qué ha establecido la evidencia de replicación» (PSY-035 y PSY-043), y añadir más
habría convertido un patrón en un molde. Quedan disponibles para pasadas futuras:

- **Estilos de aprendizaje y la hipótesis del emparejamiento**, con el diseño de interacción
  cruzada que se requiere para ponerla a prueba.
- **Mentalidad de crecimiento**: qué sostiene la teoría y qué magnitud de efecto han establecido
  los metaanálisis y los experimentos preregistrados a gran escala.

Ambos deberían generarse en una dimensión o con una estructura distinta si se incorporan.
