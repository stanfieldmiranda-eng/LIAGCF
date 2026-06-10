# Sample Control Application: GOVERN Function

This walkthrough demonstrates how to apply the LIAGCF's four GOVERN-function administrative controls within an existing GRC program. It is intended to help practitioners understand how the framework integrates with SP 800-53 control environments they already operate.

---

## Starting Point: Why GOVERN First

Expert respondents confirmed that the GOVERN-function controls are preconditions for implementation, not parallel activities. Governance structures, accountability assignments, and audit cadence must be established before technical and operational controls can be meaningfully enforced.

If your organization is adopting the LIAGCF, start here.

---

## Control A-1: Establish a formal enterprise AI governance policy and scope

**SP 800-53 families:** PM, PL
**Lifecycle phase:** Strategy & Design
**Example artifacts:** AI Governance Charter; Enterprise AI Policy

### What this control requires

Before any AI system is acquired, designed, or deployed, your organization needs a documented policy that defines:

- The scope of systems subject to AI governance requirements
- The organizational unit responsible for AI governance oversight
- The relationship between AI governance and existing information security policy
- Acceptable use parameters and prohibited AI applications

### How it maps to your existing program

If you operate under SP 800-53, you already have PM and PL controls implemented for your information systems program. A-1 extends that infrastructure to AI. The AI Governance Charter is a new artifact; the PM and PL control families that require it are not.

### What the auditor needs to see

A documented AI Governance Charter or equivalent policy with defined scope, responsible official, and approval signature. An Enterprise AI Policy that addresses acceptable use and governance obligations. Both documents should be version-controlled and traceable to a review and approval date.

---

## Control A-2: Define AI accountability, decision rights, and risk ownership

**SP 800-53 family:** PM
**Lifecycle phase:** Strategy & Design
**Example artifacts:** AI RACI Matrix; Governance Role Definitions

### What this control requires

Governance authority and risk ownership must be assigned to named roles before systems are deployed. This control defines:

- Who owns AI risk at the program level (typically the CISO or AI Risk Officer)
- Who approves AI system deployments
- Who is responsible for monitoring and remediation
- How AI governance decisions escalate when thresholds are exceeded

### How it maps to your existing program

Your organization's existing PM controls already establish program roles and responsibilities. This control applies that framework specifically to AI — creating an AI RACI that maps governance activities to organizational roles.

### What the auditor needs to see

A documented AI RACI Matrix or equivalent governance role definition that identifies responsible, accountable, consulted, and informed parties for each AI governance activity. Role definitions should map to existing organizational positions, not create standalone AI governance titles that exist only on paper.

---

## Control A-3: Establish third-party AI risk governance policies

**SP 800-53 families:** SR, SA
**Lifecycle phase:** Procurement
**Example artifacts:** Vendor AI Risk Review Checklist; Third-Party Risk Policy

### What this control requires

When your organization acquires AI systems, components, or services from external vendors, you inherit supply chain risks that require explicit governance. This control requires:

- Documented criteria for assessing vendor AI risk posture
- Contractual requirements for vendor AI governance obligations
- A process for reviewing third-party AI components before procurement

### How it maps to your existing program

SP 800-53 Rev. 5 introduced the SR control family specifically to address supply chain risks. Your existing SR and SA controls cover third-party software and services. A-3 applies those controls to AI vendors — including vendors whose products embed AI without explicitly advertising it.

### What the auditor needs to see

A Vendor AI Risk Review Checklist used in procurement decisions. A Third-Party Risk Policy that addresses AI-specific obligations. Evidence that the checklist was applied to AI vendor assessments.

---

## Control A-4: Define enterprise AI audit and governance review cadence

**SP 800-53 families:** CA, PM
**Lifecycle phase:** Operations
**Example artifacts:** AI Governance Review Plan; Audit Schedule

### What this control requires

Governance is not a one-time authorization activity. This control requires:

- A defined schedule for periodic AI governance reviews
- Criteria for triggering out-of-cycle reviews (significant model changes, performance degradation, incident occurrence)
- Documentation requirements for review findings and remediation tracking

### How it maps to your existing program

Your existing CA controls establish the authorization and continuous monitoring framework for information systems. A-4 extends that cadence to AI systems — ensuring that AI governance reviews are scheduled, resourced, and documented within the same program infrastructure.

### What the auditor needs to see

A documented AI Governance Review Plan with defined review frequency. An Audit Schedule showing when AI systems are subject to governance review. Evidence that reviews have occurred and findings have been tracked to resolution.

---

## Applying All Four Together

The four GOVERN controls work as a sequence:

1. **A-1** establishes what AI governance covers and who is responsible for it.
2. **A-2** assigns specific accountability and decision rights to named roles.
3. **A-3** extends governance obligations to third-party AI before acquisition.
4. **A-4** institutionalizes the review cadence that keeps governance active after deployment.

An organization that has implemented all four GOVERN controls has established the administrative infrastructure that makes the MAP, MEASURE, and MANAGE controls operationally enforceable — not just documented.

---

## Next Steps

After implementing the GOVERN controls, apply the MAP controls to identify and categorize AI system risk before development or procurement begins. See the full control table at [`framework/liagcf_control_table.md`](../framework/liagcf_control_table.md).

For the SP 800-53 family selection rationale underlying each control assignment, see [`docs/liagcf_sp80053_rationale.md`](liagcf_sp80053_rationale.md).
