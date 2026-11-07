# Customer Retention & Revenue Analytics

An end-to-end retail analytics portfolio project using UCI Online Retail II, Python, SQLite, SQL and Power BI. The business question is: **Which customers generate most revenue, which segments are at risk, and what should the retailer do next?**

## Dataset
Official source: [UCI Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii), Daqing Chen, DOI [10.24432/C5CG6D](https://doi.org/10.24432/C5CG6D), CC BY 4.0. The workbook contains 1,067,371 line items from Dec 2009 through Dec 9, 2011. Cite the dataset in derivative work.

## Run on Windows
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python python/download_data.py
python python/clean_data.py
python python/build_database.py
python python/generate_charts.py
```

## Data policy
- Preserve source workbook unchanged.
- Flag cancellation invoices (`Invoice` begins with C) and negative-quantity returns; export them separately.
- Keep valid anonymous-customer transactions in overall revenue, but exclude missing CustomerID from RFM and cohorts.
- Exclude exact duplicate lines from the analytical sales fact and report their count.
- Exclude non-positive unit prices and identified service/non-product codes from product sales; review the code list in `python/clean_data.py`.
- Revenue = Quantity × UnitPrice. No cost field exists; this project makes no profit or margin claims.
- December 2011 is incomplete and must be excluded from comparable full-month trends and YoY. Use like-for-like months only.

## Current status
This repository is a prepared project scaffold with executable download, audit, cleaning, database and chart scripts plus SQL. No dataset-derived metrics are claimed until the scripts run against the downloaded source workbook. The PBIX is intentionally not fabricated; create it in Power BI Desktop with PBIX-MCP after validating the SQLite outputs.

## Outputs
- `data/processed/transactions_audited.csv`: all rows with flags
- `data/processed/valid_sales_lines.csv`: valid product sales, including anonymous customers
- `data/processed/customer_sales_lines.csv`: valid sales with known CustomerID
- `data/processed/cancellations_returns.csv`: separately retained cancellation/return ledger
- `data/processed/data_quality_metrics.json`: measured reconciliation metrics
- `database/retail_analytics.db`: SQLite star schema and analysis tables
- `screenshots/`: generated charts

## Important caveats
The service-code exclusion list is explicit but should be reviewed against the dataset's actual distinct StockCode/Description inventory. RFM segments are rule-based and should be explained as heuristic groups, not predictive churn probabilities. Cohort periods beyond a cohort's observed age are unavailable, not zero retention.
