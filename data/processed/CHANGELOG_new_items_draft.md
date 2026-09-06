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

---

## Pasada 3 — dimensión `reasoning`, 34 ítems (PSY-074 a PSY-107)

Tercera pasada sobre este archivo. Los 43 ítems de las pasadas 1 y 2 **no se han modificado**: la
fusión se hizo por anexado y se verificó comparando el hash del bloque previo antes y después de
escribir el archivo (`bloque previo intacto: True`). Acumulado tras esta pasada: **77 ítems**
(14 `knowledge` + 29 `communication` + 34 `reasoning`).

**Validación:** `python3 scripts/validate_dataset.py --data data/processed/new_items_draft.json`
→ `RESULTADO: OK`, exit code 0, 77 ítems, 0 IDs duplicados, sin colisión con el piloto (máximo
previo `PSY-073`). El conjunto combinado piloto + draft (105 ítems) también pasa sin errores
bloqueantes. Los avisos de equilibrio de dimensiones son la consecuencia esperada de escalar una
dimensión por pasada y no son bloqueantes.

### Distribución

| Dificultad | N | IDs |
|---|---|---|
| `easy` | 3 | PSY-074, PSY-075, PSY-076 |
| `medium` | 11 | PSY-077 a PSY-087 |
| `hard` | 20 | PSY-088 a PSY-107 |

Los tres ítems `easy` miden errores conceptuales extendidos —leer el signo de una correlación
como indicador de intensidad, tratar una medida puntual como si describiera un rasgo estable, y
aceptar una explicación circular— y no recuerdo trivial. Dos de ellos penalizan además la
sobrecorrección opuesta (PSY-076 sanciona expresamente concluir que ningún rasgo puede explicar
conducta).

### Estructura de los ítems (sección 7.2 de la rúbrica)

Todos siguen el patrón `información → aplicación de un concepto psicológico → conclusión
justificada`. Para reforzar el constructo frente a `knowledge`, 27 de los 34 exigen además una
**predicción, una derivación o un producto** que no puede recuperarse de memoria: predecir el
efecto de una manipulación (078, 081, 086, 089, 090, 099, 103, 106), derivar cuál de dos
mecanismos opera y qué intervención le corresponde (077, 080, 100, 101, 107), seleccionar la
evidencia que hay que examinar (088), decidir entre dos cálculos correctos (091), rediseñar una
actividad condición por condición (102) o construir un contraejemplo (104).

### Frontera con `critical_analysis` (G3)

Ocho ítems parten de una conclusión ajena (079, 081, 087, 091, 093, 095, 096, 104) y podrían
confundirse con `critical_analysis`. Pasan el gate: en ninguno se pide evaluar la calidad global
de un estudio ni juzgar una afirmación en abstracto, sino aplicar un principio a un caso concreto
para derivar qué se sigue de él, qué predicción hace y qué ocurriría bajo otras condiciones. Es el
patrón que el piloto ya emplea en `reasoning` con PSY-009 y PSY-011, que también arrancan de la
conclusión de un investigador. Los criterios reservan la puntuación máxima a la derivación, no al
rechazo de la conclusión.

### Cobertura temática

Ningún subcampo domina el lote: metodología y psicometría (079, 080, 081, 091, 092, 093, 094,
095), psicología social (087, 099, 100, 101, 102, 103), aprendizaje y conducta (086, 089, 090),
cognición y juicio (077, 078, 088, 097, 105, 107), desarrollo (096, 098), evaluación y diferencias
individuales (074, 075, 076, 106), emoción y salud (082, 083), trabajo y educación (084, 085) y
razonamiento causal sobre mecanismos (104).

### Marcos reincidentes declarados (Q7)

Ninguno se repite sin declaración expresa en el campo `notes` del ítem:

| ID | Proximidad declarada | Capacidad distinta |
|---|---|---|
| PSY-077 | PSY-042 (pasada 1): frecuencias de base | Juicio intuitivo de probabilidad por semejanza, no dependencia del valor predictivo respecto de la prevalencia |
| PSY-078, PSY-105 | Densidad del dominio de memoria en el piloto (001, 002, 003, 008, 021, 027) | Dirección temporal de la interferencia; medida del rendimiento en reconocimiento. Ninguno de los previos trata ninguna de las dos |
| PSY-081 | PSY-058 (pasada 2): resultados nulos | Explicación del lado de la medida y predicción con otro instrumento, no comunicación de la asimetría lógica |
| PSY-082 | PSY-037 (pasada 1): afrontamiento | Modelo procesual distinto y predicciones diferenciales sobre tres indicadores |
| PSY-085 | PSY-007 (piloto) y PSY-060 (pasada 2) | Efecto sistémico de un criterio de medida sobre la distribución del esfuerzo |
| PSY-086, PSY-089, PSY-090 | Campo del condicionamiento: PSY-007 (piloto), PSY-040 (pasada 1) | Distinción adquisición-ejecución; resistencia a la extinción y contingencias recíprocas; acoplamiento de dos procesos en el mantenimiento de la evitación |
| PSY-087 | PSY-045 (pasada 2): placebo | Derivar y localizar el mecanismo, no comunicarlo |
| PSY-092 | PSY-066 (pasada 2): sesgo de no respuesta | Asociación creada por condicionar sobre un efecto común, no pérdida de representatividad por tasa de respuesta |
| PSY-093 | PSY-060 (pasada 2): selección de personal | Efecto de un procedimiento de selección sobre la magnitud de una correlación |
| PSY-094 | PSY-038 (pasada 1) y PSY-055 (pasada 2) | Efecto de la fiabilidad sobre la magnitud de una asociación y sobre la comparación entre estudios |
| PSY-095 | PSY-015 y PSY-022 (piloto) | Tasa de error de una familia de contrastes y contraste de la interacción |
| PSY-098 | PSY-011 (piloto): apego y causalidad | Periodo sensible, relación dosis-respuesta y validez de una comparación no aleatorizada |
| PSY-101 | PSY-044 (pasada 1): conformidad forzada | Derivación del tipo de influencia a partir de la comparación entre condiciones |
| PSY-103 | PSY-043 (pasada 1): feedback facial | Derivar el mecanismo y diseñar controles, incluida una predicción arriesgada |
| PSY-104 | PSY-059 (pasada 2): explicaciones causales de la depresión | Formulado en términos genéricos; se exige construir un contraejemplo y especificar la evidencia pertinente |
| PSY-106 | PSY-005 y PSY-016 (piloto): personalidad | Problema de medida —fiabilidad y agregación—, no sustantivo |

**No se reutiliza la teoría de la autodeterminación** (sobrerrepresentada en el piloto), ni el
espaciamiento, ni el efecto Stroop, ni la doble disociación, ni la lógica «correlación observada →
¿puede concluirse causalidad?» de PSY-009 y PSY-011: PSY-074 excluye deliberadamente toda pregunta
sobre causalidad, y los ítems causales de este lote (091, 092, 104) plantean problemas de
estructura distinta —inversión por agregación, asociación creada por la selección, e inferencia de
la causa a partir de la respuesta al tratamiento—. Ningún escenario, caso ni dato numérico del
piloto o de las pasadas anteriores reaparece.

### Datos numéricos verificables

Cinco ítems incorporan cifras construidas para que la respuesta correcta sea comprobable de forma
objetiva, lo que eleva Q4:

- **PSY-091**: la inversión es exacta (A: 90/100 y 60/300, B: 250/300 y 10/100; A supera a B en
  ambos centros y B supera a A en el agregado, 65 % frente a 37,5 %).
- **PSY-094**: con fiabilidades de 0,85 la relación desatenuada ronda 0,65 y predice para el
  segundo estudio una correlación observada de ≈0,42, próxima al 0,40 informado.
- **PSY-095**: 1 − 0,95¹² = 0,46.
- **PSY-105**: con la diferencia entre proporciones (45 frente a 50) y con la diferencia entre
  puntuaciones típicas (≈1,29 frente a ≈1,54) el orden es el mismo, de modo que la conclusión
  puntuada es robusta pese a que la lectura ingenua (85 % > 60 %) la invierte.
- **PSY-088**: solución determinada (fichas 1 y 4).

