#!/usr/bin/env sh
set -e

echo "=== [1/2] Fetching raw data into data/raw/ (if script exists) ==="
if [ -f "src/fetch_data.py" ]; then
  python src/fetch_data.py
else
  echo "src/fetch_data.py not found, skipping fetch step."
fi

echo "=== [2/2] Processing data from data/raw/ to data/processed/ ==="
python src/process_data.py

echo "=== Done. Output written to data/processed/ ==="
