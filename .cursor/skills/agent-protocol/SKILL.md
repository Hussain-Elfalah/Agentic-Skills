---
name: agent-protocol
description: Inter-agent communication protocol for C-suite agent teams. Defines invocation syntax, loop prevention, isolation rules, and response formats. Use when C-suite agents need to query each other, coordinate cross-functional analysis, or run board meetings with multiple agent roles.
---

# Inter-Agent Protocol

How C-suite agents talk to each other. Rules that prevent chaos, loops, and circular reasoning.

## Keywords
agent protocol, inter-agent communication, agent invocation, agent orchestration, multi-agent, c-suite coordination, agent chain, loop prevention, agent isolation, board meeting protocol

## Invocation Syntax

Any agent can query another using:

```
[INVOKE:role|question]
```

**Examples:**
```
[INVOKE:cfo|What's the burn rate impact of hiring 5 engineers in Q3?]
[INVOKE:cto|Can we realistically ship this feature by end of quarter?]
[INVOKE:chro|What's our typical time-to-hire for senior engineers?]
[INVOKE:cro|What does our pipeline look like for the next 90 days?]
```

**Valid roles:** `ceo`, `cfo`, `cro`, `cmo`, `cpo`, `cto`, `chro`, `coo`, `ciso`

## Response Format

Invoked agents respond using this structure:

```
[RESPONSE:role]
Key finding: [one line â€” the actual answer]
Supporting data:
  - [data point 1]
  - [data point 2]
  - [data point 3 â€” optional]
Confidence: [high | medium | low]
Caveat: [one line â€” what could make this wrong]
[/RESPONSE]
```

**Example:**
```
[RESPONSE:cfo]
Key finding: Hiring 5 engineers in Q3 extends runway from 14 to 9 months at current burn.
Supporting data:
  - Current monthly burn: $280K â†’ increases to ~$380K (+$100K fully loaded)
  - ARR needed to offset: ~$1.2M additional within 12 months
  - Current pipeline covers 60% of that target
Confidence: medium
Caveat: Assumes 3-month ramp and no change in revenue trajectory.
[/RESPONSE]
```

## Loop Prevention (Hard Rules)

These rules are enforced unconditionally. No exceptions.

### Rule 1: No Self-Invocation
An agent cannot invoke itself.
```
â‌Œ CFO â†’ [INVOKE:cfo|...] â€” BLOCKED
```

### Rule 2: Maximum Depth = 2
Chains can go Aâ†’Bâ†’C. The third hop is blocked.
```
âœ… CRO â†’ CFO â†’ COO (depth 2)
â‌Œ CRO â†’ CFO â†’ COO â†’ CHRO (depth 3 â€” BLOCKED)
```

### Rule 3: No Circular Calls
If agent A called agent B, agent B cannot call agent A in the same chain.
```
âœ… CRO â†’ CFO â†’ CMO
â‌Œ CRO â†’ CFO â†’ CRO (circular â€” BLOCKED)
```

### Rule 4: Chain Tracking
Each invocation carries its call chain. Format:
```
[CHAIN: cro â†’ cfo â†’ coo]
```
Agents check this chain before responding with another invocation.

**When blocked:** Return this instead of invoking:
```
[BLOCKED: cannot invoke cfo â€” circular call detected in chain croâ†’cfo]
State assumption used instead: [explicit assumption the agent is making]
```

## Isolation Rules

### Board Meeting Phase 2 (Independent Analysis)
**NO invocations allowed.** Each role forms independent views before cross-pollination.
- Reason: prevent anchoring and groupthink
- Duration: entire Phase 2 analysis period
- If an agent needs data from another role: state explicit assumption, flag it with `[ASSUMPTION: ...]`

### Board Meeting Phase 3 (Critic Role)
Executive Mentor can **reference** other roles' outputs but **cannot invoke** them.
- Reason: critique must be independent of new data requests
- Allowed: "The CFO's projection assumes X, which contradicts the CRO's pipeline data"
- Not allowed: `[INVOKE:cfo|...]` during critique phase

### Outside Board Meetings
Invocations are allowed freely, subject to loop prevention rules above.

## When to Invoke vs When to Assume

**Invoke when:**
- The question requires domain-specific data you don't have
- An error here would materially change the recommendation
- The question is cross-functional by nature (e.g., hiring impact on both budget and capacity)

**Assume when:**
- The data is directionally clear and precision isn't critical
- You're in Phase 2 isolation (always assume, never invoke)
- The chain is already at depth 2
- The question is minor compared to your main analysis

**When assuming, always state it:**
```
[ASSUMPTION: runway ~12 months based on typical Series A burn profile â€” not verified with CFO]
```

## Conflict Resolution

When two invoked agents give conflicting answers:

1. **Flag the conflict explicitly:**
   ```
   [CONFLICT: CFO projects 14-month runway; CRO expects pipeline to close 80% â†’ implies 18+ months]
   ```
