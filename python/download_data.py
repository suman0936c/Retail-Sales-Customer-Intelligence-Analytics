"""Download the official UCI Online Retail II workbook."""
from pathlib import Path
import urllib.request, zipfile
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
url = 'https://archive.ics.uci.edu/static/public/502/online%2Bretail%2Bii.zip'
archive = RAW / 'online_retail_ii.zip'
workbook = RAW / 'online_retail_II.xlsx'
if workbook.exists():
    print(f'Workbook already exists: {workbook}')
else:
    print('Downloading official UCI dataset (~43.5 MB)...')
    urllib.request.urlretrieve(url, archive)
    with zipfile.ZipFile(archive) as z:
        z.extractall(RAW)
    print('Extracted files:', [p.name for p in RAW.iterdir()])
