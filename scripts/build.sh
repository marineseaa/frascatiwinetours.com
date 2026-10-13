#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
hugo --cacheDir "${TMPDIR:-/tmp}/frascati-hugo-cache" --gc --minify "$@"
