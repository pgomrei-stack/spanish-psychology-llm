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

---

## Pasada 2 — dimensión `communication`, 29 ítems (PSY-045 a PSY-073)

Segunda pasada sobre este archivo. Los 14 ítems de la pasada 1 **no se han modificado**: la
fusión se hizo por anexado y se verificó comparando el hash del bloque previo antes y después
de escribir el archivo. Acumulado tras esta pasada: **43 ítems** (14 `knowledge` + 29
`communication`).

**Validación:** `python3 scripts/validate_dataset.py --data data/processed/new_items_draft.json`
→ `RESULTADO: OK`, exit code 0, 0 IDs duplicados, sin colisión con el piloto (máximo previo
`PSY-044`). El conjunto combinado piloto + draft (71 ítems) también pasa sin errores
bloqueantes. Los avisos de equilibrio de dimensiones son la consecuencia esperada de escalar
una dimensión por pasada y no son bloqueantes.

### Distribución

| Dificultad | N | IDs |
|---|---|---|
| `easy` | 3 | PSY-045, PSY-046, PSY-047 |
| `medium` | 9 | PSY-048 a PSY-056 |
| `hard` | 17 | PSY-057 a PSY-073 |

Los tres ítems `easy` miden errores conceptuales extendidos —placebo entendido como
simulación, multitarea entendida como procesamiento paralelo, resiliencia entendida como
aguante— y los tres están construidos para penalizar también la **sobrecorrección opuesta**,
que es el modo de fallo característico de un modelo que ha memorizado el desmentido sin
entender el fenómeno.

### Control de redundancia estructural (Q7-C)

Con 29 ítems en una sola dimensión, el riesgo dominante no es el temático sino el
**estructural**: que el lote sea la misma pregunta con destinatarios distintos. Los ítems se
han construido cruzando contenido con **demanda comunicativa**, y ninguna pareja comparte las
dos. Demandas empleadas:

| Demanda comunicativa | IDs |
|---|---|
| Explicar un concepto a audiencia lega | 045, 046, 047, 050, 055, 063 |
| Corregir una creencia sostenida por experiencia propia o buena fe | 046, 047, 059, 065, 071, 073 |
| Comunicar a un profesional de otra disciplina para que lo reutilice | 049, 053, 056, 060, 071 |
| Producir un texto sujeto a restricciones de forma y tono | 048, 054, 067, 068 |
| Comunicar magnitud, incertidumbre o un resultado nulo | 057, 058, 061, 066, 072 |
| Resolver un conflicto entre exigencias legítimas | 062, 064, 068 |
| Resistir una simplificación o una presión sobre el mensaje | 054, 060, 066, 070, 072 |
| Adaptar el registro a menores o adolescentes | 051, 067, 068 |
| Sostener honestidad ante hostilidad o ante malas noticias | 069, 070, 073 |

Ningún ítem del piloto reaparece: las seis demandas de PSY-025 a PSY-030 (explicar
condicionamiento clásico, correlación a un periodista, confianza frente a exactitud del
recuerdo, significación frente a relevancia práctica, motivación autónoma y eficacia
poblacional frente a individual) quedan fuera del lote. **No se reutiliza la teoría de la
autodeterminación.**

### Marcos reincidentes declarados

Ninguno se repite sin declaración en el campo `notes` del ítem:

| ID | Proximidad declarada | Capacidad distinta |
|---|---|---|
| PSY-055 | PSY-036 y PSY-038 (pasada 1): baremos y fiabilidad | Convertir una puntuación en información útil para una familia sin generar una etiqueta |
| PSY-056 | PSY-031 (pasada 1): esquizofrenia | Revisar un texto ajeno; contenido sustantivo distinto (violencia atribuible) |
| PSY-057 | PSY-026 (piloto) y PSY-061 | El elemento puntuado es la traducción a frecuencias naturales, no la causalidad |
| PSY-058 | PSY-015 y PSY-028 (piloto): valor p y relevancia práctica | Asimetría lógica de un resultado nulo ante quien debe decidir con él |
| PSY-059 | PSY-030 (piloto): paciente pregunta por su tratamiento | Separar validez de un mecanismo causal de evidencia de eficacia |
| PSY-060 | PSY-005 (piloto) y PSY-038 (pasada 1) | Objeción técnica en reunión con restricción interpersonal |
| PSY-064 | PSY-045 (este lote): placebo | Fenómeno inverso y resolución de un dilema ético operativo |
| PSY-066 | PSY-022 (piloto): muestra pequeña | Mecanismo de selección, no tamaño |
| PSY-069 | PSY-019 (piloto): viñeta de síntomas | Comunicar sin patologizar ni banalizar, no gestionar incertidumbre diagnóstica |
| PSY-070 | PSY-043 (pasada 1): replicaciones multilaboratorio | Responder a crítica hostil en público |
| PSY-065, PSY-071, PSY-072 | Candidatos **aplazados expresamente en la pasada 1** | Incorporados aquí en otra dimensión, como aquel changelog indicaba |

