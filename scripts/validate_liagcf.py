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
    python validate_liagcf.py --input your_assessment.yaml --format html --output report.html

Citation:
    Stanfield, M. (2026). Evaluating control-based AI governance in
    cybersecurity GRC programs: An expert assessment study.
    RAIS Conference Proceedings, March 12-13, 2026.
    DOI: 10.5281/zenodo.19553772
"""

import argparse
import sys
import os
from datetime import datetime

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install it with: pip3 install pyyaml")
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

STATUS_COLORS = {
    "implemented":     "#22c55e",
    "partial":         "#f59e0b",
    "planned":         "#60a5fa",
    "not-implemented": "#ef4444",
    "not-assessed":    "#6b7280",
}

STATUS_LABELS = {
    "implemented":     "Implemented",
    "partial":         "Partial",
    "planned":         "Planned",
    "not-implemented": "Not Implemented",
    "not-assessed":    "Not Assessed",
}


# ── Validation Logic ───────────────────────────────────────────────────────────

def load_assessment(filepath):
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
    assessed = {}
    errors = []
    seen_ids = {}

    for i, entry in enumerate(assessment_data.get("controls", []), start=1):
        raw_id = entry.get("id")
        raw_status = entry.get("status")

        if not raw_id:
            errors.append(f"  Entry #{i} is missing an 'id' field.")
            continue

        control_id = str(raw_id).strip().upper()

        if raw_status is None:
            errors.append(
                f"  Control {control_id} is missing a 'status' field — "
                f"must be one of: {', '.join(sorted(VALID_STATUSES))}"
            )
            continue

        status = str(raw_status).strip().lower()
        notes = entry.get("notes", "") or ""

        valid_ids = [c["id"] for c in CONTROLS]
        if control_id not in valid_ids:
            errors.append(
                f"  Unknown control ID: '{control_id}' — "
                f"valid IDs are: {', '.join(valid_ids)}"
            )
            continue

        if control_id in seen_ids:
            errors.append(
                f"  Duplicate control ID: '{control_id}' appears at "
                f"entries #{seen_ids[control_id]} and #{i}. "
                f"Each control may only be assessed once."
            )
            continue

        if status not in VALID_STATUSES:
            errors.append(
                f"  Invalid status '{status}' for {control_id} — "
                f"must be one of: {', '.join(sorted(VALID_STATUSES))}"
            )
            continue

        seen_ids[control_id] = i
        assessed[control_id] = {"status": status, "notes": notes}

    return assessed, errors


# ── Text Report ────────────────────────────────────────────────────────────────

def build_text_report(assessment_data, assessed_controls):
    lines = []
    org_name = assessment_data.get("organization", "Your Organization")
    system_name = assessment_data.get("system_name", "AI System")
    assessor = assessment_data.get("assessor", "Not specified")
    assessment_date = assessment_data.get("date", datetime.today().strftime("%Y-%m-%d"))

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

    bar_impl = "█" * implemented
    bar_part = "▒" * partial
    bar_plan = "░" * planned
    bar_none = "·" * (not_impl + not_assessed)
    lines += [f"  [{bar_impl}{bar_part}{bar_plan}{bar_none}] {coverage_pct}% fully implemented", ""]

    lines += ["COVERAGE BY NIST AI RMF FUNCTION", "-" * 70]
    for func in RMF_FUNCTIONS:
        func_controls = [c for c in CONTROLS if c["rmf_function"] == func]
        func_impl = sum(1 for c in func_controls if assessed_controls.get(c["id"], {}).get("status") == "implemented")
        func_partial = sum(1 for c in func_controls if assessed_controls.get(c["id"], {}).get("status") == "partial")
        func_total = len(func_controls)
        lines.append(f"  {func:<10} {func_impl}/{func_total} implemented, {func_partial}/{func_total} partial")
    lines.append("")

    lines += ["COVERAGE BY CONTROL CATEGORY", "-" * 70]
    for cat in CATEGORIES:
        cat_controls = [c for c in CONTROLS if c["category"] == cat]
        cat_impl = sum(1 for c in cat_controls if assessed_controls.get(c["id"], {}).get("status") == "implemented")
        cat_total = len(cat_controls)
        lines.append(f"  {cat:<15} {cat_impl}/{cat_total} implemented")
    lines.append("")

    lines += ["COVERAGE BY AI LIFECYCLE PHASE", "-" * 70]
    for phase in LIFECYCLE_ORDER:
        phase_controls = [c for c in CONTROLS if c["lifecycle_phase"] == phase]
        if not phase_controls:
            continue
        phase_impl = sum(1 for c in phase_controls if assessed_controls.get(c["id"], {}).get("status") == "implemented")
        phase_partial = sum(1 for c in phase_controls if assessed_controls.get(c["id"], {}).get("status") == "partial")
        phase_total = len(phase_controls)
        status_str = f"{phase_impl}/{phase_total} implemented"
        if phase_partial:
            status_str += f", {phase_partial} partial"
        lines.append(f"  {phase:<35} {status_str}")
    lines.append("")

    lines += ["CONTROL-BY-CONTROL DETAIL", "-" * 70]
    TXT_STATUS = {
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
        label = TXT_STATUS.get(status, status)
        lines += [
            f"  {cid}  [{label}]  {control['rmf_function']} | {control['lifecycle_phase']}",
            f"       {control['objective']}",
            f"       SP 800-53: {', '.join(control['sp80053_families'])}",
        ]
        if notes:
            lines.append(f"       Notes: {notes}")
        lines.append("")

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
        for func in RMF_FUNCTIONS:
            func_gaps = [c for c in gap_controls if c["rmf_function"] == func]
            if func_gaps:
                lines.append(f"  {func} Function:")
                for c in func_gaps:
                    lines.append(f"    {c['id']}  {c['objective']}")
                    lines.append(f"         Phase: {c['lifecycle_phase']} | SP 800-53: {', '.join(c['sp80053_families'])}")
                    lines.append(f"         Evidence needed: {'; '.join(c['artifacts'])}")
                lines.append("")

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

    lines += [
        "=" * 70,
        "  LIAGCF v1.0 | github.com/stanfieldmiranda-eng/LIAGCF",
        "  Framework by Dr. Miranda Stanfield, PhD, CISA, CISM",
        "  www.drmirandastanfield.com",
        "=" * 70,
    ]

    return "\n".join(lines)


# ── HTML Report ────────────────────────────────────────────────────────────────

def build_html_report(assessment_data, assessed_controls):
    org_name = assessment_data.get("organization", "Your Organization")
    system_name = assessment_data.get("system_name", "AI System")
    assessor = assessment_data.get("assessor", "Not specified")
    assessment_date = str(assessment_data.get("date", datetime.today().strftime("%Y-%m-%d")))
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")

    total = len(CONTROLS)
    implemented = sum(1 for v in assessed_controls.values() if v["status"] == "implemented")
    partial = sum(1 for v in assessed_controls.values() if v["status"] == "partial")
    planned = sum(1 for v in assessed_controls.values() if v["status"] == "planned")
    not_impl = sum(1 for v in assessed_controls.values() if v["status"] == "not-implemented")
    not_assessed = total - len(assessed_controls)
    coverage_pct = round((implemented / total) * 100)

    # ── Summary cards ─────────────────────────────────────────────────────────
    def summary_card(label, value, color):
        return f"""
        <div class="card">
          <div class="card-value" style="color:{color}">{value}</div>
          <div class="card-label">{label}</div>
        </div>"""

    cards_html = (
        summary_card("Implemented", f"{implemented}/{total}", "#22c55e") +
        summary_card("Partial", f"{partial}/{total}", "#f59e0b") +
        summary_card("Planned", str(planned), "#60a5fa") +
        summary_card("Not Implemented", str(not_impl), "#ef4444") +
        summary_card("Not Assessed", str(not_assessed), "#6b7280")
    )

    # ── Coverage bar ──────────────────────────────────────────────────────────
    p_impl  = round((implemented / total) * 100)
    p_part  = round((partial / total) * 100)
    p_plan  = round((planned / total) * 100)
    p_notim = round((not_impl / total) * 100)
    p_na    = 100 - p_impl - p_part - p_plan - p_notim

    coverage_bar = f"""
    <div class="coverage-bar-wrap">
      <div class="coverage-bar">
        <div style="width:{p_impl}%;background:#22c55e" title="Implemented {p_impl}%"></div>
        <div style="width:{p_part}%;background:#f59e0b" title="Partial {p_part}%"></div>
        <div style="width:{p_plan}%;background:#60a5fa" title="Planned {p_plan}%"></div>
        <div style="width:{p_notim}%;background:#ef4444" title="Not Implemented {p_notim}%"></div>
        <div style="width:{p_na}%;background:#374151"   title="Not Assessed {p_na}%"></div>
      </div>
      <div class="coverage-legend">
        <span><span class="dot" style="background:#22c55e"></span>Implemented</span>
        <span><span class="dot" style="background:#f59e0b"></span>Partial</span>
        <span><span class="dot" style="background:#60a5fa"></span>Planned</span>
        <span><span class="dot" style="background:#ef4444"></span>Not Implemented</span>
        <span><span class="dot" style="background:#374151"></span>Not Assessed</span>
      </div>
    </div>"""

    # ── RMF Function breakdown ────────────────────────────────────────────────
    rmf_rows = ""
    for func in RMF_FUNCTIONS:
        func_controls = [c for c in CONTROLS if c["rmf_function"] == func]
        func_total = len(func_controls)
        counts = {s: 0 for s in ["implemented", "partial", "planned", "not-implemented", "not-assessed"]}
        for c in func_controls:
            s = assessed_controls.get(c["id"], {}).get("status", "not-assessed")
            counts[s] += 1
        func_pct = round((counts["implemented"] / func_total) * 100)
        rmf_rows += f"""
        <tr>
          <td><span class="badge badge-rmf">{func}</span></td>
          <td>{counts['implemented']}/{func_total}</td>
          <td>{counts['partial']}/{func_total}</td>
          <td>{counts['planned']}</td>
          <td>{counts['not-implemented']}</td>
          <td>
            <div class="mini-bar">
              <div style="width:{round(counts['implemented']/func_total*100)}%;background:#22c55e"></div>
              <div style="width:{round(counts['partial']/func_total*100)}%;background:#f59e0b"></div>
              <div style="width:{round(counts['planned']/func_total*100)}%;background:#60a5fa"></div>
              <div style="width:{round(counts['not-implemented']/func_total*100)}%;background:#ef4444"></div>
            </div>
          </td>
        </tr>"""

    # ── Lifecycle phase breakdown ──────────────────────────────────────────────
    phase_rows = ""
    for phase in LIFECYCLE_ORDER:
        phase_controls = [c for c in CONTROLS if c["lifecycle_phase"] == phase]
        if not phase_controls:
            continue
        phase_total = len(phase_controls)
        counts = {s: 0 for s in ["implemented", "partial", "planned", "not-implemented", "not-assessed"]}
        for c in phase_controls:
            s = assessed_controls.get(c["id"], {}).get("status", "not-assessed")
            counts[s] += 1
        phase_rows += f"""
        <tr>
          <td>{phase}</td>
          <td>{counts['implemented']}/{phase_total}</td>
          <td>{counts['partial']}</td>
          <td>{counts['not-implemented'] + counts['not-assessed']}</td>
          <td>
            <div class="mini-bar">
              <div style="width:{round(counts['implemented']/phase_total*100)}%;background:#22c55e"></div>
              <div style="width:{round(counts['partial']/phase_total*100)}%;background:#f59e0b"></div>
              <div style="width:{round((counts['not-implemented']+counts['not-assessed'])/phase_total*100)}%;background:#ef4444"></div>
            </div>
          </td>
        </tr>"""

    # ── Control detail rows ───────────────────────────────────────────────────
    control_rows = ""
    for control in CONTROLS:
        cid = control["id"]
        entry = assessed_controls.get(cid)
        status = entry["status"] if entry else "not-assessed"
        notes = entry["notes"] if entry else ""
        color = STATUS_COLORS[status]
        label = STATUS_LABELS[status]
        families = ", ".join(control["sp80053_families"])
        artifacts = "; ".join(control["artifacts"])
        notes_html = f'<div class="notes">{notes}</div>' if notes else ""
        cat_class = control["category"].lower()
        control_rows += f"""
        <tr>
          <td><span class="control-id">{cid}</span></td>
          <td><span class="badge badge-{cat_class}">{control['category']}</span></td>
          <td class="objective">{control['objective']}</td>
          <td><span class="badge badge-rmf">{control['rmf_function']}</span></td>
          <td>{control['lifecycle_phase']}</td>
          <td>{families}</td>
          <td><span class="status-pill" style="background:{color}20;color:{color};border:1px solid {color}40">{label}</span>
          {notes_html}</td>
        </tr>"""

    # ── Priority gaps ─────────────────────────────────────────────────────────
    gap_controls = [
        c for c in CONTROLS
        if assessed_controls.get(c["id"], {}).get("status") == "not-implemented"
        or c["id"] not in assessed_controls
    ]

    gaps_html = ""
    if gap_controls:
        for func in RMF_FUNCTIONS:
            func_gaps = [c for c in gap_controls if c["rmf_function"] == func]
            if not func_gaps:
                continue
            gaps_html += f'<div class="gap-function">{func}</div>'
            for c in func_gaps:
                gaps_html += f"""
                <div class="gap-item">
                  <div class="gap-header">
                    <span class="control-id">{c['id']}</span>
                    <span class="gap-phase">{c['lifecycle_phase']}</span>
                    <span class="gap-families">SP 800-53: {', '.join(c['sp80053_families'])}</span>
                  </div>
                  <div class="gap-objective">{c['objective']}</div>
                  <div class="gap-artifacts">Evidence needed: {'; '.join(c['artifacts'])}</div>
                </div>"""
    else:
        gaps_html = '<p style="color:#22c55e;font-weight:600">No gaps identified. All controls are implemented or partially implemented.</p>'

    # ── Retirement alert ──────────────────────────────────────────────────────
    o5 = assessed_controls.get("O-5", {})
    retirement_alert = ""
    if o5.get("status") not in ("implemented", "partial"):
        retirement_alert = """
        <div class="alert">
          <div class="alert-title">⚠ Retirement Phase Alert</div>
          Control O-5 (Retire AI systems exceeding defined risk tolerance) is not implemented.
          Retired AI systems generate residual risks including unrevoked model access,
          persistent data exposure, and residual inference capabilities.
          Implement before decommissioning any AI system.
        </div>"""

    # ── Assemble full HTML ────────────────────────────────────────────────────
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LIAGCF Gap Analysis Report — {org_name}</title>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         background: #0f172a; color: #e2e8f0; line-height: 1.6; }}
  a {{ color: #60a5fa; }}

  /* Header */
  .header {{ background: linear-gradient(135deg, #1e3a5f 0%, #0f172a 100%);
             padding: 2.5rem 2rem; border-bottom: 1px solid #1e40af40; }}
  .header-top {{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem; }}
  .header h1 {{ font-size: 1.5rem; font-weight: 700; color: #f1f5f9; letter-spacing: -0.02em; }}
  .header h1 span {{ color: #60a5fa; }}
  .header-meta {{ font-size: 0.8rem; color: #94a3b8; margin-top: 0.5rem; }}
  .header-meta p {{ margin: 0.1rem 0; }}
  .author-block {{ text-align:right; font-size:0.8rem; color:#94a3b8; }}
  .author-block strong {{ color:#e2e8f0; display:block; font-size:0.9rem; }}
  .coverage-badge {{ display:inline-block; background:#1e40af; color:#bfdbfe;
                     padding:0.6rem 1.2rem; border-radius:2rem; font-size:2rem;
                     font-weight:800; margin-top:1rem; }}

  /* Layout */
  .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
  .section {{ margin-bottom: 2.5rem; }}
  .section-title {{ font-size: 0.75rem; font-weight: 700; text-transform: uppercase;
                    letter-spacing: 0.1em; color: #60a5fa; margin-bottom: 1rem;
                    padding-bottom: 0.5rem; border-bottom: 1px solid #1e3a5f; }}

  /* Cards */
  .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; }}
  .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 0.75rem;
           padding: 1.25rem; text-align: center; }}
  .card-value {{ font-size: 1.8rem; font-weight: 800; line-height: 1; }}
  .card-label {{ font-size: 0.75rem; color: #94a3b8; margin-top: 0.35rem; text-transform: uppercase; letter-spacing: 0.05em; }}

  /* Coverage bar */
  .coverage-bar-wrap {{ margin: 1rem 0; }}
  .coverage-bar {{ display:flex; height: 1.5rem; border-radius: 0.5rem; overflow:hidden; background:#1e293b; }}
  .coverage-bar div {{ transition: width 0.3s; }}
  .coverage-legend {{ display:flex; gap:1.5rem; margin-top:0.5rem; font-size:0.75rem; color:#94a3b8; flex-wrap:wrap; }}
  .dot {{ display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:4px; }}

  /* Tables */
  .table-wrap {{ overflow-x: auto; border-radius: 0.75rem; border: 1px solid #334155; }}
  table {{ width:100%; border-collapse:collapse; font-size:0.85rem; }}
  th {{ background:#1e293b; color:#94a3b8; font-size:0.7rem; text-transform:uppercase;
        letter-spacing:0.08em; padding:0.75rem 1rem; text-align:left; white-space:nowrap; }}
  td {{ padding:0.75rem 1rem; border-top:1px solid #1e293b; vertical-align:top; }}
  tr:hover td {{ background:#1e293b50; }}
  .objective {{ max-width: 280px; }}
  .notes {{ font-size:0.75rem; color:#94a3b8; margin-top:0.3rem; font-style:italic; }}

  /* Mini bar */
  .mini-bar {{ display:flex; height:0.5rem; border-radius:0.25rem; overflow:hidden;
               background:#0f172a; min-width:80px; }}
  .mini-bar div {{ transition: width 0.3s; }}

  /* Badges */
  .badge {{ display:inline-block; padding:0.2rem 0.5rem; border-radius:0.3rem;
            font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; }}
  .badge-rmf {{ background:#1e3a5f; color:#93c5fd; }}
  .badge-administrative {{ background:#1e3a2f; color:#86efac; }}
  .badge-technical {{ background:#1e2a4f; color:#a5b4fc; }}
  .badge-operational {{ background:#3f1e1e; color:#fca5a5; }}

  /* Status pill */
  .status-pill {{ display:inline-block; padding:0.2rem 0.6rem; border-radius:1rem;
                  font-size:0.7rem; font-weight:600; white-space:nowrap; }}
  .control-id {{ font-family:monospace; font-weight:700; color:#60a5fa; font-size:0.9rem; }}

  /* Gaps */
  .gap-function {{ font-size:0.75rem; font-weight:700; text-transform:uppercase;
                   letter-spacing:0.1em; color:#f59e0b; margin:1rem 0 0.5rem; }}
  .gap-item {{ background:#1e293b; border:1px solid #334155; border-left:3px solid #ef4444;
               border-radius:0.5rem; padding:0.75rem 1rem; margin-bottom:0.5rem; }}
  .gap-header {{ display:flex; gap:1rem; align-items:center; flex-wrap:wrap; margin-bottom:0.25rem; }}
  .gap-phase {{ font-size:0.75rem; color:#94a3b8; }}
  .gap-families {{ font-size:0.75rem; color:#60a5fa; }}
  .gap-objective {{ font-size:0.875rem; color:#e2e8f0; margin-bottom:0.25rem; }}
  .gap-artifacts {{ font-size:0.75rem; color:#94a3b8; font-style:italic; }}

  /* Alert */
  .alert {{ background:#450a0a; border:1px solid #ef444440; border-left:4px solid #ef4444;
            border-radius:0.5rem; padding:1rem 1.25rem; margin-bottom:1.5rem; }}
  .alert-title {{ font-weight:700; color:#fca5a5; margin-bottom:0.5rem; }}

  /* Footer */
  .footer {{ background:#1e293b; border-top:1px solid #334155; padding:1.5rem 2rem;
             text-align:center; font-size:0.75rem; color:#64748b; margin-top:3rem; }}
  .footer a {{ color:#60a5fa; text-decoration:none; }}

  @media print {{
    body {{ background:#fff; color:#000; }}
    .header {{ background:#1e3a5f; -webkit-print-color-adjust:exact; }}
    .table-wrap {{ border:1px solid #ccc; }}
    th {{ background:#f1f5f9 !important; color:#333 !important; }}
  }}
</style>
</head>
<body>

<div class="header">
  <div class="header-top">
    <div>
      <h1>LIAGCF Gap Analysis Report<br><span>{org_name}</span></h1>
      <div class="header-meta">
        <p><strong>System:</strong> {system_name}</p>
        <p><strong>Assessor:</strong> {assessor} &nbsp;|&nbsp; <strong>Date:</strong> {assessment_date} &nbsp;|&nbsp; <strong>Generated:</strong> {generated}</p>
        <p style="margin-top:0.5rem;font-size:0.72rem">
          Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs.
          RAIS Conference Proceedings, March 12–13, 2026. DOI: 10.5281/zenodo.19553772
        </p>
      </div>
      <div class="coverage-badge">{coverage_pct}% Implemented</div>
    </div>
    <div class="author-block">
      <strong>Dr. Miranda Stanfield, PhD, CISA, CISM</strong>
      <a href="https://www.drmirandastanfield.com">www.drmirandastanfield.com</a><br>
      <a href="https://github.com/stanfieldmiranda-eng/LIAGCF">github.com/stanfieldmiranda-eng/LIAGCF</a>
    </div>
  </div>
</div>

<div class="container">

  {retirement_alert}

  <div class="section">
    <div class="section-title">Overall Coverage</div>
    <div class="cards">{cards_html}</div>
    {coverage_bar}
  </div>

  <div class="section">
    <div class="section-title">Coverage by NIST AI RMF Function</div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>Function</th><th>Implemented</th><th>Partial</th>
          <th>Planned</th><th>Not Implemented</th><th>Coverage</th>
        </tr></thead>
        <tbody>{rmf_rows}</tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Coverage by AI Lifecycle Phase</div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>Lifecycle Phase</th><th>Implemented</th><th>Partial</th>
          <th>Gaps</th><th>Coverage</th>
        </tr></thead>
        <tbody>{phase_rows}</tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <div class="section-title">Priority Gaps — Controls Not Implemented</div>
    <p style="font-size:0.8rem;color:#94a3b8;margin-bottom:1rem">
      Address GOVERN controls first. Governance structures are preconditions
      for technical and operational control enforcement.
    </p>
    {gaps_html}
  </div>

  <div class="section">
    <div class="section-title">Control-by-Control Detail</div>
    <div class="table-wrap">
      <table>
        <thead><tr>
          <th>ID</th><th>Category</th><th>Control Objective</th>
          <th>RMF Function</th><th>Lifecycle Phase</th>
          <th>SP 800-53</th><th>Status / Notes</th>
        </tr></thead>
        <tbody>{control_rows}</tbody>
      </table>
    </div>
  </div>

</div>

<div class="footer">
  LIAGCF v1.0 &nbsp;|&nbsp;
  <a href="https://github.com/stanfieldmiranda-eng/LIAGCF">github.com/stanfieldmiranda-eng/LIAGCF</a>
  &nbsp;|&nbsp; Framework by Dr. Miranda Stanfield, PhD, CISA, CISM &nbsp;|&nbsp;
  <a href="https://www.drmirandastanfield.com">www.drmirandastanfield.com</a>
</div>

</body>
</html>"""

    return html


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Validate an AI governance assessment against the LIAGCF."
    )
    parser.add_argument("--input", "-i", required=True,
        help="Path to the YAML assessment file (see examples/sample_assessment.yaml)")
    parser.add_argument("--output", "-o",
        help="Path to save the report (default: print to terminal)")
    parser.add_argument("--format", "-f", choices=["text", "html"], default="text",
        help="Output format: 'text' (default) or 'html'")
    parser.add_argument("--open", action="store_true",
        help="Automatically open HTML report in browser after generating")
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

    if args.format == "html":
        report = build_html_report(assessment_data, assessed_controls)
        output_path = args.output or "liagcf_report.html"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\nHTML report saved to: {output_path}")
        if args.open or not args.output:
            import webbrowser
            webbrowser.open(f"file://{os.path.abspath(output_path)}")
            print("Opening in browser...")
    else:
        report = build_text_report(assessment_data, assessed_controls)
        print("\n" + report)
        if args.output:
            with open(args.output, "w") as f:
                f.write(report)
            print(f"\nReport saved to {args.output}")


if __name__ == "__main__":
    main()
