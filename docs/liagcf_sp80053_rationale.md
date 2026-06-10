# SP 800-53 Control Family Selection Rationale

This document provides the design rationale for every SP 800-53 control family assignment in the LIAGCF. It corresponds to Appendix E of the published paper.

Each assignment answers: *why this family, for this control objective, at this lifecycle phase?*

---

## Administrative Controls — GOVERN Function

### A-1: Establish a formal enterprise AI governance policy and scope
**Assigned families: PM (Program Management), PL (Planning)**

PM establishes the organizational infrastructure — program structure, roles, and accountability — required to sustain AI governance as an enterprise function. PL provides the planning framework that translates governance intent into documented policies, acceptable use definitions, and scope boundaries. Together, PM and PL operationalize the GOVERN function's requirement to establish organizational accountability and governance authority before any AI system is acquired or deployed.

### A-2: Define AI accountability, decision rights, and risk ownership
**Assigned family: PM (Program Management)**

PM directly governs the organizational roles, responsibilities, and decision authorities required to assign AI risk ownership and define escalation pathways. PM controls establish senior leadership accountability, designating program officials, and creating oversight structures — each of which is necessary for AI risk governance to be institutionally enforceable rather than advisory. No other SP 800-53 control family addresses organizational accountability structures at the program level.

### A-3: Establish third-party AI risk governance policies
**Assigned families: SR (Supply Chain Risk Management), SA (System & Services Acquisition)**

SR addresses risks introduced through external AI components, vendor relationships, and supply chain dependencies — the primary third-party risk domain for AI procurement. SR controls establish due diligence requirements, supplier assessment processes, and contractual governance obligations. SA complements SR by governing acquisition processes and vendor evaluation criteria, ensuring that third-party AI components meet organizational governance requirements before procurement. SP 800-53 Rev. 5 introduced SR as a distinct control family specifically because supply chain risks had become a critical, underaddressed governance domain.

### A-4: Define enterprise AI audit and governance review cadence
**Assigned families: CA (Assessment, Authorization & Monitoring), PM (Program Management)**

CA governs the formal assessment and authorization processes through which AI systems are reviewed against established governance criteria at defined intervals. CA controls establish audit schedules, ongoing authorization requirements, and continuous monitoring obligations. PM provides the program-level oversight framework that ensures review activities are resourced, scheduled, and reported within the enterprise governance architecture. Together, CA and PM establish the institutionalized oversight rhythm that distinguishes a governance program from ad hoc compliance activity.

---

## Administrative Controls — MAP Function

### A-5: Require AI risk assessments prior to deployment
**Assigned families: RA (Risk Assessment), CA (Assessment, Authorization & Monitoring)**

RA directly governs the risk assessment process, establishing the methods, criteria, and documentation requirements for identifying and evaluating risk before system deployment. CA provides the authorization gate that ensures risk assessment findings are formally reviewed and that deployment authorization is conditioned on acceptable risk posture. The combination of RA and CA creates a structured pre-deployment governance checkpoint aligned with the MAP function.

### A-6: Categorize AI systems by risk level, use context, and affected population
**Assigned families: RA (Risk Assessment), PL (Planning)**

RA governs risk categorization processes, requiring organizations to classify systems according to potential impact and risk profile. AI system categorization requires the same risk-based assessment framework that RA controls establish — identifying the sensitivity of data processed, the criticality of decisions supported, and the populations affected. PL provides the planning structure within which categorization decisions are documented and reflected in governance policies and acceptable use definitions. Categorization at the Strategy phase, before system acquisition or development, is the MAP function's foundational risk contextualization activity.

---

## Technical Controls — MAP Function

### T-1: Identify and assess potential for discriminatory or disparate impact outcomes
**Assigned families: RA (Risk Assessment), SI (System & Information Integrity)**

RA governs the identification and evaluation of risks — including algorithmic bias and disparate impact — as a systematic assessment activity. Bias risk assessment is structurally a risk identification exercise: it requires analyzing potential impacts on affected populations, documenting findings, and informing risk treatment decisions. SI governs system integrity, including the integrity of model outputs and the mechanisms needed to detect and respond to integrity failures such as biased predictions. SI controls support the technical implementation of bias testing mechanisms that generate the evidence required for RA-based assessment.

**Expert-recommended expansion (future iteration):** Add PT (Personally Identifiable Information Processing and Transparency). Affected populations are frequently defined by personal data used in training or inferencing; PT's transparency and data processing governance controls are directly relevant to bias risk governance.

### T-2: Map data provenance, lineage, and quality risks for training datasets
**Assigned families: SA (System & Services Acquisition), SR (Supply Chain Risk Management)**

SA governs the acquisition of data and system components, establishing requirements for documentation, quality standards, and vendor obligations that apply directly to training dataset sourcing. Training data often originates from third-party sources, making SR directly applicable: SR controls govern provenance verification, integrity assurance, and supply chain documentation requirements for external data components. Together, SA and SR address the full scope of training data risk at the Data Preparation phase, where provenance and quality failures introduce governance risk that cannot be remediated after model training is complete.

---

## Technical Controls — MEASURE Function

### T-3: Validate AI models prior to production release
**Assigned families: CA (Assessment, Authorization & Monitoring), SA (System & Services Acquisition)**

