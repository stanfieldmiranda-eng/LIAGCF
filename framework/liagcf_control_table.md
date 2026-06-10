# LIAGCF Control Table

**Lifecycle-Integrated AI Governance Control Framework — Table A1**

Control-based AI lifecycle mapping of governance control categories to NIST AI RMF functions and NIST SP 800-53 control families.

Published in: Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.* DOI: [10.5281/zenodo.19553772](https://doi.org/10.5281/zenodo.19553772)

---

## Administrative Controls — GOVERN and MAP Functions

| # | Control Category | Control Objective | AI RMF Function | SP 800-53 Control Family | AI Lifecycle Phase | Example Governance Artifacts |
|---|-----------------|-------------------|-----------------|--------------------------|-------------------|------------------------------|
| A-1 | Administrative | Establish a formal enterprise AI governance policy and scope | GOVERN | PM (Program Management), PL (Planning) | Strategy & Design | AI Governance Charter; Enterprise AI Policy |
| A-2 | Administrative | Define AI accountability, decision rights, and risk ownership | GOVERN | PM (Program Management) | Strategy & Design | AI RACI Matrix; Governance Role Definitions |
| A-3 | Administrative | Establish third-party AI risk governance policies | GOVERN | SR (Supply Chain Risk Management), SA (System & Services Acquisition) | Procurement | Vendor AI Risk Review Checklist; Third-Party Risk Policy |
| A-4 | Administrative | Define enterprise AI audit and governance review cadence | GOVERN | CA (Assessment, Authorization & Monitoring), PM (Program Management) | Operations | AI Governance Review Plan; Audit Schedule |
| A-5 | Administrative | Require AI risk assessments prior to deployment | MAP | RA (Risk Assessment), CA (Assessment, Authorization & Monitoring) | Development | AI Risk Assessment Report; Risk Register Entry |
| A-6 | Administrative | Categorize AI systems by risk level, use context, and affected population | MAP | RA (Risk Assessment), PL (Planning) | Strategy & Design | AI System Inventory; Risk Categorization Register |

---

## Technical Controls — MAP and MEASURE Functions

| # | Control Category | Control Objective | AI RMF Function | SP 800-53 Control Family | AI Lifecycle Phase | Example Governance Artifacts |
|---|-----------------|-------------------|-----------------|--------------------------|-------------------|------------------------------|
| T-1 | Technical | Identify and assess potential for discriminatory or disparate impact outcomes | MAP | RA (Risk Assessment), SI (System & Information Integrity) | Development | Bias Risk Assessment; Fairness Evaluation Report |
| T-2 | Technical | Map data provenance, lineage, and quality risks for training datasets | MAP | SA (System & Services Acquisition), SR (Supply Chain Risk Management) | Data Preparation | Data Lineage Map; Training Data Quality Report |
| T-3 | Technical | Validate AI models prior to production release | MEASURE | CA (Assessment, Authorization & Monitoring), SA (System & Services Acquisition) | Development | Model Validation Report; Testing Summary |
| T-4 | Technical | Monitor model performance and detect drift | MEASURE | SI (System & Information Integrity), CA (Assessment, Authorization & Monitoring) | Operations | Drift Monitoring Dashboard; Performance Metrics Report |
| T-5 | Technical | Log AI system activity for traceability and auditability | MEASURE | AU (Audit & Accountability) | Operations | Audit Logs; Monitoring Dashboard |

---

## Operational Controls — MEASURE and MANAGE Functions

| # | Control Category | Control Objective | AI RMF Function | SP 800-53 Control Family | AI Lifecycle Phase | Example Governance Artifacts |
|---|-----------------|-------------------|-----------------|--------------------------|-------------------|------------------------------|
| O-1 | Operational | Conduct periodic AI governance and risk reviews | MEASURE | CA (Assessment, Authorization & Monitoring), RA (Risk Assessment) | Operations | Governance Review Report; Risk Reassessment Summary |
| O-2 | Operational | Enforce access controls on AI training and operational data | MANAGE | AC (Access Control), IA (Identification & Authentication) | Data Preparation / Operations | Access Control Matrix; Privileged Access Review |
| O-3 | Operational | Protect AI models from unauthorized modification | MANAGE | CM (Configuration Management), SI (System & Information Integrity) | Operations | Configuration Baseline; Change Control Log |
| O-4 | Operational | Execute AI incident response playbooks | MANAGE | IR (Incident Response), SI (System & Information Integrity) | Operations | AI Incident Playbook; After-Action Report |
| O-5 | Operational | Retire AI systems exceeding defined risk tolerance | MANAGE | SA (System & Services Acquisition), CM (Configuration Management), MP (Media Protection) | Retirement | AI Retirement Plan; Risk Closure Documentation |

---

## SP 800-53 Control Family Reference

| Abbreviation | Control Family |
|-------------|---------------|
| AC | Access Control |
| AU | Audit & Accountability |
| CA | Assessment, Authorization & Monitoring |
| CM | Configuration Management |
| IA | Identification & Authentication |
| IR | Incident Response |
| MP | Media Protection |
| PL | Planning |
| PM | Program Management |
| RA | Risk Assessment |
| SA | System & Services Acquisition |
| SI | System & Information Integrity |
| SR | Supply Chain Risk Management |

---

## AI Lifecycle Phases

| Phase | Description |
|-------|-------------|
| Strategy & Design | Governance structures, policy, and risk categorization established before acquisition or development begins |
| Data Preparation | Training data sourcing, provenance, lineage, and quality governance |
| Development | Risk assessment, bias evaluation, model validation prior to deployment |
| Procurement | Third-party AI vendor assessment and supply chain risk governance |
| Deployment | Production release authorization and readiness review |
| Operations | Continuous monitoring, access control, incident response, periodic review |
| Retirement | Secure model disposal, data deletion, access revocation, audit documentation |

---

## Notes

Control objectives are illustrative and designed to support governance development and assurance alignment. Organizations should tailor control selection and implementation based on risk appetite, regulatory environment, and system importance.

The 16 controls represent a purposive cross-section validated for structural logic, not an exhaustive enterprise control catalog. Organizations adopting the LIAGCF are expected to extend the control set to reflect their specific risk profiles and operational contexts.

Governance artifacts listed are illustrative examples of implementation evidence, not prescriptive requirements.
