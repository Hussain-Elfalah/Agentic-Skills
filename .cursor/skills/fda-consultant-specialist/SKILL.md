---
name: fda-consultant-specialist
description: FDA regulatory consultant for medical device companies. Provides 510(k)/PMA/De Novo pathway guidance, QSR (21 CFR 820) compliance, HIPAA assessments, and device cybersecurity. Use when user mentions FDA submission, 510(k), PMA, De Novo, QSR, premarket, predicate device, substantial equivalence, HIPAA medical device, or FDA cybersecurity.
---

# FDA Consultant Specialist

FDA regulatory consulting for medical device manufacturers covering submission pathways, Quality System Regulation (QSR), HIPAA compliance, and device cybersecurity requirements.

## Table of Contents

- [FDA Pathway Selection](#fda-pathway-selection)
- [510(k) Submission Process](#510k-submission-process)
- [QSR Compliance](#qsr-compliance)
- [HIPAA for Medical Devices](#hipaa-for-medical-devices)
- [Device Cybersecurity](#device-cybersecurity)
- [Resources](#resources)

---

## FDA Pathway Selection

Determine the appropriate FDA regulatory pathway based on device classification and predicate availability.

### Decision Framework

```
Predicate device exists?
â”œâ”€â”€ YES â†’ Substantially equivalent?
â”‚   â”œâ”€â”€ YES â†’ 510(k) Pathway
â”‚   â”‚   â”œâ”€â”€ No design changes â†’ Abbreviated 510(k)
â”‚   â”‚   â”œâ”€â”€ Manufacturing only â†’ Special 510(k)
â”‚   â”‚   â””â”€â”€ Design/performance â†’ Traditional 510(k)
â”‚   â””â”€â”€ NO â†’ PMA or De Novo
â””â”€â”€ NO â†’ Novel device?
    â”œâ”€â”€ Low-to-moderate risk â†’ De Novo
    â””â”€â”€ High risk (Class III) â†’ PMA
```

### Pathway Comparison

| Pathway | When to Use | Timeline | Cost |
|---------|-------------|----------|------|
| 510(k) Traditional | Predicate exists, design changes | 90 days | $21,760 |
| 510(k) Special | Manufacturing changes only | 30 days | $21,760 |
| 510(k) Abbreviated | Guidance/standard conformance | 30 days | $21,760 |
| De Novo | Novel, low-moderate risk | 150 days | $134,676 |
| PMA | Class III, no predicate | 180+ days | $425,000+ |

### Pre-Submission Strategy

1. Identify product code and classification
2. Search 510(k) database for predicates
3. Assess substantial equivalence feasibility
4. Prepare Q-Sub questions for FDA
5. Schedule Pre-Sub meeting if needed

**Reference:** See [fda_submission_guide.md](references/fda_submission_guide.md) for pathway decision matrices and submission requirements.

---

## 510(k) Submission Process

### Workflow

```
Phase 1: Planning
â”œâ”€â”€ Step 1: Identify predicate device(s)
â”œâ”€â”€ Step 2: Compare intended use and technology
â”œâ”€â”€ Step 3: Determine testing requirements
â””â”€â”€ Checkpoint: SE argument feasible?

Phase 2: Preparation
â”œâ”€â”€ Step 4: Complete performance testing
â”œâ”€â”€ Step 5: Prepare device description
â”œâ”€â”€ Step 6: Document SE comparison
â”œâ”€â”€ Step 7: Finalize labeling
â””â”€â”€ Checkpoint: All required sections complete?

Phase 3: Submission
â”œâ”€â”€ Step 8: Assemble submission package
â”œâ”€â”€ Step 9: Submit via eSTAR
â”œâ”€â”€ Step 10: Track acknowledgment
â””â”€â”€ Checkpoint: Submission accepted?

Phase 4: Review
â”œâ”€â”€ Step 11: Monitor review status
â”œâ”€â”€ Step 12: Respond to AI requests
â”œâ”€â”€ Step 13: Receive decision
â””â”€â”€ Verification: SE letter received?
```

### Required Sections (21 CFR 807.87)

| Section | Content |
|---------|---------|
| Cover Letter | Submission type, device ID, contact info |
| Form 3514 | CDRH premarket review cover sheet |
| Device Description | Physical description, principles of operation |
| Indications for Use | Form 3881, patient population, use environment |
| SE Comparison | Side-by-side comparison with predicate |
| Performance Testing | Bench, biocompatibility, electrical safety |
| Software Documentation | Level of concern, hazard analysis (IEC 62304) |
| Labeling | IFU, package labels, warnings |
| 510(k) Summary | Public summary of submission |

### Common RTA Issues

| Issue | Prevention |
|-------|------------|
| Missing user fee | Verify payment before submission |
| Incomplete Form 3514 | Review all fields, ensure signature |
| No predicate identified | Confirm K-number in FDA database |
| Inadequate SE comparison | Address all technological characteristics |

---

## QSR Compliance

Quality System Regulation (21 CFR Part 820) requirements for medical device manufacturers.

### Key Subsystems

| Section | Title | Focus |
|---------|-------|-------|
| 820.20 | Management Responsibility | Quality policy, org structure, management review |
| 820.30 | Design Controls | Input, output, review, verification, validation |
| 820.40 | Document Controls | Approval, distribution, change control |
| 820.50 | Purchasing Controls | Supplier qualification, purchasing data |
| 820.70 | Production Controls | Process validation, environmental controls |
| 820.100 | CAPA | Root cause analysis, corrective actions |
| 820.181 | Device Master Record | Specifications, procedures, acceptance criteria |

### Design Controls Workflow (820.30)

```
Step 1: Design Input
â””â”€â”€ Capture user needs, intended use, regulatory requirements
    Verification: Inputs reviewed and approved?

Step 2: Design Output
â””â”€â”€ Create specifications, drawings, software architecture
    Verification: Outputs traceable to inputs?

Step 3: Design Review
â””â”€â”€ Conduct reviews at each phase milestone
    Verification: Review records with signatures?

Step 4: Design Verification
â””â”€â”€ Perform testing against specifications
    Verification: All tests pass acceptance criteria?

Step 5: Design Validation
â””â”€â”€ Confirm device meets user needs in actual use conditions
    Verification: Validation report approved?

Step 6: Design Transfer
â””â”€â”€ Release to production with DMR complete
    Verification: Transfer checklist complete?
```

### CAPA Process (820.100)

1. **Identify**: Document nonconformity or potential problem
2. **Investigate**: Perform root cause analysis (5 Whys, Fishbone)
3. **Plan**: Define corrective/preventive actions
4. **Implement**: Execute actions, update documentation
5. **Verify**: Confirm implementation complete
6. **Effectiveness**: Monitor for recurrence (30-90 days)
7. **Close**: Management approval and closure

**Reference:** See [qsr_compliance_requirements.md](references/qsr_compliance_requirements.md) for detailed QSR implementation guidance.

---

## HIPAA for Medical Devices

HIPAA requirements for devices that create, store, transmit, or access Protected Health Information (PHI).

### Applicability

| Device Type | HIPAA Applies |
|-------------|---------------|
| Standalone diagnostic (no data transmission) | No |
| Connected device transmitting patient data | Yes |
| Device with EHR integration | Yes |
| SaMD storing patient information | Yes |
| Wellness app (no diagnosis) | Only if stores PHI |

### Required Safeguards

```
Administrative (آ§164.308)
â”œâ”€â”€ Security officer designation
â”œâ”€â”€ Risk analysis and management
â”œâ”€â”€ Workforce training
â”œâ”€â”€ Incident response procedures
â””â”€â”€ Business associate agreements

Physical (آ§164.310)
â”œâ”€â”€ Facility access controls
â”œâ”€â”€ Workstation security
â””â”€â”€ Device disposal procedures

Technical (آ§164.312)
â”œâ”€â”€ Access control (unique IDs, auto-logoff)
â”œâ”€â”€ Audit controls (logging)
â”œâ”€â”€ Integrity controls (checksums, hashes)
â”œâ”€â”€ Authentication (MFA recommended)
â””â”€â”€ Transmission security (TLS 1.2+)
```

### Risk Assessment Steps

1. Inventory all systems handling ePHI
2. Document data flows (collection, storage, transmission)
3. Identify threats and vulnerabilities
4. Assess likelihood and impact
5. Determine risk levels
6. Implement controls
7. Document residual risk

**Reference:** See [hipaa_compliance_framework.md](references/hipaa_compliance_framework.md) for implementation checklists and BAA templates.

---

## Device Cybersecurity

FDA cybersecurity requirements for connected medical devices.

### Premarket Requirements

| Element | Description |
|---------|-------------|
| Threat Model | STRIDE analysis, attack trees, trust boundaries |
| Security Controls | Authentication, encryption, access control |
| SBOM | Software Bill of Materials (CycloneDX or SPDX) |
| Security Testing | Penetration testing, vulnerability scanning |
| Vulnerability Plan | Disclosure process, patch management |

### Device Tier Classification

**Tier 1 (Higher Risk):**
- Connects to network/internet
- Cybersecurity incident could cause patient harm

**Tier 2 (Standard Risk):**
- All other connected devices

### Postmarket Obligations

1. Monitor NVD and ICS-CERT for vulnerabilities
2. Assess applicability to device components
3. Develop and test patches
4. Communicate with customers
5. Report to FDA per guidance

### Coordinated Vulnerability Disclosure

```
Researcher Report
    â†“
Acknowledgment (48 hours)
    â†“
Initial Assessment (5 days)
    â†“
Fix Development
    â†“
Coordinated Public Disclosure
```

**Reference:** See [device_cybersecurity_guidance.md](references/device_cybersecurity_guidance.md) for SBOM format examples and threat modeling templates.

---

## Resources

### scripts/

| Script | Purpose |
|--------|---------|
| `fda_submission_tracker.py` | Track 510(k)/PMA/De Novo submission milestones and timelines |
| `qsr_compliance_checker.py` | Assess 21 CFR 820 compliance against project documentation |
| `hipaa_risk_assessment.py` | Evaluate HIPAA safeguards in medical device software |

### references/

| File | Content |
|------|---------|
| `fda_submission_guide.md` | 510(k), De Novo, PMA submission requirements and checklists |
| `qsr_compliance_requirements.md` | 21 CFR 820 implementation guide with templates |
| `hipaa_compliance_framework.md` | HIPAA Security Rule safeguards and BAA requirements |
| `device_cybersecurity_guidance.md` | FDA cybersecurity requirements, SBOM, threat modeling |
| `fda_capa_requirements.md` | CAPA process, root cause analysis, effectiveness verification |

### Usage Examples

```bash
# Track FDA submission status
python scripts/fda_submission_tracker.py /path/to/project --type 510k

# Assess QSR compliance
python scripts/qsr_compliance_checker.py /path/to/project --section 820.30

# Run HIPAA risk assessment
python scripts/hipaa_risk_assessment.py /path/to/project --category technical
```
