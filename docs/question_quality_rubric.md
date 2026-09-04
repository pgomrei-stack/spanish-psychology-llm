\# Question Quality Rubric v1.0



\*\*Project:\*\* spanish-psychology-llm  

\*\*Version:\*\* 1.0  

\*\*Status:\*\* Frozen for pilot evaluation  

\*\*Language:\*\* Spanish (`es-ES`)  

\*\*Domain:\*\* Psychology  

\*\*Last updated:\*\* 2026-09-04



\---



\## 1. Purpose



The Question Quality Rubric (QQR) defines the methodological criteria used to evaluate questions proposed for the Spanish Psychology LLM Benchmark.



Its purpose is to ensure that benchmark items:



\- measure the intended psychological capability;

\- are scientifically correct;

\- are sufficiently discriminative between LLM performance levels;

\- can be evaluated reproducibly;

\- have appropriate difficulty;

\- avoid unintended ambiguity;

\- are not unnecessarily redundant;

\- use appropriate scientific sources when required;

\- are linguistically appropriate for Spanish (`es-ES`);

\- comply with the methodological constraints of the benchmark.



The QQR is applied during item validation, after question generation and before inclusion in the final benchmark dataset.



\---



\# 2. Evaluation philosophy



The benchmark is not intended to measure only factual recall.



Questions should collectively evaluate different capabilities, including:



1\. psychological knowledge;

2\. psychological reasoning;

3\. critical analysis of claims and evidence;

4\. reasoning under uncertainty;

5\. scientific communication.



The quality of an item therefore depends not only on whether its expected answer is scientifically correct, but also on whether the item provides a meaningful test of the intended capability.



\---



\# 3. Evaluation procedure



Each candidate question must pass two stages:



1\. \*\*Mandatory rejection gates\*\*

2\. \*\*Quality scoring\*\*



An item that fails a mandatory gate cannot be accepted regardless of its numerical score.



Items that pass all gates are scored using nine quality criteria, each from 0 to 2 points.



Maximum score:



\*\*18 points\*\*



\---



\# 4. Mandatory rejection gates



\## G1. Scientific error



Reject the item if the question, expected answer, evaluation criteria, or source contains a relevant factual or conceptual error.



Examples:



\- incorrect definition of a psychological construct;

\- unsupported causal claim presented as established fact;

\- incorrect interpretation of a statistical concept.



\---



\## G2. Substantive ambiguity



Reject the item if two or more substantially different interpretations of the question are reasonably possible and could lead to different valid answers.



Open-ended questions may have multiple valid formulations. This is not itself a problem.



The problem is ambiguity about what the question is actually asking.



\---



\## G3. Construct-question misalignment



Reject the item if the question does not primarily measure the declared benchmark dimension.



For example, an item labelled `reasoning` that merely asks the model to define a psychological concept is primarily a knowledge item.



\---



\## G4. Non-evaluable expected answer



Reject the item if it is not possible to establish sufficiently objective criteria for determining whether an answer is correct, partially correct, or incorrect.



\---



\## G5. Unjustified inference embedded in the item



Reject or redesign the item if the question assumes a conclusion that the evidence presented does not justify.



This gate is particularly important for `critical\_analysis` and `uncertainty` items.



\---



\## G6. Inappropriate clinical task



Reject the item if its primary purpose is:



\- diagnosing an individual;

\- recommending a personalized treatment;

\- making a personalized clinical assessment.



Clinical psychology may be evaluated when the task concerns psychological concepts, evidence, reasoning, limitations, or communication.



\---



\## G7. Unintended cultural dependence



Reject the item if successful completion depends primarily on knowledge of a specific Spanish cultural characteristic that is not relevant to the psychological construct being evaluated.



\---



\## G8. Technical or schema failure



Reject the item if it does not comply with the benchmark data schema or contains structural information incompatible with the dataset.



\---



\# 5. Quality scoring criteria



Items that pass all rejection gates are evaluated on nine criteria.



Each criterion receives:



\- \*\*0 = deficient\*\*

\- \*\*1 = acceptable but improvable\*\*

\- \*\*2 = excellent\*\*



Maximum score: \*\*18 points\*\*.



\---



\## Q1. Construct validity



\### Question



Does the item actually measure the psychological capability represented by its declared dimension?



\### 2 points



The relationship between the item and the intended dimension is direct and clear.



\### 1 point



The intended dimension is present, but the item also contains substantial contamination from another capability.



\### 0 points



The item primarily measures another capability.



\---



\## Q2. Scientific accuracy



\### Question



Are the question, expected answer, evaluation criteria, and supporting evidence scientifically accurate?



