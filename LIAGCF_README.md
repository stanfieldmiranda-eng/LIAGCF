# Lifecycle-Integrated AI Governance Control Framework (LIAGCF)

> **The first lifecycle-integrated, control-categorized governance framework to operationalize both NIST AI RMF core functions and NIST SP 800-53 control families within a unified enterprise cybersecurity GRC architecture.**

---

## What This Is

The LIAGCF maps 16 administrative, technical, and operational AI governance controls across seven AI system lifecycle phases. Each control aligns to a NIST AI RMF core function (GOVERN, MAP, MEASURE, MANAGE) and a NIST SP 800-53 control family, within a unified enterprise GRC architecture.

This framework is designed for GRC practitioners, CISOs, and federal risk management program leads who need to govern AI systems using the same control infrastructure they already operate — not a parallel program built from scratch.

**This repository is the public reference implementation of the LIAGCF.** The framework was developed through Design Science Research methodology and validated by a structured expert panel (N=10) of credentialed practitioners with expertise in cybersecurity governance, federal GRC programs, and enterprise risk management.

---

## Published Research

**Stanfield, M. (2026).** Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.*
[https://doi.org/10.5281/zenodo.19553772](https://doi.org/10.5281/zenodo.19553772)

If you use or build on the LIAGCF, please cite the published paper.

---

## The Problem This Framework Solves

Major AI governance frameworks — NIST AI RMF, ISO/IEC 42001, the EU AI Act — operate at the level of principles and risk categories. They do not provide assignable, verifiable controls. Organizations are left to close the gap on their own.

Within cybersecurity GRC programs, the specific problem is that functions operating under NIST SP 800-53 and the NIST AI RMF lack an integrated, operationalizable governance model. No existing model addresses AI-specific risks across the full system lifecycle — including the Retirement and Decommissioning phase, which is the most systematically underspecified component of AI lifecycle governance.

The LIAGCF addresses this gap by providing:

- **16 governance controls** organized by administrative, technical, and operational category
- **7 lifecycle phases** from Strategy and Design through Retirement
- **4 NIST AI RMF function alignments** (GOVERN, MAP, MEASURE, MANAGE)
- **13 SP 800-53 control family mappings** with documented design rationale
- **Example governance artifacts** for each control — the implementation evidence that auditors need

---

## Framework Structure: The Six-Column Alignment Pathway

Each of the 16 controls is defined across six dimensions:

| Column | Purpose |
|--------|---------|
| **Control Category** | Administrative, Technical, or Operational |
| **Control Objective** | The governance purpose the control is designed to achieve |
| **NIST AI RMF Function** | GOVERN, MAP, MEASURE, or MANAGE |
| **SP 800-53 Control Family** | The operational enforcement pathway |
| **AI Lifecycle Phase** | Where in the lifecycle the control applies |
| **Example Governance Artifacts** | Documentary evidence of implementation |

This six-column structure creates a continuous traceability chain from governance intent to implementation evidence — the audit defensibility that GRC practitioners need and that principles-based frameworks do not provide.

---

## Control Distribution

| AI RMF Function | Control Category | # Controls | Lifecycle Phases Covered |
|----------------|-----------------|------------|--------------------------|
| GOVERN | Administrative | 4 | Strategy & Design, Procurement, Operations |
| MAP | Administrative + Technical | 4 | Strategy & Design, Development, Data Preparation |
| MEASURE | Technical + Operational | 4 | Development, Operations |
| MANAGE | Operational | 4 | Data Preparation/Operations, Operations, Retirement |

All three control categories are represented. All seven lifecycle phases are covered. Thirteen SP 800-53 control families are instantiated across the 16 controls.

---

## Repository Contents

```
LIAGCF/
├── README.md                          # This file
├── framework/
│   └── liagcf_control_table.md        # The 16-control framework (Table A1)
├── docs/
│   ├── liagcf_methodology.md          # Six-column pathway and design logic
│   ├── liagcf_sp80053_rationale.md    # SP 800-53 family selection rationale (Appendix E)
│   ├── liagcf_lifecycle_phases.md     # Seven lifecycle phases defined
│   └── liagcf_glossary.md             # Working definitions
├── citation/
│   └── liagcf_citation.md             # Citation, DOI, and abstract
├── examples/
│   └── liagcf_sample_assessment.md    # Sample control application walkthrough
└── LICENSE
```

---

## Validation Summary

Expert assessment (N=10) validated the LIAGCF across five dimensions:

- **NIST AI RMF structural alignment** confirmed by 9 of 10 respondents
- **SP 800-53 control family assignments** assessed as technically defensible by 7 of 10 respondents
- **Seven-phase lifecycle coverage** validated as comprehensive by 7 of 10 respondents
- **Meaningful scholarly and practical contribution** affirmed by 9 of 10 respondents
- **Integration feasibility within NIST-aligned organizations** confirmed by 8 of 10 respondents

Expert panel expertise: Cybersecurity Governance (80%), Compliance & Audit (70%), Federal GRC Programs (70%), Enterprise Risk Management (60%).

---

## Who This Is For

**GRC Practitioners** implementing AI governance within existing SP 800-53 control environments. The LIAGCF is designed to extend your existing program — not replace it.

**CISOs and AI Risk Leads** who need a standards-aligned, auditable structure for governing AI systems across their full lifecycle.

**Federal Program Managers** operating under FISMA, FedRAMP, or agency-specific RMF requirements who need AI-specific governance that integrates with continuous authorization processes.

**Auditors and Assessors** who need an evidence-based governance structure with documented artifact requirements at each control.

**Researchers and Framework Developers** building on AI governance scholarship. The LIAGCF is published under Design Science Research methodology with a full codebook and audit trail available in the published paper.

---

## Scope and Limitations

The LIAGCF is scoped to operationalizable governance controls within cybersecurity GRC programs. AI ethics constructs — such as fairness and transparency where these operate independently of verifiable control structures — fall outside its architectural scope.

The 16 controls represent a purposive cross-section validated for structural logic, not an exhaustive enterprise control catalog. Organizations adopting the LIAGCF are expected to extend the control set to reflect their specific risk profiles and regulatory context.

Operational effectiveness has not been empirically tested in deployed settings. Expert assessment establishes face and construct validity. Longitudinal deployment studies are identified as a direction for future research.

---

## Extending the Framework

Expert assessment identified the following as priority development areas for future iterations:

1. Explicit controls for model transparency, explainability, and human oversight
2. Post-deployment fairness monitoring (Operations phase)
3. Deployment authorization and production readiness review controls
4. Retraining and model re-certification governance
5. Maturity-tiered implementation pathway (analogous to NIST CSF maturity tiers)

Contributions, issue reports, and implementation experience are welcome.

---

## Author

**Dr. Miranda Stanfield, PhD, CISA, CISM**
Cybersecurity GRC Policy | AI Governance | Federal Risk Management
Founder, [MBS.Tech](https://mbs.tech) | MBS.Tech Foundation (501(c)(3))

[LinkedIn](https://linkedin.com/in/mirandastanfield) · [RAIS Publication](https://doi.org/10.5281/zenodo.19553772)

---

## License

The LIAGCF framework content is published for public use with attribution required. See [LICENSE](LICENSE) for terms.

When using or adapting this framework, cite:

> Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.* https://doi.org/10.5281/zenodo.19553772
