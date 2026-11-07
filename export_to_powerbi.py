
import sqlite3
import csv
from pathlib import Path

# Project database
DB_PATH = Path("database/retail_analytics.db")

# Folder for Power BI files
OUTPUT_DIR = Path("powerbi_data")
OUTPUT_DIR.mkdir(exist_ok=True)

# Tables required for the dashboard
TABLES = [
    "fact_sales",
    "dim_customer",
    "dim_product",
    "dim_date",
    "dim_country",
    "rfm",
    "cohort_retention"
]

conn = sqlite3.connect(DB_PATH)

try:
    for table in TABLES:
        output_file = OUTPUT_DIR / f"{table}.csv"

        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM "{table}"')

        columns = [item[0] for item in cursor.description]
        row_count = 0

        with open(output_file, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(columns)

            while True:
                rows = cursor.fetchmany(50000)

                if not rows:
                    break

                writer.writerows(rows)
                row_count += len(rows)

        print(f"Exported {table}: {row_count:,} rows")

    print("\nAll tables exported successfully!")

finally:
    conn.close()
