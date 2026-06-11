#!/usr/bin/env python3
"""
LIAGCF Control Validator
------------------------
Lifecycle-Integrated AI Governance Control Framework (LIAGCF)
Dr. Miranda Stanfield, PhD, CISA, CISM
www.drmirandastanfield.com

Validates an organization's AI governance posture against the LIAGCF.
Reads a YAML input file documenting implemented controls and produces
a gap analysis report showing coverage, gaps, and priorities by
lifecycle phase, RMF function, and control category.

Usage:
    python validate_liagcf.py --input your_assessment.yaml
    python validate_liagcf.py --input your_assessment.yaml --output report.txt

Citation:
    Stanfield, M. (2026). Evaluating control-based AI governance in
    cybersecurity GRC programs: An expert assessment study.
    RAIS Conference Proceedings, March 12-13, 2026.
    DOI: 10.5281/zenodo.19553772
"""

import argparse
import sys
from datetime import datetime

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install it with: pip install pyyaml")
    sys.exit(1)


# ── LIAGCF Framework Definition ───────────────────────────────────────────────

CONTROLS = [
    {
        "id": "A-1",
        "category": "Administrative",
        "objective": "Establish a formal enterprise AI governance policy and scope",
        "rmf_function": "GOVERN",
        "sp80053_families": ["PM", "PL"],
        "lifecycle_phase": "Strategy & Design",
        "artifacts": ["AI Governance Charter", "Enterprise AI Policy"],
    },
    {
        "id": "A-2",
        "category": "Administrative",
        "objective": "Define AI accountability, decision rights, and risk ownership",
        "rmf_function": "GOVERN",
        "sp80053_families": ["PM"],
        "lifecycle_phase": "Strategy & Design",
        "artifacts": ["AI RACI Matrix", "Governance Role Definitions"],
    },
    {
        "id": "A-3",
        "category": "Administrative",
        "objective": "Establish third-party AI risk governance policies",
        "rmf_function": "GOVERN",
        "sp80053_families": ["SR", "SA"],
        "lifecycle_phase": "Procurement",
        "artifacts": ["Vendor AI Risk Review Checklist", "Third-Party Risk Policy"],
    },
    {
        "id": "A-4",
        "category": "Administrative",
        "objective": "Define enterprise AI audit and governance review cadence",
        "rmf_function": "GOVERN",
        "sp80053_families": ["CA", "PM"],
        "lifecycle_phase": "Operations",
        "artifacts": ["AI Governance Review Plan", "Audit Schedule"],
    },
    {
        "id": "A-5",
        "category": "Administrative",
        "objective": "Require AI risk assessments prior to deployment",
        "rmf_function": "MAP",
        "sp80053_families": ["RA", "CA"],
        "lifecycle_phase": "Development",
        "artifacts": ["AI Risk Assessment Report", "Risk Register Entry"],
    },
    {
        "id": "A-6",
        "category": "Administrative",
        "objective": "Categorize AI systems by risk level, use context, and affected population",
        "rmf_function": "MAP",
        "sp80053_families": ["RA", "PL"],
        "lifecycle_phase": "Strategy & Design",
        "artifacts": ["AI System Inventory", "Risk Categorization Register"],
    },
    {
        "id": "T-1",
        "category": "Technical",
        "objective": "Identify and assess potential for discriminatory or disparate impact outcomes",
        "rmf_function": "MAP",
        "sp80053_families": ["RA", "SI"],
        "lifecycle_phase": "Development",
        "artifacts": ["Bias Risk Assessment", "Fairness Evaluation Report"],
    },
    {
        "id": "T-2",
        "category": "Technical",
        "objective": "Map data provenance, lineage, and quality risks for training datasets",
        "rmf_function": "MAP",
        "sp80053_families": ["SA", "SR"],
        "lifecycle_phase": "Data Preparation",
        "artifacts": ["Data Lineage Map", "Training Data Quality Report"],
    },
    {
        "id": "T-3",
        "category": "Technical",
        "objective": "Validate AI models prior to production release",
        "rmf_function": "MEASURE",
        "sp80053_families": ["CA", "SA"],
        "lifecycle_phase": "Development",
        "artifacts": ["Model Validation Report", "Testing Summary"],
    },
    {
        "id": "T-4",
        "category": "Technical",
        "objective": "Monitor model performance and detect drift",
        "rmf_function": "MEASURE",
        "sp80053_families": ["SI", "CA"],
        "lifecycle_phase": "Operations",
        "artifacts": ["Drift Monitoring Dashboard", "Performance Metrics Report"],
    },
    {
        "id": "T-5",
        "category": "Technical",
        "objective": "Log AI system activity for traceability and auditability",
        "rmf_function": "MEASURE",
        "sp80053_families": ["AU"],
        "lifecycle_phase": "Operations",
        "artifacts": ["Audit Logs", "Monitoring Dashboard"],
    },
    {
        "id": "O-1",
        "category": "Operational",
        "objective": "Conduct periodic AI governance and risk reviews",
        "rmf_function": "MEASURE",
        "sp80053_families": ["CA", "RA"],
        "lifecycle_phase": "Operations",
        "artifacts": ["Governance Review Report", "Risk Reassessment Summary"],
    },
    {
        "id": "O-2",
        "category": "Operational",
        "objective": "Enforce access controls on AI training and operational data",
        "rmf_function": "MANAGE",
        "sp80053_families": ["AC", "IA"],
        "lifecycle_phase": "Data Preparation / Operations",
        "artifacts": ["Access Control Matrix", "Privileged Access Review"],
    },
    {
        "id": "O-3",
        "category": "Operational",
        "objective": "Protect AI models from unauthorized modification",
        "rmf_function": "MANAGE",
        "sp80053_families": ["CM", "SI"],
        "lifecycle_phase": "Operations",
        "artifacts": ["Configuration Baseline", "Change Control Log"],
    },
    {
        "id": "O-4",
        "category": "Operational",
        "objective": "Execute AI incident response playbooks",
        "rmf_function": "MANAGE",
        "sp80053_families": ["IR", "SI"],
        "lifecycle_phase": "Operations",
        "artifacts": ["AI Incident Playbook", "After-Action Report"],
    },
    {
        "id": "O-5",
        "category": "Operational",
        "objective": "Retire AI systems exceeding defined risk tolerance",
        "rmf_function": "MANAGE",
        "sp80053_families": ["SA", "CM", "MP"],
        "lifecycle_phase": "Retirement",
        "artifacts": ["AI Retirement Plan", "Risk Closure Documentation"],
    },
]

