# Technical Documentation

Pipeline: official workbook → Python audit/flags → processed CSVs → SQLite staging table → star schema → RFM/cohort tables → Python charts → Power BI semantic model/report.

The fact grain is one valid sales invoice line. Dimensions are customer, product, date and country. Anonymous customers have a NULL CustomerID and do not join to the customer dimension; they remain in fact_sales for overall revenue. Fact rows use date and country surrogate keys. SQLite schema and analytical SQL are in `sql/`.

Power BI model guidance: relate dimensions 1:* to fact_sales; use a contiguous calendar table for time intelligence; apply a full-month flag to exclude Dec 2011 from comparable monthly/YoY visuals; build DAX measures only after checking invoice/cancellation semantics and distinct order definitions.
