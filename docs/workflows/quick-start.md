# Quick Start Guide

Get up and running with docker-ops workflows in 5 minutes.

## Basic Setup

### 1. Choose Your Workflow Pattern

#### Option A: Full CI/CD Pipeline

```yaml
# .github/workflows/ci-cd.yml
name: Container CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  quality-check:
    uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.3.0
    secrets: inherit

  security-scan:
    uses: broadsage-containers/docker-ops/.github/workflows/dependency-review.yml@v0.3.0
    secrets: inherit

  build-validate:
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.3.0
    with:
      push_image: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
    secrets: inherit
```

#### Option B: Minimal Quality Gate

```yaml
# .github/workflows/quality.yml
name: Quality Check
on: [push, pull_request]

jobs:
  quality:
    uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.3.0
    secrets: inherit
```

### 2. Version Selection

- **Production**: Pin to specific version `@v0.3.0`
- **Development**: Use latest `@main` (higher risk)

### 3. Required Secrets

Most workflows work with default `GITHUB_TOKEN`. For advanced features:

- `AUTOBOT_GITHUB_TOKEN` - Enhanced automation
- `GPG_PRIVATE_KEY` - Commit signing
- `REGISTRY_TOKEN` - Container registry access

## Next Steps

- [Configuration Guide](configuration.md) - Customize workflow behavior
- [Workflow Catalog](catalog.md) - Explore all available workflows
- [VERSION.md](../../VERSION.md) - Check latest versions
