set -euo pipefail

echo "Container started at $(date)"

ls -la /data || true

if [ -z "$(ls -A /data/raw 2>/dev/null)" ]; then
  echo "/data/raw is empty — running fetch_data.py"
  python /app/src/fetch_data.py --out-dir /data/raw
else
  echo "/data/raw already has files — skipping fetch"
fi

# Run processing (always or only when new data exists — your choice)
echo "Running processing to /data/processed"
python /app/src/process_data.py --in-dir /data/raw --out-dir /data/processed

echo "Done at $(date)"
