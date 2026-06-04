---
name: code-to-prd
description: Reverse-engineer any codebase into a complete Product Requirements Document (PRD). Analyzes routes, components, state management, API integrations, and user interactions to produce business-readable documentation detailed enough for engineers or AI agents to fully reconstruct every page and endpoint. Works with frontend frameworks (React, Vue, Angular, Svelte, Next.js, Nuxt), backend frameworks (NestJS, Django, Express, FastAPI), and fullstack applications. Trigger when users mention: generate PRD, reverse-engineer requirements, code to documentation, extract product specs from code, document page logic, analyze page fields and interactions, create a functional inventory, write requirements from an existing codebase, document API endpoints, or analyze backend routes.
---

## Name

Code â†’ PRD

## Description

Reverse-engineer any frontend, backend, or fullstack codebase into a complete Product Requirements Document (PRD). Analyzes routes, components, models, APIs, and user interactions to produce business-readable documentation detailed enough for engineers or AI agents to fully reconstruct every page and endpoint.

# Code â†’ PRD: Reverse-Engineer Any Codebase into Product Requirements

## Features

- **3-phase workflow**: global scan â†’ page-by-page analysis â†’ structured document generation
- **Frontend support**: React, Vue, Angular, Svelte, Next.js (App + Pages Router), Nuxt, SvelteKit, Remix
- **Backend support**: NestJS, Express, Django, Django REST Framework, FastAPI, Flask
- **Fullstack support**: Combined frontend + backend analysis with unified PRD output
- **Mock detection**: Automatically distinguishes real API integrations from mock/fixture data
- **Enum extraction**: Exhaustively lists all status codes, type mappings, and constants
- **Model extraction**: Parses Django models, NestJS entities, Pydantic schemas
- **Automation scripts**: `codebase_analyzer.py` for scanning, `prd_scaffolder.py` for directory generation
- **Quality checklist**: Validation checklist for completeness, accuracy, readability

## Usage

```bash
# Analyze a project and generate PRD skeleton
python3 scripts/codebase_analyzer.py /path/to/project -o analysis.json
python3 scripts/prd_scaffolder.py analysis.json -o prd/ -n "My App"

# Or use the slash command
/code-to-prd /path/to/project
```

## Examples

### Frontend (React)
```bash
/code-to-prd ./src
# â†’ Scans components, routes, API calls, state management
# â†’ Generates prd/ with per-page docs, enum dictionary, API inventory
```

### Backend (Django)
```bash
/code-to-prd ./myproject
# â†’ Detects Django via manage.py, scans urls.py, views.py, models.py
# â†’ Documents endpoints, model schemas, admin config, permissions
```

### Fullstack (Next.js)
```bash
/code-to-prd .
# â†’ Analyzes both app/ pages and api/ routes
# â†’ Generates unified PRD covering UI pages and API endpoints
```

---

## Role

You are a senior product analyst and technical architect. Your job is to read a frontend codebase, understand every page's business purpose, and produce a complete PRD in **product-manager-friendly language**.

### Dual Audience

1. **Product managers / business stakeholders** â€” need to understand *what* the system does, not *how*
2. **Engineers / AI agents** â€” need enough detail to **fully reconstruct** every page's fields, interactions, and relationships

Your document must describe functionality in non-technical language while omitting zero business details.

### Supported Stacks

| Stack | Frameworks |
|-------|-----------|
| **Frontend** | React, Vue, Angular, Svelte, Next.js (App/Pages Router), Nuxt, SvelteKit, Remix, Astro |
| **Backend** | NestJS, Express, Fastify, Django, Django REST Framework, FastAPI, Flask |
| **Fullstack** | Next.js (API routes + pages), Nuxt (server/ + pages/), Django (views + templates) |

For **backend-only** projects, the "page" concept maps to **API resource groups** or **admin views**. The same 3-phase workflow applies â€” routes become endpoints, components become controllers/views, and interactions become request/response flows.

---

## Workflow

### Phase 1 â€” Project Global Scan

Build global context before diving into pages.

#### 1. Identify Project Structure

Scan the root directory and understand organization:

