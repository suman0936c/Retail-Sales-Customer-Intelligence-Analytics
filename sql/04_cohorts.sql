DROP TABLE IF EXISTS cohort_retention;
CREATE TABLE cohort_retention AS
WITH customer_months AS (
 SELECT DISTINCT CustomerID, strftime('%Y-%m',InvoiceDate) AS ActivityMonth FROM fact_sales WHERE CustomerID IS NOT NULL
), first_month AS (
 SELECT CustomerID, MIN(ActivityMonth) AS CohortMonth FROM customer_months GROUP BY CustomerID
), cohort_size AS (
 SELECT CohortMonth, COUNT(DISTINCT CustomerID) AS CohortCustomers FROM first_month GROUP BY CohortMonth
), activity AS (
 SELECT cm.CustomerID, fm.CohortMonth, cm.ActivityMonth,
 (CAST(substr(cm.ActivityMonth,1,4) AS INTEGER)*12+CAST(substr(cm.ActivityMonth,6,2) AS INTEGER)) -
 (CAST(substr(fm.CohortMonth,1,4) AS INTEGER)*12+CAST(substr(fm.CohortMonth,6,2) AS INTEGER)) AS Period
 FROM customer_months cm JOIN first_month fm USING(CustomerID)
), counts AS (
 SELECT CohortMonth, Period, COUNT(DISTINCT CustomerID) AS ActiveCustomers FROM activity GROUP BY CohortMonth,Period
)
SELECT c.CohortMonth,c.CohortCustomers,a.Period,a.ActiveCustomers,
 ROUND(1.0*a.ActiveCustomers/c.CohortCustomers,4) AS RetentionRate
FROM counts a JOIN cohort_size c USING(CohortMonth) ORDER BY c.CohortMonth,a.Period;
