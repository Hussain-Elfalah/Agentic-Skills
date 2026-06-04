---
name: patent
description: Patent prior-art and landscape intelligence skill â€” not generic patent help. Commits to one of five sub-use-cases via forcing intake (novelty search / freedom-to-operate / competitive landscape / acquisition diligence / litigation prior-art) before any search runs. Searches Google Patents, Espacenet, USPTO, and optionally Lens.org for citation-graph signals. Output is an editable Word document (.docx) with verdict, ranked closest art (claim-text extracted), CPC-class-aware landscape, family-resolved hits, geographic coverage, FTO flags where applicable, strategy recommendations, and full audit log. Triggers: 'prior art search for [invention]', 'patent search on [topic]', 'freedom to operate analysis', 'FTO for [product]', 'patent landscape for [field]', 'is [invention] novel', 'patents on [topic]', 'competitive patent analysis', 'prior art for litigation', 'patent diligence on [company]'. Produces search signal, not legal advice â€” always recommends consulting a patent attorney before filing or licensing decisions. Trademark, copyright, and trade-secret questions are out of scope.
---

# Patent â€” Prior-Art + Landscape Intelligence

> **Portability:** Requires `web_fetch` (Google Patents, Espacenet, USPTO), `WebSearch` (adjacent academic art), Node.js with `docx` package, and optionally Lens.org API key for citation-graph signals. Works in Claude Code CLI natively. In Claude.ai with web tools + Code Execution + BYOK Lens.org, the workflow is supported.

> **Out of scope:** trademark, copyright, trade-secret. These are flagged at intake. Use a different skill or qualified counsel.

> **Legal disclaimer:** This skill produces search signal, not legal advice. Verdicts are technical assessments. **Always consult a patent attorney before filing or licensing decisions.**

## Non-Generic Framing â€” The Differentiator

This skill is **prior-art + landscape intelligence**. It **refuses to be a bucket**. Every invocation commits to one of five sub-use-cases via the grill-me intake before any search runs. The chosen sub-use-case dictates the entire search strategy, ranking heuristics, and DOCX emphasis.

| Sub-use-case | Search strategy | DOCX emphasis |
|---|---|---|
| **Novelty search** | Narrow + claims-text focused; pre-filing date irrelevant | Closest art + claim-differentiation |
| **Freedom-to-operate** | Broad + active patents only; jurisdiction-filtered | FTO flags + claim-by-claim risk |
| **Competitive landscape** | Breadth + filer tally + CPC trends | Filer map + investment hotspots |
| **Acquisition diligence** | Specific assignee + portfolio scope + assignment chain | Portfolio table + ownership verification |
| **Litigation prior-art** | Specific target patent + adjacent art before priority date | Knock-out candidates ranked by relevance |

See [`references/sub_use_case_routing.md`](references/sub_use_case_routing.md) for the canon.

## Agent Integrity Rules (Research-Pack Convention)

Locked verbatim per PR #657 audit.

- **Execution discipline.** Sequential search calls only. **1 query/sec rate limit.** Confirm response received before next call.
- **Source discipline.** Cite only patents returned by THIS session's tool calls. Training knowledge labeled `[Not from search â€” reference information]` and excluded from counts.
- **Three-count tracking.** Queries sent / patents received (shown) / patents cited. Surfaced in audit log.
- **Retry policy.** On failure â†’ wait 3s â†’ retry once â†’ log. After 3 consecutive failures across tools: stop, alert user, explain what's missing.
- **Plan-tier detection.** Lens.org free tier = 1000 queries/month. Google Patents has no auth but rate-limits per IP. Detect and surface caps.

## Phase 1: Grill-Me Intake (6 forcing questions, one at a time)

### Q1 (root) â€” Invention description

> **Describe the invention in 2â€“3 sentences. What does it do, and what's new about it?**
>
> *Why I'm asking:* Concept and keyword extraction depends entirely on a precise description. Vague descriptions ("AI for healthcare", "a better widget") will be rejected â€” push back and ask the user to specify what the invention does and what differentiates it from existing approaches.