```
Frontend directories:
- Pages/routes (pages/, views/, routes/, app/, src/pages/)
- Components (components/, modules/)
- Route config (router.ts, routes.ts, App.tsx route definitions)
- API/service layer (services/, api/, requests/)
- State management (store/, models/, context/)
- i18n files (locales/, i18n/) â€” field display names often live here

Backend directories (NestJS):
- Modules (src/modules/, src/*.module.ts)
- Controllers (*.controller.ts) â€” route handlers
- Services (*.service.ts) â€” business logic
- DTOs (dto/, *.dto.ts) â€” request/response shapes
- Entities (entities/, *.entity.ts) â€” database models
- Guards/pipes/interceptors â€” auth, validation, transformation

Backend directories (Django):
- Apps (*/apps.py, */views.py, */models.py, */urls.py)
- URL config (urls.py, */urls.py)
- Views (views.py, viewsets.py) â€” route handlers
- Models (models.py) â€” database schema
- Serializers (serializers.py) â€” request/response shapes
- Forms (forms.py) â€” validation and field definitions
- Templates (templates/) â€” server-rendered pages
- Admin (admin.py) â€” admin panel configuration
```

**Identify framework** from `package.json` (Node.js frameworks) or project files (`manage.py` for Django, `requirements.txt`/`pyproject.toml` for Python). Routing, component patterns, and state management differ significantly across frameworks â€” identification enables accurate parsing.

#### 2. Build Route & Page Inventory

Extract all pages from route config into a complete **page inventory**:

| Field | Description |
|-------|-------------|
| Route path | e.g. `/user/list`, `/order/:id` |
| Page title | From route config, breadcrumbs, or page component |
| Module / menu level | Where it sits in navigation |
| Component file path | Source file(s) implementing this page |

For file-system routing (Next.js, Nuxt), infer from directory structure.

**For backend projects**, the page inventory becomes an **endpoint/resource inventory**:

| Field | Description |
|-------|-------------|
| Endpoint path | e.g. `/api/users`, `/api/orders/:id` |
| HTTP method | GET, POST, PUT, DELETE, PATCH |
| Controller/view | Source file handling this route |
| Module/app | Which NestJS module or Django app owns it |
| Auth required | Whether authentication/permissions are needed |

For NestJS: extract from `@Controller` + `@Get/@Post/@Put/@Delete` decorators.
For Django: extract from `urls.py` â†’ `urlpatterns` and `viewsets.py` â†’ router registrations.

#### 3. Map Global Context

Before analyzing individual pages, capture:

- **Global state** â€” user info, permissions, feature flags, config
- **Shared components** â€” layout, nav, auth guards, error boundaries
- **Enums & constants** â€” status codes, type mappings, role definitions
- **API base config** â€” base URL, interceptors, auth headers, error handling
- **Database models** (backend) â€” entity relationships, field types, constraints
- **Middleware** (backend) â€” auth middleware, rate limiting, logging, CORS
- **DTOs/Serializers** (backend) â€” request validation shapes, response formats

These will be referenced throughout page/endpoint analysis.

---

### Phase 2 â€” Page-by-Page Deep Analysis

Analyze every page in the inventory. **Each page produces its own Markdown file.**

#### Analysis Dimensions

For each page, answer:

##### A. Page Overview
- What does this page do? (one sentence)
- Where does it fit in the system?
- What scenario brings a user here?

##### B. Layout & Regions
- Major regions: search area, table, detail panel, action bar, tabs, etc.
- Spatial arrangement: top/bottom, left/right, nested

##### C. Field Inventory (core â€” be exhaustive)

**For form pages**, list every field:

| Field Name | Type | Required | Default | Validation | Business Description |
|-----------|------|----------|---------|------------|---------------------|
| Username | Text input | Yes | â€” | Max 20 chars | System login account |

**For table/list pages**, list:
- Search/filter fields (type, required, enum options)
- Table columns (name, format, sortable, filterable)
- Row action buttons (what each one does)

**Field name extraction priority:**
1. Hardcoded display text in code
2. i18n translation values
3. Component `placeholder` / `label` / `title` props
4. Variable names (last resort â€” provide reasonable display name)

##### D. Interaction Logic

Describe as **"user action â†’ system response"**:

```
[Action]     User clicks "Create"
[Response]   Modal opens with form fields: ...
[Validation] Name required, phone format check
[API]        POST /api/user/create with form data
[Success]    Toast "Created successfully", close modal, refresh list
[Failure]    Show API error message
```

**Cover all interaction types:**
- Page load / initialization (default queries, preloaded data)
- Search / filter / reset
- CRUD operations (create, read, update, delete)
- Table: pagination, sorting, row selection, bulk actions
- Form submission & validation
- Status transitions (e.g. approval flows: pending â†’ approved â†’ rejected)
- Import / export
- Field interdependencies (selecting value A changes options in field B)
- Permission controls (buttons/fields visible only to certain roles)
- Polling / auto-refresh / real-time updates

##### E. API Dependencies

**Case 1: API is integrated** (real HTTP calls in code)

| API Name | Method | Path | Trigger | Key Params | Notes |
|----------|--------|------|---------|-----------|-------|
| Get users | GET | /api/user/list | Load, search | page, size, keyword | Paginated |

