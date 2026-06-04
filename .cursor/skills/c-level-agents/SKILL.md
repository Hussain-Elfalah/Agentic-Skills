---
name: c-level-agents
description: Founder-mode executive team. 8 cs-* C-suite agents (CFO, CMO, CRO, CPO, COO, CHRO, CISO, Chief of Staff) and 17 /cs:* slash commands for forcing-question office hours, multi-role boardroom deliberation, strategic sprint pipeline, and meta routing. Use when the founder needs a virtual executive team, when invoking /cs:* commands, or when orchestrating multi-role decisions.
---

# c-level-agents â€” Founder-Mode Executive Team

A virtual C-suite delivered through slash commands and persona agents.

## Keywords

founder mode, virtual c-suite, executive team, boardroom, office hours, cfo review, cmo review, strategic sprint, decision logging, cross-model consensus, persona agents, chief of staff, forcing questions

## What This Plugin Provides

### 8 cs-* Agents (in `agents/`)

Each agent wraps an existing c-level skill and adds:
- A distinct cognitive voice (numerate skeptic, narrative-first, etc.)
- Forcing questions specific to the role
- Workflow orchestration tied to skill Python tools
- Output template: Bottom Line â†’ What â†’ Why â†’ How to Act â†’ Your Decision

See `../references/persona-voices.md` for voice specs.

### 17 /cs:* Slash Commands (in `skills/`)

**Forcing-question office hours (8):**
- `/cs:office-hours` â€” YC-style 6-question intake
- `/cs:cfo-review` â€” unit economics, runway, dilution
- `/cs:cmo-review` â€” ICP, CAC payback, positioning
- `/cs:cpo-review` â€” RICE, JTBD, North Star, PMF
- `/cs:cro-review` â€” pipeline coverage, win rate, NRR
- `/cs:cto-review` â€” architecture risk, scaling cliff
- `/cs:ciso-review` â€” threat model, blast radius, compliance
- `/cs:gc-review` â€” contracts, IP, regulatory, term sheets

**Strategic sprint pipeline (5):**
- `/cs:brief` â†’ `/cs:boardroom` â†’ `/cs:decide` â†’ `/cs:execute` â†’ `/cs:post-mortem`

**Meta + safety (4):**
- `/cs:founder-mode` â€” auto-routes to the right C-role
- `/cs:onboard` â€” founder interview â†’ `company-context.md`
- `/cs:cross-eval` â€” multi-model consensus
- `/cs:freeze` â€” cooldown lock on a decision

## Quick Start

```
/cs:onboard                          # populate company context first
/cs:office-hours "should we hire a VP Sales?"
/cs:founder-mode "runway pressure"   # auto-routes to CFO
/cs:boardroom briefs/pricing-v3.md   # full panel
```

## Architecture

```
User question
   â”‚
   â”œâ”€ Single-role? â†’ cs-{role}-advisor agent
   â”‚                     â†“
   â”‚                  /cs:{role}-review command (forcing Qs)
   â”‚                     â†“
   â”‚                  Skill tools + references
   â”‚                     â†“
   â”‚                  Bottom Line + Memo
   â”‚
   â””â”€ Multi-role?  â†’ /cs:boardroom
                        â†“
                     6-phase deliberation (Phase 2 isolation)
                        â†“
                     /cs:decide â†’ decision-logger (two-layer memory)
                        â†“
                     /cs:execute â†’ 90-day plan
```

## Integration Points

- **Existing 28 c-level skills** â€” wrapped, not replaced
- **decision-logger** â€” every `/cs:decide` writes here
- **chief-of-staff** â€” routing layer the agent orchestrates
- **board-meeting** â€” protocol the `/cs:boardroom` command runs
- **llm-wiki** â€” optional persistent memory bridge (see `../references/llm-wiki-bridge.md`)
- **executive-mentor** â€” adversarial `/em:*` commands stack cleanly on top

## Design Principles

1. **Voice is bookended, analysis is neutral.**
2. **Artifacts over chat.** Every command produces a Markdown artifact the next command consumes.
3. **Phase 2 isolation in boardroom.** Independent thinking before cross-examination.
4. **Graceful degradation.** `/cs:cross-eval` falls back to Claude-only.
5. **No paid dependencies.** All Python tools are stdlib-only.

## References

- [persona-voices.md](../../references/persona-voices.md)
- [llm-wiki-bridge.md](../../references/llm-wiki-bridge.md)
- [Parent c-level CLAUDE.md](../../../CLAUDE.md)
- [Existing executive-mentor sibling](../../../executive-mentor/)

---

**Version:** 1.0.0
**Last Updated:** 2026-05-12
**Status:** Production Ready
