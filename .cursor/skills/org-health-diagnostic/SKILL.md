---
name: org-health-diagnostic
description: Cross-functional organizational health check combining signals from all C-suite roles. Scores 8 dimensions on a traffic-light scale with drill-down recommendations. Use when assessing overall company health, preparing for board reviews, identifying at-risk functions, or when user mentions org health, health check, or health dashboard.
---

# Org Health Diagnostic

Eight dimensions. Traffic lights. Real benchmarks. Surfaces the problems you don't know you have.

## Keywords
org health, organizational health, health diagnostic, health dashboard, health check, company health, functional health, team health, startup health, health scorecard, health assessment, risk dashboard

## Quick Start

```bash
python scripts/health_scorer.py        # Guided CLI â€” enter metrics, get scored dashboard
python scripts/health_scorer.py --json # Output raw JSON for integration
```

Or describe your metrics:
```
/health [paste your key metrics or answer prompts]
/health:dimension [financial|revenue|product|engineering|people|ops|security|market]
```

## The 8 Dimensions

### 1. ًں’° Financial Health (CFO)
**What it measures:** Can we fund operations and invest in growth?

Key metrics:
- **Runway** â€” months at current burn (Green: >12, Yellow: 6-12, Red: <6)
- **Burn multiple** â€” net burn / net new ARR (Green: <1.5x, Yellow: 1.5-2.5x, Red: >2.5x)
- **Gross margin** â€” SaaS target: >65% (Green: >70%, Yellow: 55-70%, Red: <55%)
- **MoM growth rate** â€” contextual by stage (see benchmarks)
- **Revenue concentration** â€” top customer % of ARR (Green: <15%, Yellow: 15-25%, Red: >25%)

### 2. ًں“ˆ Revenue Health (CRO)
**What it measures:** Are customers staying, growing, and recommending us?

Key metrics:
- **NRR (Net Revenue Retention)** â€” Green: >110%, Yellow: 100-110%, Red: <100%
- **Logo churn rate (annualized)** â€” Green: <5%, Yellow: 5-10%, Red: >10%
- **Pipeline coverage (next quarter)** â€” Green: >3x, Yellow: 2-3x, Red: <2x
- **CAC payback period** â€” Green: <12 months, Yellow: 12-18, Red: >18 months
- **Average ACV trend** â€” directional: growing, flat, declining

### 3. ًںڑ€ Product Health (CPO)
**What it measures:** Do customers love and use the product?

Key metrics:
- **NPS** â€” Green: >40, Yellow: 20-40, Red: <20
- **DAU/MAU ratio** â€” engagement proxy (Green: >40%, Yellow: 20-40%, Red: <20%)
- **Core feature adoption** â€” % of users using primary value feature (Green: >60%)
- **Time-to-value** â€” days from signup to first core action (lower is better)
- **Customer satisfaction (CSAT)** â€” Green: >4.2/5, Yellow: 3.5-4.2, Red: <3.5

### 4. âڑ™ï¸ڈ Engineering Health (CTO)
**What it measures:** Can we ship reliably and sustain velocity?

Key metrics:
- **Deployment frequency** â€” Green: daily, Yellow: weekly, Red: monthly or less
- **Change failure rate** â€” % of deployments causing incidents (Green: <5%, Red: >15%)
- **Mean time to recovery (MTTR)** â€” Green: <1 hour, Yellow: 1-4 hours, Red: >4 hours
- **Tech debt ratio** â€” % of sprint capacity on debt (Green: <20%, Yellow: 20-35%, Red: >35%)
- **Incident frequency** â€” P0/P1 per month (Green: <2, Yellow: 2-5, Red: >5)

### 5. ًں‘¥ People Health (CHRO)
**What it measures:** Is the team stable, engaged, and growing?

Key metrics:
- **Regrettable attrition (annualized)** â€” Green: <10%, Yellow: 10-20%, Red: >20%
- **Engagement score** â€” (eNPS or similar; Green: >30, Yellow: 0-30, Red: <0)
- **Time-to-fill (avg days)** â€” Green: <45, Yellow: 45-90, Red: >90
- **Manager-to-IC ratio** â€” Green: 1:5â€“1:8, Yellow: 1:3â€“1:5 or 1:8â€“1:12, Red: outside
- **Internal promotion rate** â€” at least 25-30% of senior roles filled internally

### 6. ًں”„ Operational Health (COO)
**What it measures:** Are we executing our strategy with discipline?

Key metrics:
- **OKR completion rate** â€” % of key results hitting target (Green: >70%, Yellow: 50-70%, Red: <50%)
- **Decision cycle time** â€” days from decision needed to decision made (Green: <48h, Yellow: 48h-1w)
- **Meeting effectiveness** â€” % of meetings with clear outcome (qualitative)
- **Process maturity** â€” level 1-5 scale (see COO advisor)
- **Cross-functional initiative completion** â€” % on time, on scope

