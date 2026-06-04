---
name: docker-development
description: Docker and container development agent skill and plugin for Dockerfile optimization, docker-compose orchestration, multi-stage builds, and container security hardening. Use when: user wants to optimize a Dockerfile, create or improve docker-compose configurations, implement multi-stage builds, audit container security, reduce image size, or follow container best practices. Covers build performance, layer caching, secret management, and production-ready container patterns.
---

# Docker Development

> Smaller images. Faster builds. Secure containers. No guesswork.

Opinionated Docker workflow that turns bloated Dockerfiles into production-grade containers. Covers optimization, multi-stage builds, compose orchestration, and security hardening.

Not a Docker tutorial â€” a set of concrete decisions about how to build containers that don't waste time, space, or attack surface.

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/docker:optimize` | Analyze and optimize a Dockerfile for size, speed, and layer caching |
| `/docker:compose` | Generate or improve docker-compose.yml with best practices |
| `/docker:security` | Audit a Dockerfile or running container for security issues |

---

## When This Skill Activates

Recognize these patterns from the user:

- "Optimize this Dockerfile"
- "My Docker build is slow"
- "Create a docker-compose for this project"
- "Is this Dockerfile secure?"
- "Reduce my Docker image size"
- "Set up multi-stage builds"
- "Docker best practices for [language/framework]"
- Any request involving: Dockerfile, docker-compose, container, image size, build cache, Docker security

If the user has a Dockerfile or wants to containerize something â†’ this skill applies.

---

## Workflow

### `/docker:optimize` â€” Dockerfile Optimization

1. **Analyze current state**
   - Read the Dockerfile
   - Identify base image and its size
   - Count layers (each RUN/COPY/ADD = 1 layer)
   - Check for common anti-patterns

2. **Apply optimization checklist**

   ```
   BASE IMAGE
   â”œâ”€â”€ Use specific tags, never :latest in production
   â”œâ”€â”€ Prefer slim/alpine variants (debian-slim > ubuntu > debian)
   â”œâ”€â”€ Pin digest for reproducibility in CI: image@sha256:...
   â””â”€â”€ Match base to runtime needs (don't use python:3.12 for a compiled binary)

   LAYER OPTIMIZATION
   â”œâ”€â”€ Combine related RUN commands with && \
   â”œâ”€â”€ Order layers: least-changing first (deps before source code)
   â”œâ”€â”€ Clean package manager cache in the same RUN layer
   â”œâ”€â”€ Use .dockerignore to exclude unnecessary files
   â””â”€â”€ Separate build deps from runtime deps

   BUILD CACHE
   â”œâ”€â”€ COPY dependency files before source code (package.json, requirements.txt, go.mod)
   â”œâ”€â”€ Install deps in a separate layer from code copy
   â”œâ”€â”€ Use BuildKit cache mounts: --mount=type=cache,target=/root/.cache
   â””â”€â”€ Avoid COPY . . before dependency installation

   MULTI-STAGE BUILDS
   â”œâ”€â”€ Stage 1: build (full SDK, build tools, dev deps)
   â”œâ”€â”€ Stage 2: runtime (minimal base, only production artifacts)
   â”œâ”€â”€ COPY --from=builder only what's needed
   â””â”€â”€ Final image should have NO build tools, NO source code, NO dev deps
   ```

3. **Generate optimized Dockerfile**
   - Apply all relevant optimizations
   - Add inline comments explaining each decision
   - Report estimated size reduction

4. **Validate**
   ```bash
   python3 scripts/dockerfile_analyzer.py Dockerfile
   ```

### `/docker:compose` â€” Docker Compose Configuration

1. **Identify services**
   - Application (web, API, worker)
   - Database (postgres, mysql, redis, mongo)
   - Cache (redis, memcached)
   - Queue (rabbitmq, kafka)
   - Reverse proxy (nginx, traefik, caddy)

2. **Apply compose best practices**

   ```
   SERVICES
   â”œâ”€â”€ Use depends_on with condition: service_healthy
   â”œâ”€â”€ Add healthchecks for every service
   â”œâ”€â”€ Set resource limits (mem_limit, cpus)
   â”œâ”€â”€ Use named volumes for persistent data
   â””â”€â”€ Pin image versions

   NETWORKING
   â”œâ”€â”€ Create explicit networks (don't rely on default)
   â”œâ”€â”€ Separate frontend and backend networks
   â”œâ”€â”€ Only expose ports that need external access
   â””â”€â”€ Use internal: true for backend-only networks

   ENVIRONMENT
   â”œâ”€â”€ Use env_file for secrets, not inline environment
   â”œâ”€â”€ Never commit .env files (add to .gitignore)
   â”œâ”€â”€ Use variable substitution: ${VAR:-default}
   â””â”€â”€ Document all required env vars

   DEVELOPMENT vs PRODUCTION
   â”œâ”€â”€ Use compose profiles or override files
   â”œâ”€â”€ Dev: bind mounts for hot reload, debug ports exposed
   â”œâ”€â”€ Prod: named volumes, no debug ports, restart: unless-stopped
   â””â”€â”€ docker-compose.override.yml for dev-only config
   ```

3. **Generate compose file**
   - Output docker-compose.yml with healthchecks, networks, volumes
   - Generate .env.example with all required variables documented
   - Add dev/prod profile annotations

### `/docker:security` â€” Container Security Audit

1. **Dockerfile audit**

   | Check | Severity | Fix |
   |-------|----------|-----|
   | Running as root | Critical | Add `USER nonroot` after creating user |
   | Using :latest tag | High | Pin to specific version |
   | Secrets in ENV/ARG | Critical | Use BuildKit secrets: `--mount=type=secret` |
   | COPY with broad glob | Medium | Use specific paths, add .dockerignore |
   | Unnecessary EXPOSE | Low | Only expose ports the app uses |
   | No HEALTHCHECK | Medium | Add HEALTHCHECK with appropriate interval |
   | Privileged instructions | High | Avoid `--privileged`, drop capabilities |
   | Package manager cache retained | Low | Clean in same RUN layer |

2. **Runtime security checks**

   | Check | Severity | Fix |
   |-------|----------|-----|
   | Container running as root | Critical | Set user in Dockerfile or compose |
   | Writable root filesystem | Medium | Use `read_only: true` in compose |
   | All capabilities retained | High | Drop all, add only needed: `cap_drop: [ALL]` |
   | No resource limits | Medium | Set `mem_limit` and `cpus` |
   | Host network mode | High | Use bridge or custom network |
   | Sensitive mounts | Critical | Never mount /etc, /var/run/docker.sock in prod |
   | No log driver configured | Low | Set `logging:` with size limits |

3. **Generate security report**
   ```
   SECURITY AUDIT â€” [Dockerfile/Image name]
   Date: [timestamp]

   CRITICAL: [count]
   HIGH:     [count]
   MEDIUM:   [count]
   LOW:      [count]

   [Detailed findings with fix recommendations]
   ```

---

## Tooling

### `scripts/dockerfile_analyzer.py`

CLI utility for static analysis of Dockerfiles.

**Features:**
- Layer count and optimization suggestions
- Base image analysis with size estimates
- Anti-pattern detection (15+ rules)
- Security issue flagging
- Multi-stage build detection and validation
- JSON and text output

**Usage:**
```bash
# Analyze a Dockerfile
python3 scripts/dockerfile_analyzer.py Dockerfile

# JSON output
python3 scripts/dockerfile_analyzer.py Dockerfile --output json

# Analyze with security focus
python3 scripts/dockerfile_analyzer.py Dockerfile --security

# Check a specific directory
python3 scripts/dockerfile_analyzer.py path/to/Dockerfile
```

### `scripts/compose_validator.py`

CLI utility for validating docker-compose files.

**Features:**
- Service dependency validation
- Healthcheck presence detection
- Network configuration analysis
- Volume mount validation
- Environment variable audit
- Port conflict detection
- Best practice scoring

**Usage:**
```bash
# Validate a compose file
python3 scripts/compose_validator.py docker-compose.yml

# JSON output
python3 scripts/compose_validator.py docker-compose.yml --output json

# Strict mode (fail on warnings)
python3 scripts/compose_validator.py docker-compose.yml --strict
```

---

## Multi-Stage Build Patterns

### Pattern 1: Compiled Language (Go, Rust, C++)

```dockerfile
# Build stage
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -ldflags="-s -w" -o /app/server ./cmd/server

# Runtime stage
FROM gcr.io/distroless/static-debian12
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

### Pattern 2: Node.js / TypeScript

```dockerfile
# Dependencies stage
FROM node:20-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --production=false

# Build stage
FROM deps AS builder
COPY . .
RUN npm run build

# Runtime stage
FROM node:20-alpine
WORKDIR /app
RUN addgroup -g 1001 -S appgroup && adduser -S appuser -u 1001
COPY --from=builder /app/dist ./dist
COPY --from=deps /app/node_modules ./node_modules
COPY package.json ./
USER appuser
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Pattern 3: Python

```dockerfile
# Build stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Runtime stage
FROM python:3.12-slim
WORKDIR /app
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
COPY --from=builder /install /usr/local
COPY . .
USER appuser
EXPOSE 8000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Base Image Decision Tree

```
Is it a compiled binary (Go, Rust, C)?
â”œâ”€â”€ Yes â†’ distroless/static or scratch
â””â”€â”€ No
    â”œâ”€â”€ Need a shell for debugging?
    â”‚   â”œâ”€â”€ Yes â†’ alpine variant (e.g., node:20-alpine)
    â”‚   â””â”€â”€ No â†’ distroless variant
    â”œâ”€â”€ Need glibc (not musl)?
    â”‚   â”œâ”€â”€ Yes â†’ slim variant (e.g., python:3.12-slim)
    â”‚   â””â”€â”€ No â†’ alpine variant
    â””â”€â”€ Need specific OS packages?
        â”œâ”€â”€ Many â†’ debian-slim
        â””â”€â”€ Few â†’ alpine + apk add
```

---

## Proactive Triggers

Flag these without being asked:

- **Dockerfile uses :latest** â†’ Suggest pinning to a specific version tag.
- **No .dockerignore** â†’ Create one. At minimum: `.git`, `node_modules`, `__pycache__`, `.env`.
- **COPY . . before dependency install** â†’ Cache bust. Reorder to install deps first.
- **Running as root** â†’ Add USER instruction. No exceptions for production.
- **Secrets in ENV or ARG** â†’ Use BuildKit secret mounts. Never bake secrets into layers.
- **Image over 1GB** â†’ Multi-stage build required. No reason for a production image this large.
- **No healthcheck** â†’ Add one. Orchestrators (Compose, K8s) need it for proper lifecycle management.
- **apt-get without cleanup in same layer** â†’ `rm -rf /var/lib/apt/lists/*` in the same RUN.

---

## Installation

### One-liner (any tool)
```bash
git clone https://github.com/alirezarezvani/claude-skills.git
cp -r claude-skills/engineering/docker-development ~/.claude/skills/
```

### Multi-tool install
```bash
./scripts/convert.sh --skill docker-development --tool codex|gemini|cursor|windsurf|openclaw
```

### OpenClaw
```bash
clawhub install cs-docker-development
```

---

## Related Skills

- **senior-devops** â€” Broader DevOps scope (CI/CD, IaC, monitoring). Complementary â€” use docker-development for container-specific work, senior-devops for pipeline and infrastructure.
- **senior-security** â€” Application security. Complementary â€” docker-development covers container security, senior-security covers application-level threats.
- **autoresearch-agent** â€” Can optimize Docker build times or image sizes as measurable experiments.
- **ci-cd-pipeline-builder** â€” Pipeline construction. Complementary â€” docker-development builds the containers, ci-cd-pipeline-builder deploys them.
