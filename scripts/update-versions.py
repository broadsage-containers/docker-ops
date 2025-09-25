#!/usr/bin/env python3
"""
Update version references in README.md

This script safely updates all docker-ops workflow version references
in README.md to a specified version, handling any corrupted versions.

Usage:
    python3 scripts/update-versions.py v0.2.7
    python3 scripts/update-versions.py --latest
"""

import re
import sys
import subprocess
from pathlib import Path

def get_latest_version():
    """Get the latest git tag version"""
    try:
        result = subprocess.run([
            'git', 'tag', '-l', '--sort=-version:refname'
        ], capture_output=True, text=True, check=True)
        
        tags = result.stdout.strip().split('\n')
        for tag in tags:
            if re.match(r'^v[0-9]+\.[0-9]+\.[0-9]+$', tag):
                return tag
        return "v0.0.0"
    except subprocess.CalledProcessError:
        return "v0.0.0"

def update_readme_versions(new_version):
    """Update version references in README.md"""
    readme_path = Path('README.md')
    
    if not readme_path.exists():
        print("❌ README.md not found")
        return False
    
    # Read current README
    with open(readme_path, 'r') as f:
        content = f.read()
    
    print(f"🔄 Updating to version: {new_version}")
    
    # Pattern to match: broadsage-containers/docker-ops/.github/workflows/{workflow}.yml@v{version}
    pattern = r'(broadsage-containers/docker-ops/\.github/workflows/[^@\s]+)@v[0-9]+(?:\.[0-9]+)*'
    replacement = rf'\1@{new_version}'
    
    # Count matches before replacement
    matches = re.findall(pattern, content)
    print(f"📋 Found {len(matches)} version references to update")
    
    if matches:
        for i, match in enumerate(matches[:5], 1):  # Show first 5 matches
            print(f"  {i}. {match}@v... → {match}@{new_version}")
        if len(matches) > 5:
            print(f"  ... and {len(matches) - 5} more")
    
    # Replace all matches
    new_content = re.sub(pattern, replacement, content)
    
    # Write back if changed
    if content != new_content:
        with open(readme_path, 'w') as f:
            f.write(new_content)
        print(f"✅ README.md updated successfully to {new_version}")
        return True
    else:
        print("ℹ️  No changes needed in README.md")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 update-versions.py <version|--latest>")
        print("Examples:")
        print("  python3 update-versions.py v0.2.7")
        print("  python3 update-versions.py --latest")
        sys.exit(1)
    
    if sys.argv[1] == '--latest':
        version = get_latest_version()
        print(f"🔍 Latest version detected: {version}")
    else:
        version = sys.argv[1]
        if not version.startswith('v'):
            version = f'v{version}'
    
    # Validate version format
    if not re.match(r'^v[0-9]+\.[0-9]+\.[0-9]+$', version):
        print(f"❌ Invalid version format: {version}")
        print("Expected format: v1.2.3")
        sys.exit(1)
    
    success = update_readme_versions(version)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()