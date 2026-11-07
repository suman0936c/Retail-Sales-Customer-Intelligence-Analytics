from pathlib import Path
import sqlite3, pandas as pd
ROOT=Path(__file__).resolve().parents[1]; csv=ROOT/'data/processed/valid_sales_lines.csv'; db=ROOT/'database/retail_analytics.db'
if not csv.exists(): raise SystemExit('Run python python/clean_data.py first')
df=pd.read_csv(csv,parse_dates=['InvoiceDate']); df['CustomerID']=pd.to_numeric(df['CustomerID'],errors='coerce').astype('Int64')
db.parent.mkdir(exist_ok=True)
with sqlite3.connect(db) as con:
    df.to_sql('stg_sales',con,if_exists='replace',index=False)
    con.executescript((ROOT/'sql/02_star_schema.sql').read_text(encoding='utf-8'))
    con.executescript((ROOT/'sql/03_rfm.sql').read_text(encoding='utf-8'))
    con.executescript((ROOT/'sql/04_cohorts.sql').read_text(encoding='utf-8'))
    con.executescript((ROOT/'sql/05_kpis.sql').read_text(encoding='utf-8'))
print(f'Database created: {db}')
