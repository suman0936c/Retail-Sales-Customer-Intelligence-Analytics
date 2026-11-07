from pathlib import Path
import sqlite3, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
ROOT=Path(__file__).resolve().parents[1]; DB=ROOT/'database/retail_analytics.db'; OUT=ROOT/'screenshots'; OUT.mkdir(exist_ok=True)
if not DB.exists(): raise SystemExit('Build database first')
with sqlite3.connect(DB) as c:
    monthly=pd.read_sql_query('SELECT strftime("%Y-%m", InvoiceDate) month, SUM(Revenue) revenue FROM fact_sales GROUP BY 1 ORDER BY 1',c)
    seg=pd.read_sql_query('SELECT Segment, COUNT(*) customers FROM rfm GROUP BY Segment ORDER BY customers DESC',c)
    cohort=pd.read_sql_query('SELECT CohortMonth, Period, RetentionRate FROM cohort_retention',c)
plt.figure(figsize=(12,5)); plt.plot(monthly['month'],monthly['revenue']); plt.xticks(rotation=60); plt.title('Monthly Revenue (£)'); plt.tight_layout(); plt.savefig(OUT/'monthly_revenue.png',dpi=160); plt.close()
plt.figure(figsize=(10,5)); sns.barplot(data=seg,x='Segment',y='customers'); plt.xticks(rotation=35,ha='right'); plt.title('Customer Segments'); plt.tight_layout(); plt.savefig(OUT/'rfm_segments.png',dpi=160); plt.close()
if not cohort.empty:
    p=cohort.pivot(index='CohortMonth',columns='Period',values='RetentionRate')
    plt.figure(figsize=(14,8)); sns.heatmap(p,annot=True,fmt='.0%',cmap='Blues'); plt.title('Cohort Retention'); plt.tight_layout(); plt.savefig(OUT/'cohort_retention.png',dpi=160); plt.close()
print('Charts saved in screenshots/')