VALID_STATUSES = {"implemented", "partial", "planned", "not-implemented"}
LIFECYCLE_ORDER = [
    "Strategy & Design",
    "Data Preparation",
    "Development",
    "Procurement",
    "Deployment",
    "Operations",
    "Data Preparation / Operations",
    "Retirement",
]
RMF_FUNCTIONS = ["GOVERN", "MAP", "MEASURE", "MANAGE"]
CATEGORIES = ["Administrative", "Technical", "Operational"]


# ── Validation Logic ───────────────────────────────────────────────────────────

def load_assessment(filepath):
    """Load and validate the YAML assessment file."""
    try:
        with open(filepath, "r") as f:
            data = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"ERROR: File not found: {filepath}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"ERROR: Could not parse YAML file: {e}")
        sys.exit(1)

    if "controls" not in data:
        print("ERROR: YAML file must contain a 'controls' section.")
        sys.exit(1)

    return data


def validate_controls(assessment_data):
    """
    Cross-reference assessment controls against the LIAGCF.
    Returns a dict of control_id -> assessment entry with status.
    """
    assessed = {}
    errors = []
    seen_ids = {}

    for i, entry in enumerate(assessment_data.get("controls", []), start=1):
        raw_id = entry.get("id")
        raw_status = entry.get("status")

        # Catch missing id field
        if not raw_id:
            errors.append(f"  Entry #{i} is missing an 'id' field.")
            continue

        control_id = str(raw_id).strip().upper()

        # Catch missing or null status field
        if raw_status is None:
            errors.append(
                f"  Control {control_id} is missing a 'status' field — "
                f"must be one of: {', '.join(sorted(VALID_STATUSES))}"
            )
            continue

        status = str(raw_status).strip().lower()
        notes = entry.get("notes", "") or ""

        # Validate control ID exists in LIAGCF
        valid_ids = [c["id"] for c in CONTROLS]
        if control_id not in valid_ids:
            errors.append(
                f"  Unknown control ID: '{control_id}' — "
                f"valid IDs are: {', '.join(valid_ids)}"
            )
            continue

        # Catch duplicate control IDs
        if control_id in seen_ids:
            errors.append(
                f"  Duplicate control ID: '{control_id}' appears at "
                f"entries #{seen_ids[control_id]} and #{i}. "
                f"Each control may only be assessed once."
            )
            continue

        # Validate status value
        if status not in VALID_STATUSES:
            errors.append(
                f"  Invalid status '{status}' for {control_id} — "
                f"must be one of: {', '.join(sorted(VALID_STATUSES))}"
            )
            continue

        seen_ids[control_id] = i
        assessed[control_id] = {"status": status, "notes": notes}

    return assessed, errors


