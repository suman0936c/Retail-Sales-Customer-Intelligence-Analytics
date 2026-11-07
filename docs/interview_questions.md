# Interview Questions and Answer Guide

1. **Why treat cancellations separately?** They represent reversals/voided sales, not successful demand. Keeping them flagged preserves auditability and enables cancellation analysis without inflating successful sales.
2. **What about missing CustomerID?** Keep otherwise valid lines in overall revenue because the sale still occurred; exclude them from RFM/cohorts because customer identity and repeat behavior cannot be established.
3. **How are RFM bins chosen?** Use quintiles (`NTILE(5)`) across customers. Recency ordering is reversed so more recent customers score higher; Frequency and Monetary increase with value.
4. **What does 5-5-5 mean?** A customer in the best quintile for recency, frequency and monetary value under the chosen scoring population/cutoff.
5. **What is a cohort?** Customers grouped by calendar month of first identified valid purchase. Retention in period n is the share of cohort members with a purchase n months after acquisition.
6. **Why does retention decline?** Fewer cohort members make a subsequent purchase in later observed periods; this is descriptive and does not prove why they stopped.
7. **Why exclude Dec 2011 from YoY?** Only the first nine days are present, so comparing it with a complete December would be misleading. Use matched complete months/periods.
8. **Why no profit or margin?** No cost-of-goods or operating cost data is supplied. Revenue cannot be substituted for profit.
