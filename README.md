# Docker Operations (docker-ops)

Centralized GitHub Actions workflows for Docker container operations across Broadsage repositories.

## Quick Start

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  quality:
    uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@v0.3.2
    secrets: inherit
    
  build:
    uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@v0.3.2
    secrets: inherit
```

## Available Workflows

| Workflow | Purpose |
|----------|---------|
| [quality-gate.yml](.github/workflows/quality-gate.yml) | Code quality & linting |
| [dependency-review.yml](.github/workflows/dependency-review.yml) | Security & license scanning |
| [pr-build-validate.yml](.github/workflows/pr-build-validate.yml) | Container build & validation |
| [pr-build-publish.yml](.github/workflows/pr-build-publish.yml) | Production publishing |

## Documentation

📚 **Detailed workflow documentation** is available in the [`docs/workflows/`](docs/workflows/) directory:

- [📋 Quick Start Guide](docs/workflows/quick-start.md) - Get up and running in 5 minutes
- [⚙️ Configuration Options](docs/workflows/configuration.md) - Customize workflows for your needs  
- [📖 Complete Workflow Catalog](docs/workflows/catalog.md) - Full feature reference
- [🔒 Security Features](docs/workflows/security.md) - Built-in security capabilities

## Version Information

- **Current Version**: See [VERSION.md](VERSION.md)
- **Production**: Use pinned versions like `@v0.3.0`  
- **Development**: Use `@main` for latest features

## 📞 Support

For questions about these workflows:

- **GitHub Issues**: Technical issues and bug reports
- **GitHub Discussions**: Questions and community support  
- **Email**: [containers@broadsage.com](mailto:containers@broadsage.com)
