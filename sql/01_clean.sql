-- Cleaning is performed in python/clean_data.py to preserve source-level flags.
-- This file documents equivalent staging checks against the imported source.
SELECT COUNT(*) AS source_rows FROM stg_sales;
SELECT COUNT(*) AS missing_customer_rows FROM stg_sales WHERE CustomerID IS NULL;
SELECT COUNT(*) AS cancellation_rows FROM stg_sales WHERE IsCancellation = 1;
SELECT COUNT(*) AS return_rows FROM stg_sales WHERE IsReturn = 1;