CA governs the formal assessment and authorization process, including testing and evaluation activities that determine whether a system meets established requirements before production release. Model validation is structurally an authorization activity: it generates the evidence required to make a deployment authorization decision. SA governs system development and acquisition requirements, establishing the validation and testing criteria that models must satisfy before organizational acceptance. The CA-SA combination mirrors the MEASURE function's requirement to analyze and assess AI risk through systematic evaluation before deployment.

### T-4: Monitor model performance and detect drift
**Assigned families: SI (System & Information Integrity), CA (Assessment, Authorization & Monitoring)**

SI governs the mechanisms for detecting unauthorized changes, anomalies, and integrity failures — including the performance degradation and distributional drift that characterize AI model decay in production. CA provides the ongoing authorization and continuous monitoring framework within which drift detection findings are assessed against governance thresholds and trigger re-authorization or remediation requirements. Together, SI and CA address the MEASURE function's continuous assessment obligation for deployed AI systems.

### T-5: Log AI system activity for traceability and auditability
**Assigned family: AU (Audit & Accountability)**

AU is the SP 800-53 control family specifically designed to govern audit logging, log integrity, and the accountability mechanisms that make system activity traceable and reviewable. AU controls require organizations to capture sufficient event data to reconstruct AI system decisions and actions, protect log integrity, and retain audit records for defined periods. For AI systems, AU-based logging directly supports the MEASURE function's requirement to generate evidence of system behavior that can be independently verified. No other SP 800-53 control family addresses auditability and decision traceability as its primary purpose.

---

## Operational Controls — MEASURE Function

### O-1: Conduct periodic AI governance and risk reviews
**Assigned families: CA (Assessment, Authorization & Monitoring), RA (Risk Assessment)**

CA governs the ongoing assessment, authorization, and monitoring processes that constitute periodic governance review — the structured activities through which organizations evaluate whether deployed AI systems continue to operate within accepted risk parameters. RA provides the risk assessment methodology that drives the substantive content of periodic reviews, requiring organizations to reassess risk profiles, update risk registers, and validate that risk treatment decisions remain appropriate. The CA-RA combination operationalizes the MEASURE function's requirement to continuously evaluate AI system risk through systematic, documented review cycles.

---

## Operational Controls — MANAGE Function

### O-2: Enforce access controls on AI training and operational data
**Assigned families: AC (Access Control), IA (Identification & Authentication)**

AC governs the authorization and enforcement of access rights to information and systems — the direct mechanism for restricting who can read, modify, or delete AI training datasets and operational model components. AC controls require organizations to define least-privilege access policies and enforce separation of duties, which are essential protections for AI data integrity. IA establishes the identity verification mechanisms that ensure access control decisions are applied to correctly identified principals. Together, AC and IA address the MANAGE function's requirement to operationally enforce governance policies through runtime access restrictions.

### O-3: Protect AI models from unauthorized modification
**Assigned families: CM (Configuration Management), SI (System & Information Integrity)**

CM governs the formal change control processes that prevent unauthorized modifications to systems, configurations, and software components — including AI model artifacts, weights, and pipeline code. CM controls require organizations to maintain configuration baselines, document authorized changes, and review change requests against governance criteria before implementation. SI provides the integrity monitoring mechanisms that detect unauthorized modifications and alert governance functions. The CM-SI combination creates a two-layer protection architecture: CM prevents unauthorized changes through process controls, while SI detects them through technical monitoring.

### O-4: Execute AI incident response playbooks
**Assigned families: IR (Incident Response), SI (System & Information Integrity)**

IR governs the organizational processes for detecting, responding to, and recovering from security and operational incidents — the control family most directly applicable to AI system failures, misuse events, and governance breaches. IR controls require organizations to maintain incident response plans, train response personnel, and execute documented playbooks when incidents occur. SI provides the monitoring and integrity checking mechanisms that generate the alerts and anomaly signals that trigger incident response. Together, IR and SI address the MANAGE function's requirement to actively respond to and manage AI risks as they materialize in production environments.

### O-5: Retire AI systems exceeding defined risk tolerance
**Assigned families: SA (System & Services Acquisition), CM (Configuration Management), MP (Media Protection)**

SA governs system decommissioning and the formal processes through which systems are removed from authorized operation — the acquisition lifecycle control that covers retirement decisions and closure documentation. CM governs the configuration management activities required at retirement: removing system components from baselines, revoking change control records, and documenting final system states. MP governs the secure handling, sanitization, and disposal of media containing AI model artifacts, training data, and operational records — addressing the residual risk that Frimpong (2026) identifies as "AI debris." The SA-CM-MP combination is the only control family grouping that collectively addresses the governance, documentation, and secure disposal obligations of the Retirement lifecycle phase.

**Expert-recommended expansion (future iteration):** Add AU (Audit & Accountability) to support audit trail requirements for demonstrating compliant decommissioning.

---

## Notes

This rationale was developed as part of the DSR artifact design process and reviewed through structured expert assessment (N=10). Expert panel recommendations for future iterations are noted inline above.

Full citation: Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.* DOI: `10.5281/zenodo.19553772` (copy and paste into browser address bar)
