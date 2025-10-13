#!/bin/bash
# rename_ignition_full.sh
# Usage: ./rename_ignition_full.sh /path/to/project

set -e

PROJECT_ROOT="$1"
if [[ -z "$PROJECT_ROOT" ]]; then
    echo "Usage: $0 /path/to/project"
    exit 1
fi

cd "$PROJECT_ROOT"

# Backup
# BACKUP_DIR="${PROJECT_ROOT}_backup_$(date +%Y%m%d%H%M%S)"
# echo "Creating backup at $BACKUP_DIR ..."
# cp -r "$PROJECT_ROOT" "$BACKUP_DIR"

# Update Python import statements
echo "Updating Python import statements ..."
find . -name "*.py" -exec sed -i \
    -e 's/ignition./pygnition./' \
    -e 's/`ignition`/`pygnition`/' {} +

# Rename the package directory if it exists
if [[ -d "ignition" ]]; then
    echo "Renaming ignition/ directory → pygnition/ ..."
    mv ignition pygnition
fi

# Update Sphinx docs and Markdown files
echo "Updating .rst and .md files ..."
find . -type f \( -name "*.rst" -o -name "*.md" \) -exec sed -i 's/ignition/pygnition/g' {} +

# Update Jupyter notebooks
echo "Updating .ipynb files ..."
for nb in $(find . -name "*.ipynb"); do
    # Use jq to replace ignition with pygnition in all string fields
    jq 'walk(if type == "string" then gsub("`ignition`"; "`pygnition`") else . end)' "$nb" > "${nb}.tmp" && mv "${nb}.tmp" "$nb"
done

echo "Done! Backup saved at $BACKUP_DIR"
