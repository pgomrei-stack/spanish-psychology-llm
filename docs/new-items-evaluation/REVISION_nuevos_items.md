# Revisión de los ítems nuevos (PSY-031 a PSY-172): primera pasada con la QQR v1.0

**Plantilla:** `docs/new-items-evaluation/spanish_psychology_llm_new_items_evaluation.xlsx`
**Datos:** `data/raw/new_items/new_items_questions.json` (142 ítems, sin modificar)
**Rúbrica aplicada:** `docs/question_quality_rubric.md` (QQR v1.0)
**Fecha:** 2026-09-24
**Estado:** revisión asistida por modelo completada; **pendiente de decisión humana**

---

## 0. Qué se ha hecho y qué no

Siguiendo el flujo de la sección 12 de la rúbrica, esta es la etapa **MODEL-ASSISTED QUALITY REVIEW**.
La etapa siguiente es la **HUMAN REVIEW**.

- Se han rellenado en la plantilla, para los 142 ítems, las columnas **G1-G8**, **Q1-Q9** y **Notas**,
  con el mismo formato que la revisión del piloto: `ACCEPT`/`REVISE`/`REJECT` en los gates, 0-2 en
  Q1-Q9 y `NA` en Q8 cuando el ítem declara que no requiere fuente externa.
- `Q Total`, `Q Máx.`, `Score %` y `Decisión sugerida` son las fórmulas que ya traía la plantilla
  (no se ha tocado ninguna). El libro se recalculó con LibreOffice: 568 fórmulas y 0 errores.
- **`Decisión final`, `Reviewer` y `Fecha` quedan vacías**: corresponden al revisor humano.
- **No se ha modificado ningún ítem**: ni el JSON ni las columnas de contenido de la plantilla. Las
  correcciones propuestas están en `Notas` y se resumen abajo; se aplicarán, si se aprueban, en un
  dataset curado aparte en `data/processed/`, como se hizo con el piloto.

**Limitaciones que conviene tener presentes:**

1. **Independencia.** Esta revisión la ha hecho un modelo de lenguaje, y los ítems parecen generados
   también por un modelo (a juzgar por `Generator_Notes`). La rúbrica exige que el modelo generador
   no sea la autoridad final, así que la decisión humana es imprescindible. Se recomienda que el
   revisor humano mire con especial atención los 7 `REVISE`, los ítems con Q2 = 1 y una muestra de
   los 57 ítems con puntuación perfecta.
2. **Fuentes no verificadas de forma independiente.** La política de red del entorno bloquea doi.org,
   Crossref y OpenAlex. Q8 se ha puntuado según la pertinencia de cada fuente para la afirmación que
   respalda, con los datos bibliográficos contrastados contra el conocimiento de la literatura. La
   etapa **SOURCE VERIFICATION** sigue pendiente.
3. **Q3 es una predicción.** El potencial discriminativo solo se confirmará al pasar los ítems por
   varios modelos reales (fase 2 del plan).

---

## 1. Resultado global

| Decisión sugerida | Ítems |
|---|---|
| ACCEPT | **135** |
| REVISE | **7** |
| REJECT | 0 |

- **Score % medio:** 95,8 %. **Puntuación perfecta:** 57 ítems.
- **Criterios más débiles:** Q7, no redundancia (48 ítems con 1), y Q3, potencial discriminativo
  (38 ítems con 1 y uno con 0). El resto está prácticamente en 2.
- **Por dimensión:**

| Dimensión | Ítems | ACCEPT | REVISE |
|---|---|---|---|
| knowledge | 14 | 14 | 0 |
| reasoning | 34 | 31 | 3 |
| uncertainty | 30 | 29 | 1 |
| critical_analysis | 35 | 33 | 2 |
| communication | 29 | 28 | 1 |

---

## 2. Ítems con decisión sugerida REVISE

