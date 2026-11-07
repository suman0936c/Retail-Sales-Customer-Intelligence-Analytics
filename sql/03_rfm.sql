DROP TABLE IF EXISTS rfm;
CREATE TABLE rfm AS
WITH customer_metrics AS (
 SELECT CustomerID, CAST(julianday((SELECT MAX(date(InvoiceDate)) FROM fact_sales)) - julianday(MAX(date(InvoiceDate))) AS INTEGER) AS Recency,
 COUNT(DISTINCT Invoice) AS Frequency, ROUND(SUM(Revenue),2) AS Monetary
 FROM fact_sales WHERE CustomerID IS NOT NULL GROUP BY CustomerID
), scored AS (
 SELECT *, NTILE(5) OVER (ORDER BY Recency DESC) AS R_Score,
 NTILE(5) OVER (ORDER BY Frequency ASC) AS F_Score,
 NTILE(5) OVER (ORDER BY Monetary ASC) AS M_Score FROM customer_metrics
)
SELECT *, (R_Score||F_Score||M_Score) AS RFM_Score,
 CASE WHEN R_Score>=4 AND F_Score>=4 AND M_Score>=4 THEN 'Champions'
 WHEN R_Score>=3 AND F_Score>=4 THEN 'Loyal Customers'
 WHEN R_Score>=4 AND F_Score BETWEEN 2 AND 3 THEN 'Potential Loyalists'
 WHEN R_Score BETWEEN 2 AND 3 AND F_Score>=2 THEN 'At Risk'
 WHEN R_Score=1 AND F_Score<=2 THEN 'Hibernating'
 WHEN R_Score=5 AND F_Score=1 THEN 'New Customers'
 ELSE 'Potential Loyalists' END AS Segment FROM scored;
