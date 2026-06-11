# LIAGCF Examples

This folder contains two ways to assess your organization's AI governance posture against the LIAGCF. Use whichever fits your situation.

---

## Option 1: Interactive web tool (no installation required)

**File:** `liagcf_interactive.html`

Open this file in any browser. No Python, no terminal, no setup.

**How to use:**
1. Download `liagcf_interactive.html` to your computer
2. Double-click it to open in your browser
3. Enter your organization and system name
4. For each of the 16 controls, click your status: Implemented, Partial, Planned, or Not Implemented
5. Click **Generate gap analysis report**

You'll see your coverage percentage, a breakdown by NIST AI RMF function and control category, and a prioritized list of gaps with evidence requirements.

To save your report: use your browser's **Print → Save as PDF** option.

**Best for:** CISOs, program managers, governance leads, and anyone who wants results without touching a terminal.

---

## Option 2: Python validator with HTML or text report

**Files:** `sample_assessment.yaml` + `../scripts/validate_liagcf.py`

Fill out the YAML file documenting your control statuses, then run the validator to produce a gap analysis report — either as a styled HTML file or a text report.

**How to use:**

1. Copy `sample_assessment.yaml` and rename it for your organization
2. Update the header fields and set a status for each control
3. Run from your terminal:

```
python3 validate_liagcf.py --input my_assessment.yaml --format html
```

This generates an HTML report that opens in your browser automatically.

For full instructions see [`../scripts/README.md`](../scripts/README.md).

**Best for:** GRC teams who want to run assessments programmatically, save reports to files, or integrate the validator into existing workflows.

---

## Status options

| Status | Meaning |
|--------|---------|
| `implemented` | Control is fully in place with documented evidence |
| `partial` | Control is partially implemented; gaps remain |
| `planned` | Control is on the roadmap but not yet active |
| `not-implemented` | Control has not been addressed |

---

## The sample assessment

`sample_assessment.yaml` shows a realistic federal agency at 50% implementation. It models how to fill out the YAML and what detailed notes look like. Use it as a template — copy it, replace the content with your organization's actual control statuses, and run the validator.

---

## Citation

Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.*
DOI: `10.5281/zenodo.19553772` (copy and paste into browser address bar to access)

**Dr. Miranda Stanfield, PhD, CISA, CISM**
[www.drmirandastanfield.com](https://www.drmirandastanfield.com) · [LinkedIn](https://linkedin.com/in/mirandastanfield) · [GitHub](https://github.com/stanfieldmiranda-eng/LIAGCF)