\### 2 points



The item is conceptually precise and consistent with established scientific evidence.



\### 1 point



The item is broadly correct but contains a minor simplification or imprecision that does not substantially affect the task.



\### 0 points



The item contains a relevant scientific or conceptual error.



A score of 0 on Q2 normally requires rejection or substantial redesign.



\---



\## Q3. Discriminative potential



\### Question



Is the item likely to distinguish between LLMs with different levels of psychological competence?



\### 2 points



The item requires meaningful reasoning, integration, evaluation, uncertainty management, conceptual distinction, or another capability that weaker models are plausibly likely to perform less reliably.



\### 1 point



The item has some discriminative value but can largely be solved through straightforward knowledge retrieval.



\### 0 points



The item is trivial for essentially any competent modern LLM.



\---



\## Q4. Evaluability



\### Question



Can model responses be scored in a sufficiently reproducible way?



\### 2 points



The response can be evaluated using explicit, observable criteria.



\### 1 point



Evaluation is possible but leaves some meaningful subjective judgement.



\### 0 points



Evaluation depends predominantly on subjective judgement.



Whenever possible, evaluation criteria should be expressed as atomic conceptual elements.



\---



\## Q5. Clarity and lack of ambiguity



\### Question



Does the wording communicate precisely what the model is expected to do?



\### 2 points



The task is clear and contains no relevant ambiguity.



\### 1 point



There is a minor wording issue that does not materially affect evaluation.



\### 0 points



The wording creates substantial uncertainty about the intended task.



\---



\## Q6. Difficulty appropriateness



\### Question



Does the assigned difficulty correspond to the actual cognitive demand of the item?



\### Easy



Primarily requires:



\- recall;

\- identification;

\- straightforward definition;

\- simple recognition.



\### Medium



Primarily requires:



\- application;

\- comparison;

\- interpretation;

\- explanation;

\- integration of a limited number of concepts.



\### Hard



Requires one or more of:



\- evaluation of evidence;

\- integration of multiple concepts;

\- identification of assumptions;

\- comparison of competing explanations;

\- reasoning under uncertainty;

\- methodological critique;

\- interpretation of conflicting evidence.



Difficulty must be based primarily on cognitive demand, not vocabulary complexity or unnecessarily complicated wording.



\### Scoring



\*\*2 points:\*\* assigned difficulty accurately reflects the item's cognitive demand.



\*\*1 point:\*\* difficulty is plausible but could reasonably be one level higher or lower.



\*\*0 points:\*\* difficulty label is clearly inconsistent with the cognitive demands of the task.



\---



\## Q7. Non-redundancy



\### Question



Does the item provide sufficiently distinct value compared with other benchmark items?



Redundancy should be evaluated at three levels:



\### A. Thematic redundancy



Does the item concern essentially the same psychological phenomenon?



\### B. Cognitive redundancy



Does it require essentially the same reasoning process?



\### C. Structural redundancy



Is it simply another instance of the same question pattern with a different context?



\### 2 points



The item contributes clearly distinct content or cognitive demand.



\### 1 point



There is some overlap but the item adds a useful additional perspective.



\### 0 points



The item is substantially redundant with an existing item.



\---



\## Q8. Source quality



This criterion applies when the item requires an external scientific source.



\### 2 points



The source is:



\- a primary research article;

\- systematic review;

\- meta-analysis;

\- major scholarly review;

\- or another high-quality academic source



and directly supports the relevant claim.



\### 1 point



The source is academically reasonable but indirect, outdated, or less appropriate than a stronger available source.



\### 0 points



The source is incorrect, unverifiable, or does not support the claim it is cited for.



\### N/A



N/A may be used when the item evaluates a general methodological reasoning principle or an original scenario that does not require a specific external citation.



Sources must not be added merely to create an appearance of scientific rigor.



\---



\## Q9. Linguistic appropriateness



\### Question



Does the item use appropriate Spanish (`es-ES`) without introducing unnecessary linguistic difficulty?



\### 2 points



The Spanish is natural, precise, accessible, and appropriate for the intended audience.



\### 1 point



There are minor stylistic or terminology issues that do not materially affect comprehension.



\### 0 points



The difficulty of the item is substantially caused by confusing, unnatural, excessively complex, or unnecessarily technical wording.



For `communication` items, linguistic adaptation is itself part of the construct and should therefore be evaluated accordingly.



\---



\# 6. Acceptance thresholds



After passing all mandatory rejection gates:



| Score | Decision |

|---|---|

| 16–18 | ACCEPT |

| 14–15 | REVISE |

