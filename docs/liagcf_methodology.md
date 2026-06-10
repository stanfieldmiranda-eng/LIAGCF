# LIAGCF Methodology: The Six-Column Alignment Pathway

The six-column alignment pathway is the LIAGCF's primary translation mechanism. It converts governance intent into verifiable implementation requirements across six sequential dimensions.

---

## Why a Six-Column Structure

Major AI governance frameworks — NIST AI RMF, ISO/IEC 42001, the EU AI Act — are structured at the level of principles and risk categories. They do not provide assignable, verifiable controls. Organizations implementing these frameworks encounter the same problem: a policy declaring that AI systems will be used responsibly does not constitute governance unless it is translated into defined controls with identifiable owners, documented artifacts, and enforceable review processes.

The six-column pathway addresses this by building a continuous traceability chain from governance intent to implementation evidence.

---

## The Six Columns

### Column 1: Control Category

Each control is classified as **Administrative**, **Technical**, or **Operational**.

This taxonomy has an established pedigree in information security governance and is applied here as the primary organizational structure — not a secondary label.

- **Administrative controls** encompass policies, governance structures, organizational accountability, and decision rights.
- **Technical controls** implement governance through automated or technological mechanisms — bias assessment tools, monitoring pipelines, audit logging systems.
- **Operational controls** cover runtime enforcement, incident response, access control, and lifecycle management activities.

### Column 2: Control Objective

Each control objective states the governance purpose the control is intended to achieve. This makes design intent explicit and auditable, and allows assessors to evaluate whether an organization's implementation actually addresses the governance problem the control targets.

### Column 3: NIST AI RMF Function

Each control is assigned to one of the four NIST AI RMF core functions:

| Function | Governance Purpose |
|----------|-------------------|
| **GOVERN** | Establishes policies, processes, roles, and accountability structures that enable AI risk management |
| **MAP** | Directs identification, categorization, and analysis of AI-specific risks |
| **MEASURE** | Directs analysis and assessment of AI risk through technical evaluation and monitoring |
| **MANAGE** | Directs prioritization and response to AI risks through operational mechanisms |

### Column 4: SP 800-53 Control Family

Each control is assigned to one or more SP 800-53 control families. This is the operationalization layer — it translates governance intent into an auditable control specification that enterprise GRC programs can implement, test, and report against.

This is the column that existing frameworks consistently omit. Without a specific SP 800-53 family assignment, AI RMF alignment produces principles rather than actionable requirements.

See [`liagcf_sp80053_rationale.md`](liagcf_sp80053_rationale.md) for documented design rationale for every control family assignment.

### Column 5: AI Lifecycle Phase

Each control is anchored to one of seven AI lifecycle phases:

1. Strategy & Design
2. Data Preparation
3. Development
4. Procurement
5. Deployment
6. Operations
7. Retirement

Lifecycle anchoring makes controls contextually actionable. A uniform control set applied across all phases imposes disproportionate governance burden on low-risk phases while leaving critical transition points exposed. Phase-specific assignment enables phase-gated governance reviews aligned with the actual risk requirements of each stage.

### Column 6: Example Governance Artifacts

Each control specifies documentary outputs that demonstrate implementation and provide the evidentiary basis for audit.

These are illustrative examples of implementation evidence, not prescriptive requirements. They answer the auditor's question: *what would I look for to confirm this control is in place?*

---

## Framework Design Logic

### Control Distribution Rationale

The 16 controls are evenly distributed across the four AI RMF functions (4 per function) to demonstrate structural logic and internal alignment across control categories, SP 800-53 families, and lifecycle phases.

**GOVERN — Four Administrative Controls.** Governance structures must precede system acquisition, design, or deployment. All four GOVERN controls are Administrative, consistent with the function's role in establishing organizational accountability before technical or operational controls can be meaningfully enforced.

**MAP — Two Administrative and Two Technical Controls.** MAP has a dual nature: establishing administrative risk-identification processes and implementing technical mechanisms to characterize system-level risks. The Administrative MAP controls address risk assessment requirements and AI system categorization. The Technical MAP controls address bias risk and data provenance.

**MEASURE — Three Technical and One Operational Control.** MEASURE outputs — bias metrics, performance benchmarks, drift detection results — are generated through technical mechanisms. Three of the four MEASURE controls are Technical. One Operational control addresses the procedural governance of the assessment process.

**MANAGE — Four Operational Controls.** MANAGE directs runtime enforcement, incident response, continuous monitoring, and lifecycle management. All four MANAGE controls are Operational. The four controls span Data Preparation/Operations, Operations, and Retirement — covering the full range of post-deployment governance obligations including secure system retirement.

---

## Three Structural Layers

The LIAGCF delivers its governance function through three mutually constitutive structural layers. Each is necessary; none is sufficient on its own.

**Layer 1: AI RMF Functional Alignment.** Situates each control within the risk management vocabulary established by NIST AI RMF 1.0. Ensures every control traces to an organizational risk management obligation.

**Layer 2: SP 800-53 Operationalization.** Bridges the principles-to-practice gap by assigning each control to a specific SP 800-53 control family. Translates governance intent into an auditable specification that enterprise GRC programs can implement, test, and report against.

**Layer 3: Lifecycle Phase Anchoring.** Specifies which of the seven AI lifecycle phases each control applies to. Makes SP 800-53 assignments contextually actionable rather than context-free. Enables phase-gated governance reviews.

---

## Methodological Foundation

The LIAGCF was developed using Design Science Research (DSR) methodology as formalized by Hevner et al. (2004) and operationalized through the six-stage process model of Peffers et al. (2007). Expert panel evaluation followed the Framework for Evaluation in Design Science Research (FEDS) established by Venable et al. (2016).

Full methodological documentation, including the thematic analysis codebook and survey instrument, is available in the published paper.

**Citation:** Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.* DOI: `10.5281/zenodo.19553772` (copy and paste into browser address bar)