---

## Autoevaluación de la pasada 3 (QQR v1.0)

### Gates obligatorios

Los 34 ítems pasan los ocho gates. Comprobaciones que requerían atención específica:

| Gate | Ítems | Resultado |
|---|---|---|
| G3 (desalineación constructo-pregunta) | 079, 081, 087, 091, 093, 095, 096, 104 | Pasan. Véase la sección «Frontera con `critical_analysis`». |
| G5 (inferencia injustificada incrustada) | 087, 092, 098, 103 | Pasan. En 092 y 098 el enunciado declara expresamente los supuestos (que ambas observaciones son correctas y sin error de medida; que se trata de un patrón observado en estudios de seguimiento) y la tarea consiste precisamente en examinar qué los explica. En 087 la aleatoriedad de la lista es el dato del que hay que partir, no una conclusión. En 103 la respuesta correcta incluye señalar la autoselección de los participantes, de modo que el ítem no da por supuesta la interpretación. |
| G6 (tarea clínica inapropiada) | 075, 089, 090, 092, 098, 104 | Pasan. Ninguno pide diagnosticar, evaluar ni tratar a una persona. Los enunciados de 089 y 090 **prohíben expresamente** proponer un plan de intervención, y esa abstención figura entre los errores críticos de 090. En 075 lo que se pide es determinar qué autoriza a concluir un dato de medida; en 092 y 104 los problemas y tratamientos se designan de forma genérica; en 098 se razona sobre resultados de grupo de un cuerpo de investigación. |
| G7 (dependencia cultural) | Todos, en particular 099 y 102 | Pasan. Ningún ítem depende de conocimiento cultural específicamente español; en 102 los grupos se designan de forma genérica y sin atribuirles identidad alguna. |
| G4 (respuesta no evaluable) | 088, 091, 094, 095, 105 | Pasan con holgura: la respuesta correcta está determinada numérica o lógicamente. |

### Criterios de calidad

Umbral de aceptación: 16/18 (88,9 %). Ningún ítem puntúa 0 en Q1, Q2, Q3 o Q4.

| ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Total | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSY-074 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | N/A | 2 | **15/16** | ACCEPT |
| PSY-075 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-076 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | N/A | 2 | **15/16** | ACCEPT |
| PSY-077 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-078 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-079 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16/16** | ACCEPT |
| PSY-080 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-081 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16/16** | ACCEPT |
| PSY-082 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-083 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-084 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-085 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-086 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-087 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-088 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-089 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-090 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-091 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-092 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-093 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-094 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-095 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-096 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-097 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-098 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-099 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-100 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-101 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-102 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-103 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-104 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16/16** | ACCEPT |
| PSY-105 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-106 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-107 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |

29 ítems puntuados sobre 18: media **17,93**, mínimo 17. Cinco ítems se puntúan sobre 16 por
`Q8 = N/A`: PSY-079, PSY-081 y PSY-104 obtienen 16/16 (100 %), y PSY-074 y PSY-076 obtienen 15/16
(93,75 %). Todos por encima del umbral del 88,9 %.

### Matices honestos sobre las puntuaciones

1. **Q3 = 1 en los tres ítems `easy`.** Puntuación deliberadamente conservadora, coherente con las
   dos pasadas anteriores: una parte sustancial de la respuesta es recuperable por un modelo
   competente. Los tres incorporan un elemento que sí discrimina —la descripción del patrón de
   datos esperable, la exigencia de un procedimiento de medida que sostenga la afirmación sobre el
   rasgo, y la condición mínima que haría explicativa una atribución disposicional—, pero no se les
   atribuye Q3 = 2. Los tres siguen en ACCEPT y cumplen el mínimo Q3 ≥ 1 de la sección 6.
2. **Q7 = 1 en PSY-089.** Es la reincidencia temática más marcada del lote: con PSY-007 (piloto),
   PSY-040 (pasada 1) y PSY-086 y PSY-090 de esta pasada, el campo del condicionamiento reúne cinco
   ítems en el conjunto. Se mantienen los tres de esta pasada porque las capacidades son
   distintas y así se declara en sus `notes` —distinción adquisición-ejecución, resistencia a la
   extinción con contingencias recíprocas, y acoplamiento de dos procesos en el mantenimiento de la
   evitación—, pero la penalización se refleja en la puntuación en lugar de negarse. Con 17/18 la
   decisión no cambia.
3. **Lecturas conservadoras que no se han aplicado.** Un revisor estricto podría puntuar Q7 = 1 en
   PSY-105 por la densidad de ítems de memoria en el conjunto, en PSY-094 por compartir con
   PSY-038 el terreno de la fiabilidad, o en PSY-100 y PSY-101 por compartir el campo de la
   influencia del grupo. En todos los casos el resultado sería 17/18 y la decisión seguiría siendo
   ACCEPT.
4. **Q6 en la frontera medium/hard.** PSY-080 y PSY-087 podrían defenderse como `hard`, y PSY-091
   como `medium` una vez identificada la variable responsable. Se ha asignado la dificultad por la
   cantidad de elementos que la respuesta completa debe integrar, criterio de la sección 6; en los
   tres casos un revisor podría desplazarla un nivel, lo que corresponde a Q6 = 1 y no altera la
   decisión.
5. **Q2 y magnitudes.** Cuatro ítems tocan literaturas donde las cifras están en discusión o
   dependen del criterio: PSY-087 (magnitud de los efectos de expectativa), PSY-098 (resultados de
   los estudios de adopción), PSY-102 (peso de las condiciones de Allport) y PSY-103 (replicación
   del estudio del puente). En los cuatro, el `expected_answer` y los criterios están redactados
   para puntuar **el argumento y no la cifra**, y la cautela sobre el estatus de la evidencia forma
   parte de lo evaluado, no de una nota al margen.
6. **Q8 y verificación de fuentes.** Se puntúa Q8 = 2 cuando la fuente citada sostiene directamente
   la afirmación del ítem. En **21 ítems** (077, 078, 080, 082, 083, 084, 085, 086, 088, 093, 095,
   096, 097, 098, 099, 100, 101, 102, 103, 106 y 107) se han **omitido deliberadamente los DOI**
   por no haber podido confirmarlos en una fuente autorizada desde este entorno de ejecución, con
   la omisión anotada en el `notes` o en el propio `source` del ítem; es el mismo criterio de
   prudencia de las pasadas 1 y 2 y de la curación del piloto. Ocho ítems citan monografías o
   artículos anteriores a la asignación sistemática de DOI (075, 087, 089, 090, 091, 092, 094,
   105) y cinco no citan fuente por tratarse de principios metodológicos o lógicos generales (074,
   076, 079, 081, 104), uso de `Q8 = N/A` que la sección 5 admite expresamente. **El paso de
   verificación de fuentes (sección 12 de la rúbrica) debe cerrar este punto antes de la inclusión
   en el dataset final.**
7. **Separación entre generación y validación.** Se mantiene lo dicho en las pasadas 1 y 2: esta
   autoevaluación es el filtro previo exigido por el encargo, no un sustituto de la revisión
   humana.

---

## Ítems descartados durante la generación (pasada 3)

| Candidato | Motivo del descarte |
|---|---|
| Falsa creencia: mentalización frente a demandas ejecutivas en una tarea modificada | Redundancia estructural con PSY-041 (pasada 1), que emplea exactamente el patrón «discrepancia entre paradigmas → explicaciones en competencia» con la permanencia del objeto. Q7 = 0. |
| Inflación del tamaño del efecto en un estudio pequeño con resultado significativo | Solapa con PSY-022 (piloto), cuya viñeta es un estudio de 20 participantes con resultado significativo. Sustituido por PSY-095, cuyo problema es la tasa de error de una familia de contrastes. |
| Regresión a la media aplicada a la evaluación de un tratamiento | Ya incorporada en PSY-065 (pasada 2) y solapada con PSY-024 (piloto). |
| Inferencia inversa en neuroimagen | Solapa con PSY-012 (piloto), como ya se documentó en la pasada 1. |
| Efecto de sobrejustificación de las recompensas externas | Excluido por la restricción 1: pertenece al campo de la teoría de la autodeterminación, sobrerrepresentada en el piloto y ya cuestionada en PSY-017. |
| Fiabilidad alta con validez nula en un test | Solapa con PSY-038 (pasada 1). El terreno psicométrico se cubre en esta pasada con PSY-094 (atenuación) y PSY-093 (restricción del rango), que evalúan capacidades no cubiertas. |
| Práctica intercalada y variabilidad de la práctica | Redundancia **cognitiva**, no temática: la lógica «peor adquisición, mejor transferencia» reproduce la distinción aprendizaje-ejecución que ya evalúa PSY-086, y el campo del espaciamiento está cubierto por PSY-003 y PSY-008. |
| Falacia ecológica | Proximidad excesiva con PSY-061 (pasada 2), que trata el salto del grupo al individuo. |
| Sesgo de retrospectiva en el análisis de un incidente | Aplazado, no descartado por calidad: la pasada 2 lo dejó documentado como candidato disponible para `communication`, y anticiparlo aquí cerraría esa vía. |

