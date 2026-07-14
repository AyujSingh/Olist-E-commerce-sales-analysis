# Olist-E-commerce-sales-analysis
Data Analytics project showcasing E-commerce sales analysis using python,sql and power BI

## Project Overview

This is an end-to-end data analytics project analyzing the **Olist Brazilian E-Commerce Dataset** using **SQL, Power Query, DAX, and Power BI**.

The project analyzes **100K+ e-commerce orders** to understand overall sales performance, customer activity, revenue trends, and product category performance. An interactive two-page Power BI dashboard was developed to transform raw transactional data into meaningful business insights.

## Dataset

The dataset used in this project is the **Brazilian E-Commerce Public Dataset by Olist**, available on Kaggle.

**Dataset:**  
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Due to the large size of the CSV files, the raw dataset is not included directly in this repository. It can be downloaded from the Kaggle link above.

### Datasets Used

- Customers
- Orders
- Order Items
- Products

## Tools & Technologies

- **SQL** — Data exploration and analysis
- **Power Query** — Data cleaning and transformation
- **Power BI** — Data modeling and dashboard development
- **DAX** — Creation of calculated measures and KPIs

## Key KPIs

The dashboard includes the following business metrics:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value (AOV)
- Total Items Sold
- Unique Products Sold
- Average Selling Price

## Dashboard

### Page 1: Executive Overview

Provides a high-level overview of overall e-commerce performance.

**Key Features:**
- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Total Items Sold
- Revenue Trend Over Time
- Top Product Categories by Revenue
- Interactive slicers for Order Date, Customer State, Product Category, and Order Status

### Page 2: Product & Sales Analysis

Provides a deeper analysis of product and category-level performance.

**Key Features:**
- Total Revenue
- Total Items Sold
- Unique Products Sold
- Average Selling Price
- Top 10 Categories by Revenue
- Top 10 Categories by Items Sold
- Revenue vs. Items Sold by Category

## Key Insights

- High sales volume does not always translate into the highest revenue, indicating differences in average selling prices across product categories.
- Comparing category-level revenue and items sold helps identify both **high-value** and **high-demand** product segments.
- Revenue trends and interactive filters reveal how business performance varies across different time periods, customer states, product categories, and order statuses.

## Data Model

The project integrates four related datasets:

- **Customers → Orders** using `customer_id`
- **Orders → Order Items** using `order_id`
- **Products → Order Items** using `product_id`

These relationships enable cross-table analysis across customer, order, product, and sales data.

## Project Workflow

1. Collected the Olist e-commerce dataset from Kaggle.
2. Explored and analyzed the data using SQL.
3. Cleaned and transformed the datasets using Power Query.
4. Built relationships between multiple tables in Power BI.
5. Created DAX measures for key business KPIs.
6. Developed an interactive two-page Power BI dashboard.
7. Analyzed revenue trends and product category performance.
8. Generated business insights from the dashboard.

## Repository Contents

- SQL queries used for data analysis
- Power BI dashboard (`.pbix`)
- Dashboard screenshots
- Project documentation

> The raw CSV files are not included due to their size. Download the dataset from the Kaggle link provided above.

## Author

**Ayuj Singh**

**Skills:** SQL | Power BI | Power Query | DAX | Data Modeling | Data Visualization