def build_report(assessment_data, assessed_controls):
    """Generate the full gap analysis report as a string."""
    lines = []
    org_name = assessment_data.get("organization", "Your Organization")
    system_name = assessment_data.get("system_name", "AI System")
    assessor = assessment_data.get("assessor", "Not specified")
    assessment_date = assessment_data.get("date", datetime.today().strftime("%Y-%m-%d"))

    # ── Header ────────────────────────────────────────────────────────────────
    lines += [
        "=" * 70,
        "  LIAGCF CONTROL VALIDATION REPORT",
        "  Lifecycle-Integrated AI Governance Control Framework",
        "  Dr. Miranda Stanfield, PhD, CISA, CISM",
        "  www.drmirandastanfield.com",
        "=" * 70,
        "",
        f"  Organization : {org_name}",
        f"  System       : {system_name}",
        f"  Assessor     : {assessor}",
        f"  Date         : {assessment_date}",
        f"  Generated    : {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "  Citation: Stanfield, M. (2026). Evaluating control-based AI",
        "  governance in cybersecurity GRC programs: An expert assessment",
        "  study. RAIS Conference Proceedings, March 12-13, 2026.",
        "  DOI: 10.5281/zenodo.19553772",
        "=" * 70,
        "",
    ]

    # ── Overall Summary ───────────────────────────────────────────────────────
    total = len(CONTROLS)
    assessed_count = len(assessed_controls)
    implemented = sum(1 for v in assessed_controls.values() if v["status"] == "implemented")
    partial = sum(1 for v in assessed_controls.values() if v["status"] == "partial")
    planned = sum(1 for v in assessed_controls.values() if v["status"] == "planned")
    not_impl = sum(1 for v in assessed_controls.values() if v["status"] == "not-implemented")
    not_assessed = total - assessed_count

    coverage_pct = round((implemented / total) * 100)
    partial_pct = round((partial / total) * 100)

    lines += [
        "OVERALL COVERAGE SUMMARY",
        "-" * 70,
        f"  Total LIAGCF controls         : {total}",
        f"  Assessed in this submission   : {assessed_count}",
        f"  Not assessed (gap)            : {not_assessed}",
        "",
        f"  Implemented                   : {implemented} / {total} ({coverage_pct}%)",
        f"  Partial                       : {partial} / {total} ({partial_pct}%)",
        f"  Planned                       : {planned}",
        f"  Not Implemented               : {not_impl}",
        "",
    ]

    # Coverage bar
    bar_impl = "█" * implemented
    bar_part = "▒" * partial
    bar_plan = "░" * planned
    bar_none = "·" * (not_impl + not_assessed)
    lines += [
        f"  [{bar_impl}{bar_part}{bar_plan}{bar_none}] {coverage_pct}% fully implemented",
        "",
    ]

    # ── By RMF Function ───────────────────────────────────────────────────────
    lines += [
        "COVERAGE BY NIST AI RMF FUNCTION",
        "-" * 70,
    ]
    for func in RMF_FUNCTIONS:
        func_controls = [c for c in CONTROLS if c["rmf_function"] == func]
        func_impl = sum(
            1 for c in func_controls
            if assessed_controls.get(c["id"], {}).get("status") == "implemented"
        )
        func_partial = sum(
            1 for c in func_controls
            if assessed_controls.get(c["id"], {}).get("status") == "partial"
        )
        func_total = len(func_controls)
        lines.append(
            f"  {func:<10} {func_impl}/{func_total} implemented, "
            f"{func_partial}/{func_total} partial"
        )
    lines.append("")

    # ── By Control Category ───────────────────────────────────────────────────
    lines += [
        "COVERAGE BY CONTROL CATEGORY",
        "-" * 70,
    ]
    for cat in CATEGORIES:
        cat_controls = [c for c in CONTROLS if c["category"] == cat]
        cat_impl = sum(
            1 for c in cat_controls
            if assessed_controls.get(c["id"], {}).get("status") == "implemented"
        )
        cat_total = len(cat_controls)
        lines.append(f"  {cat:<15} {cat_impl}/{cat_total} implemented")
    lines.append("")

    # ── By Lifecycle Phase ────────────────────────────────────────────────────
    lines += [
        "COVERAGE BY AI LIFECYCLE PHASE",
        "-" * 70,
    ]
    phases_seen = []
    for phase in LIFECYCLE_ORDER:
        phase_controls = [c for c in CONTROLS if c["lifecycle_phase"] == phase]
        if not phase_controls:
            continue
        phases_seen.append(phase)
        phase_impl = sum(
            1 for c in phase_controls
            if assessed_controls.get(c["id"], {}).get("status") == "implemented"
        )
        phase_partial = sum(
            1 for c in phase_controls
            if assessed_controls.get(c["id"], {}).get("status") == "partial"
        )
        phase_total = len(phase_controls)
        status_str = f"{phase_impl}/{phase_total} implemented"
        if phase_partial:
            status_str += f", {phase_partial} partial"
        lines.append(f"  {phase:<35} {status_str}")
    lines.append("")

    # ── Full Control Detail ───────────────────────────────────────────────────
    lines += [
        "CONTROL-BY-CONTROL DETAIL",
        "-" * 70,
    ]

    STATUS_LABELS = {
        "implemented":     "✓ IMPLEMENTED    ",
        "partial":         "~ PARTIAL        ",
        "planned":         "○ PLANNED        ",
        "not-implemented": "✗ NOT IMPLEMENTED",
        "not-assessed":    "? NOT ASSESSED   ",
    }

    for control in CONTROLS:
        cid = control["id"]
        entry = assessed_controls.get(cid)
        status = entry["status"] if entry else "not-assessed"
        notes = entry["notes"] if entry else ""
        label = STATUS_LABELS.get(status, status)

        lines += [
            f"  {cid}  [{label}]  {control['rmf_function']} | {control['lifecycle_phase']}",
            f"       {control['objective']}",
            f"       SP 800-53: {', '.join(control['sp80053_families'])}",
        ]
        if notes:
            lines.append(f"       Notes: {notes}")
        lines.append("")

    # ── Priority Gaps ─────────────────────────────────────────────────────────
    gap_controls = [
        c for c in CONTROLS
        if assessed_controls.get(c["id"], {}).get("status") == "not-implemented"
        or c["id"] not in assessed_controls
    ]

    if gap_controls:
        lines += [
            "PRIORITY GAPS — CONTROLS NOT IMPLEMENTED",
            "-" * 70,
            "  Address GOVERN controls first. Governance structures are",
            "  preconditions for technical and operational control enforcement.",
            "",
        ]
        # GOVERN gaps first
        for func in RMF_FUNCTIONS:
            func_gaps = [c for c in gap_controls if c["rmf_function"] == func]
            if func_gaps:
                lines.append(f"  {func} Function:")
                for c in func_gaps:
                    lines.append(f"    {c['id']}  {c['objective']}")
                    lines.append(f"         Phase: {c['lifecycle_phase']} | SP 800-53: {', '.join(c['sp80053_families'])}")
                    lines.append(f"         Evidence needed: {'; '.join(c['artifacts'])}")
                lines.append("")

    # ── Retirement Warning ────────────────────────────────────────────────────
    o5 = assessed_controls.get("O-5", {})
    if o5.get("status") not in ("implemented", "partial"):
        lines += [
            "⚠  RETIREMENT PHASE ALERT",
            "-" * 70,
            "  Control O-5 (Retire AI systems exceeding defined risk tolerance)",
            "  is not implemented. Retired AI systems generate residual risks",
            "  including unrevoked model access, persistent data exposure, and",
            "  residual inference capabilities. Implement before decommissioning",
            "  any AI system.",
            "",
        ]

    # ── Footer ────────────────────────────────────────────────────────────────
    lines += [
        "=" * 70,
        "  LIAGCF v1.0 | github.com/stanfieldmiranda-eng/LIAGCF",
        "  Framework by Dr. Miranda Stanfield, PhD, CISA, CISM",
        "  www.drmirandastanfield.com",
        "=" * 70,
    ]

    return "\n".join(lines)


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Validate an AI governance assessment against the LIAGCF."
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the YAML assessment file (see examples/sample_assessment.yaml)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Optional path to save the report as a text file"
    )
    args = parser.parse_args()

    print(f"\nLIAGCF Validator — loading {args.input}...")
    assessment_data = load_assessment(args.input)
    assessed_controls, errors = validate_controls(assessment_data)

    if errors:
        print("\nValidation errors found in your assessment file:")
        for e in errors:
            print(e)
        print("\nFix the errors above and re-run the validator.")
        sys.exit(1)

    report = build_report(assessment_data, assessed_controls)
    print("\n" + report)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()