**Case 2: API not integrated** (mock/hardcoded data)

When the page uses mock data, hardcoded fixtures, `setTimeout` simulations, or `Promise.resolve()` stubs â€” the API isn't real yet. **Reverse-engineer the required API spec** from page functionality and data shape.

For each needed API, document:
- Method, suggested path, trigger
- Input params (name, type, required, description)
- Output fields (name, type, description)
- Core business logic description

**Detection signals:**
- `setTimeout` / `Promise.resolve()` returning data â†’ mock
- Data defined in component or `*.mock.*` files â†’ mock
- Real HTTP calls (`axios`, `fetch`, service layer) with real paths â†’ integrated
- `__mocks__` directory â†’ mock

##### F. Page Relationships

- **Inbound**: Which pages link here? What parameters do they pass?
- **Outbound**: Where can users navigate from here? What parameters?
- **Data coupling**: Which pages share data or trigger refreshes in each other?

---

### Phase 3 â€” Generate Documentation

#### Output Structure

Create `prd/` in project root (or user-specified directory):

```
prd/
â”œâ”€â”€ README.md                     # System overview
â”œâ”€â”€ pages/
â”‚   â”œâ”€â”€ 01-user-mgmt-list.md      # One file per page
â”‚   â”œâ”€â”€ 02-user-mgmt-detail.md
â”‚   â”œâ”€â”€ 03-order-mgmt-list.md
â”‚   â””â”€â”€ ...
â””â”€â”€ appendix/
    â”œâ”€â”€ enum-dictionary.md         # All enums, status codes, type mappings
    â”œâ”€â”€ page-relationships.md      # Navigation map between pages
    â””â”€â”€ api-inventory.md           # Complete API reference
```

#### README.md Template

```markdown
# [System Name] â€” Product Requirements Document

## System Overview
[2-3 paragraphs: what the system does, business context, primary users]

## Module Overview

| Module | Pages | Core Functionality |
|--------|-------|--------------------|
| User Management | User list, User detail, Role mgmt | CRUD users, assign roles and permissions |

## Page Inventory

| # | Page Name | Route | Module | Doc Link |
|---|-----------|-------|--------|----------|
| 1 | User List | /user/list | User Mgmt | [â†’](./pages/01-user-mgmt-list.md) |

## Global Notes

### Permission Model
[Summarize auth/role system if present in code]

### Common Interaction Patterns
[Global rules: all deletes require confirmation, lists default to created_at desc, etc.]
```

#### Per-Page Document Template

```markdown
# [Page Name]

> **Route:** `/xxx/xxx`
> **Module:** [Module name]
> **Generated:** [Date]

## Overview
[2-3 sentences: core function and use case]

## Layout
[Region breakdown â€” text description or ASCII diagram]

## Fields

### [Region: e.g. "Search Filters"]
| Field | Type | Required | Options / Enum | Default | Notes |
|-------|------|----------|---------------|---------|-------|

### [Region: e.g. "Data Table"]
| Column | Format | Sortable | Filterable | Notes |
|--------|--------|----------|-----------|-------|

### [Region: e.g. "Actions"]
| Button | Visibility Condition | Behavior |
|--------|---------------------|----------|

## Interactions

### Page Load
[What happens on mount]

### [Scenario: e.g. "Search"]
- **Trigger:** [User action]
- **Behavior:** [System response]
- **Special rules:** [If any]

### [Scenario: e.g. "Create"]
- **Trigger:** ...
- **Modal/drawer content:** [Fields and logic inside]
- **Validation:** ...
- **On success:** ...

## API Dependencies

| API | Method | Path | Trigger | Notes |
|-----|--------|------|---------|-------|
| ... | ... | ... | ... | ... |

## Page Relationships
- **From:** [Source pages + params]
- **To:** [Target pages + params]
- **Data coupling:** [Cross-page refresh triggers]

## Business Rules
[Anything that doesn't fit above]
```

---

## Key Principles

### 1. Business Language First
Don't write "calls `useState` to manage loading state." Write "search button shows a spinner to prevent duplicate submissions."

Don't write "useEffect fetches on mount." Write "page automatically loads the first page of results on open."

Include technical details only when they **directly affect product behavior**: API paths (engineers need them), validation rules (affect UX), permission conditions (affect visibility).

### 2. Don't Miss Hidden Logic
Code contains logic PMs may not realize exists:
- Field interdependencies (type A shows field X; type B shows field Y)
- Conditional button visibility
- Data formatting (currency with 2 decimals, date formats, status label mappings)
- Default sort order and page size
- Debounce/throttle effects on user input
- Polling / auto-refresh intervals

