# Data Dictionary

## Source fields
| Field | Meaning | Analytical treatment |
|---|---|---|
| Invoice | Invoice identifier; values beginning C indicate cancellation | Text key; cancellations flagged |
| StockCode | Product/service code | Text key; non-product codes excluded from product sales |
| Description | Item description | Descriptive product attribute |
| Quantity | Units on invoice line | Positive quantity used for sales; negative values flagged as returns |
| InvoiceDate | Transaction timestamp | Parsed datetime; date dimension derived |
| UnitPrice | Unit price in GBP | Non-positive values excluded from valid product sales |
| CustomerID | Customer identifier | Missing values retained in overall revenue, excluded from customer analytics |
| Country | Customer country | Country dimension |

## Derived fields
`Revenue = Quantity * UnitPrice`; `IsCancellation`; `IsReturn`; `HasCustomerID`; `IsDuplicate`; `IsNonProduct`; `IsValidSaleLine`; `IsCustomerAnalysisLine`.
