# LIAGCF Control Validator

Validates your organization's AI governance posture against the Lifecycle-Integrated AI Governance Control Framework (LIAGCF). Fill out a YAML file documenting your implemented controls and the validator produces a gap analysis report — by lifecycle phase, RMF function, and control category.

Two output options: a text report in your terminal, or a styled HTML report that opens in your browser.

---

## What You Need

- Python 3 (check by running `python3 --version` in your terminal)
- PyYAML library

Install PyYAML if you don't have it:
```
pip3 install pyyaml
```

---

## Quick Start

**1. Download these two files from this repo:**
- `scripts/validate_liagcf.py`
- `examples/sample_assessment.yaml`

Put them in the same folder on your computer.

**2. Open Terminal** (Mac: press `Command + Space`, type Terminal, hit Enter)

**3. Navigate to your folder:**
```
cd ~/Downloads
```

**4. Run the validator:**
```
python3 validate_liagcf.py --input sample_assessment.yaml
```

You'll see a full gap analysis report in your terminal.

---

## Output Options

**Text report in terminal (default):**
```
python3 validate_liagcf.py --input sample_assessment.yaml
```

**Save text report to a file:**
```
python3 validate_liagcf.py --input sample_assessment.yaml --output report.txt
```

**HTML report — opens in your browser automatically:**
```
python3 validate_liagcf.py --input sample_assessment.yaml --format html
```

**HTML report saved to a specific file:**
```
python3 validate_liagcf.py --input sample_assessment.yaml --format html --output my_report.html
```

The HTML report includes color-coded control status, coverage bars by RMF function and lifecycle phase, and a priority gaps section. It can be printed or shared as a standalone file.

---

## Assessing Your Own Organization

The `sample_assessment.yaml` file is a completed example using a fictional federal agency. To assess your own organization:

**1. Copy the sample file and rename it:**
```
cp sample_assessment.yaml my_org_assessment.yaml
```

**2. Open it in any text editor and update the header:**
```yaml
organization: "Your Organization Name"
system_name: "Your AI System Name"
assessor: "Your Name or Team"
date: "2026-06-10"
```

**3. For each of the 16 controls, set a status:**

| Status | Meaning |
|--------|---------|
| `implemented` | Control is fully in place with documented evidence |
| `partial` | Control is partially implemented; gaps remain |
| `planned` | Control is on the roadmap but not yet active |
| `not-implemented` | Control has not been addressed |

**4. Add notes explaining your status (optional but recommended):**
```yaml
- id: A-1
  status: implemented
  notes: AI Governance Charter approved by CISO. Last reviewed March 2026.
```

**5. Run the validator against your file:**
```
python3 validate_liagcf.py --input my_org_assessment.yaml --format html
```

---

## The 16 LIAGCF Controls

| ID | Category | Control Objective | RMF Function | Lifecycle Phase |
|----|----------|-------------------|--------------|-----------------|
| A-1 | Administrative | Establish a formal enterprise AI governance policy and scope | GOVERN | Strategy & Design |
| A-2 | Administrative | Define AI accountability, decision rights, and risk ownership | GOVERN | Strategy & Design |
| A-3 | Administrative | Establish third-party AI risk governance policies | GOVERN | Procurement |
| A-4 | Administrative | Define enterprise AI audit and governance review cadence | GOVERN | Operations |
| A-5 | Administrative | Require AI risk assessments prior to deployment | MAP | Development |
| A-6 | Administrative | Categorize AI systems by risk level, use context, and affected population | MAP | Strategy & Design |
| T-1 | Technical | Identify and assess potential for discriminatory or disparate impact outcomes | MAP | Development |
| T-2 | Technical | Map data provenance, lineage, and quality risks for training datasets | MAP | Data Preparation |
| T-3 | Technical | Validate AI models prior to production release | MEASURE | Development |
| T-4 | Technical | Monitor model performance and detect drift | MEASURE | Operations |
| T-5 | Technical | Log AI system activity for traceability and auditability | MEASURE | Operations |
| O-1 | Operational | Conduct periodic AI governance and risk reviews | MEASURE | Operations |
| O-2 | Operational | Enforce access controls on AI training and operational data | MANAGE | Data Preparation / Operations |
| O-3 | Operational | Protect AI models from unauthorized modification | MANAGE | Operations |
| O-4 | Operational | Execute AI incident response playbooks | MANAGE | Operations |
| O-5 | Operational | Retire AI systems exceeding defined risk tolerance | MANAGE | Retirement |

---

## Troubleshooting

**"command not found" when running pip3:**
Install Python from [https://python.org](https://python.org), then try again.

**"No such file or directory" error:**
Make sure you navigated to the right folder in Terminal. Run `ls` to see what files are in your current location.

**"could not parse YAML file" error:**
YAML is sensitive to indentation. Make sure you're using spaces, not tabs, and that each entry follows the format in the sample file exactly.

**Duplicate control ID error:**
Each control ID (A-1, T-2, etc.) can only appear once in your assessment file. Remove the duplicate entry.

---

## Citation

Stanfield, M. (2026). Evaluating control-based AI governance in cybersecurity GRC programs: An expert assessment study. *RAIS Conference Proceedings, March 12–13, 2026.*
DOI: `10.5281/zenodo.19553772` (copy and paste into browser address bar to access)

**Dr. Miranda Stanfield, PhD, CISA, CISM**
[www.drmirandastanfield.com](https://www.drmirandastanfield.com) · [LinkedIn](https://linkedin.com/in/mirandastanfield)