| ID | Motivo principal | Corrección propuesta |
|---|---|---|
| **PSY-047** | **G1 = REVISE.** La respuesta esperada dice que la trayectoria más frecuente tras la adversidad es la de *recuperación* tras reacciones intensas; la fuente citada (Bonanno, 2004) sostiene que la más frecuente es la *resiliente*, distinta de la recuperación. | Separar resiliencia y recuperación en la respuesta esperada; matizar el error crítico sobre «ausencia de reacciones intensas». |
| **PSY-086** | **G1 = REVISE.** El criterio de 3 puntos exige predecir que, sin consecuencia visible, la imitación sería *menor* que con recompensa; en Bandura (1965) ambas condiciones no difirieron. | Exigir solo que la imitación sea mayor que tras la sanción. |
| **PSY-074** | **Q3 = 0** (veto de la sección 6). Ordenar r = -0,62 y r = +0,31 por su valor absoluto es trivial para cualquier LLM. | Aumentar la demanda: varianza compartida, factores que hacen que r infraestime una asociación. |
| **PSY-081** | Q2 = 1 y Q3 = 1 (14/16). La respuesta esperada atribuye la pérdida de sensibilidad a la *compresión de la varianza*; el mecanismo central es el truncamiento del cambio posible. | Corregir la explicación del mecanismo en la respuesta esperada y en el criterio de 3 puntos. |
| **PSY-108** | Q3 = 1 y Q7 = 1 (14/16). Muy próximo a PSY-111 y a PSY-024 del piloto. | Diferenciarlo de PSY-111 o conservar solo uno de los dos. |
| **PSY-140** | Q3, Q7 y Q8 = 1 (15/18). La fuente es un artículo de divulgación (Skeptical Inquirer). | Sustituir por Lilienfeld et al. (2014), *Perspectives on Psychological Science*, 9(4), 355-387; con eso pasaría a 16/18. |
| **PSY-148** | Q3, Q7 y Q8 = 1 (15/18). Es la cuarta vez que se evalúa «significación ≠ relevancia» (PSY-015 y PSY-028 del piloto, PSY-113, PSY-167). | Decidir si se conserva; si se conserva, citar Jaeschke, Singer & Guyatt (1989) para la diferencia mínima importante basada en anclas. |

## 3. ACCEPT con corrección recomendada

Estos ítems superan el umbral, pero su respuesta esperada contiene una imprecisión (Q2 = 1) que
conviene corregir antes de usarlos para puntuar respuestas de modelos, porque un evaluador que siga
la respuesta esperada podría penalizar una respuesta correcta:

| ID | Imprecisión |
|---|---|
| PSY-037 | Presenta la controlabilidad como determinante «principal» de la utilidad del afrontamiento; la hipótesis de bondad de ajuste tiene apoyo mixto. |
| PSY-092 | La condición que da para una asociación inducida positiva (sesgo de Berkson) es insuficiente: con efectos aditivos sobre la probabilidad de ser atendido la asociación sale negativa (comprobado numéricamente); hace falta una interacción supermultiplicativa. |
| PSY-107 | Exige recomendar foco interno al principiante; la literatura sobre foco atencional encuentra ventajas del foco externo también en principiantes. |
| PSY-112 | Describe como «habitual» que el efecto de los programas escolares desaparezca; la fuente citada (Durlak et al., 2011) encontró efectos reducidos pero significativos en el seguimiento. |

Ajustes menores sin efecto en la puntuación (detalle en `Notas`): PSY-080 (contraste de la mediación
con la lógica de pasos de Baron & Kenny), PSY-114 (la concordancia media entre informantes de
contextos distintos es de alrededor de 0,28, no 0,20), PSY-164 (4 frente a 16 veces más muestra para
una interacción) y PSY-171 (el diseño antes-después carece de grupo de comparación, y señalarlo no
debería penalizarse).

Fuentes que respaldan solo parte de lo que se les atribuye (Q8 = 1), con la alternativa propuesta en
`Notas`: PSY-031, PSY-046, PSY-056, PSY-059 y PSY-087.

---

## 4. Redundancia: grupos que conviene decidir (sección 9 de la rúbrica)

Ningún ítem es un duplicado (Q7 = 0), pero hay grupos en los que se repite el mismo patrón. La
decisión de conservar, fusionar o rediseñar corresponde al revisor humano:

| Grupo | Ítems | Qué se repite |
|---|---|---|
| Corregir una propuesta institucional | PSY-049, 052, 054, 060, 066, 071, 072 | Una dirección o un centro propone algo sin respaldo; explicarlo sin desautorizar y ofrecer una alternativa. |
| Persona afectada o familiar | PSY-059, 063, 069, 073 (+ PSY-027 y PSY-030 del piloto) | Corregir una creencia sin culpabilizar, sin valorar el caso y remitiendo al profesional. |
| Depresión y serotonina | PSY-059, 104, 110, 144 | Mecanismo causal, eficacia y nivel de explicación de la depresión. Se recomienda conservar como mucho dos. |
| Significación, magnitud y relevancia | PSY-113, 148, 159, 167 (+ PSY-015 y PSY-028 del piloto, PSY-072) | Significación ≠ importancia; un efecto pequeño puede valer la pena a escala. |
| Resultado nulo ≠ ausencia de efecto | PSY-058, 081, 147, 170 | La misma asimetría lógica como núcleo o como componente. |
| Artefactos que atenúan una correlación | PSY-093, 094, 106 | Restricción del rango, error de medida y agregación. |
| Condicionar sobre una variable posterior | PSY-091, 123, 166 | Ajustar o seleccionar por algo posterior a la asignación. |
| Flexibilidad analítica y selección posterior | PSY-095, 152, 153, 159, 164 | El valor p o la magnitud pierden su sentido tras seleccionar. |
| Caso único y testimonio | PSY-108, 111, 140 (+ PSY-024 del piloto) | Las mismas explicaciones alternativas de una mejoría individual. |
| Validez de constructo entre medidas | PSY-130, 134, 165 | Dos medidas «del mismo» constructo que no convergen, o dos nombres para el mismo contenido. |
| Falsabilidad | PSY-088, 158, 161 (+ PSY-170) | Hipótesis que ningún resultado puede contradecir. |
| Transferencia de la evidencia | PSY-116, 136, 137, 156 | El aval es relativo a las condiciones evaluadas; más datos del mismo tipo no amplían el rango. |
| Heredabilidad | PSY-039, 143 (+ PSY-129) | La predicción contraintuitiva de PSY-039 es el núcleo de PSY-143. |
| Tipologías y selección de personal | PSY-060, 142 (+ PSY-093, 118, 154) | El mismo test de dieciséis tipos, los mismos argumentos y la misma fuente en PSY-060 y PSY-142. |

---

## 5. Equilibrio del benchmark (sección 11 de la rúbrica)

1. **`knowledge` está infrarrepresentada.** 14 ítems nuevos (20 con el piloto curado) frente a 34-40
   en las demás dimensiones. El validador ya lo avisa. Si el objetivo es un reparto equilibrado,
   harían falta unos 15-20 ítems nuevos de conocimiento, o recortar otras dimensiones.
2. **Peso de la metodología.** Aproximadamente 60 de los 142 ítems (≈40 %, clasificación orientativa)
   tratan sobre todo de diseño de investigación y estadística más que de contenido psicológico: casi
   todos los de `critical_analysis` y buena parte de `uncertainty` y `reasoning`. Son ítems de alta
   calidad, pero la sección 11 pide que el benchmark no quede dominado por un tipo de evidencia ni
   por un subcampo. Conviene decidir qué proporción se quiere.
3. **Dificultad.** 84 `hard`, 44 `medium`, 14 `easy`. Q6 no señala desajustes relevantes (solo
   PSY-040, por coherencia con PSY-004).
4. **Frontera entre dimensiones.** PSY-075 (`reasoning`) tiene la estructura «qué permite y qué no
   permite concluir» que la sección 7.4 asigna a `uncertainty` (Q1 = 1). Es el mismo `RUBRIC_ISSUE`
   que el revisor señaló en PSY-009 del piloto: la frontera entre `reasoning`, `uncertainty` y
   `critical_analysis` sigue sin estar operativizada en la rúbrica.

## 6. Nota de forma para la curación

En 80 ítems (de PSY-077 en adelante) el campo `source` incluye notas de proceso del tipo «Se omite el
DOI por no haber podido verificarlo desde este entorno». No afectan a la puntuación, pero en el
dataset curado conviene moverlas a `notes`, y completar los DOI durante la verificación de fuentes.

## 7. Siguientes pasos

1. **Revisor humano:** rellenar `Decisión final` (y `Reviewer`/`Fecha`) en la plantilla, empezando
   por los 7 `REVISE` y los 4 ítems de la sección 3.
2. **Decidir los grupos de redundancia** de la sección 4 y el reparto por dimensiones de la sección 5.
3. **Verificación de fuentes** (etapa SOURCE VERIFICATION), idealmente desde un entorno con acceso a
   doi.org o Crossref.
4. **Curación:** con las decisiones cerradas, generar `data/processed/` con los ítems aceptados y las
   correcciones aplicadas, y su changelog, como se hizo con el piloto.