Un candidato válido queda disponible para pasadas futuras: **exigencia de una respuesta
dicotómica sobre una cuestión con evidencia conflictiva**, ya anotado como pendiente en la pasada
2 y adecuado para `uncertainty`, dimensión aún sin escalar junto con `critical_analysis`.

---

## Pasada 4 — dimensión `uncertainty`, 30 ítems (PSY-108 a PSY-137)

Cuarta pasada sobre este archivo. Acumulado tras esta pasada: **107 ítems** (77 de las pasadas 1 a
3 + 30 nuevos). No se ha modificado ningún ítem de pasadas anteriores ni ningún archivo del piloto:
el diff sobre `new_items_draft.json` es de 898 líneas añadidas y 0 eliminadas.

**Validación:** `python3 scripts/validate_dataset.py --data data/processed/new_items_draft.json`
→ `RESULTADO: OK`, exit code 0, 107 ítems, 0 IDs duplicados, sin colisión con los IDs del piloto ni
con los de pasadas anteriores (máximo previo `PSY-107`).

Validado también el conjunto combinado piloto + draft (135 ítems): sin errores bloqueantes. Los
avisos de equilibrio de dimensiones se mantienen y se reducirán al escalar `critical_analysis`, la
única dimensión que sigue sin escalar (5 ítems). Tras esta pasada, `uncertainty` pasa de 5 a 35
ítems en el conjunto combinado.

### Distribución

| Dificultad | N | IDs |
|---|---|---|
| `easy` | 3 | PSY-108, PSY-109, PSY-110 |
| `medium` | 9 | PSY-111 a PSY-119 |
| `hard` | 18 | PSY-120 a PSY-137 |

Los tres ítems `easy` miden errores conceptuales extendidos y no recuerdo: el tratamiento
asimétrico de las anécdotas confirmatorias y desconfirmatorias (108), la aceptación de un
presupuesto no verificado incrustado en la petición (109) y la búsqueda de una causa única de un
trastorno (110). El 60 % del lote es `hard`, conforme al encargo y a la naturaleza de la dimensión.

### Estructura de los ítems (sección 7.4 de la rúbrica)

La sección 7.4 exige que una buena respuesta no se limite a «no se puede saber», sino que
identifique qué puede concluirse, qué no, por qué la evidencia es insuficiente, qué explicaciones
alternativas existen y qué evidencia reduciría la incertidumbre. Los 30 enunciados están redactados
para exigir explícitamente esa partición: **los 30 piden delimitar lo afirmable frente a lo no
afirmable**, y ninguno admite como respuesta completa una negativa genérica. En consecuencia, los
criterios de 1 punto describen sistemáticamente la respuesta que se queda en la negativa sin
articular sus componentes, y **28 de los 30 ítems incluyen entre sus errores críticos al menos uno
de sobreafirmación**; siete incluyen además el error simétrico de **infraafirmación** —negar todo
valor a la evidencia disponible— porque el sobreajuste escéptico es el modo de fallo característico
de esta dimensión: PSY-108, PSY-111, PSY-113, PSY-120, PSY-124, PSY-126, PSY-131 y PSY-133.

Dos ítems del lote llevan la dimensión más allá de la descripción de la incertidumbre:
**PSY-120** exige decidir bajo evidencia insuficiente sin sobreafirmar, y **PSY-137** exige separar
la incertidumbre reducible acumulando datos del mismo tipo de la que solo se reduce cambiando el
tipo de dato. **PSY-128** añade una tercera variante: incertidumbre que no procede de los datos
sino del tramo valorativo que va de la evidencia a la recomendación, y que no se resuelve con más
datos.

### Frontera con `critical_analysis` (G3)

`critical_analysis` es la dimensión limítrofe y sigue sin escalar, de modo que la separación se ha
cuidado especialmente para no ocupar su terreno. El criterio aplicado: un ítem es
`critical_analysis` cuando la tarea es **evaluar una afirmación y localizar sus fallos**, y es
`uncertainty` cuando la información es **genuinamente insuficiente** y la tarea es **repartir
conclusiones entre justificadas e injustificadas y decir qué las resolvería**. Los ítems que más se
acercan a la frontera son PSY-121, PSY-122, PSY-123 y PSY-131, todos ellos con una conclusión ajena
citada en el enunciado; en los cuatro, la conclusión ajena no es el objeto de la respuesta
puntuada, sino el punto de partida para una partición que el propio enunciado exige, y en los
cuatro la respuesta correcta mantiene abierta alguna posibilidad en lugar de cerrar el caso. En
particular, PSY-122 exige no concluir que el efecto no existe, PSY-131 no concluir que el aumento
sea artefactual, y PSY-123 no fijar la dirección del sesgo.

### Cobertura temática y control de redundancia (Q7)

Ningún marco teórico del piloto se reutiliza. Los cinco ítems `uncertainty` del piloto —diagnóstico
con datos insuficientes (019), confianza y exactitud del recuerdo (021), generalización desde una
muestra pequeña (022), subdeterminación de la conducta observable (023) y atribución causal con
cambios concurrentes (024)— quedan fuera del lote, y los ítems que rozan su terreno lo declaran en
sus `notes`: PSY-133 y PSY-135 respecto a PSY-021, PSY-113 y PSY-136 respecto a PSY-022, PSY-108 y
PSY-111 respecto a PSY-024, y PSY-132 respecto a PSY-019 (allí la incertidumbre es previa al
diagnóstico; aquí es la que persiste después de tenerlo).

Los campos cubiertos por el lote son nuevos en el conjunto: síntesis de evidencia (121, 122),
dependencia entre estudios (124), atrición y datos ausentes (123), componentes activos de una
intervención (125), transferencia del aprendizaje (127), desacuerdo entre expertos (128), predicción
individual a partir de puntuaciones genéticas (129), series de datos administrativos (131), alcance
informativo de una categoría diagnóstica (132), identidad de etiqueta y de constructo (134),
calibración de juicios (135), transportabilidad (136) y tipos de incertidumbre (137).

### Marcos reincidentes y coincidencias de escenario declaradas (Q7)

Todas figuran en el campo `notes` del ítem correspondiente:

