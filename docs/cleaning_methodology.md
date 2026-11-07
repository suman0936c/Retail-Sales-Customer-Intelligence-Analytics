# Cleaning Methodology

The raw UCI workbook is immutable. Both worksheets are combined with a source-sheet label. Invoice IDs are treated as strings; dates and numeric fields are parsed explicitly. Cancellation invoices (`C*`) and negative quantities are flagged and exported to a separate ledger, not silently deleted. Exact duplicate source lines are flagged and excluded once from the valid sales fact. Rows with non-positive prices, invalid dates, and identified service/non-product codes are excluded from valid product sales. Valid lines with missing CustomerID remain in overall sales revenue but are excluded from customer-level RFM and cohorts. December 2011 is incomplete and is excluded from comparable full-month trend/YoY calculations.

The non-product code/description rules are transparent in `python/clean_data.py`; inspect distinct codes/descriptions and revise only with documented evidence. Revenue is not profit: the dataset has no cost field.
