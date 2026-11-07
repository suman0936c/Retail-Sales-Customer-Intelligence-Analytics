$ErrorActionPreference = 'Stop'
python -m pip install -r requirements.txt
python python/download_data.py
python python/clean_data.py
python python/build_database.py
python python/generate_charts.py
Write-Host 'Pipeline finished. Review docs/data_quality_report.md and screenshots/.'
