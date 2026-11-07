# Retail Customer Retention Dashboard

## Premium redesign

The final report uses a light-neutral enterprise canvas, white card surfaces, deep-navy typography, teal primary metrics and blue secondary comparison series. The former visual layer was removed and rebuilt on aligned 1920×1080 grids. The final report contains these three pages:

1. **RETAIL PERFORMANCE | EXECUTIVE OVERVIEW** — four core KPIs, year/country slicers, monthly revenue performance, country contribution, product contribution, and prior-year revenue comparison.
2. **CUSTOMER INTELLIGENCE | RFM SEGMENTATION** — RFM KPIs, segment slicer, segment/customer-value analysis, individual-customer RFM scatter, high-value table, and real risk-priority KPI cards.
3. **CUSTOMER RETENTION | COHORT ANALYSIS** — repeat and weighted-cohort KPIs, maturity KPI strip, cohort matrix, retention curve excluding Period 0, and Month 1 cohort comparison.

## Measure conventions

- Currency is formatted in GBP (£).
- Customer and order measures exclude blank `CustomerID` and `Invoice` values respectively.
- `Cohort Retention %` is calculated as `ActiveCustomers / CohortCustomers`; it is not an average or sum of row-level retention percentages.
- The custom `dim_date` table contains 604 dates across 2009-12-01 to 2011-12-09, so `Revenue LY` uses explicit selected year/month matching rather than a standard complete-calendar time-intelligence function.
- `Revenue by Segment` uses the existing `rfm[Monetary]` values. It represents the RFM monetary dataset, not an inferred profit or margin calculation.

## Source model

- `fact_sales`: 1,003,166 rows
- `dim_customer`: 5,852 rows
- `dim_product`: 4,726 rows
- `dim_date`: 604 rows
- `dim_country`: 43 rows
- `rfm`: 5,852 rows, six existing segment classifications
- `cohort_retention`: 325 rows, 25 cohort months

All original tables and relationships were preserved. No source data was reloaded or reprocessed.

See `DESIGN_SYSTEM.md`, `PAGE_GUIDE.md`, and `VALIDATION_REPORT.md` for the supporting design, storytelling, and validation records.
