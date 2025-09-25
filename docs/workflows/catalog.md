# Available Workflows

Complete catalog of reusable GitHub Actions workflows for Docker operations.

## Core Workflows

| Workflow | Purpose | Inputs | Secrets |
|----------|---------|---------|---------|
| **quality-gate.yml** | Code quality & linting | `apply_fixes`, `megalinter_flavor` | `GITHUB_TOKEN` |
| **dependency-review.yml** | Dependency analysis | `fail_on_severity`, `allow_licenses` | `GITHUB_TOKEN` |
| **pr-build-validate.yml** | Build & validate containers | `build_platforms`, `enable_security_scan` | `GITHUB_TOKEN` |
| **pr-build-publish.yml** | Publish containers | `enable_cosign`, `enable_attestations` | `GITHUB_TOKEN` |

## Specialized Workflows

| Workflow | Purpose | Use Case |
|----------|---------|----------|
| **security-scorecard.yml** | OpenSSF security analysis | Security posture assessment |
| **community-management.yml** | Issue/PR lifecycle | Automated community management |
| **workflow-release.yml** | Workflow versioning | Internal workflow management |
| **version-docs.yml** | Documentation updates | Version reference management |

## Quick Reference

### Most Common Usage Patterns

```yaml
# Quality gate for all PRs
quality:
  uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.3.0
  secrets: inherit

# Container build and security scan  
build:
  uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.3.0
  secrets: inherit

# Dependency vulnerability check
security:
  uses: broadsage-containers/docker-ops/.github/workflows/dependency-review.yml@v0.3.0
  secrets: inherit
```

For detailed configuration options, see [configuration.md](configuration.md).