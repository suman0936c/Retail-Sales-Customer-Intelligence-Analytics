# Data Quality Report

Generated from the source workbook. Counts below are measured, not estimated.

```json
{
  "source_rows": 1067371,
  "exact_duplicate_rows": 34335,
  "missing_customer_id_rows": 243007,
  "cancellation_invoice_rows": 19494,
  "negative_quantity_rows": 22950,
  "zero_or_negative_price_rows": 6207,
  "non_product_rows": 6114,
  "invalid_date_rows": 0,
  "valid_sales_lines": 1003166,
  "valid_customer_sales_lines": 776404,
  "anonymous_valid_sales_lines": 226762,
  "unique_invoices_source": 53628,
  "unique_customers_source": 5942,
  "unique_products_source": 5304,
  "countries_source": 43,
  "date_min": "2009-12-01 07:45:00",
  "date_max": "2011-12-09 12:50:00",
  "valid_sales_revenue_gbp": 19653089.85,
  "customer_identified_revenue_gbp": 17065909.65,
  "service_codes_excluded": [
    "ADJUST",
    "AMAZONFEE",
    "BANK CHARGES",
    "C2",
    "CRUK",
    "D",
    "DCGS",
    "DCGSSBOY",
    "DCGSSGIRL",
    "DOT",
    "GIFT",
    "M",
    "PADS",
    "POST",
    "S",
    "TEST001"
  ]
}
```

**Cleaning policy:** cancellations and negative-quantity returns are retained in `cancellations_returns.csv`; anonymous valid sales remain in overall revenue; customer analysis excludes missing CustomerID. Duplicate rows are flagged and excluded from the valid sales fact. Non-product exclusions use the documented code/description rule and should be reviewed.