2. **State the resolution approach:**
   - Conservative: use the worse case
   - Probabilistic: weight by confidence scores
   - Escalate: flag for human decision
3. **Never silently pick one** â€” surface the conflict to the user.

## Broadcast Pattern (Crisis / CEO)

CEO can broadcast to all roles simultaneously:
```
[BROADCAST:all|What's the impact if we miss the fundraise?]
```

Responses come back independently (no agent sees another's response before forming its own). Aggregate after all respond.

## Quick Reference

| Rule | Behavior |
|------|----------|
| Self-invoke | â‌Œ Always blocked |
| Depth > 2 | â‌Œ Blocked, state assumption |
| Circular | â‌Œ Blocked, state assumption |
| Phase 2 isolation | â‌Œ No invocations |
| Phase 3 critique | â‌Œ Reference only, no invoke |
| Conflict | âœ… Surface it, don't hide it |
| Assumption | âœ… Always explicit with `[ASSUMPTION: ...]` |

## Internal Quality Loop (before anything reaches the founder)

No role presents to the founder without passing through this verification loop. The founder sees polished, verified output â€” not first drafts.

### Step 1: Self-Verification (every role, every time)

Before presenting, every role runs this internal checklist:

```
SELF-VERIFY CHECKLIST:
â–، Source Attribution â€” Where did each data point come from?
  âœ… "ARR is $2.1M (from CRO pipeline report, Q4 actuals)"
  â‌Œ "ARR is around $2M" (no source, vague)

â–، Assumption Audit â€” What am I assuming vs what I verified?
  Tag every assumption: [VERIFIED: checked against data] or [ASSUMED: not verified]
  If >50% of findings are ASSUMED â†’ flag low confidence

â–، Confidence Score â€” How sure am I on each finding?
  ًںں¢ High: verified data, established pattern, multiple sources
  ًںں، Medium: single source, reasonable inference, some uncertainty
  ًں”´ Low: assumption-based, limited data, first-time analysis

â–، Contradiction Check â€” Does this conflict with known context?
  Check against company-context.md and recent decisions in decision-log
  If it contradicts a past decision â†’ flag explicitly

â–، "So What?" Test â€” Does every finding have a business consequence?
  If you can't answer "so what?" in one sentence â†’ cut it
```

### Step 2: Peer Verification (cross-functional validation)

When a recommendation impacts another role's domain, that role validates BEFORE presenting.

| If your recommendation involves... | Validate with... | They check... |
|-------------------------------------|-------------------|---------------|
| Financial numbers or budget | CFO | Math, runway impact, budget reality |
| Revenue projections | CRO | Pipeline backing, historical accuracy |
| Headcount or hiring | CHRO | Market reality, comp feasibility, timeline |
| Technical feasibility or timeline | CTO | Engineering capacity, technical debt load |
| Operational process changes | COO | Capacity, dependencies, scaling impact |
| Customer-facing changes | CRO + CPO | Churn risk, product roadmap conflict |
| Security or compliance claims | CISO | Actual posture, regulation requirements |
| Market or positioning claims | CMO | Data backing, competitive reality |

**Peer validation format:**
```
[PEER-VERIFY:cfo]
Validated: âœ… Burn rate calculation correct
Adjusted: âڑ ï¸ڈ Hiring timeline should be Q3 not Q2 (budget constraint)
Flagged: ًں”´ Missing equity cost in total comp projection
[/PEER-VERIFY]
```

**Skip peer verification when:**
- Single-domain question with no cross-functional impact
- Time-sensitive proactive alert (send alert, verify after)
- Founder explicitly asked for a quick take

### Step 3: Critic Pre-Screen (high-stakes decisions only)

For decisions that are **irreversible, high-cost, or bet-the-company**, the Executive Mentor pre-screens before the founder sees it.

**Triggers for pre-screen:**
- Involves spending > 20% of remaining runway
- Affects >30% of the team (layoffs, reorg)
- Changes company strategy or direction
- Involves external commitments (fundraising terms, partnerships, M&A)
- Any recommendation where all roles agree (suspicious consensus)

**Pre-screen output:**
```
[CRITIC-SCREEN]
Weakest point: [The single biggest vulnerability in this recommendation]
Missing perspective: [What nobody considered]
If wrong, the cost is: [Quantified downside]
Proceed: âœ… With noted risks | âڑ ï¸ڈ After addressing [specific gap] | ًں”´ Rethink
[/CRITIC-SCREEN]
```

### Step 4: Course Correction (after founder feedback)

The loop doesn't end at delivery. After the founder responds:

```
FOUNDER FEEDBACK LOOP:
1. Founder approves â†’ log decision (Layer 2), assign actions
2. Founder modifies â†’ update analysis with corrections, re-verify changed parts
3. Founder rejects â†’ log rejection with DO_NOT_RESURFACE, understand WHY
4. Founder asks follow-up â†’ deepen analysis on specific point, re-verify

POST-DECISION REVIEW (30/60/90 days):
- Was the recommendation correct?
- What did we miss?
- Update company-context.md with what we learned
- If wrong â†’ document the lesson, adjust future analysis
```

### Verification Level by Stakes

| Stakes | Self-Verify | Peer-Verify | Critic Pre-Screen |
|--------|-------------|-------------|-------------------|
| Low (informational) | âœ… Required | â‌Œ Skip | â‌Œ Skip |
| Medium (operational) | âœ… Required | âœ… Required | â‌Œ Skip |
| High (strategic) | âœ… Required | âœ… Required | âœ… Required |
| Critical (irreversible) | âœ… Required | âœ… Required | âœ… Required + board meeting |

### What Changes in the Output Format

The verified output adds confidence and source information:

```
BOTTOM LINE
[Answer] â€” Confidence: ًںں¢ High

WHAT
â€¢ [Finding 1] [VERIFIED: Q4 actuals] ًںں¢
â€¢ [Finding 2] [VERIFIED: CRO pipeline data] ًںں¢  
â€¢ [Finding 3] [ASSUMED: based on industry benchmarks] ًںں،

PEER-VERIFIED BY: CFO (math âœ…), CTO (timeline âڑ ï¸ڈ adjusted to Q3)
```

---

## User Communication Standard

All C-suite output to the founder follows ONE format. No exceptions. The founder is the decision-maker â€” give them results, not process.

### Standard Output (single-role response)

```
â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ

ًں“ٹ [ROLE] â€” [Topic]

BOTTOM LINE
[One sentence. The answer. No preamble.]

WHAT
â€¢ [Finding 1 â€” most critical]
â€¢ [Finding 2]
â€¢ [Finding 3]
(Max 5 bullets. If more needed â†’ reference doc.)

WHY THIS MATTERS
[1-2 sentences. Business impact. Not theory â€” consequence.]

HOW TO ACT
1. [Action] â†’ [Owner] â†’ [Deadline]
2. [Action] â†’ [Owner] â†’ [Deadline]
3. [Action] â†’ [Owner] â†’ [Deadline]

âڑ ï¸ڈ RISKS (if any)
â€¢ [Risk + what triggers it]

ًں”‘ YOUR DECISION (if needed)
Option A: [Description] â€” [Trade-off]
Option B: [Description] â€” [Trade-off]
Recommendation: [Which and why, in one line]

ًں“ژ DETAIL: [reference doc or script output for deep-dive]

â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ
```

### Proactive Alert (unsolicited â€” triggered by context)

```
â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ

ًںڑ© [ROLE] â€” Proactive Alert

WHAT I NOTICED
[What triggered this â€” specific, not vague]

WHY IT MATTERS
[Business consequence if ignored â€” in dollars, time, or risk]

RECOMMENDED ACTION
[Exactly what to do, who does it, by when]

URGENCY: ًں”´ Act today | ًںں، This week | âڑھ Next review

â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ
```

### Board Meeting Output (multi-role synthesis)

```
â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ

ًں“‹ BOARD MEETING â€” [Date] â€” [Agenda Topic]

DECISION REQUIRED
[Frame the decision in one sentence]

PERSPECTIVES
  CEO: [one-line position]
  CFO: [one-line position]
  CRO: [one-line position]
  [... only roles that contributed]

WHERE THEY AGREE
â€¢ [Consensus point 1]
â€¢ [Consensus point 2]

WHERE THEY DISAGREE
â€¢ [Conflict] â€” CEO says X, CFO says Y
â€¢ [Conflict] â€” CRO says X, CPO says Y

CRITIC'S VIEW (Executive Mentor)
[The uncomfortable truth nobody else said]

RECOMMENDED DECISION
[Clear recommendation with rationale]

ACTION ITEMS
1. [Action] â†’ [Owner] â†’ [Deadline]
2. [Action] â†’ [Owner] â†’ [Deadline]
3. [Action] â†’ [Owner] â†’ [Deadline]

ًں”‘ YOUR CALL
[Options if you disagree with the recommendation]

â”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پâ”پ
```

### Communication Rules (non-negotiable)

1. **Bottom line first.** Always. The founder's time is the scarcest resource.
2. **Results and decisions only.** No process narration ("First I analyzed..."). No thinking out loud.
3. **What + Why + How.** Every finding explains WHAT it is, WHY it matters (business impact), and HOW to act on it.
4. **Max 5 bullets per section.** Longer = reference doc.
5. **Actions have owners and deadlines.** "We should consider" is banned. Who does what by when.
6. **Decisions framed as options.** Not "what do you think?" â€” "Option A or B, here's the trade-off, here's my recommendation."
7. **The founder decides.** Roles recommend. The founder approves, modifies, or rejects. Every output respects this hierarchy.
8. **Risks are concrete.** Not "there might be risks" â€” "if X happens, Y breaks, costing $Z."
9. **No jargon without explanation.** If you use a term, explain it on first use.
10. **Silence is an option.** If there's nothing to report, don't fabricate updates.

## Reference
- `references/invocation-patterns.md` â€” common cross-functional patterns with examples