| Ítem | Coincide con | Qué lo distingue |
|---|---|---|
| PSY-110 | PSY-059 (pasada 2) | Allí, responder a una persona en tratamiento sobre el mito de la serotonina; aquí, enunciar el estado del conocimiento con confianza calibrada. |
| PSY-113 | PSY-028 (piloto), PSY-022 (piloto) | Allí, significación frente a relevancia práctica y generalización desde muestra pequeña; aquí, qué magnitudes admite un intervalo. |
| PSY-114 | PSY-106 (pasada 3) | Allí, agregar observaciones para estimar una disposición; aquí, interpretar un desacuerdo sin criterio externo que arbitre. |
| PSY-116 | PSY-099 (pasada 3) | Coincidencia de dominio (alcohol y adolescentes), sin solapamiento de marco ni de demanda. |
| PSY-117 | PSY-055 (pasada 2) | Allí, comunicar el error de una puntuación única; aquí, la fiabilidad de una diferencia entre dos administraciones. |
| PSY-118 | PSY-060 (pasada 2), PSY-093 (pasada 3) | Coincidencia de escenario (selección de personal), con tres marcos teóricos distintos. |
| PSY-121 | PSY-014 (piloto) | Allí, qué valorar antes de aceptar una afirmación metaanalítica; aquí, interpretar el I² y reformular la conclusión. |
| PSY-123 | PSY-066 (pasada 2), PSY-092 (pasada 3) | Allí, no respuesta en una encuesta y condicionamiento sobre efecto común; aquí, pérdida de la garantía de la aleatorización. |
| PSY-126 | PSY-063, PSY-045, PSY-064 (pasada 2) | Coincidencia de dominio (dolor, placebo), con demanda inferencial y no comunicativa. |
| PSY-129 | PSY-039 (pasada 1) | Allí, qué significa un coeficiente de heredabilidad; aquí, la predicción individual desde una puntuación. |
| PSY-132 | PSY-019 (piloto), PSY-076 (pasada 3) | Allí, insuficiencia de datos para diagnosticar y circularidad explicativa; aquí, el alcance informativo de la categoría. |
| PSY-133 | PSY-021 (piloto) | Allí, recuerdo propio y disociación confianza-exactitud; aquí, informes retrospectivos como variable de un diseño. |
| PSY-134 | PSY-094, PSY-038 | Allí, atenuación por error de medida y consistencia interna; aquí, identidad de etiqueta frente a identidad de constructo. |
| PSY-135 | PSY-021 (piloto), PSY-084 (pasada 3) | Allí, exactitud de un recuerdo y condiciones de la pericia; aquí, la calibración como propiedad de un conjunto de juicios. |
| PSY-136 | PSY-022 (piloto), PSY-116 (esta pasada) | Allí, estudio débil y cambio de parámetros de la intervención; aquí, estudios sólidos y cambio de población. |
| PSY-137 | PSY-092 (pasada 3), PSY-113 (esta pasada) | Allí, creación de una asociación por el muestreo y anchura del intervalo; aquí, qué operación reduce cada tipo de incertidumbre. |

La familia más densa del lote es la de **medidas que discrepan** (PSY-114, PSY-126, PSY-130 y
PSY-134). Se mantienen los cuatro porque la demanda es distinta en cada uno —ausencia de criterio
externo entre informantes, divergencia entre tipos de resultado en un ensayo sin cegamiento,
discordancia entre medida indirecta y autoinforme, e identidad de la etiqueta frente a identidad
del constructo—, pero la proximidad se reconoce con `Q7 = 1` en PSY-126 y se declara en las `notes`
de los cuatro. Un quinto candidato de esta familia se descartó (véase más abajo).

### Datos numéricos verificables

Cinco ítems contienen cifras elegidas para que la conclusión puntuada sea comprobable y no dependa
del criterio del evaluador:

- **PSY-113**: intervalo [0,02; 0,88], con límite inferior prácticamente nulo y superior
  considerable, de modo que la impropiedad de calificar el efecto de «moderado» es verificable.
- **PSY-117**: fiabilidad 0,85 y desviación típica 10 producen un error típico de medida de ≈ 3,9,
  un error típico de la diferencia de ≈ 5,5 y un margen del 95 % de ≈ ±11 puntos; el cambio de 7
  puntos queda dentro de ese margen. El cálculo formal no se exige: se puntúa la conclusión.
- **PSY-123**: 65 % frente a 92 % de retención, diferencia suficiente para que la pérdida de
  comparabilidad no sea discutible.
- **PSY-121**: I² del 82 % con intervalo de confianza estrecho, combinación elegida expresamente
  para que la confusión entre precisión de la media y acuerdo entre estudios sea el error modal.
- **PSY-129**: 12-15 % de varianza explicada, orden de magnitud comunicado por la literatura
  reciente para el rendimiento educativo; los criterios puntúan el argumento y no la cifra.

---

## Autoevaluación de la pasada 4 (QQR v1.0)

### Gates obligatorios

Los 30 ítems pasan los ocho gates. Comprobaciones que requerían atención específica:

| Gate | Ítems | Resultado |
|---|---|---|
| G3 (desalineación constructo-pregunta) | 121, 122, 123, 131 | Pasan. Véase la sección «Frontera con `critical_analysis`». |
| G5 (inferencia injustificada incrustada) | 109, 118, 124, 129, 130, 131, 133 | Pasan. En todos ellos la afirmación no justificada se **atribuye expresamente a un tercero** del escenario y constituye el objeto de la evaluación, nunca la voz del ítem, siguiendo el patrón de PSY-023 y PSY-024 del piloto. En 109 el caso es límite y se documenta en sus `notes`: el presupuesto falso es deliberado y la respuesta correcta consiste en no colaborar con él. |
| G6 (tarea clínica inapropiada) | 110, 111, 114, 117, 120, 126, 130, 132, 135, 136 | Pasan. Ninguno pide diagnosticar, pronosticar ni tratar a una persona. Los enunciados de **114, 132 y 136 lo excluyen expresamente**, y en 114 y 132 la abstención figura entre los errores críticos. Los trastornos se designan de forma genérica en 131 y 132. |
| G7 (dependencia cultural) | 119 en particular | Pasa. En 119 la diferencia entre poblaciones es el objeto psicométrico del ítem y no un conocimiento cultural accesorio; los países se dejan sin especificar precisamente para que la respuesta no dependa de conocer ninguna cultura concreta. |
| G4 (respuesta no evaluable) | 113, 117, 121, 123 | Pasan con holgura: la conclusión correcta está determinada numéricamente. En el resto, los criterios están redactados como elementos observables enumerables. |
| G1 (error científico) | 129, 130 | Pasan. Ambos tocan literaturas en discusión; el `expected_answer` describe el estado del desacuerdo en lugar de cerrarlo, y en 130 se citan expresamente dos metaanálisis que llegaron a valoraciones distintas. |

### Criterios de calidad

Umbral de aceptación: 16/18 (88,9 %). Ningún ítem puntúa 0 en Q1, Q2, Q3 o Q4.

| ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Total | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSY-108 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | N/A | 2 | **15/16** | ACCEPT |
| PSY-109 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16/16** | ACCEPT |
| PSY-110 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-111 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-112 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-113 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-114 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-115 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-116 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-117 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-118 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-119 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-120 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16/16** | ACCEPT |
| PSY-121 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-122 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-123 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-124 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-125 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-126 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-127 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-128 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16/16** | ACCEPT |
| PSY-129 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-130 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-131 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-132 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-133 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-134 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-135 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-136 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-137 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |

26 ítems puntuados sobre 18: media **17,85**, mínimo 17. Cuatro ítems se puntúan sobre 16 por
`Q8 = N/A`: PSY-109, PSY-120 y PSY-128 obtienen 16/16 (100 %), y PSY-108 obtiene 15/16 (93,75 %).
Todos por encima del umbral del 88,9 %.

### Matices honestos sobre las puntuaciones

1. **Q3 = 1 en PSY-108 y PSY-110.** Puntuación conservadora, coherente con las tres pasadas
   anteriores: buena parte de la respuesta es recuperable por un modelo competente. Ambos
   incorporan un elemento que sí discrimina —la simetría del límite inferencial en 108, y la
   exigencia de separar asociación replicada de mecanismo establecido en 110—, pero no se les
   atribuye Q3 = 2. **PSY-109 es la excepción entre los `easy`**: se le asigna Q3 = 2 porque la
   capacidad que mide —no colaborar con un presupuesto falso incrustado en la petición— es
   precisamente aquella en la que los modelos difieren de forma marcada, con independencia de la
   sencillez conceptual de la tarea.
2. **Q7 = 1 en PSY-113, PSY-126 y PSY-135.** Las tres proximidades más marcadas del lote: 113 con
   PSY-028 y PSY-022 en el terreno de la interpretación de estimaciones, 126 con PSY-063, PSY-045 y
   PSY-064 en el del dolor y el placebo, y 135 con PSY-021 en el de la confianza subjetiva. Los tres
   se mantienen porque las capacidades evaluadas son distintas y así se declara en sus `notes`, pero
   la penalización se refleja en la puntuación en lugar de negarse. Con 17/18 la decisión no cambia.
