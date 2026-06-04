---
name: performance-profiler
description: Systematic performance profiling for Node.js, Python, and Go applications. Identifies CPU, memory, and I/O bottlenecks, generates flamegraphs, analyzes bundle sizes, optimizes database queries, runs load tests with k6 and Artillery. Always measures before and after. Use when investigating a slow endpoint, planning a performance budget, or hunting a memory leak in production.
---

# Performance Profiler

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** Performance Engineering  

---

## Overview

Systematic performance profiling for Node.js, Python, and Go applications. Identifies CPU, memory, and I/O bottlenecks; generates flamegraphs; analyzes bundle sizes; optimizes database queries; detects memory leaks; and runs load tests with k6 and Artillery. Always measures before and after.

## Core Capabilities

- **CPU profiling** â€” flamegraphs for Node.js, py-spy for Python, pprof for Go
- **Memory profiling** â€” heap snapshots, leak detection, GC pressure
- **Bundle analysis** â€” webpack-bundle-analyzer, Next.js bundle analyzer
- **Database optimization** â€” EXPLAIN ANALYZE, slow query log, N+1 detection
- **Load testing** â€” k6 scripts, Artillery scenarios, ramp-up patterns
- **Before/after measurement** â€” establish baseline, profile, optimize, verify

---

## When to Use

- App is slow and you don't know where the bottleneck is
- P99 latency exceeds SLA before a release
- Memory usage grows over time (suspected leak)
- Bundle size increased after adding dependencies
- Preparing for a traffic spike (load test before launch)
- Database queries taking >100ms

---

## Quick Start

```bash
# Analyze a project for performance risk indicators
python3 scripts/performance_profiler.py /path/to/project

# JSON output for CI integration
python3 scripts/performance_profiler.py /path/to/project --json

# Custom large-file threshold
python3 scripts/performance_profiler.py /path/to/project --large-file-threshold-kb 256
```

---

## Golden Rule: Measure First

```bash
# Establish baseline BEFORE any optimization
# Record: P50, P95, P99 latency | RPS | error rate | memory usage

# Wrong: "I think the N+1 query is slow, let me fix it"
# Right: Profile â†’ confirm bottleneck â†’ fix â†’ measure again â†’ verify improvement
```

---

## Node.js Profiling
â†’ See references/profiling-recipes.md for details

## Before/After Measurement Template

```markdown
## Performance Optimization: [What You Fixed]

**Date:** 2026-03-01  
**Engineer:** @username  
**Ticket:** PROJ-123  

### Problem
[1-2 sentences: what was slow, how was it observed]

### Root Cause
[What the profiler revealed]

### Baseline (Before)
| Metric | Value |
|--------|-------|
| P50 latency | 480ms |
| P95 latency | 1,240ms |
| P99 latency | 3,100ms |
| RPS @ 50 VUs | 42 |
| Error rate | 0.8% |
| DB queries/req | 23 (N+1) |

Profiler evidence: [link to flamegraph or screenshot]

### Fix Applied
[What changed â€” code diff or description]

### After
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| P50 latency | 480ms | 48ms | -90% |
| P95 latency | 1,240ms | 120ms | -90% |
| P99 latency | 3,100ms | 280ms | -91% |
| RPS @ 50 VUs | 42 | 380 | +804% |
| Error rate | 0.8% | 0% | -100% |
| DB queries/req | 23 | 1 | -96% |

### Verification
Load test run: [link to k6 output]
```

---

## Optimization Checklist

### Quick wins (check these first)

```
Database
â–، Missing indexes on WHERE/ORDER BY columns
â–، N+1 queries (check query count per request)
â–، Loading all columns when only 2-3 needed (SELECT *)
â–، No LIMIT on unbounded queries
â–، Missing connection pool (creating new connection per request)

Node.js
â–، Sync I/O (fs.readFileSync) in hot path
â–، JSON.parse/stringify of large objects in hot loop
â–، Missing caching for expensive computations
â–، No compression (gzip/brotli) on responses
â–، Dependencies loaded in request handler (move to module level)

Bundle
â–، Moment.js â†’ dayjs/date-fns
â–، Lodash (full) â†’ lodash/function imports
â–، Static imports of heavy components â†’ dynamic imports
â–، Images not optimized / not using next/image
â–، No code splitting on routes

API
â–، No pagination on list endpoints
â–، No response caching (Cache-Control headers)
â–، Serial awaits that could be parallel (Promise.all)
â–، Fetching related data in a loop instead of JOIN
```

---

## Common Pitfalls

- **Optimizing without measuring** â€” you'll optimize the wrong thing
- **Testing in development** â€” profile against production-like data volumes
- **Ignoring P99** â€” P50 can look fine while P99 is catastrophic
- **Premature optimization** â€” fix correctness first, then performance
- **Not re-measuring** â€” always verify the fix actually improved things
- **Load testing production** â€” use staging with production-size data

---

## Best Practices

1. **Baseline first, always** â€” record metrics before touching anything
2. **One change at a time** â€” isolate the variable to confirm causation
3. **Profile with realistic data** â€” 10 rows in dev, millions in prod â€” different bottlenecks
4. **Set performance budgets** â€” `p(95) < 200ms` in CI thresholds with k6
5. **Monitor continuously** â€” add Datadog/Prometheus metrics for key paths
6. **Cache invalidation strategy** â€” cache aggressively, invalidate precisely
7. **Document the win** â€” before/after in the PR description motivates the team
