"""Audit and clean UCI Online Retail II. Keeps cancellation/return records separate."""
from pathlib import Path
import pandas as pd
import numpy as np
import json
ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data/raw'; OUT=ROOT/'data/processed'; DOC=ROOT/'docs'
OUT.mkdir(parents=True,exist_ok=True); DOC.mkdir(parents=True,exist_ok=True)
files=list(RAW.glob('*.xlsx'))
if not files: raise SystemExit('Dataset missing. Run: python python/download_data.py')
frames=[]
for f in files:
    if f.name.lower().startswith('online_retail_ii'):
        xls=pd.ExcelFile(f)
        for sh in xls.sheet_names:
            d=pd.read_excel(f,sheet_name=sh)
            d['SourceSheet']=sh; frames.append(d)
if not frames: raise SystemExit('No workbook sheets found.')
df=pd.concat(frames,ignore_index=True)
rename={'Invoice':'Invoice','InvoiceNo':'Invoice','StockCode':'StockCode','Description':'Description','Quantity':'Quantity','InvoiceDate':'InvoiceDate','Price':'UnitPrice','UnitPrice':'UnitPrice','Customer ID':'CustomerID','CustomerID':'CustomerID','Country':'Country'}
df=df.rename(columns={c:rename.get(c,c) for c in df.columns})
required=['Invoice','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country']
missing=[c for c in required if c not in df.columns]
if missing: raise ValueError(f'Missing expected columns: {missing}. Found: {list(df.columns)}')
df['Invoice']=df['Invoice'].astype('string').str.strip(); df['StockCode']=df['StockCode'].astype('string').str.strip()
df['CustomerID']=pd.to_numeric(df['CustomerID'],errors='coerce').astype('Int64')
df['Quantity']=pd.to_numeric(df['Quantity'],errors='coerce'); df['UnitPrice']=pd.to_numeric(df['UnitPrice'],errors='coerce')
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'],errors='coerce')
df['IsCancellation']=df['Invoice'].str.upper().str.startswith('C',na=False)
df['IsReturn']=df['Quantity'].lt(0)
df['HasCustomerID']=df['CustomerID'].notna()
df['IsDuplicate']=df.duplicated(subset=required,keep='first')
# Non-product codes are explicitly listed; additional nonnumeric/known service codes are reviewed, not guessed away.
service_codes={'POST','D','M','DOT','CRUK','BANK CHARGES','PADS','S','AMAZONFEE','C2','GIFT','M','DCGS','DCGSSBOY','DCGSSGIRL','ADJUST','TEST001'}
desc=df['Description'].fillna('').str.upper()
df['IsNonProduct']=df['StockCode'].str.upper().isin(service_codes) | desc.str.contains(r'POSTAGE|BANK CHARGES|CARRIAGE|MANUAL|ADJUSTMENT|DOTCOM POSTAGE',regex=True)
df['IsValidPrice']=df['UnitPrice'].gt(0)
df['IsValidDate']=df['InvoiceDate'].notna()
df['Revenue']=df['Quantity']*df['UnitPrice']
# Transaction-line flags retain the source; valid sales excludes cancellation invoices, negative quantities, invalid prices and non-product lines.
df['IsValidSaleLine']=(~df['IsCancellation']) & (~df['IsReturn']) & df['Quantity'].gt(0) & df['IsValidPrice'] & (~df['IsNonProduct']) & df['IsValidDate'] & (~df['IsDuplicate'])
df['IsCustomerAnalysisLine']=df['IsValidSaleLine'] & df['HasCustomerID']
# Overall sales keeps anonymous customers; customer-level extracts require ID.
df.to_csv(OUT/'transactions_audited.csv',index=False)
sales=df[df['IsValidSaleLine']].copy(); cust=sales[sales['HasCustomerID']].copy()
sales.to_csv(OUT/'valid_sales_lines.csv',index=False); cust.to_csv(OUT/'customer_sales_lines.csv',index=False)
# Cancellation/return ledger remains separately inspectable.
df[df['IsCancellation']|df['IsReturn']].to_csv(OUT/'cancellations_returns.csv',index=False)
metrics={
 'source_rows':int(len(df)), 'exact_duplicate_rows':int(df['IsDuplicate'].sum()),
 'missing_customer_id_rows':int((~df['HasCustomerID']).sum()),
 'cancellation_invoice_rows':int(df['IsCancellation'].sum()), 'negative_quantity_rows':int(df['IsReturn'].sum()),
 'zero_or_negative_price_rows':int((df['UnitPrice']<=0).sum()), 'non_product_rows':int(df['IsNonProduct'].sum()),
 'invalid_date_rows':int((~df['IsValidDate']).sum()), 'valid_sales_lines':int(len(sales)),
 'valid_customer_sales_lines':int(len(cust)), 'anonymous_valid_sales_lines':int(sales['CustomerID'].isna().sum()),
 'unique_invoices_source':int(df['Invoice'].nunique()), 'unique_customers_source':int(df['CustomerID'].nunique()),
 'unique_products_source':int(df['StockCode'].nunique()), 'countries_source':int(df['Country'].nunique()),
 'date_min':str(df['InvoiceDate'].min()), 'date_max':str(df['InvoiceDate'].max()),
 'valid_sales_revenue_gbp':round(float(sales['Revenue'].sum()),2),
 'customer_identified_revenue_gbp':round(float(cust['Revenue'].sum()),2),
 'service_codes_excluded':sorted(service_codes)
}
(OUT/'data_quality_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
(DOC/'data_quality_report.md').write_text('# Data Quality Report\n\nGenerated from the source workbook. Counts below are measured, not estimated.\n\n```json\n'+json.dumps(metrics,indent=2)+'\n```\n\n**Cleaning policy:** cancellations and negative-quantity returns are retained in `cancellations_returns.csv`; anonymous valid sales remain in overall revenue; customer analysis excludes missing CustomerID. Duplicate rows are flagged and excluded from the valid sales fact. Non-product exclusions use the documented code/description rule and should be reviewed.\n',encoding='utf-8')
print(json.dumps(metrics,indent=2))
