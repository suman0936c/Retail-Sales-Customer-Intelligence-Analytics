-- Pareto: share of customers required to reach 80% of identified-customer revenue.
WITH ranked AS (SELECT CustomerID, Monetary, SUM(Monetary) OVER(ORDER BY Monetary DESC,CustomerID) AS CumRevenue,
 SUM(Monetary) OVER() AS TotalRevenue, ROW_NUMBER() OVER(ORDER BY Monetary DESC,CustomerID) AS RankNo,
 COUNT(*) OVER() AS CustomerCount FROM rfm)
SELECT MIN(RankNo)*1.0/MAX(CustomerCount) AS CustomerShareToReach80Pct
FROM ranked WHERE CumRevenue >= 0.8*TotalRevenue;
-- At-risk segment historical revenue
SELECT Segment, COUNT(*) Customers, ROUND(SUM(Monetary),2) HistoricalRevenue FROM rfm GROUP BY Segment ORDER BY HistoricalRevenue DESC;