| 11–13 | MAJOR REVISION |

| 0–10 | REJECT |



Additional rule:



An item cannot receive `ACCEPT` if it scores \*\*0\*\* on any of the following essential criteria:



\- Q1 Construct validity

\- Q2 Scientific accuracy

\- Q3 Discriminative potential

\- Q4 Evaluability



\---



\# 7. Dimension-specific requirements



\## 7.1 Knowledge



Knowledge items should evaluate genuine psychological knowledge.



The benchmark should not be dominated by simple textbook definitions.



Knowledge items should include, where appropriate:



\- conceptual distinctions;

\- precise definitions;

\- relationships between constructs;

\- interpretation of established findings;

\- knowledge that cannot be reduced to superficial keyword matching.



\---



\## 7.2 Reasoning



Reasoning items must contain an actual reasoning problem.



A reasoning item should require the model to transform information into a justified conclusion rather than merely reproduce a definition.



Typical structure:



\*\*information → application of psychological concept → justified conclusion\*\*



\---



\## 7.3 Critical analysis



Critical-analysis items should provide a claim, argument, study, result, or interpretation that can be evaluated.



Relevant analytical dimensions may include:



\- overgeneralization;

\- causal overinterpretation;

\- methodological limitations;

\- alternative explanations;

\- sample limitations;

\- measurement problems;

\- statistical interpretation;

\- publication bias;

\- external validity;

\- replicability;

\- unsupported assumptions.



\---



\## 7.4 Uncertainty



Uncertainty items should contain situations where the available information does not justify a strong conclusion.



A high-quality response should not merely state:



> "No se puede saber."



It should identify:



1\. what can reasonably be concluded;

2\. what cannot reasonably be concluded;

3\. why the evidence is insufficient;

4\. plausible alternative explanations;

5\. what additional evidence would reduce the uncertainty.



\---



\## 7.5 Communication



Communication items must specify an intended audience whenever appropriate.



Evaluation should consider:



\- scientific accuracy;

\- clarity;

\- adaptation to the audience;

\- appropriate terminology;

\- avoidance of unnecessary jargon;

\- useful examples;

\- preservation of important scientific nuance;

\- responsible communication of uncertainty.



A response should not receive a high score merely because it sounds fluent or persuasive.



\---



\# 8. Expected-answer design



The `expected\_answer` field represents the conceptual content expected in a strong answer.



It is not intended to define one unique textual response.



Different formulations may be equally correct.



Whenever possible, evaluation criteria should therefore be expressed as atomic conceptual elements.



Example:



Instead of:



> 3 = excellent answer



prefer:



\- identifies that correlation does not establish causality;

\- identifies at least one plausible alternative explanation;

\- explains why that alternative limits causal inference;

\- identifies an appropriate design or additional evidence.



This structure improves scoring reproducibility.



\---



\# 9. Redundancy control



Before accepting a new item, it should be compared with existing benchmark items.



Particular attention should be paid to repeated reasoning patterns.



For example, several items may concern correlation and causality, but they should not all require the same inference:



> "A correlación con B. ¿Puede concluirse que A causa B?"



Different causal-inference items are justified only when they test meaningfully different capabilities, contexts, evidence structures, or reasoning demands.



\---



\# 10. Difficulty control



Difficulty must not be increased artificially through:



\- unnecessarily complex syntax;

\- obscure vocabulary;

\- excessive question length;

\- irrelevant information;

\- ambiguous wording.



The preferred method for increasing difficulty is to increase the cognitive demand.



Examples:



\### Lower difficulty



Define a psychological concept.



\### Moderate difficulty



Apply the concept to a concrete scenario.



\### Higher difficulty



Evaluate competing explanations using incomplete or potentially conflicting evidence.



\---



\# 11. Benchmark balance



The final benchmark should contain a diverse set of cognitive demands.



It should not be dominated by:



\- simple factual recall;

\- correlation-versus-causality questions;

\- one psychological subfield;

\- one question structure;

\- one type of evidence;

\- one style of answer.



The benchmark should include sufficient diversity across psychological domains and reasoning structures.



\---



\# 12. Human and model evaluation



Question generation and question validation must remain conceptually separate.



The generation model must not be considered the final authority on the validity of its own questions.



Recommended workflow:



```text

QUESTION GENERATION

&#x20;       ↓

AUTOMATED STRUCTURAL CHECKS

&#x20;       ↓

MODEL-ASSISTED QUALITY REVIEW

&#x20;       ↓

HUMAN REVIEW

&#x20;       ↓

SOURCE VERIFICATION

&#x20;       ↓

FINAL DATASET

