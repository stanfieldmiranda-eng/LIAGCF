# LIAGCF AI System Lifecycle Phases

The LIAGCF organizes governance controls across seven AI system lifecycle phases. This structure reflects published AI lifecycle models that have converged on a seven-phase governance framework, differing fundamentally from traditional software lifecycle models by accounting for AI systems' distinctive properties: data dependencies, continuous learning, probabilistic outputs, and performance degradation over time.

Each phase has distinct governance requirements. A uniform control set applied across all phases imposes disproportionate burden on low-risk phases while leaving critical transition points — particularly development-to-deployment and operations-to-retirement — exposed to governance gaps.

---

## Phase 1: Strategy and Design

**Governance focus:** Establishing the organizational infrastructure that must exist before any AI system is acquired, designed, or deployed.

Controls anchored here establish the governance authority, policy scope, accountability structures, risk categorization criteria, and decision rights that all downstream controls depend on. This is where the AI RACI matrix is defined, where the enterprise AI governance policy is scoped, and where AI systems are categorized by risk level and affected population.

**LIAGCF controls anchored here:** A-1, A-2, A-6

**Why this phase matters:** Governance structures established at Strategy and Design are preconditions for enforcement, not parallel activities. Administrative controls here set the accountability and policy foundation without which technical and operational controls cannot be meaningfully enforced.

---

## Phase 2: Data Preparation

**Governance focus:** Training data sourcing, provenance, lineage quality, and access control.

Data governance failures at this phase — unverified provenance, missing lineage documentation, inadequate quality controls, unrestricted access to training datasets — introduce governance risk that cannot be remediated after model training is complete. This phase is frequently overlooked in comparable frameworks despite being a foundational source of downstream AI risk.

**LIAGCF controls anchored here:** T-2, O-2 (shared with Operations)

**Why this phase matters:** Data quality and provenance issues affect nearly everything downstream. Governing data at its source is structurally different from, and more effective than, attempting to detect data-derived failures after model training or deployment.

---

## Phase 3: Development

**Governance focus:** Pre-deployment risk assessment, bias and disparate impact evaluation, and model validation.

This phase addresses the governance activities that must occur before a model transitions to production. Risk assessments must be completed. Bias and fairness evaluations must be documented. Model validation must establish that the system meets organizational requirements before authorization to deploy.

**LIAGCF controls anchored here:** A-5, T-1, T-3

**Why this phase matters:** Development is the last point at which governance findings can redirect or halt deployment. Controls here create the pre-deployment authorization checkpoint that separates a governed deployment from an ungoverned one.

---

## Phase 4: Procurement

**Governance focus:** Third-party AI vendor assessment, supply chain risk governance, and contractual obligations.

Procurement addresses the governance requirements for AI systems and components acquired from external vendors — a significant and growing portion of enterprise AI deployments. When organizations consume third-party AI, they inherit supply chain risks that require explicit governance structures, not assumptions that vendors have addressed them.

**LIAGCF controls anchored here:** A-3

**Why this phase matters:** Procurement governance is consistently absent from comparable AI governance frameworks despite the prevalence of third-party AI adoption. The LIAGCF treats Procurement as a first-class lifecycle phase with explicit control requirements aligned to SP 800-53's SR and SA families.

---

## Phase 5: Deployment

**Governance focus:** Production release authorization, readiness review, and deployment controls.

Deployment is one of the highest-risk transition points for AI systems, particularly when outputs begin affecting real users, business decisions, or regulated processes. Controls here ensure that deployment authorization is conditioned on completed risk assessment, documented validation, and defined rollback criteria.

**Note:** Expert assessment identified Deployment phase governance as underrepresented in the current 16-control framework. Additional controls for deployment authorization, production readiness review, and rollback criteria are identified as development priorities for future iterations.

**LIAGCF controls anchored here:** (Deployment authorization is addressed through A-5 pre-deployment assessment; dedicated Deployment-phase controls are a future iteration priority)

---

## Phase 6: Operations

**Governance focus:** Continuous monitoring, drift detection, access control, incident response, audit cadence, and model integrity protection.

Operations is the most control-dense phase in the LIAGCF because deployed AI systems require ongoing governance, not one-time authorization. Model performance degrades. Input distributions shift. Bias and fairness risks that were evaluated at Development persist and evolve through the operational lifecycle. Incident response playbooks must be maintained and exercised.

**LIAGCF controls anchored here:** A-4, T-4, T-5, O-1, O-2 (shared with Data Preparation), O-3, O-4

**Why this phase matters:** Post-deployment governance is where most AI governance programs fail. Controls here address the continuous monitoring, change management, access enforcement, and incident response capabilities that distinguish an active governance program from a compliance documentation exercise.

---

## Phase 7: Retirement and Decommissioning

**Governance focus:** Secure model disposal, training data deletion, access revocation, and audit documentation.

Retirement is the most systematically underspecified phase in comparable AI governance frameworks. Retired AI systems generate residual risks — unrevoked model access, persistent data exposure, residual inference capabilities, incomplete audit trails — that existing frameworks do not account for. The LIAGCF treats Retirement as a fully specified lifecycle phase with explicit control requirements.

**LIAGCF controls anchored here:** O-5

**Why this phase matters:** "AI debris" — the residual risk and afterlife of retired AI systems — is a documented governance failure category (Frimpong, 2026). The SP 800-53 MP (Media Protection) family is the only control family that directly addresses secure disposal of model artifacts and training data. This assignment is unique among comparable frameworks.

---

## Notes

The seven-phase structure reflects the convergence of published AI lifecycle models between 2022 and 2026. The inclusion of Procurement and Retirement as first-class phases with explicit control requirements distinguishes the LIAGCF from frameworks that address only development and operations.

Expert panel validation confirmed the seven-phase structure as comprehensive (7 of 10 respondents). Data Preparation, Procurement, and Retirement were specifically recognized as phases that comparable frameworks consistently underrepresent.

Full citation: Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.* DOI: `10.5281/zenodo.19553772` (copy and paste into browser address bar)
