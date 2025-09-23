# 🐳 Docker Operations (docker-ops)

Centralized GitHub Actions workflows for **Docker Container** operations across all Broadsage Container repositories.

## 🚀 Quick Start

### Using in Your Repository

Add one of these workflow files to your repository's `.github/workflows/` directory:

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
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/quality-gate.yml@v1
    secrets: inherit

  security-scan:
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/security-scorecard.yml@v1
    secrets: inherit

  dependency-check:
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/dependency-review.yml@v1
    secrets: inherit

  build-validate:
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/pr-build-validate.yml@v1
    with:
      push_image: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
    secrets: inherit

  publish:
    needs: [quality-check, security-scan, build-validate]
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/pr-build-publish.yml@v1
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
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/community-management.yml@v1
    with:
      days_before_stale: 60
      days_before_close: 7
    secrets: inherit
```

## 📋 Available Workflows

| Workflow | Purpose | Key Features |
|----------|---------|--------------|
| [quality-gate.yml](.github/workflows/reusable/quality-gate.yml) | Code quality & linting | MegaLinter, automated fixes |
| [security-scorecard.yml](.github/workflows/reusable/security-scorecard.yml) | OpenSSF security analysis | Repository security posture, scoring |
| [dependency-review.yml](.github/workflows/reusable/dependency-review.yml) | PR dependency analysis | Vulnerability & license checking |
| [security-full.yml](.github/workflows/reusable/security-full.yml) | Complete security analysis | Combined scorecard + dependency review |
| [pr-build-validate.yml](.github/workflows/reusable/pr-build-validate.yml) | PR container builds & validation | Multi-platform builds, Hadolint, Trivy |
| [pr-build-publish.yml](.github/workflows/reusable/pr-build-publish.yml) | PR container publishing | Cosign signing, SBOM, attestations |
| [community-management.yml](.github/workflows/reusable/community-management.yml) | Issue/PR lifecycle | Stale management, solved issues |

## 🎛️ **Workflow Configuration**

All workflows come with **sensible defaults** for enterprise use. Most repositories can use workflows without any configuration:

```yaml
# Minimal configuration - uses all defaults
jobs:
  quality:
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/quality-gate.yml@v1
    secrets: inherit
    
  build:
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/pr-build-validate.yml@v1
    secrets: inherit
```

### **Customization When Needed**

Override only the settings that differ from defaults:

```yaml
# Custom configuration - override specific settings
jobs:
  build:
    uses: broadsage-containers/docker-ops/.github/workflows/reusable/pr-build-validate.yml@v1
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

### security-full.yml

- `run_scorecard`: Enable Scorecard analysis - default: `true`
- `run_dependency_review`: Enable dependency review - default: `true`
- `publish_scorecard_results`: Publish Scorecard results - default: `true`

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

## 📚 Documentation

- [Getting Started Guide](docs/getting-started/quick-start.md)
- [Migration Guide](docs/getting-started/migration-guide.md)
- [Workflow Reference](docs/reference/workflows.md)
- [Security Features](docs/reference/security.md)
- [Troubleshooting](docs/troubleshooting/common-issues.md)

## 🔒 Security Features

All workflows include enterprise-grade security features:

- **Container Signing**: Cosign signatures for authenticity
- **SBOM Generation**: Software Bill of Materials  
- **Build Attestations**: Provenance tracking
- **Vulnerability Scanning**: Trivy security scans
- **OpenSSF Scorecard**: Security posture analysis
- **Dependency Review**: Automated dependency checks

## 📊 Versioning

This repository follows semantic versioning:

- `v1` - Latest stable major version
- `v1.2` - Latest in v1.2.x series  
- `v1.2.3` - Specific version

### Usage Examples

```yaml
# Always use latest v1.x.x
uses: broadsage-containers/docker-ops/.github/workflows/reusable/quality-gate.yml@v1

# Pin to specific minor version
uses: broadsage-containers/docker-ops/.github/workflows/reusable/quality-gate.yml@v1.2

# Pin to exact version (most secure)
uses: broadsage-containers/docker-ops/.github/workflows/reusable/quality-gate.yml@v1.2.3
```

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

### Made with ❤️ by the Broadsage Team
