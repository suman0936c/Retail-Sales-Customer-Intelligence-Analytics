PRAGMA foreign_keys=ON;
DROP TABLE IF EXISTS fact_sales; DROP TABLE IF EXISTS dim_customer; DROP TABLE IF EXISTS dim_product; DROP TABLE IF EXISTS dim_date; DROP TABLE IF EXISTS dim_country;
CREATE TABLE dim_customer(CustomerKey INTEGER PRIMARY KEY, CustomerID INTEGER UNIQUE);
CREATE TABLE dim_product(ProductKey INTEGER PRIMARY KEY, StockCode TEXT UNIQUE, Description TEXT);
CREATE TABLE dim_date(DateKey INTEGER PRIMARY KEY, Date TEXT UNIQUE, Year INTEGER, Month INTEGER, MonthNumber INTEGER, Quarter INTEGER, YearMonth TEXT);
CREATE TABLE dim_country(CountryKey INTEGER PRIMARY KEY, Country TEXT UNIQUE);
CREATE TABLE fact_sales(SalesKey INTEGER PRIMARY KEY, Invoice TEXT, StockCode TEXT, CustomerID INTEGER, InvoiceDate TEXT, DateKey INTEGER, Country TEXT, CountryKey INTEGER, Quantity REAL, UnitPrice REAL, Revenue REAL, FOREIGN KEY(CustomerID) REFERENCES dim_customer(CustomerID), FOREIGN KEY(StockCode) REFERENCES dim_product(StockCode), FOREIGN KEY(DateKey) REFERENCES dim_date(DateKey), FOREIGN KEY(CountryKey) REFERENCES dim_country(CountryKey));
INSERT INTO dim_customer(CustomerID) SELECT DISTINCT CustomerID FROM stg_sales WHERE CustomerID IS NOT NULL;
INSERT INTO dim_product(StockCode,Description) SELECT StockCode, MAX(Description) FROM stg_sales GROUP BY StockCode;
INSERT INTO dim_date(DateKey,Date,Year,Month,MonthNumber,Quarter,YearMonth)
SELECT CAST(strftime('%Y%m%d',date(InvoiceDate)) AS INTEGER), date(InvoiceDate), CAST(strftime('%Y',InvoiceDate) AS INTEGER), strftime('%m',InvoiceDate), CAST(strftime('%m',InvoiceDate) AS INTEGER), ((CAST(strftime('%m',InvoiceDate) AS INTEGER)-1)/3)+1, strftime('%Y-%m',InvoiceDate) FROM stg_sales GROUP BY date(InvoiceDate);
INSERT INTO dim_country(Country) SELECT DISTINCT Country FROM stg_sales WHERE Country IS NOT NULL;
INSERT INTO fact_sales(Invoice,StockCode,CustomerID,InvoiceDate,DateKey,Country,CountryKey,Quantity,UnitPrice,Revenue)
SELECT s.Invoice,s.StockCode,s.CustomerID,s.InvoiceDate,d.DateKey,s.Country,c.CountryKey,s.Quantity,s.UnitPrice,s.Revenue
FROM stg_sales s JOIN dim_date d ON d.Date=date(s.InvoiceDate) LEFT JOIN dim_country c ON c.Country=s.Country;
CREATE INDEX idx_fact_date ON fact_sales(DateKey); CREATE INDEX idx_fact_customer ON fact_sales(CustomerID); CREATE INDEX idx_fact_invoice ON fact_sales(Invoice);
