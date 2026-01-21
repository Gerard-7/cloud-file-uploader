
# Cloud File Uploader (S3-ready)

Python automation tool that scans a local folder, filters files by extension, and generates an upload manifest (CSV) ready to be used for S3 uploads.

## Features
- Scans files in a source folder
- Filters by allowed extensions
- Generates upload_manifest.csv with bucket and S3 key
- Uses JSON configuration

## How to run
```bash
python main.py

## Output example
local_path,bucket,s3_key
sample_data/report.csv,my-demo-bucket,uploads/report.csv

