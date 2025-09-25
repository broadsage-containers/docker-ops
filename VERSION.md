# Version Information

## Current Release

- **Latest Version**: 0.1.6
- **Major Version**: 0
- **Release Date**: 2025-09-25

## Usage Recommendations

### 🏆 Production (Recommended)
Pin to exact versions for maximum stability:
```yaml
uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@0.1.6
uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@0.1.6
uses: broadsage-containers/docker-ops/.github/workflows/pr-build-publish.yml@0.1.6
```

### ⚡ Development
Use main branch for latest features (higher risk):
```yaml
uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@main
uses: broadsage-containers/docker-ops/.github/workflows/pr-build-validate.yml@main
uses: broadsage-containers/docker-ops/.github/workflows/pr-build-publish.yml@main
```

## Available Versions

### Recent Releases
```
v0.1.6
v0.1.5
v0.1.4
v0.1.3
v0.1.2
v0.1.1
v0.1.0
v0.0.1
```

## Migration Guide

If you were using the old per-workflow versioning:

```yaml
# ❌ OLD (no longer supported)
uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@quality-gate-v1.2.3

# ✅ NEW (unified versioning)  
uses: broadsage-containers/docker-ops/.github/workflows/quality-gate.yml@0.1.6
```

## Resources

- [Releases](https://github.com/broadsage-containers/docker-ops/releases) - Full changelog and release notes
- [Workflow Versioning Strategy](WORKFLOW_VERSIONING.md) - Detailed versioning approach
- [README](README.md) - Getting started guide

---
*Generated automatically on 2025-09-25 07:10:39 UTC from release 0.1.6*
