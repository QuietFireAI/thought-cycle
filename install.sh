#!/usr/bin/env bash
# Install the full thought-cycle (all three skills' engines).
# Each is an independent package; uninstall any one with `pip uninstall <name>`.
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
for skill in before-turn open-mind pre-response-selfcheck; do
  echo ">> installing $skill"
  pip install -e "$DIR/$skill"
done
echo ">> thought-cycle installed (before-turn, open-mind, pre-response-selfcheck)"