3. **Lecturas conservadoras que no se han aplicado.** Un revisor estricto podría puntuar Q7 = 1 en
   PSY-130 y PSY-134 por la densidad de la familia de «medidas que discrepan», en PSY-136 por
   compartir con PSY-116 la estructura de la extrapolación fuera de lo evaluado, o en PSY-122 por
   compartir con PSY-070 el terreno de la replicabilidad. En todos los casos el resultado sería
   17/18 y la decisión seguiría siendo ACCEPT.
4. **Q6 en la frontera medium/hard.** PSY-117 podría defenderse como `hard` por contener un cálculo,
   y PSY-118 y PSY-119 por el número de elementos que la respuesta completa debe integrar; a la
   inversa, PSY-131 podría leerse como `medium` una vez identificado que el indicador depende de la
   detección. Se ha asignado la dificultad por la cantidad de elementos que la respuesta debe
   integrar, criterio de la sección 6, y en los cuatro casos un revisor podría desplazarla un nivel,
   lo que corresponde a Q6 = 1 y no altera la decisión.
5. **Q2 y literaturas en discusión.** Cuatro ítems tocan cuestiones no cerradas: PSY-129 (magnitud y
   portabilidad de las puntuaciones poligénicas), PSY-130 (validez predictiva de las medidas
   implícitas), PSY-127 (alcance de la transferencia del entrenamiento cognitivo) y PSY-125
   (resultados de los estudios de desmantelamiento). En los cuatro, el `expected_answer` y los
   criterios están redactados para **puntuar el argumento y la calibración, no la cifra ni la toma
   de partido**, y describir el estado del desacuerdo forma parte de lo evaluado.
6. **Q8 y verificación de fuentes.** Se puntúa Q8 = 2 cuando la fuente citada sostiene directamente
   la afirmación del ítem. En **24 ítems** (110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 121,
   122, 124, 125, 126, 127, 129, 130, 131, 132, 133, 134, 136 y 137) se han **omitido
   deliberadamente los DOI** por no haber podido confirmarlos en una fuente autorizada desde este
   entorno de ejecución, con la omisión anotada en el propio campo `source`; es el mismo criterio de
   prudencia de las pasadas 1 a 3 y de la curación del piloto. PSY-135 cita dos obras, una de ellas
   un capítulo de libro sin DOI y la otra con el DOI omitido por la misma razón; PSY-123 cita un
   informe monográfico sin DOI asignado. Cuatro ítems no citan fuente por tratarse de
   principios inferenciales generales (108, 109, 120, 128), uso de `Q8 = N/A` que la sección 5
   admite expresamente. **El paso de verificación de fuentes (sección 12 de la rúbrica) debe cerrar
   este punto antes de la inclusión en el dataset final.**
7. **Separación entre generación y validación.** Se mantiene lo dicho en las pasadas anteriores:
   esta autoevaluación es el filtro previo exigido por el encargo, no un sustituto de la revisión
   humana.

---

## Ítems descartados durante la generación (pasada 4)

| Candidato | Motivo del descarte |
|---|---|
| Incoherencia entre sistemas de respuesta emocional (fisiología, autoinforme, conducta) | Redundancia **cognitiva** con la familia de «medidas que discrepan», ya representada por cuatro ítems (114, 126, 130, 134). Quinto miembro innecesario. Queda disponible para pasadas futuras si esa familia se aligera. |
| Resultado nulo con potencia insuficiente | Solapa con PSY-058 (pasada 2), cuya demanda es exactamente distinguir «no se encontró efecto» de «se demostró que no hay efecto». |
| Identificación de un testigo presencial emitida con alta confianza | Proximidad excesiva con PSY-021 (piloto). La disociación confianza-exactitud se cubre en esta pasada desde ángulos distintos en PSY-133 y PSY-135. |
| Cribado de riesgo con tasa base muy baja | Solapa con PSY-042 (pasada 1), que ya trata la dependencia del valor predictivo respecto de la prevalencia. El cribado aparece en PSY-128 solo como escenario. |
| Dirección causal en un panel longitudinal de dos olas | La sección 9 de la rúbrica desaconseja acumular ítems de correlación y causalidad; el terreno ya está cubierto por PSY-009, PSY-011 (piloto) y PSY-026 (piloto). |
| Comparación con controles históricos y tendencia secular | Solapa con PSY-054 (pasada 2) y PSY-024 (piloto). |
| Inferencia inversa a partir de un resultado de neuroimagen | Ya descartado en las pasadas 1 y 3 por solapamiento con PSY-012 (piloto). |
| Ausencia total de evidencia sobre una práctica muy extendida | Redundancia cognitiva con PSY-108: es la misma simetría del límite inferencial trasladada del testimonio individual al cuerpo de literatura. |
| Estudio cualitativo y tipo de afirmación que sostiene | Redundancia con PSY-111 (caso único): idéntica demanda de asignar tipos de afirmación a lo que un diseño puede sostener. El terreno del autoinforme de las causas propias se cubre en su lugar con PSY-118. |

Dos candidatos quedan disponibles para pasadas futuras: **el sesgo de retrospectiva en el análisis
de un incidente**, anotado ya como pendiente en las pasadas 2 y 3 y adecuado para
`critical_analysis`, y **la incoherencia entre sistemas de respuesta emocional**, descartado aquí
solo por densidad de familia. `critical_analysis` es la única dimensión que sigue sin escalar.

---

## Pasada 5 — dimensión `critical_analysis`, 35 ítems (PSY-138 a PSY-172)

Quinta pasada sobre este archivo y última dimensión pendiente de escalar. Acumulado tras esta
pasada: **142 ítems** (107 de las pasadas 1 a 4 + 35 nuevos). No se ha modificado ningún ítem de
pasadas anteriores ni ningún archivo del piloto: el diff sobre `new_items_draft.json` es de 1.053
líneas añadidas y 0 eliminadas, y `git status` no registra cambios en
`pilot_questions_curated.json` ni en `question_schema.json`.

**Validación:** `python3 scripts/validate_dataset.py --data data/processed/new_items_draft.json`
→ `RESULTADO: OK`, exit code 0, 142 ítems, 0 IDs duplicados, sin colisión con los IDs del piloto ni
con los de pasadas anteriores (máximo previo `PSY-137`).

Validado también el conjunto combinado piloto + draft (170 ítems): sin errores bloqueantes.
`critical_analysis` pasa de 5 a 40 ítems en el conjunto combinado, y el único aviso de equilibrio
que subsiste es el de `knowledge` (20 ítems frente a una media de 34), la dimensión menos escalada
del conjunto; no es bloqueante y queda anotado como candidato natural para una pasada futura.

### Distribución

| Dificultad | N | IDs |
|---|---|---|
| `easy` | 3 | PSY-138, PSY-139, PSY-140 |
| `medium` | 10 | PSY-141 a PSY-150 |
| `hard` | 22 | PSY-151 a PSY-172 |

El 63 % del lote es `hard`, conforme al encargo y a la naturaleza de la dimensión. Los tres ítems
`easy` miden errores conceptuales extendidos y no recuerdo: tomar la publicación con revisión por
pares como garantía de la conclusión (138), aplicar el principio de que la correlación no implica
causalidad a un experimento aleatorizado (139) y aceptar la antigüedad y la popularidad de una
práctica como evidencia de eficacia (140). Los tres exigen sostener a la vez la crítica y su
límite, que es donde falla la respuesta débil.

### Estructura de los ítems (sección 7.3 de la rúbrica)

La sección 7.3 pide que un ítem de esta dimensión presente una afirmación, argumento, estudio,
resultado o interpretación evaluable. **Los 35 lo hacen y en los 35 la afirmación se atribuye
expresamente a un tercero** —un artículo, un titular, una consultora, un asistente a un seminario,
una comisión—, nunca a la voz del ítem, requisito de G5. Las dimensiones analíticas de la sección
7.3 quedan cubiertas sin que ninguna domine:

| Dimensión analítica | Ítems |
|---|---|
| Sobregeneralización y extrapolación fuera de las condiciones | 141, 143, 149, 156 |
| Interpretación estadística | 148, 159, 164, 172 |
| Limitaciones metodológicas y decisiones del analista | 145, 147, 152, 153, 166, 171 |
| Problemas de medida y de constructo | 142, 150, 157, 163, 165 |
| Explicaciones alternativas | 140, 151, 158, 162 |
| Supuestos no justificados y estructura del argumento | 138, 144, 161, 169 |
| Validez externa y de constructo del paradigma | 149, 155, 160 |
| Replicabilidad y estatus de la evidencia | 138, 170 |
| Unidad de análisis y sesgo de selección | 146, 162 |
| Validez predictiva e incremental | 154 |

### La familia de crítica invertida

Cinco ítems del lote —**PSY-139, PSY-160, PSY-167, PSY-168 y PSY-170**— están construidos de modo
que la respuesta correcta exige **defender en parte lo criticado**, porque el modo de fallo
característico de un modelo entrenado a enumerar limitaciones es la crítica refleja. La familia se
declara aquí y en las `notes` de cada ítem, y cada miembro tiene un objeto distinto:

| Ítem | Qué hay que reconocer como improcedente |
|---|---|
| PSY-139 | Aplicar un principio válido (correlación y causalidad) al tipo de diseño en que no rige. |
| PSY-160 | Atribuir a la validez interna objeciones que corresponden a la medida o a la generalización. |
| PSY-167 | Descartar un efecto por su magnitud sin considerar alcance, coste ni alternativas. |
| PSY-168 | Aplicar objeciones de muestra a una conclusión a la que no amenazan. |
| PSY-170 | Concluir la inexistencia de un efecto a partir de una única replicación fallida. |

El contraste entre **PSY-156 y PSY-168** es deliberado: la misma objeción sobre la composición de
la muestra es decisiva en el primero, donde la afirmación evaluada es de universalidad, e
improcedente en el segundo, donde la afirmación es sobre un mecanismo perceptivo básico. El par
**PSY-148 / PSY-167** cumple la misma función con la magnitud del efecto: en uno se presenta como
demostrada la relevancia de una diferencia pequeña por ser significativa y en el otro se descarta
un efecto pequeño por serlo, de modo que un modelo que aplique una regla fija a los tamaños del
efecto falla necesariamente en uno de los dos.

### Cobertura temática y control de redundancia (Q7)

**Ningún marco teórico de los cinco ítems `critical_analysis` del piloto se reutiliza.** Amenaza
del estereotipo (013), superioridad de la terapia cognitivo-conductual frente a lista de espera
(014), interpretación del valor p aislado (015), estabilidad de la personalidad (016) y
absolutismo de la teoría de la autodeterminación (017) quedan fuera del lote. En particular **no se
reutiliza la teoría de la autodeterminación**, señalada por el revisor del piloto como
sobrerrepresentada.

Ningún escenario, caso ni dato numérico del piloto o de pasadas anteriores reaparece. Los tres
escenarios que podrían parecer repetidos no lo son: la lista de espera aparece en PSY-139 como una
objeción secundaria dentro de una enumeración y no como objeto (PSY-014); la selección de personal
aparece en PSY-154 con el marco de la validez incremental, distinto del de PSY-060 y PSY-093; y la
prevención escolar aparece en PSY-167 como escenario de una decisión de recursos, no de diseño
(PSY-052, PSY-095).

Campos nuevos en el conjunto: estatus epistémico de la publicación (138), condiciones de obtención
de un dato divulgado (141), validación de una tipología (142), niveles de explicación (144),
finalidad de un estudio piloto (145), unidad de análisis (146), dicotomización (147), relevancia
clínica anclada empíricamente (148), inferencia traslacional desde modelos animales (149),
formulación de ítems de encuesta (150), sesgo retrospectivo y de resultado (151), discrepancia entre
protocolo registrado y publicación (152), circularidad analítica (153), validez incremental (154),
cadena artículo-nota de prensa-noticia (155), base muestral de una afirmación de universalidad
(156), reificación de un factor (157), adaptacionismo post hoc (158), espacio de especificaciones
(159), separación de tipos de validez (160), inmunización de hipótesis (161), denominador ausente
(162), construcción de una categoría y derivación de su prevalencia (163), comparación de veredictos
de significación (164), solapamiento de contenido entre escalas (165), ajuste por variable posterior
al tratamiento (166), pertinencia de una crítica (168), salto de la descripción a la prescripción
(169), alcance de una replicación fallida (170), codificación no ciega (171) y traducción de la
varianza explicada (172).

### Marcos reincidentes y coincidencias declaradas (Q7)

Todas figuran en el campo `notes` del ítem correspondiente:

| Ítem | Coincide con | Qué lo distingue |
|---|---|---|
| PSY-139 | PSY-009, PSY-011, PSY-026 (piloto) | Allí, detectar el salto causal; aquí, reconocer que el principio se aplica fuera de su ámbito. |
| PSY-140 | PSY-108 (pasada 4) | Allí, el límite inferencial de un testimonio individual; aquí, la estructura de un argumento de tradición y los mecanismos de transmisión de una práctica. |
| PSY-141 | PSY-032 (pasada 1) | Allí, un neuromito sin base; aquí, un dato real cuyas condiciones de obtención hay que reconstruir. |
| PSY-142 | PSY-005 (piloto), PSY-154 (esta pasada) | Allí, estructura de rasgos y aportación sobre predictores existentes; aquí, que el dato aportado no es de validez. |
| PSY-143 | PSY-039 (pasada 1) | Allí, qué es la heredabilidad; aquí, una inferencia de política educativa que la usa como premisa. |
| PSY-144 | PSY-059 (pasada 2) | Allí, comunicar a un paciente; aquí, desmontar una inferencia entre niveles de explicación. |
| PSY-145 | PSY-022 (piloto) | Allí, qué concluir de una muestra pequeña; aquí, la finalidad declarada del diseño y el uso posterior de su estimación. |
| PSY-146 | PSY-091 (pasada 3), PSY-119 (pasada 4) | Allí, inversión de una asociación al agregar y equivalencia de medida; aquí, la unidad de análisis. |
| PSY-147 | PSY-094 (pasada 3), PSY-058 (pasada 2) | Allí, atenuación por el instrumento y lectura de resultados nulos; aquí, la atenuación creada por una decisión evitable. |
| PSY-148 | PSY-028 (piloto), PSY-167 (esta pasada) | Allí, comunicar la distinción; aquí, evaluarla y especificar qué evidencia decide la relevancia. |
| PSY-149 | PSY-155 (esta pasada) | Allí, la distancia entre titular y artículo; aquí, la validez de constructo de un modelo animal. |
| PSY-150 | PSY-066 (pasada 2), PSY-109 (pasada 4) | Allí, quién responde y una premisa falsa que hay que rechazar; aquí, el efecto de la formulación sobre la distribución de respuestas. |
| PSY-151 | PSY-042 (pasada 1), PSY-062 (pasada 2) | Allí, valor predictivo y comunicación responsable; aquí, la epistemología de una revisión de casos. |
| PSY-152 | PSY-095 (pasada 3), PSY-015 (piloto) | Allí, multiplicidad informada; aquí, selección oculta entre lo planificado y lo publicado. |
| PSY-153 | PSY-094, PSY-095 (pasada 3), PSY-012 (piloto) | Allí, atenuación, multiplicidad e inferencia inversa; aquí, circularidad entre selección y estimación. |
| PSY-154 | PSY-060 (pasada 2), PSY-093 (pasada 3) | Allí, comunicación y restricción del rango; aquí, la aportación sobre los predictores ya en uso. |
| PSY-155 | PSY-058 (pasada 2), PSY-126 (pasada 4) | Allí, resultados nulos y divergencia entre medidas; aquí, la comparación de dos textos y la redacción de la conclusión ajustada. |
| PSY-156 | PSY-136, PSY-119 (pasada 4) | Allí, decidir si aplicar evidencia a otra población; aquí, evaluar una afirmación de universalidad. |
| PSY-157 | PSY-036 (pasada 1) | Allí, baremos e interpretación de puntuaciones; aquí, un resumen estadístico frente a una hipótesis sustantiva sobre su causa. |
| PSY-158 | PSY-088 (pasada 3), PSY-161 (esta pasada) | Allí, diseñar una prueba falsadora e inmunización clínica; aquí, la narración adaptativa construida a posteriori. |
| PSY-159 | PSY-152, PSY-153 (esta pasada), PSY-072 (pasada 2) | Allí, registro y circularidad; aquí, el espacio de especificaciones defendibles. |
| PSY-160 | PSY-139 (esta pasada) | Allí, defender la aleatorización; aquí, clasificar cada objeción según la inferencia que amenaza. |
| PSY-161 | PSY-076 (pasada 3), PSY-158 (esta pasada) | Allí, circularidad definicional; aquí, uso asimétrico de un supuesto auxiliar legítimo. |
| PSY-162 | PSY-092, PSY-084 (pasada 3) | Allí, efecto común y condiciones de la práctica; aquí, la inversión entre dos proporciones condicionales. |
| PSY-163 | PSY-042 (pasada 1), PSY-132, PSY-134 (pasada 4) | Allí, categorías ya establecidas; aquí, el procedimiento de construcción de una y la derivación de su prevalencia. |
| PSY-164 | PSY-095 (pasada 3), PSY-058 (pasada 2) | Allí, la tasa de error de doce contrastes; aquí, dos veredictos de significación y la potencia de la interacción. |
| PSY-165 | PSY-038 (pasada 1), PSY-094 (pasada 3), PSY-134 (pasada 4) | Allí, propiedades métricas e identidad de etiqueta; aquí, el solapamiento material de ítems entre dos escalas. |
| PSY-166 | PSY-080, PSY-092 (pasada 3) | Allí, distinguir mediación de moderación; aquí, evaluar una decisión de ajuste y su efecto sobre la conclusión. |
| PSY-167 | PSY-148 (esta pasada), PSY-072 (pasada 2) | Allí, la relevancia dada por supuesta y la comunicación de magnitudes; aquí, el descarte por magnitud. |
| PSY-168 | PSY-105 (pasada 3), PSY-156 (esta pasada) | Allí, sensibilidad y criterio, y una afirmación que sí depende de la muestra; aquí, la pertinencia de la objeción. |
| PSY-169 | PSY-085 (pasada 3) | Allí, predecir la conducta bajo un indicador; aquí, la premisa normativa no declarada. |
| PSY-170 | PSY-070 (pasada 2), PSY-122 (pasada 4), PSY-161 (esta pasada) | Allí, comunicación pública, sesgo de una literatura e inmunización; aquí, dos afirmaciones opuestas sobre un mismo resultado. |
| PSY-171 | PSY-087 (pasada 3), PSY-038 (pasada 1) | Allí, la expectativa modifica la conducta evaluada; aquí, modifica el registro de una conducta que no cambia. |
| PSY-172 | PSY-061 (pasada 2), PSY-039 (pasada 1), PSY-093 (pasada 3) | Allí, comunicar variabilidad y describir constructos; aquí, traducir un estadístico de varianza a decisiones sobre personas. |

