# Configuration Guide

Detailed configuration options for all docker-ops workflows.

## Common Patterns

### Default Configuration (Recommended)

```yaml
jobs:
  quality:
    uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.3.0
    secrets: inherit
```

### Custom Configuration

```yaml
jobs:
  build:
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.3.0
    with:
      build_platforms: "linux/amd64"
      timeout_minutes: 120
      containers_path: "docker"
    secrets: inherit
```

## Workflow-Specific Options

### quality-gate.yml

- **apply_fixes**: `all`, `none` (default: `all`)
- **megalinter_flavor**: `cupcake`, `docker`, `ci_light` (default: `cupcake`)
- **enable_comments**: `true`, `false` (default: `true`)

### dependency-review.yml

- **fail_on_severity**: `low`, `moderate`, `high`, `critical` (default: `moderate`)
- **allow_licenses**: License list (default: `MIT, Apache-2.0, BSD-*`)
- **comment_summary_in_pr**: `true`, `false` (default: `true`)

### pr-build-validate.yml

- **build_platforms**: Platform list (default: `linux/amd64`)
- **push_image**: `true`, `false` (default: `false`)
- **enable_security_scan**: `true`, `false` (default: `true`)
- **containers_path**: Directory path (default: `library`)

### pr-build-publish.yml

- **build_platforms**: Platform list (default: `linux/amd64,linux/arm64`)
- **enable_cosign**: `true`, `false` (default: `true`)
- **enable_attestations**: `true`, `false` (default: `true`)
- **enable_sbom**: `true`, `false` (default: `true`)

## Required Secrets

### Basic Workflows

- **GITHUB_TOKEN**: Automatically provided by GitHub

### Advanced Features

- **AUTOBOT_GITHUB_TOKEN**: Enhanced automation capabilities
- **GPG_PRIVATE_KEY**: Commit signing
- **REGISTRY_TOKEN**: Container registry access
- **COSIGN_KEY**: Container signing key

## Best Practices

1. **Pin versions in production**: Use specific versions like `@v0.3.0`
2. **Start with defaults**: Override only when needed
3. **Use secrets inherit**: Simplifies secret management
4. **Monitor workflow runs**: Check for failures and warnings