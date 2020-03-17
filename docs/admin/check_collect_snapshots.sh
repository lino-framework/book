#/bin/bash
# designed to run as cron job
set -e
TARGET=/path/to/snapshots_collection

if [[ $(find $TARGET -mtime +1 -print) ]]; then
  echo "File $filename exists and is older than one day"
fi

