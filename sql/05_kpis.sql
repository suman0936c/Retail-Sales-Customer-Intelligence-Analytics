-- Revenue, invoices, customers and AOV; source policy excludes cancellations/returns/invalid lines in Python.
SELECT ROUND(SUM(Revenue),2) AS TotalRevenue, COUNT(DISTINCT Invoice) AS Orders,
 COUNT(DISTINCT CustomerID) AS IdentifiedCustomers,
 ROUND(SUM(Revenue)/NULLIF(COUNT(DISTINCT Invoice),0),2) AS AOV FROM fact_sales;
SELECT strftime('%Y-%m',InvoiceDate) AS Month, ROUND(SUM(Revenue),2) Revenue,
 COUNT(DISTINCT Invoice) Orders FROM fact_sales GROUP BY 1 ORDER BY 1;
SELECT Segment, COUNT(*) Customers, ROUND(SUM(Monetary),2) Revenue FROM rfm GROUP BY Segment ORDER BY Revenue DESC;
SELECT Period, ROUND(AVG(RetentionRate),4) AverageRetention FROM cohort_retention WHERE Period IN (1,3,6) GROUP BY Period;
