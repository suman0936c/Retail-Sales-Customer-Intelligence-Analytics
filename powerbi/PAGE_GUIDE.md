# Page-by-page business questions

## RETAIL PERFORMANCE | EXECUTIVE OVERVIEW

Answers how much revenue, orders, and customer activity the business generated; how revenue changes monthly; and which countries and products contribute the most revenue. Year and country slicers provide focused exploration. The comparison chart uses matching monthly revenue/prior-year revenue; December 2011 is incomplete and should be excluded from any fair year-over-year narrative.

## CUSTOMER INTELLIGENCE | RFM SEGMENTATION

Answers which RFM segments contain the most customers and monetary value; which individual customers are valuable; and where retention action should focus. The scatter plot is detailed by `CustomerID`, preventing accidental one-bubble aggregation. The risk cards expose counts for At Risk, Hibernating, and Potential Loyalists customers, which map to win-back, reactivation, and conversion actions respectively.

## CUSTOMER RETENTION | COHORT ANALYSIS

Answers who returns, how retention evolves after acquisition, and how mature cohorts compare at the same Month 1 maturity. The matrix shows cohort month × period retention. Retention values use `SUM(ActiveCustomers) / SUM(CohortCustomers)`, not a mean of percentages. The curve excludes Period 0 so the acquisition-month 100% point does not mask later behaviour. Cohorts with no Month 1 observation render blank in the comparison.
