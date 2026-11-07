# Dashboard validation report

## Verified whole-model KPIs

| Measure | Result | Status |
|---|---:|---|
| Total Revenue | £19,653,089.85 | Pass |
| Total Orders | 39,517 | Pass |
| Total Customers | 5,852 | Pass |
| Repeat Customers | 4,234 | Pass |
| Repeat Customer Rate | 72.4% | Pass |
| Weighted Cohort Retention | 26.0% | Pass |

## Additional validated calculations

| Measure | Result |
|---|---:|
| Champions Customers | 1,337 |
| At Risk Customers | 1,360 |
| Month 1 Retention | 23.0% |
| Month 3 Retention | 24.6% |
| Month 6 Retention | 21.9% |
| Month 12 Retention | 22.4% |
| Average Active Customers | 78.5 |

## QA notes

- Original tables and the nine existing active relationships were retained.
- Measures exclude blank invoices/customers where required.
- No profit or margin measure was added because no cost data exists.
- `dim_date` has 604 active dates, not a complete calendar; year-over-year logic uses explicit aligned year/month selection rather than invalid standard time intelligence.
- December 2011 is incomplete. It remains in the raw model and trend, but should be excluded from fair month-matched 2010/2011 interpretation.
- Tooling supports structural inspection of visual bindings but does not provide a rendered page export; visual rendering requires opening the PBIX in Power BI Desktop.
