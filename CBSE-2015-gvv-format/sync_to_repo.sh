#!/usr/bin/env bash
# Overlay this completed Class X folder on an existing Miscellaneous clone.
# Usage: ./sync_to_repo.sh /path/to/Miscellaneous
set -euo pipefail
if [[ $# -ne 1 ]]; then
  echo "Usage: $0 /path/to/Miscellaneous" >&2
  exit 2
fi
SOURCE="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$1" && pwd)"
TARGET="$REPO_ROOT/CBSE-2015-gvv-format"
mkdir -p "$TARGET"
cp -a "$SOURCE"/. "$TARGET"/
echo "Copied Class X sources and build outputs to: $TARGET"
echo "Next, rebuild there (./build.sh), then review with git diff before committing."