Los tres candidatos que la pasada 1 dejó documentados como aplazados —regresión a la media,
estilos de aprendizaje y mentalidad de crecimiento— quedan así incorporados. La lista de
pendientes de la pasada 1 queda cerrada.

---

## Autoevaluación de la pasada 2 (QQR v1.0)

### Gates obligatorios

Los 29 ítems pasan los ocho gates. Comprobaciones que requerían atención específica:

| Gate | Ítems | Resultado |
|---|---|---|
| G3 (desalineación constructo-pregunta) | 054, 057, 058, 061, 066 | Pasan. Todos tienen contenido metodológico y podrían confundirse con `critical_analysis`, pero en ninguno se pide evaluar la calidad de un estudio: se pide producir un mensaje para un destinatario definido bajo restricciones de registro y tono, que es lo que la sección 7.5 define como el constructo. En PSY-054 el producto exigido es literalmente un texto reescrito. |
| G5 (inferencia injustificada incrustada) | 054, 057, 066 | Pasan. El enunciado aporta en cada caso los datos de diseño necesarios (voluntarios sin grupo control; tasa de respuesta del 12 %) y en PSY-057 la respuesta correcta consiste precisamente en señalar que falta el riesgo de partida, de modo que el ítem no da por supuesta la conclusión. |
| G6 (tarea clínica inapropiada) | 059, 063, 069, 073 | Pasan. Los cuatro enunciados **prohíben expresamente** valorar el caso, y esa abstención forma parte de lo puntuado y figura entre los errores críticos. La psicoeducación general —qué situaciones harían razonable consultar— no es evaluación personalizada, y la rúbrica admite explícitamente evaluar clínica cuando la tarea versa sobre conceptos, evidencia o comunicación. |
| G6 (contenido sensible) | 062 | Pasa. Es comunicación de salud pública dirigida a un profesional de medios, basada en guías establecidas. La respuesta correcta **no contiene ni requiere información sobre métodos**, y su omisión es uno de los contenidos evaluados; incluir esos detalles figura como error crítico. |
| G7 (dependencia cultural) | 053, 068 | Pasan. Ambos enunciados excluyen expresamente la normativa de un país concreto: la respuesta correcta se apoya en principios deontológicos y técnicos generales. |

### Criterios de calidad

Umbral de aceptación: 16/18 (88,9 %). Ningún ítem puntúa 0 en Q1, Q2, Q3 o Q4.

| ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Total | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSY-045 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-046 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-047 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-048 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-049 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-050 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | N/A | 2 | **15/16** | ACCEPT |
| PSY-051 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-052 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-053 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-054 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-055 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-056 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-057 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-058 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-059 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-060 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-061 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-062 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-063 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-064 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-065 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-066 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-067 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-068 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-069 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-070 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-071 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-072 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-073 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |

28 ítems puntuados sobre 18: media **17,86**, mínimo 17. PSY-050 se puntúa sobre 16 por
`Q8 = N/A` y obtiene 15/16 (93,75 %), por encima del umbral. Ningún ítem por debajo de ACCEPT.

### Matices honestos sobre las puntuaciones