### 7. ًں”’ Security Health (CISO)
**What it measures:** Are we protecting customers and maintaining compliance?

Key metrics:
- **Security incidents (last 90 days)** â€” Green: 0, Yellow: 1-2 minor, Red: 1+ major
- **Compliance status** â€” certifications current/in-progress vs. overdue
- **Vulnerability remediation SLA** â€” % of critical CVEs patched within SLA (Green: 100%)
- **Security training completion** â€” % of team current (Green: >95%)
- **Pen test recency** â€” Green: <12 months, Yellow: 12-24, Red: >24 months

### 8. ًں“£ Market Health (CMO)
**What it measures:** Are we winning in the market and growing efficiently?

Key metrics:
- **CAC trend** â€” improving, flat, or worsening QoQ
- **Organic vs paid lead mix** â€” more organic = healthier (less fragile)
- **Win rate** â€” % of qualified opportunities closed-won (Green: >25%, Yellow: 15-25%, Red: <15%)
- **Competitive win rate** â€” against primary competitors specifically
- **Brand NPS** â€” awareness + preference scores in ICP

---

## Scoring & Traffic Lights

Each dimension is scored 1-10 with traffic light:
- ًںں¢ **Green (7-10):** Healthy â€” maintain and optimize
- ًںں، **Yellow (4-6):** Watch â€” trend matters; improving or declining?
- ًں”´ **Red (1-3):** Action required â€” address within 30 days

**Overall Health Score:**
Weighted average by company stage (see `references/health-benchmarks.md` for weights).

---

## Dimension Interactions (Why One Problem Creates Another)

| If this dimension is red... | Watch these dimensions next |
|-----------------------------|----------------------------|
| Financial Health | People (freeze hiring) â†’ Engineering (freeze infra) â†’ Product (cut scope) |
| Revenue Health | Financial (cash gap) â†’ People (attrition risk) â†’ Market (lose positioning) |
| People Health | Engineering (velocity drops) â†’ Product (quality drops) â†’ Revenue (churn rises) |
| Engineering Health | Product (features slip) â†’ Revenue (deals stall on product) |
| Product Health | Revenue (NRR drops, churn rises) â†’ Market (CAC rises; referrals dry up) |
| Operational Health | All dimensions degrade over time (execution failure cascades everywhere) |

---

## Dashboard Output Format

```
ORG HEALTH DIAGNOSTIC â€” [Company] â€” [Date]
Stage: [Seed/A/B/C]   Overall: [Score]/10   Trend: [â†‘ Improving / â†’ Stable / â†“ Declining]

DIMENSION SCORES
â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ
ًں’° Financial    ًںں¢ 8.2  Runway 14mo, burn 1.6x â€” strong
ًں“ˆ Revenue      ًںں، 5.8  NRR 104%, pipeline thin (1.8x coverage)
ًںڑ€ Product      ًںں¢ 7.4  NPS 42, DAU/MAU 38%
âڑ™ï¸ڈ  Engineering  ًںں، 5.2  Debt at 30%, MTTR 3.2h
ًں‘¥ People       ًں”´ 3.8  Attrition 24%, eng morale low
ًں”„ Operations   ًںں، 6.0  OKR 65% completion
ًں”’ Security     ًںں¢ 7.8  SOC 2 Type II complete, 0 incidents
ًں“£ Market       ًںں، 5.5  CAC rising, win rate dropped to 22%
â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ

TOP PRIORITIES
ًں”´ [1] People: attrition at 24% â€” engineering velocity will drop in 60 days
   Action: CHRO + CEO to run retention audit; target top 5 at-risk this week
ًںں، [2] Revenue: pipeline coverage at 1.8x â€” Q+1 miss risk is high
   Action: CRO to add 3 qualified opps within 30 days or shift forecast down
ًںں، [3] Engineering: tech debt at 30% of sprint â€” shipping will slow by Q3
   Action: CTO to propose debt sprint plan; COO to protect capacity

WATCH
â†’ People â†’ Engineering cascade risk if attrition continues (see dimension interactions)
```

---

## Graceful Degradation

You don't need all metrics to run a diagnostic. The tool handles partial data:
- Missing metric â†’ excluded from score, flagged as "[data needed]"
- Score still valid for available dimensions
- Report flags which gaps to fill for next cycle

## References
- `references/health-benchmarks.md` â€” benchmarks by stage (Seed, A, B, C)
- `scripts/health_scorer.py` â€” CLI scoring tool with traffic light output