**Refuse mush.** If answer is generic, ask once more: "What does it do that existing systems don't?" Then commit (with caveat in DOCX).

### Q2 (depends on Q1) â€” Sub-use-case commitment

> **What's the purpose of this search? Pick one:**
>
> 1. Novelty search (am I novel enough to file)
> 2. Freedom-to-operate (will I get sued if I ship)
> 3. Competitive landscape (who else plays here)
> 4. Acquisition diligence (does target really own X)
> 5. Litigation prior-art hunting (kill a specific patent)
>
> *Why I'm asking:* Each path uses a fundamentally different search strategy. I'll **refuse to start without you picking one**.

Forcing format. If user says "all of them", push for the primary purpose â€” secondary purposes can run as follow-up searches.

### Q3 (asked only if Q2 âˆˆ {FTO, landscape, diligence}) â€” Jurisdictions

> **Which jurisdictions matter? Pick all that apply: US / EP / CN / JP / KR / PCT / worldwide.**
>
> *Why I'm asking:* FTO only matters where you'll sell. Landscape changes radically by region. Diligence requires checking all jurisdictions where the target operates.

Skip for novelty (priority date is jurisdictionally portable) and litigation (jurisdiction is set by the target patent).

### Q4 (depends on Q1) â€” Known prior art

> **Have you already seen prior art close to this? Cite a patent number or paper.**
>
> *Why I'm asking:* If you know one piece of art, I can search adjacent to it â€” much more precise than starting cold. If you don't, that's fine â€” just confirm.

Anchoring. Accept "none" but ask if the user has seen *any* related work even informally.

### Q5 (depends on Q2) â€” Risk tolerance

> **Risk tolerance for this search: strict (one close hit means abandon the path) or signal-gathering (you want the lay of the land regardless)?**
>
> *Why I'm asking:* Strict mode ranks aggressively and surfaces verdict-grade hits; signal mode prioritizes breadth and visualizations.

Asked for novelty and FTO; skipped for pure landscape (always signal-gathering by definition).

### Q6 (asked only if Q2 âˆˆ {novelty, FTO}) â€” Attorney status

> **Have you spoken to a patent attorney? This skill produces search signal, not legal advice. Confirm you understand this is for technical assessment only.**
>
> *Why I'm asking:* Novelty and FTO have legal consequences. The skill's verdict is signal-grade; legal positions require qualified counsel.

**Triggers the legal-disclaimer footer in the DOCX.** Skipped for landscape and diligence (lower legal exposure).

**Stop condition:** After Q6 (or earlier if dependency skips applied), commit and start Phase 2. Never re-open intake after Phase 2 begins.

## Phase 2: Search Strategy Selection

Deterministic from intake answers. Use `scripts/sub_use_case_router.py`:

```bash
python ../scripts/sub_use_case_router.py \
  --sub-use-case novelty \
  --jurisdictions "" \
  --risk strict \
  --known-art "US10000000B2"
```

Returns: query plan (5-8 queries) + ranking heuristic + DOCX emphasis flags.

## Phase 3: Multi-Source Search (Sequential)

### Source priority