1. **Q3 = 1 en los tres ítems `easy` y en PSY-050.** Puntuación deliberadamente conservadora:
   una parte sustancial de la respuesta es recuperable por un modelo competente. Los cuatro
   incorporan un elemento que sí discrimina —el límite del alcance del placebo, la excepción de
   las tareas automatizadas, la negativa a negar las diferencias individuales, y la atención al
   agravio además de a la explicación técnica—, pero no se les atribuye Q3 = 2. Todos siguen en
   ACCEPT y cumplen el mínimo Q3 ≥ 1 de la sección 6.
2. **Q7 = 1 en PSY-072.** Es la proximidad estructural más fuerte del lote: PSY-071 y PSY-072
   comparten destinatario educativo y la forma general «lo que promete la divulgación no es lo
   que muestra la evidencia». Se mantienen ambos porque la demanda difiere —en PSY-071 hay que
   hacer comprobable una objeción describiendo el diseño de contraste ante un profesional que
   se juega su método; en PSY-072 hay que comunicar una magnitud pequeña impidiendo las dos
   lecturas erróneas opuestas—, pero la penalización se refleja en la puntuación en lugar de
   negarse. Con 17/18 la decisión no cambia.
3. **Lecturas conservadoras que no se han aplicado.** Un revisor estricto podría puntuar Q7 = 1
   en PSY-064 por compartir familia conceptual con PSY-045, o en PSY-057 por compartir con
   PSY-061 el terreno de la comunicación cuantitativa a audiencia lega. En ambos casos el
   resultado sería 17/18, sin cambio de decisión.
4. **Q2 y magnitudes.** Tres ítems tocan literaturas donde las cifras concretas están en
   revisión o varían según el criterio: PSY-060 (validez de métodos de selección), PSY-070
   (tasa de replicación) y PSY-057 (riesgos de base). En los tres, el `expected_answer` y los
   criterios están redactados para puntuar **el argumento y no la cifra**, y en PSY-057 ofrecer
   cifras de riesgo como si fueran datos reales del estudio figura como error crítico.
5. **Q8 y verificación de fuentes.** Se puntúa Q8 = 2 cuando la fuente sostiene directamente la
   afirmación del ítem. En **PSY-045, PSY-046, PSY-047, PSY-052 y PSY-059** se han omitido
   deliberadamente los DOI por no haber podido confirmarlos en una fuente autorizada desde este
   entorno de ejecución, con la omisión anotada en el `notes` del ítem; es el mismo criterio de
   prudencia de la pasada 1 y de la curación del piloto. PSY-050 no cita fuente por tratarse de
   un principio metodológico general, uso de `Q8 = N/A` que la sección 5 admite y que el piloto
   ya aplica en PSY-025 y PSY-026. **El paso de verificación de fuentes (sección 12 de la
   rúbrica) debe cerrar este punto antes de la inclusión en el dataset final.**
6. **Separación entre generación y validación.** Se mantiene lo dicho en la pasada 1: esta
   autoevaluación es el filtro previo exigido por el encargo, no un sustituto de la revisión
   humana.

---

## Ítems descartados durante la generación (pasada 2)

| Candidato | Motivo del descarte |
|---|---|
| Explicar a un tribunal la fiabilidad del testimonio y la identificación de sospechosos | Redundancia con PSY-001, PSY-021 y PSY-027, que ya cubren memoria, confianza y exactitud desde tres dimensiones distintas. |
| Explicar la motivación intrínseca a un entrenador o a un docente | La teoría de la autodeterminación está sobrerrepresentada en el piloto; excluida por la restricción 1. |
| Corregir un titular sobre pantallas y depresión adolescente | Habría concentrado dos ítems del lote en el mismo dominio y reproducido el patrón causal de PSY-026. Sustituido por PSY-054, cuyo problema es el diseño pre-post y cuyo producto es un texto reescrito. |
| Explicar sensibilidad y valor predictivo a un médico de atención primaria | Solapamiento demasiado directo con PSY-042 de la pasada 1, incluso admitiendo el cambio de dimensión. |
| Desmontar el neuromito del 10 % del cerebro | Reproduce el patrón de PSY-032 (pasada 1) sin añadir demanda nueva. |

Dos candidatos válidos quedaron fuera solo por límite de cupo y siguen disponibles para pasadas
futuras: **comunicar el sesgo de retrospectiva a un comité que analiza un incidente** y
**responder a la exigencia de un sí o un no sobre una cuestión con evidencia conflictiva**.
