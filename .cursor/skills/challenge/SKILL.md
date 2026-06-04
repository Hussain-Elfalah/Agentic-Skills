---
name: challenge
description: Pre-mortem plan analysis. Imagine the plan failed 12 months from now and work backwards to find the weaknesses. Surfaces assumptions, dependencies, and execution risks before committing resources. Use when before significant resource commitment, before presenting to a board or investors, when feedback has been one-sidedly positive, or when there is pressure to move fast and figure it out later.
---

# /em:challenge â€” Pre-Mortem Plan Analysis

**Command:** `/em:challenge <plan>`

Systematically finds weaknesses in any plan before reality does. Not to kill the plan â€” to make it survive contact with reality.

---

## The Core Idea

Most plans fail for predictable reasons. Not bad luck â€” bad assumptions. Overestimated demand. Underestimated complexity. Dependencies nobody questioned. Timing that made sense in a spreadsheet but not in the real world.

The pre-mortem technique: **imagine it's 12 months from now and this plan failed spectacularly. Now work backwards. Why?**

That's not pessimism. It's how you build something that doesn't collapse.

---

## When to Run a Challenge

- Before committing significant resources to a plan
- Before presenting to the board or investors
- When you notice you're only hearing positive feedback about the plan
- When the plan requires multiple external dependencies to align
- When there's pressure to move fast and "figure it out later"
- When you feel excited about the plan (excitement is a signal to scrutinize harder)

---

## The Challenge Framework

### Step 1: Extract Core Assumptions
Before you can test a plan, you need to surface everything it assumes to be true.

For each section of the plan, ask:
- What has to be true for this to work?
- What are we assuming about customer behavior?
- What are we assuming about competitor response?
- What are we assuming about our own execution capability?
- What external factors does this depend on?

**Common assumption categories:**
- **Market assumptions** â€” size, growth rate, customer willingness to pay, buying cycle
- **Execution assumptions** â€” team capacity, velocity, no major hires needed
- **Customer assumptions** â€” they have the problem, they know they have it, they'll pay to solve it
- **Competitive assumptions** â€” incumbents won't respond, no new entrant, moat holds
- **Financial assumptions** â€” burn rate, revenue timing, CAC, LTV ratios
- **Dependency assumptions** â€” partner will deliver, API won't change, regulations won't shift

### Step 2: Rate Each Assumption

For every assumption extracted, rate it on two dimensions:

**Confidence level (how sure are you this is true):**
- **High** â€” verified with data, customer conversations, market research
- **Medium** â€” directionally right but not validated
- **Low** â€” plausible but untested
- **Unknown** â€” we simply don't know

**Impact if wrong (what happens if this assumption fails):**
- **Critical** â€” plan fails entirely
- **High** â€” major delay or cost overrun
- **Medium** â€” significant rework required
- **Low** â€” manageable adjustment

### Step 3: Map Vulnerabilities

The matrix of Low/Unknown confidence أ— Critical/High impact = your highest-risk assumptions.

**Vulnerability = Low confidence + High impact**

These are not problems to ignore. They're the bets you're making. The question is: are you making them consciously?

### Step 4: Find the Dependency Chain

Many plans fail not because any single assumption is wrong, but because multiple assumptions have to be right simultaneously.

Map the chain:
- Does assumption B depend on assumption A being true first?
- If the first thing goes wrong, how many downstream things break?
- What's the critical path? What has zero slack?

### Step 5: Test the Reversibility

For each critical vulnerability: if this assumption turns out to be wrong at month 3, what do you do?

- Can you pivot?
- Can you cut scope?
- Is money already spent?
- Are commitments already made?

The less reversible, the more rigorously you need to validate before committing.

---

## Output Format

**Challenge Report: [Plan Name]**

```
CORE ASSUMPTIONS (extracted)
1. [Assumption] â€” Confidence: [H/M/L/?] â€” Impact if wrong: [Critical/High/Medium/Low]
2. ...

VULNERABILITY MAP
Critical risks (act before proceeding):
â€¢ [#N] [Assumption] â€” WHY it might be wrong â€” WHAT breaks if it is

High risks (validate before scaling):
â€¢ ...

DEPENDENCY CHAIN
[Assumption A] â†’ depends on â†’ [Assumption B] â†’ which enables â†’ [Assumption C]
Weakest link: [X] â€” if this breaks, [Y] and [Z] also fail

REVERSIBILITY ASSESSMENT
â€¢ Reversible bets: [list]
â€¢ Irreversible commitments: [list â€” treat with extreme care]

KILL SWITCHES
What would have to be true at [30/60/90 days] to continue vs. kill/pivot?
â€¢ Continue if: ...
â€¢ Kill/pivot if: ...

HARDENING ACTIONS
1. [Specific validation to do before proceeding]
2. [Alternative approach to consider]
3. [Contingency to build into the plan]
```

---

## Challenge Patterns by Plan Type

### Product Roadmap
- Are we building what customers will pay for, or what they said they wanted?
- Does the velocity estimate account for real team capacity (not theoretical)?
- What happens if the anchor feature takes 3أ— longer than estimated?
- Who owns decisions when requirements conflict?

### Go-to-Market Plan
- What's the actual ICP conversion rate, not the hoped-for one?
- How many touches to close, and do you have the sales capacity for that?
- What happens if the first 10 deals take 3 months instead of 1?
- Is "land and expand" a real motion or a hope?

### Hiring Plan
- What happens if the key hire takes 4 months to find, not 6 weeks?
- Is the plan dependent on retaining specific people who might leave?
- Does the plan account for ramp time (usually 3â€“6 months before full productivity)?
- What's the burn impact if headcount leads revenue by 6 months?

### Fundraising Plan
- What's your fallback if the lead investor passes?
- Have you modeled the timeline if it takes 6 months, not 3?
- What's your runway at current burn if the round closes at the low end?
- What assumptions break if you raise 50% of the target amount?

---

## The Hardest Questions

These are the ones people skip:
- "What's the bear case, not the base case?"
- "If this exact plan was run by a team we don't trust, would it work?"
- "What are we not saying out loud because it's uncomfortable?"
- "Who has incentives to make this plan sound better than it is?"
- "What would an enemy of this plan attack first?"

---

## Deliverable

The output of `/em:challenge` is not permission to stop. It's a vulnerability map. Now you can make conscious decisions: validate the risky assumptions, hedge the critical ones, or accept the bets you're making knowingly.

Unknown risks are dangerous. Known risks are manageable.