La familia más densa del lote es la de **libertad del analista** (PSY-152, PSY-153 y PSY-159), con
tres objetos distintos: la discrepancia entre el análisis registrado y el publicado, la circularidad
entre selección y estimación dentro de un mismo análisis, y el espacio de especificaciones
igualmente defendibles. La proximidad se reconoce con `Q7 = 1` en PSY-152 y PSY-159 y se declara en
las `notes` de los tres.

### Datos numéricos y comprobaciones verificables

Diez ítems contienen cifras elegidas para que la conclusión puntuada sea comprobable y no dependa
del criterio del evaluador: la diferencia de 1,4 puntos en un rango de 0 a 63 con d = 0,17 (148);
r = -0,04 con 300.000 casos y un rango de especificaciones de -0,15 a +0,02 (159); r = 0,78 por
encima del techo que imponen las fiabilidades (153); d = 0,31 con p = 0,03 frente a d = 0,24 con
p = 0,11, estimaciones deliberadamente próximas (164); r = 0,72 entre escalas con ítems solapados
(165); el 91 % de práctica temprana entre 250 casos seleccionados por el resultado (162); el corte
en el decil superior que produce el 10 % de prevalencia (163); el 35 % de varianza explicada, que
corresponde a una correlación múltiple de ≈ 0,59 (172); el 89 % de reconocimiento subjetivo (142);
y d = 0,25 en la tarea de laboratorio (160). En ninguno se exige el cálculo formal: se puntúa la
conclusión que la cifra hace verificable.

---

## Autoevaluación de la pasada 5 (QQR v1.0)

### Gates obligatorios

Los 35 ítems pasan los ocho gates. Puntos que requerían comprobación específica:

| Gate | Ítems implicados | Resultado |
|---|---|---|
| G3 (desalineación constructo-pregunta) | PSY-147, PSY-153, PSY-166, PSY-171 | Pasan. Los cuatro podrían leerse como `reasoning` por su contenido metodológico, pero en los cuatro la tarea es evaluar una decisión ajena ya tomada y la conclusión que se extrajo de ella, no resolver un problema. La sección 7.3 incluye expresamente «limitaciones metodológicas», «problemas de medida» e «interpretación estadística» dentro de la dimensión. |
| G3 (frontera con `uncertainty`) | PSY-159, PSY-167, PSY-170 | Pasan. Los tres exigen delimitar lo que no queda establecido, pero el objeto puntuado es la evaluación de una afirmación concreta y de sus fallos, no el reparto de conclusiones ante información insuficiente. Se ha aplicado el criterio fijado en la pasada 4. |
| G5 (inferencia injustificada incrustada) | Todos | Pasan. En los 35 ítems la afirmación evaluada se atribuye a un tercero identificado y nunca se enuncia en la voz del ítem. Los datos que el enunciado da por ocurridos son resultados de estudios descritos, no conclusiones. |
| G6 (tarea clínica inapropiada) | PSY-144, PSY-151, PSY-161, PSY-163, PSY-171 | Pasan. Ninguno pide diagnosticar, evaluar ni tratar a una persona: se evalúan un argumento sobre niveles de explicación, el procedimiento de una comisión, la estructura de un razonamiento, la construcción de un instrumento y un procedimiento de codificación. En PSY-151 el desenlace se deja sin especificar y los errores críticos incluyen expresamente emitir un juicio sobre la responsabilidad del equipo. |
| G7 (dependencia cultural) | PSY-150, PSY-169 | Pasan. Los dos escenarios con contenido institucional —una encuesta sobre recursos públicos y una recomendación sobre deberes escolares— están redactados de forma genérica y no requieren conocimiento del sistema sanitario, político o educativo de ningún país. |
| G2 (ambigüedad sustantiva) | PSY-144, PSY-149, PSY-157, PSY-159, PSY-160 | Pasan. Los cinco tocan literaturas en discusión (hipótesis serotoninérgica, interpretación del nado forzado, naturaleza de *g*, efectos de las pantallas, videojuegos y agresión). En los cinco, el enunciado pide analizar la estructura de la inferencia y los criterios puntúan el argumento, de modo que la tarea está determinada aunque la literatura no lo esté. |

### Criterios de calidad

Umbral de aceptación: 16/18 (88,9 %). Ningún ítem puntúa 0 en Q1, Q2, Q3 o Q4.

| ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Total | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PSY-138 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-139 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-140 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | **17** | ACCEPT |
| PSY-141 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-142 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-143 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-144 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-145 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-146 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-147 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-148 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-149 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-150 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-151 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-152 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-153 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-154 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-155 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-156 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-157 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-158 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-159 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-160 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-161 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-162 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-163 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-164 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-165 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-166 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-167 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-168 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-169 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | N/A | 2 | **16 (sobre 16)** | ACCEPT |
| PSY-170 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |
| PSY-171 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | **18** | ACCEPT |
| PSY-172 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | **17** | ACCEPT |

Media de los 34 ítems puntuados sobre 18: **17,56 / 18**. Mínimo: 17. Ningún ítem por debajo del
umbral. PSY-169 se puntúa sobre 16 porque `Q8 = N/A` (sección 5) y alcanza **16/16**, equivalente
al 100 % y por tanto también ACCEPT.

### Matices honestos sobre las puntuaciones

