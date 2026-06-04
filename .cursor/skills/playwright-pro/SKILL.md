---
name: playwright-pro
description: Production-grade Playwright testing toolkit. Use when the user mentions Playwright tests, end-to-end testing, browser automation, fixing flaky tests, test migration, CI/CD testing, or test suites. Generate tests, fix flaky failures, migrate from Cypress/Selenium, sync with TestRail, run on BrowserStack. 55 templates, 3 agents, smart reporting.
---

# Playwright Pro

Production-grade Playwright testing toolkit for AI coding agents.

## Available Commands

When installed as a Claude Code plugin, these are available as `/pw:` commands:

| Command | What it does |
|---|---|
| `/pw:init` | Set up Playwright â€” detects framework, generates config, CI, first test |
| `/pw:generate <spec>` | Generate tests from user story, URL, or component |
| `/pw:review` | Review tests for anti-patterns and coverage gaps |
| `/pw:fix <test>` | Diagnose and fix failing or flaky tests |
| `/pw:migrate` | Migrate from Cypress or Selenium to Playwright |
| `/pw:coverage` | Analyze what's tested vs. what's missing |
| `/pw:testrail` | Sync with TestRail â€” read cases, push results |
| `/pw:browserstack` | Run on BrowserStack, pull cross-browser reports |
| `/pw:report` | Generate test report in your preferred format |

## Quick Start Workflow

The recommended sequence for most projects:

```
1. /pw:init          â†’ scaffolds config, CI pipeline, and a first smoke test
2. /pw:generate      â†’ generates tests from your spec or URL
3. /pw:review        â†’ validates quality and flags anti-patterns      â†گ always run after generate
4. /pw:fix <test>    â†’ diagnoses and repairs any failing/flaky tests  â†گ run when CI turns red
```

**Validation checkpoints:**
- After `/pw:generate` â€” always run `/pw:review` before committing; it catches locator anti-patterns and missing assertions automatically.
- After `/pw:fix` â€” re-run the full suite locally (`npx playwright test`) to confirm the fix doesn't introduce regressions.
- After `/pw:migrate` â€” run `/pw:coverage` to confirm parity with the old suite before decommissioning Cypress/Selenium tests.

### Example: Generate â†’ Review â†’ Fix

```bash
# 1. Generate tests from a user story
/pw:generate "As a user I can log in with email and password"

# Generated: tests/auth/login.spec.ts
# â†’ Playwright Pro creates the file using the auth template.

# 2. Review the generated tests
/pw:review tests/auth/login.spec.ts

# â†’ Flags: one test used page.locator('input[type=password]') â€” suggests getByLabel('Password')
# â†’ Fix applied automatically.

# 3. Run locally to confirm
npx playwright test tests/auth/login.spec.ts --headed

# 4. If a test is flaky in CI, diagnose it
/pw:fix tests/auth/login.spec.ts
# â†’ Identifies missing web-first assertion; replaces waitForTimeout(2000) with expect(locator).toBeVisible()
```

## Golden Rules

1. `getByRole()` over CSS/XPath â€” resilient to markup changes
2. Never `page.waitForTimeout()` â€” use web-first assertions
3. `expect(locator)` auto-retries; `expect(await locator.textContent())` does not
4. Isolate every test â€” no shared state between tests
5. `baseURL` in config â€” zero hardcoded URLs
6. Retries: `2` in CI, `0` locally
7. Traces: `'on-first-retry'` â€” rich debugging without slowdown
8. Fixtures over globals â€” `test.extend()` for shared state
9. One behavior per test â€” multiple related assertions are fine
10. Mock external services only â€” never mock your own app

## Locator Priority

```
1. getByRole()        â€” buttons, links, headings, form elements
2. getByLabel()       â€” form fields with labels
3. getByText()        â€” non-interactive text
4. getByPlaceholder() â€” inputs with placeholder
5. getByTestId()      â€” when no semantic option exists
6. page.locator()     â€” CSS/XPath as last resort
```

## What's Included

- **9 skills** with detailed step-by-step instructions
- **3 specialized agents**: test-architect, test-debugger, migration-planner
- **55 test templates**: auth, CRUD, checkout, search, forms, dashboard, settings, onboarding, notifications, API, accessibility
- **2 MCP servers** (TypeScript): TestRail and BrowserStack integrations
- **Smart hooks**: auto-validate test quality, auto-detect Playwright projects
- **6 reference docs**: golden rules, locators, assertions, fixtures, pitfalls, flaky tests
- **Migration guides**: Cypress and Selenium mapping tables

## Integration Setup

### TestRail (Optional)
```bash
export TESTRAIL_URL="https://your-instance.testrail.io"
export TESTRAIL_USER="your@email.com"
export TESTRAIL_API_KEY="your-api-key"
```

### BrowserStack (Optional)
```bash
export BROWSERSTACK_USERNAME="your-username"
export BROWSERSTACK_ACCESS_KEY="your-access-key"
```

## Quick Reference

See `reference/` directory for:
- `golden-rules.md` â€” The 10 non-negotiable rules
- `locators.md` â€” Complete locator priority with cheat sheet
- `assertions.md` â€” Web-first assertions reference
- `fixtures.md` â€” Custom fixtures and storageState patterns
- `common-pitfalls.md` â€” Top 10 mistakes and fixes
- `flaky-tests.md` â€” Diagnosis commands and quick fixes

See `templates/README.md` for the full template index.
