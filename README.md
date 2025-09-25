# 🐳 Docker Operations (docker-ops)

Centralized GitHub Actions workflows for **Docker Container** operations across all Broadsage Container repositories.

> **📋 Version Information**: See [VERSION.md](VERSION.md) for current versions and usage recommendations.

## 🚀 Quick Start

### Using in Your Repository

Add one of these workflow files to your repository's `.github/workflows/` directory:

> **📋 Version Note**: Examples below show `v0.2.4`. Check [VERSION.md](VERSION.md) for the latest version numbers.

#### Basic Container CI/CD

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
    uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.2.6.2.5
    secrets: inherit

  security-scan:
    uses: broadsage-containers/docker-ops/.github/workflows/security-scorecard.yml@v0.2.6.2.5
    permissions:
      security-events: write
      contents: read
      actions: read

  dependency-check:
    uses: broadsage-containers/docker-ops/.github/workflows/dependency-review.yml@v0.2.6.2.5
    secrets: inherit

  build-validate:
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.2.6.2.5
    with:
      push_image: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
    secrets: inherit

  publish:
    needs: [quality-check, security-scan, build-validate]
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-publish.yml@v0.2.6.2.5
    with:
      enable_cosign: true
      enable_attestations: true
    secrets: inherit
```

#### Community Management

```yaml
# .github/workflows/community.yml
name: Community Management
on:
  schedule:
    - cron: "0 2 * * *"  # Daily at 02:00 UTC
  workflow_dispatch:

jobs:
  community-management:
    uses: broadsage-containers/docker-ops/.github/workflows/community-management.yml@v0.2.6.2.5
    with:
      days_before_stale: 60
      days_before_close: 7
    secrets: inherit
```

## 📋 Available Workflows

| Workflow | Purpose | Key Features |
|----------|---------|--------------|
| [quality-gate.yml](.github/workflows/quality-gate.yml) | Code quality & linting | MegaLinter, automated fixes |
| [security-scorecard.yml](.github/workflows/security-scorecard.yml) | OpenSSF security analysis | Repository security posture, scoring |
| [dependency-review.yml](.github/workflows/dependency-review.yml) | PR dependency analysis | Vulnerability & license checking |
| [pr-build-validate.yml](.github/workflows/pr-build-validate.yml) | PR container builds & validation | Multi-platform builds, Hadolint, Trivy |
| [pr-build-publish.yml](.github/workflows/pr-build-publish.yml) | PR container publishing | Cosign signing, SBOM, attestations |
| [community-management.yml](.github/workflows/community-management.yml) | Issue/PR lifecycle | Stale management, solved issues |

## 🎛️ **Workflow Configuration**

All workflows come with **sensible defaults** for enterprise use. Most repositories can use workflows without any configuration:

> **📋 Version Reference**: Examples show `v0.2.4`. Check [VERSION.md](VERSION.md) for the latest version numbers.

```yaml
# Minimal configuration - uses all defaults
jobs:
  quality:
    uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.2.6.2.5
    secrets: inherit
    
  build:
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.2.6.2.5
    secrets: inherit
```

### **Customization When Needed**

Override only the settings that differ from defaults:

```yaml
# Custom configuration - override specific settings
jobs:
  build:
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.2.6.2.5
    with:
      build_platforms: "linux/amd64"        # Override: single platform
      timeout_minutes: 120                  # Override: longer timeout
      containers_path: "docker"             # Override: different path
      # All other settings use secure defaults
    secrets: inherit
```

## 🛠️ Workflow Inputs

### quality-gate.yml

- `apply_fixes`: Apply linter fixes (`all`, `none`) - default: `all`
- `megalinter_flavor`: MegaLinter flavor - default: `cupcake`
- `enable_comments`: Enable PR comments - default: `true`

### security-scorecard.yml

- `publish_results`: Publish to OpenSSF API - default: `true`
- `retention_days`: Artifact retention - default: `5`
- `enable_code_scanning_upload`: Upload to code scanning - default: `true`

### dependency-review.yml

- `fail_on_severity`: Vulnerability severity threshold - default: `moderate`
- `allow_licenses`: Allowed license list - default: `MIT, Apache-2.0, BSD-*`
- `comment_summary_in_pr`: Comment in PR - default: `true`

### pr-build-validate.yml

- `build_platforms`: Build platforms - default: `linux/amd64`
- `push_image`: Push built images - default: `false`
- `enable_security_scan`: Enable Trivy scanning - default: `true`
- `containers_path`: Container directory - default: `library`

### pr-build-publish.yml

- `build_platforms`: Production platforms - default: `linux/amd64,linux/arm64`
- `enable_cosign`: Enable signing - default: `true`
- `enable_attestations`: Enable attestations - default: `true`
- `enable_sbom`: Enable SBOM - default: `true`

### community-management.yml

- `days_before_stale`: Days before stale - default: `60`
- `days_before_close`: Days before close - default: `7`
- `exempt_issue_labels`: Protected labels - default: `pinned,security,enhancement`

## 🔒 Security Features

All workflows include enterprise-grade security features:

- **Container Signing**: Cosign signatures for authenticity
- **SBOM Generation**: Software Bill of Materials  
- **Build Attestations**: Provenance tracking
- **Vulnerability Scanning**: Trivy security scans
- **OpenSSF Scorecard**: Security posture analysis
- **Dependency Review**: Automated dependency checks

## ✨ Why Unified Versioning?

Our new unified versioning approach provides significant benefits:

- **🎯 Simplified Management**: One version number for all workflows
- **📦 Consistent Releases**: All workflow updates bundled together
- **🔒 Stable References**: No force-updated tags that break consumers
- **📈 Industry Standard**: Follows GitHub Actions best practices
- **🔍 Clear Changelog**: Single release notes with all changes
- **⚡ Easier Upgrades**: Update once to get all improvements

This approach eliminates the complexity of managing dozens of workflow-specific tags while providing a more predictable and maintainable versioning strategy.

## 📊 Versioning

This repository uses **unified semantic versioning** for all workflows:

- **v1.2.3** - Specific release version (recommended for production)
- **main** - Latest development version (automatic updates)

### 🏆 Recommended Usage Patterns

```yaml
# 🔒 PRODUCTION: Pin to specific version for maximum stability
uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@0.1.6

# ⚡ DEVELOPMENT: Use main branch for latest features (higher risk)
uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@main
```

### Version Bump Strategy

This repository follows **semantic versioning**:

- **Major (v2.0.0)**: Breaking changes that require consumer updates
- **Minor (v1.1.0)**: New features, backward compatible
- **Patch (v1.0.1)**: Bug fixes, security updates, dependencies

### 📈 Version History

See our [Releases](https://github.com/broadsage-containers/docker-ops/releases) page for detailed changelogs and upgrade guides.

## 🤝 Contributing

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'feat: add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- **Issues**: [GitHub Issues](https://github.com/broadsage-containers/docker-ops/issues)
- **Discussions**: [GitHub Discussions](https://github.com/broadsage-containers/docker-ops/discussions)
- **Email**: [containers@broadsage.com](mailto:containers@broadsage.com)

---

### Made with ❤️ by the Broadsage Containers Team