Se declaran las lecturas alternativas más estrictas que un revisor conservador podría aplicar, con
su efecto sobre la decisión.

1. **Q3 = 1 en PSY-138 y PSY-140.** Puntuación deliberadamente conservadora. Los dos evalúan
   argumentos con estructura reconocible y una parte sustancial de la respuesta es recuperable por
   un modelo competente. Lo que sí discrimina en ambos es la exigencia de sostener el límite de la
   crítica —que la revisión por pares sí filtra algo, que la antigüedad tampoco es evidencia en
   contra—, pero no se les atribuye `Q3 = 2`. Con 17/18 la decisión es ACCEPT y se cumple el
   mínimo `Q3 ≥ 1` de la sección 6.
2. **Q7 = 1 en trece ítems.** Corresponde a las proximidades declaradas en la tabla anterior, que se
   reflejan en la puntuación en lugar de negarse: PSY-143 con PSY-039, PSY-146 con PSY-091, PSY-148
   con PSY-028, PSY-152 y PSY-159 con PSY-095 y entre sí, PSY-154 con PSY-060 y PSY-093, PSY-156 con
   PSY-136, PSY-161 con PSY-158, PSY-163 con PSY-132 y PSY-134, PSY-164 con PSY-095, PSY-167 con
   PSY-148, PSY-170 con PSY-070 y PSY-122, y PSY-172 con PSY-061. En todos ellos la capacidad
   evaluada es distinta y así se declara en las `notes`; con 17/18 la decisión no cambia.
3. **Lecturas conservadoras que no se han aplicado.** Un revisor estricto podría puntuar `Q7 = 1`
   también en PSY-153 por compartir con PSY-152 y PSY-159 el terreno de la flexibilidad analítica,
   en PSY-165 por la densidad de la familia de problemas de medida (038, 094, 134), en PSY-158 por
   compartir con PSY-161 el criterio de falsabilidad, y en PSY-168 por compartir con PSY-139 la
   estructura de la crítica invertida. En los cuatro casos el resultado sería 17/18 y la decisión
   seguiría siendo ACCEPT.
4. **Q6 en la frontera medium/hard.** PSY-145 y PSY-142 podrían defenderse como `hard` por el
   número de elementos que la respuesta completa debe integrar —el sesgo al alza de la estimación
   del piloto, la exigencia de distribución bimodal—, y PSY-146 y PSY-148 se sitúan también cerca
   del límite. A la inversa, PSY-164 podría leerse como `medium` una vez identificado el contraste
   pertinente. Se ha asignado la dificultad por el número de elementos independientes que la
   respuesta debe articular, criterio de la sección 6; en esos cinco casos un revisor podría
   desplazarla un nivel, lo que corresponde a `Q6 = 1` y no altera la decisión.
5. **Q2 y literaturas en discusión.** Cinco ítems tocan cuestiones no cerradas: PSY-144 (hipótesis
   serotoninérgica de la depresión), PSY-149 (interpretación de la prueba de nado forzado), PSY-157
   (naturaleza del factor general), PSY-159 (efectos del uso de pantallas) y PSY-160 (videojuegos
   violentos y agresión). En los cinco, el `expected_answer` y los criterios están redactados para
   **puntuar la estructura de la inferencia y no la toma de partido**, y en los cinco el enunciado
   pide analizar un argumento concreto y no resolver la controversia. PSY-144 lo declara
   explícitamente en su campo `source`.
6. **Q8 y verificación de fuentes.** Se puntúa `Q8 = 2` cuando la fuente citada sostiene
   directamente la afirmación del ítem. En **30 ítems** se han **omitido deliberadamente los DOI**
   por no haber podido confirmarlos en una fuente autorizada desde este entorno de ejecución, con
   la omisión anotada en el propio campo `source`; es el mismo criterio de prudencia de las pasadas
   1 a 4 y de la curación del piloto. Seis ítems citan además monografías o publicaciones sin DOI
   asignado (PSY-139, PSY-140, PSY-150, PSY-158, PSY-161 y PSY-165), lo que se hace constar en el
   propio campo. Un ítem, **PSY-169**, no cita fuente por evaluar un principio inferencial general,
   uso de `Q8 = N/A` que la sección 5 admite expresamente. **El paso de verificación de fuentes
   (sección 12 de la rúbrica) debe cerrar este punto antes de la inclusión en el dataset final**, y
   con particular atención a PSY-154, cuyas dos referencias se citan precisamente porque la segunda
   revisa a la baja las estimaciones de la primera.
7. **Separación entre generación y validación.** Se mantiene lo dicho en las pasadas anteriores:
   esta autoevaluación es el filtro previo exigido por el encargo, no un sustituto de la revisión
   humana. La advertencia es especialmente pertinente en esta dimensión, donde el generador evalúa
   la calidad de argumentos que él mismo ha construido para que fallen.

---

## Ítems descartados durante la generación (pasada 5)

| Candidato | Motivo del descarte |
|---|---|
| Testimonios seleccionados en la publicidad de un programa de bienestar | Redundancia cognitiva con PSY-108 (pasada 4), que ya cubre los límites inferenciales del testimonio y sus mecanismos. Sustituido, como tercer ítem `easy`, por el argumento de tradición y popularidad (PSY-140), cuyo objeto es colectivo y no individual. |
| La experiencia clínica acumulada como evidencia de eficacia | Mismo motivo: los mecanismos que habría que enumerar coinciden con los de PSY-108 y PSY-140. |
| Expansión conceptual de un término clínico | Solapa con PSY-131 (pasada 4), sobre el aumento de casos diagnosticados y los cambios en la detección, y con PSY-163 de esta pasada, que cubre la sobreinclusión de criterios desde el instrumento. |
| Análisis por protocolo frente a análisis por intención de tratar | Solapa con PSY-123 (pasada 4), cuyo objeto es la pérdida de comparabilidad por abandono diferencial. |
| Regresión a la media en un programa aplicado a quienes puntúan en el extremo | Solapa con PSY-065 (pasada 2); la regresión aparece además como componente en PSY-140 y PSY-145. |
| Inferencia inversa a partir de un resultado de neuroimagen | Descartado por tercera vez, por solapamiento con PSY-012 (piloto). El terreno de la neuroimagen se cubre en PSY-153 desde un problema estrictamente estadístico, trasladable a cualquier conjunto de medidas numerosas. |
| Equivalencia entre psicoterapias interpretada como igualdad de eficacia | Proximidad excesiva con PSY-014 (piloto), cuya demanda es exactamente la inferencia desde un comparador concreto a una afirmación general. |
| «Se necesitan 21 días para crear un hábito» | Redundancia **estructural** con PSY-141: idéntico patrón de cifra popular con origen empírico acotado. Un solo miembro de ese patrón por lote. |
| Conflicto de interés y fuente de financiación de un estudio | Solapa con PSY-124 (pasada 4), sobre alianza del investigador y dependencia entre estudios. |
| Muestreo no probabilístico presentado como representativo | Solapa con PSY-066 (pasada 2). El terreno de la encuesta se cubre en PSY-150 desde la formulación del ítem, que es una amenaza distinta. |
| Efecto de expectativa en un programa sin comparador activo | Solapa con PSY-125 (pasada 4), sobre identificación de los componentes activos, y con PSY-014 (piloto). |
| Truncamiento del eje en el gráfico de resultados | La demanda es de presentación visual y corresponde antes a `communication` (PSY-057). Potencial discriminativo bajo. |
| Resultado nulo con potencia insuficiente | Ya descartado en la pasada 4 por solapamiento con PSY-058 (pasada 2). Reaparece aquí como componente secundario de PSY-147 y PSY-164, no como ítem. |

Con esta pasada quedan escaladas las cinco dimensiones. El candidato pendiente anotado en pasadas
anteriores —**el sesgo retrospectivo en el análisis de un incidente**— se ha incorporado en
PSY-151. Sigue disponible para pasadas futuras **la incoherencia entre sistemas de respuesta
emocional**, descartado en la pasada 4 solo por densidad de familia. La dimensión menos escalada
del conjunto pasa a ser `knowledge`, con 20 ítems en el conjunto combinado frente a una media de
34, y es la candidata natural para la siguiente pasada.