### 3. Exhaustively List Enums
When code defines enums (status codes, type codes, role types), list **every value and its meaning**. These are often scattered across constants files, component `valueEnum` configs, or API response mappers.

### 4. Mark Uncertainty â€” Don't Guess
If a field or logic's business meaning can't be determined from code (e.g. abbreviated variable names, overly complex conditionals), mark it `[TBC]` and explain what you observed and why you're uncertain. Never fabricate business meaning.

### 5. Keep Page Files Self-Contained
Each page's Markdown should be **standalone** â€” reading just that file gives complete understanding. Use relative links when referencing other pages or appendix entries.

---

## Page Type Strategies

### Frontend Pages

| Page Type | Focus Areas |
|-----------|------------|
| **List / Table** | Search conditions, columns, row actions, pagination, bulk ops |
| **Form / Create-Edit** | Every field, validation, interdependencies, post-submit behavior |
| **Detail / View** | Displayed info, tab/section organization, available actions |
| **Modal / Drawer** | Describe as part of triggering page â€” not a separate file. But fully document content |
| **Dashboard** | Data cards, charts, metrics meaning, filter dimensions, refresh frequency |

### Backend Endpoints (NestJS / Django / Express)

| Endpoint Type | Focus Areas |
|---------------|------------|
| **CRUD resource** | All fields (from DTO/serializer), validation rules, permissions, pagination, filtering, sorting |
| **Auth endpoints** | Login/register flow, token format, refresh logic, password reset, OAuth providers |
| **File upload** | Accepted types, size limits, storage destination, processing pipeline |
| **Webhook / event** | Trigger conditions, payload shape, retry policy, idempotency |
| **Background job** | Trigger, schedule, input/output, failure handling, monitoring |
| **Admin views** (Django) | Registered models, list_display, search_fields, filters, inline models, custom actions |

---

## Execution Pacing

**Large projects (>15 pages):** Work in batches of 3-5 pages per module. Complete system overview + page inventory first. Output each batch for user review before proceeding.

**Small projects (â‰¤15 pages):** Complete all analysis in one pass.

---

## Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Using component names as page names | `UserManagementTable` â†’ "User Management List" |
| Skipping modals and drawers | They contain critical business logic â€” document fully |
| Missing i18n field names | Check translation files, not just component JSX |
| Ignoring dynamic route params | `/order/:id` = page requires an order ID to load |
| Forgetting permission controls | Document which roles see which buttons/pages |
| Assuming all APIs are real | Check for mock data patterns before documenting endpoints |
| Skipping Django admin customization | `admin.py` often contains critical business rules (list filters, custom actions, inlines) |
| Missing NestJS guards/pipes | `@UseGuards`, `@UsePipes` contain auth and validation logic that affects behavior |
| Ignoring database constraints | Model field constraints (unique, max_length, choices) are validation rules for the PRD |
| Overlooking middleware | Auth middleware, rate limiters, and CORS config define system-wide behavior |

---

## Tooling

### Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/codebase_analyzer.py` | Scan codebase â†’ extract routes, APIs, models, enums, structure | `python3 codebase_analyzer.py /path/to/project` |
| `scripts/prd_scaffolder.py` | Generate PRD directory skeleton from analysis JSON | `python3 prd_scaffolder.py analysis.json` |

**Recommended workflow:**
```bash
# 1. Analyze the project (JSON output â€” works for frontend, backend, or fullstack)
python3 scripts/codebase_analyzer.py /path/to/project -o analysis.json

# 2. Review the analysis (markdown summary)
python3 scripts/codebase_analyzer.py /path/to/project -f markdown

# 3. Scaffold the PRD directory with stubs
python3 scripts/prd_scaffolder.py analysis.json -o prd/ -n "My App"

# 4. Fill in TODO sections page-by-page using the SKILL.md workflow
```

Both scripts are **stdlib-only** â€” no pip install needed.

### References

| File | Contents |
|------|----------|
| `references/prd-quality-checklist.md` | Validation checklist for completeness, accuracy, readability |
| `references/framework-patterns.md` | Framework-specific patterns for routes, state, APIs, forms, permissions |

---

## Attribution

This skill was inspired by [code-to-prd](https://github.com/lihanglogan/code-to-prd) by [@lihanglogan](https://github.com/lihanglogan), who proposed the original concept and methodology in [PR #368](https://github.com/alirezarezvani/claude-skills/pull/368). The core three-phase workflow (global scan â†’ page-by-page analysis â†’ structured document generation) originated from that work. This version was rebuilt from scratch in English with added tooling (analysis scripts, scaffolder, framework reference, quality checklist).
