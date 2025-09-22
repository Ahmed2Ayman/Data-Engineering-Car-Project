# Data-Engineering-Car-Project
<img width="511" height="314" alt="cars dashboard" src="https://github.com/user-attachments/assets/56b30d88-f644-4eb1-83ec-8c31f4414f5d" />

## 📋 Project Overview

This project is an end-to-end data engineering and business intelligence project. It transforms a raw, messy dataset of car specifications into a clean, structured star schema, loads it into a cloud data warehouse (Snowflake), and visualizes it in an interactive Power BI dashboard to uncover key performance and pricing insights.

## 🛠️ Tech Stack

- **Data Transformation:** Python (Pandas)
- **Data Warehousing:** SQL, Snowflake
- **Data Visualization:** Power BI

## ⚙️ Project Workflow

1.  **Data Cleaning & Transformation:** A Python script was developed to handle inconsistencies (e.g., '2+2' seats, messy company names), convert data types, and handle ranges in numeric columns.
2.  **Data Modeling:** The cleaned data was modeled into a **Star Schema** with one fact table (`Fact_Car`) and four dimension tables (`Dim_Company`, `Dim_Model`, `Dim_Engine`, `Dim_FuelType`).
3.  **Database Integration:** The schema was built in Snowflake using SQL, and the five transformed CSV files were uploaded.
4.  **Dashboard Creation:** The data was connected to Power BI to build a dashboard featuring KPIs, interactive filters, and charts that answer key business questions.

## 📊 Key Insights

- **Price of Power:** The dashboard confirms a strong positive correlation between a vehicle's horsepower and its price.
- **Performance Tiers:** The "Top 10" table clearly identifies an elite group of hypercars (like Bugatti and Ferrari) that significantly outperform others in acceleration.
- **Market Segments:** Different market segments are visible, from economical 4-cylinder cars to luxury V12-powered vehicles, each with distinct performance characteristics.
