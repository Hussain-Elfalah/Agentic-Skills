---
name: gdpr-dsgvo-expert
description: GDPR and German DSGVO compliance automation. Scans codebases for privacy risks, generates DPIA documentation, tracks data subject rights requests. Use for GDPR compliance assessments, privacy audits, data protection planning, DPIA generation, and data subject rights management.
---

# GDPR/DSGVO Expert

Tools and guidance for EU General Data Protection Regulation (GDPR) and German Bundesdatenschutzgesetz (BDSG) compliance.

---

## Table of Contents

- [Tools](#tools)
  - [GDPR Compliance Checker](#gdpr-compliance-checker)
  - [DPIA Generator](#dpia-generator)
  - [Data Subject Rights Tracker](#data-subject-rights-tracker)
- [Reference Guides](#reference-guides)
- [Workflows](#workflows)

---

## Tools

### GDPR Compliance Checker

Scans codebases for potential GDPR compliance issues including personal data patterns and risky code practices.

```bash
# Scan a project directory
python scripts/gdpr_compliance_checker.py /path/to/project

# JSON output for CI/CD integration
python scripts/gdpr_compliance_checker.py . --json --output report.json
```

**Detects:**
- Personal data patterns (email, phone, IP addresses)
- Special category data (health, biometric, religion)
- Financial data (credit cards, IBAN)
- Risky code patterns:
  - Logging personal data
  - Missing consent mechanisms
  - Indefinite data retention
  - Unencrypted sensitive data
  - Disabled deletion functionality

**Output:**
- Compliance score (0-100)
- Risk categorization (critical, high, medium)
- Prioritized recommendations with GDPR article references

---

### DPIA Generator

Generates Data Protection Impact Assessment documentation following Art. 35 requirements.

```bash
# Get input template
python scripts/dpia_generator.py --template > input.json

# Generate DPIA report
python scripts/dpia_generator.py --input input.json --output dpia_report.md
```

**Features:**
- Automatic DPIA threshold assessment
- Risk identification based on processing characteristics
- Legal basis requirements documentation
- Mitigation recommendations
- Markdown report generation

**DPIA Triggers Assessed:**
- Systematic monitoring (Art. 35(3)(c))
- Large-scale special category data (Art. 35(3)(b))
- Automated decision-making (Art. 35(3)(a))
- WP29 high-risk criteria

---

### Data Subject Rights Tracker

Manages data subject rights requests under GDPR Articles 15-22.

```bash
# Add new request
python scripts/data_subject_rights_tracker.py add \
  --type access --subject "John Doe" --email "john@example.com"

# List all requests
python scripts/data_subject_rights_tracker.py list

# Update status
python scripts/data_subject_rights_tracker.py status --id DSR-202601-0001 --update verified

# Generate compliance report
python scripts/data_subject_rights_tracker.py report --output compliance.json

# Generate response template
python scripts/data_subject_rights_tracker.py template --id DSR-202601-0001
```

**Supported Rights:**

| Right | Article | Deadline |
|-------|---------|----------|
| Access | Art. 15 | 30 days |
| Rectification | Art. 16 | 30 days |
| Erasure | Art. 17 | 30 days |
| Restriction | Art. 18 | 30 days |
| Portability | Art. 20 | 30 days |
| Objection | Art. 21 | 30 days |
| Automated decisions | Art. 22 | 30 days |

**Features:**
- Deadline tracking with overdue alerts
- Identity verification workflow
- Response template generation
- Compliance reporting

---

## Reference Guides

### GDPR Compliance Guide
`references/gdpr_compliance_guide.md`

Comprehensive implementation guidance covering:
- Legal bases for processing (Art. 6)
- Special category requirements (Art. 9)
- Data subject rights implementation
- Accountability requirements (Art. 30)
- International transfers (Chapter V)
- Breach notification (Art. 33-34)

### German BDSG Requirements
`references/german_bdsg_requirements.md`

German-specific requirements including:
- DPO appointment threshold (آ§ 38 BDSG - 20+ employees)
- Employment data processing (آ§ 26 BDSG)
- Video surveillance rules (آ§ 4 BDSG)
- Credit scoring requirements (آ§ 31 BDSG)
- State data protection laws (Landesdatenschutzgesetze)
- Works council co-determination rights

### DPIA Methodology
`references/dpia_methodology.md`

Step-by-step DPIA process:
- Threshold assessment criteria
- WP29 high-risk indicators
- Risk assessment methodology
- Mitigation measure categories
- DPO and supervisory authority consultation
- Templates and checklists

---

## Workflows

### Workflow 1: New Processing Activity Assessment

```
Step 1: Run compliance checker on codebase
        â†’ python scripts/gdpr_compliance_checker.py /path/to/code

Step 2: Review findings and compliance score
        â†’ Address critical and high issues

Step 3: Determine if DPIA required
        â†’ Check references/dpia_methodology.md threshold criteria

Step 4: If DPIA required, generate assessment
        â†’ python scripts/dpia_generator.py --template > input.json
        â†’ Fill in processing details
        â†’ python scripts/dpia_generator.py --input input.json --output dpia.md

Step 5: Document in records of processing activities
```

### Workflow 2: Data Subject Request Handling

```
Step 1: Log request in tracker
        â†’ python scripts/data_subject_rights_tracker.py add --type [type] ...

Step 2: Verify identity (proportionate measures)
        â†’ python scripts/data_subject_rights_tracker.py status --id [ID] --update verified

Step 3: Gather data from systems
        â†’ python scripts/data_subject_rights_tracker.py status --id [ID] --update in_progress

Step 4: Generate response
        â†’ python scripts/data_subject_rights_tracker.py template --id [ID]

Step 5: Send response and complete
        â†’ python scripts/data_subject_rights_tracker.py status --id [ID] --update completed

Step 6: Monitor compliance
        â†’ python scripts/data_subject_rights_tracker.py report
```

### Workflow 3: German BDSG Compliance Check

```
Step 1: Determine if DPO required
        â†’ 20+ employees processing personal data automatically
        â†’ OR processing requires DPIA
        â†’ OR business involves data transfer/market research

Step 2: If employees involved, review آ§ 26 BDSG
        â†’ Document legal basis for employee data
        â†’ Check works council requirements

Step 3: If video surveillance, comply with آ§ 4 BDSG
        â†’ Install signage
        â†’ Document necessity
        â†’ Limit retention

Step 4: Register DPO with supervisory authority
        â†’ See references/german_bdsg_requirements.md for authority list
```

---

## Key GDPR Concepts

### Legal Bases (Art. 6)

- **Consent**: Marketing, newsletters, analytics (must be freely given, specific, informed)
- **Contract**: Order fulfillment, service delivery
- **Legal obligation**: Tax records, employment law
- **Legitimate interests**: Fraud prevention, security (requires balancing test)

### Special Category Data (Art. 9)

Requires explicit consent or Art. 9(2) exception:
- Health data
- Biometric data
- Racial/ethnic origin
- Political opinions
- Religious beliefs
- Trade union membership
- Genetic data
- Sexual orientation

### Data Subject Rights

All rights must be fulfilled within **30 days** (extendable to 90 for complex requests):
- **Access**: Provide copy of data and processing information
- **Rectification**: Correct inaccurate data
- **Erasure**: Delete data (with exceptions for legal obligations)
- **Restriction**: Limit processing while issues are resolved
- **Portability**: Provide data in machine-readable format
- **Object**: Stop processing based on legitimate interests

### German BDSG Additions

| Topic | BDSG Section | Key Requirement |
|-------|--------------|-----------------|
| DPO threshold | آ§ 38 | 20+ employees = mandatory DPO |
| Employment | آ§ 26 | Detailed employee data rules |
| Video | آ§ 4 | Signage and proportionality |
| Scoring | آ§ 31 | Explainable algorithms |