1. **Google Patents** (https://patents.google.com) â€” workhorse, no auth required, broad coverage
2. **Espacenet** (https://worldwide.espacenet.com) â€” global coverage, good for non-US art
3. **USPTO PPS** (https://ppubs.uspto.gov) â€” US deep dive
4. **Lens.org** (https://www.lens.org) â€” citation graph, BYOK API key required

### Per-sub-use-case query patterns

**Novelty:**
- 3 narrow queries on invention-specific terminology (Google Patents)
- 2 broad concept queries with synonyms (Google Patents + Espacenet)
- 1 CPC-class-restricted query if class identified from initial hits

**FTO:**
- Jurisdiction-filtered: only active patents (not expired, not abandoned)
- Date filter: priority < today
- Active-claim text extraction for each hit

**Competitive landscape:**
- Broader queries on the technology space
- CPC class identification â†’ tally top filers in that class
- 10-year filing trend by year per top-5 filer

**Acquisition diligence:**
- Specific assignee searches (target company + subsidiaries + named inventors)
- Assignment chain check (USPTO assignment recordation)
- Family resolution for deduplication

**Litigation prior-art:**
- Target patent input required (number)
- Priority date extraction
- Search for art before priority date in same CPC classes
- Adjacent-claim-language search

### Sequential discipline

1 q/sec across ALL sources combined. Tracked via `scripts/citation_tracker.py` with timestamp-enforced gap.

## Phase 4: Claim Extraction + Relevance Scoring

For each closest-art hit:
- Pull **independent claim 1** (the broadest claim â€” primary anticipation/obviousness vehicle)
- Pull **key dependent claims** (claims that add the inventive step)
- Score relevance against invention description (overlap of claim language with Q1 terminology)

Rank by score. Verdict per sub-use-case (NOVEL / POTENTIALLY NOVEL / NOT NOVEL for novelty; CLEAR / FLAGGED / HIGH RISK per jurisdiction for FTO).

## Phase 5: Citation Graph + Family Resolution

### Citation graph (Lens.org BYOK)

If user provides Lens.org API key:
- Foundational-patent identification (cited-by count > threshold, typically 50+)
- Recent high-cite signals (citations in last 24 months as proxy for current activity)
- Forward citations from target patent (litigation prior-art) or from closest art (novelty)

If no Lens.org key: skip; note in audit log; recommend manual citation review on Google Patents.

### Family resolution

Same invention often filed in multiple jurisdictions (US + EP + JP + CN). Group by family ID or priority number to avoid double-counting. Use `scripts/family_resolver.py`:

```bash
python ../scripts/family_resolver.py --hits-file hits.json
# Returns: deduplicated family list + family-member jurisdictions
```

## CPC/IPC Classification Awareness

**Critical:** keyword search alone misses adjacent art. After initial search, extract the CPC/IPC classes from top 5 hits and run **one class-restricted query**. This consistently surfaces art that keyword search misses.

See [`references/cpc_classification_canon.md`](references/cpc_classification_canon.md) for the canon.

## Phase 6: DOCX Generation (8 Sections)

Sub-use-case-dependent emphasis. Via Node.js + `docx` library.

1. **Executive Summary + Verdict** â€” Sub-use-case banner + one-line verdict (NOVEL / FLAGGED / etc.) + 3-4 key findings + legal disclaimer footer
2. **Closest Prior Art** â€” 5-10 patents in ranked order. Per hit: hyperlinked title + assignee + filing/priority dates + independent claim 1 text (italicized) + relevance score + relevance rationale (1-2 sentences)
3. **Patent Landscape** â€” Top filers table (top 10 by count) + 10-year filing trend description + CPC class distribution table. Only for landscape and diligence; abbreviated otherwise.
4. **Citation Graph Signals** â€” Foundational patents (if Lens-enabled) + recent high-cite activity. If Lens unavailable, note "manual review recommended" and skip table.
5. **Geographic Coverage** â€” Filings by jurisdiction for top 10 hits. Only for FTO, landscape, diligence; skipped for novelty and litigation.
6. **FTO Flags** (FTO only) â€” Active patents posing infringement risk. Per flag: hyperlinked patent + jurisdiction + relevant claims + risk level (HIGH/MEDIUM/LOW) + mitigation note.
7. **Strategy + Recommendations** â€” Sub-use-case-specific:
   - Novelty â†’ claim differentiation suggestions
   - FTO â†’ design-around hints + jurisdiction strategy
   - Landscape â†’ who-to-watch list
   - Diligence â†’ red flags in portfolio
   - Litigation â†’ ranked knock-out candidates
   - **Mandatory disclaimer to consult patent attorney** for any filing/licensing decision.
8. **Audit Log** â€” Searches table (#, query, source, results, status), counts (sent/shown/cited), tool constraints (plan-tier notes), failed steps, attorney-consultation reminder

### Styling

Arial 12pt body, navy headings (#1a3a5c), light blue table headers (#e8f0f8), red FTO-flag callout. `ExternalHyperlink` patterns:
- Google Patents: `https://patents.google.com/patent/[number]`
- Espacenet: `https://worldwide.espacenet.com/patent/...`
- USPTO: `https://patents.uspto.gov/patent/...`

## Date Discipline

Distinguish at every hit:
- **Filing date** â€” when the application was first submitted
- **Priority date** â€” earliest claim of priority (often earlier than filing)
- **Publication date** â€” when the application became public (typically 18 months after priority)
- **Grant date** â€” when the patent was granted (later than publication)

Surface the **legally-relevant date** per sub-use-case:
- Novelty â†’ priority date (vs invention's anticipated filing date)
- FTO â†’ grant date + status (active vs expired)
- Landscape â†’ publication date (when public knowledge began)
- Diligence â†’ grant date + assignment date
- Litigation â†’ priority date of target patent (sets the prior-art cutoff)

## Phase 7: Deliver

- Save: `<output-dir>/patent_<invention-slug>_<sub-use-case>_<YYYY-MM-DD>.docx`
- Chat summary: file path + sub-use-case + verdict + audit counts + plan-tier
- Validate: `python scripts/office/validate.py <docx>`
- Reminder: "Consult patent attorney before filing/licensing"

## Tooling

| Script | Role |
|---|---|
| `scripts/citation_tracker.py` | Multi-source three-count audit (Google Patents + Espacenet + USPTO + Lens.org) at `~/.patent_sessions/<session>.json` |
| `scripts/family_resolver.py` | Group same-invention filings across jurisdictions by family ID / priority number |
| `scripts/sub_use_case_router.py` | Deterministic search-strategy selection from intake answers |

## References

- [`references/sub_use_case_routing.md`](references/sub_use_case_routing.md) â€” 5-sub-use-case canon (7+ sources)
- [`references/cpc_classification_canon.md`](references/cpc_classification_canon.md) â€” CPC/IPC class follow-up rationale (7+ sources)
- [`references/legal_disclaimer_discipline.md`](references/legal_disclaimer_discipline.md) â€” when + why disclaimer mandatory (7+ sources)

## Error Handling

| Failure | Behavior |
|---|---|
| User refuses to commit to sub-use-case | Refuse to proceed. Re-ask Q2 with examples. |
| Invention description is generic | Reject answer. Re-ask Q1 with "what does it do that existing systems don't?" |
| Google Patents rate-limits | Wait 3s, retry once. Fall back to Espacenet for that query. Log in audit. |
| Lens.org key missing | Skip citation graph section, note "manual review recommended" in DOCX. |
| Claim text extraction fails | Fall back to abstract; flag as "abstract-only" in relevance rationale. |
| Family resolution incomplete | Note in audit; same-invention duplicates may appear; suggest manual deduplication. |
| All searches return <3 hits | Surface explicitly as "either niche art or genuine gap"; never fabricate. |
| 3 consecutive tool failures | Stop, alert user, explain what's missing. |
| DOCX generation fails | Save raw data as JSON fallback so user doesn't lose work. |
| Target patent number invalid (litigation) | Validate format before search; ask user to confirm. |

## Anti-Patterns To Reject

- Starting any search before user commits to a sub-use-case (refuses generic "patent help")
- Batching all intake questions instead of one at a time
- Accepting vague invention descriptions ("AI for healthcare")
- Keyword-only search without CPC/IPC class follow-up
- Treating family members as separate hits (must be deduplicated)
- Confusing filing date with priority date with publication date
- Skipping the legal disclaimer when sub-use-case has legal consequences
- Reporting a verdict without claim-text evidence
- Fabricating Lens.org citation data when key is absent
- Suggesting design-arounds without acknowledging attorney review is required
- Skipping the audit log

---

**Version:** 1.0.0
**Source spec:** [`megaprompts/11-patent-megaprompt.md`](../../../../megaprompts/11-patent-megaprompt.md)
**Build pattern:** Path B (direct conversion). Research-pack sibling, sub-use-case routing variant.
