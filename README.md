# Mutual Fund Analytics Capstone Project

## Overview

This project is an end-to-end **Mutual Fund Analytics** solution developed using **Python, SQL (SQLite), and data visualization libraries**. The project focuses on collecting, cleaning, storing, analyzing, and visualizing mutual fund data to generate meaningful business insights.

## Project Objectives

* Collect and process mutual fund datasets.
* Integrate live NAV data using the MFAPI API.
* Perform data cleaning and preprocessing.
* Store cleaned data in a SQLite database.
* Execute SQL-based business analysis.
* Conduct exploratory data analysis (EDA).
* Perform mutual fund performance analytics.
* Generate visual insights and analytical reports.

## Project Structure

```text
mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── src/
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Requests
* Git & GitHub

## Work Completed

### Day 1: Project Setup & Data Ingestion

* Created project folder structure.
* Set up Python virtual environment.
* Installed required dependencies.
* Loaded and validated **10 mutual fund datasets**.
* Performed dataset inspection (`shape`, `dtypes`, `head`).
* Integrated **MFAPI** for live NAV data.
* Validated AMFI scheme codes across datasets.
* Initialized Git repository and pushed the project to GitHub.

### Day 2: Data Cleaning & SQLite Database

* Removed duplicate records.
* Trimmed extra spaces.
* Handled missing values.
* Standardized text and numerical formats.
* Created processed datasets.
* Built a **SQLite database**.
* Imported cleaned datasets into database tables.
* Wrote SQL queries for:

  * Fund house analysis
  * Category analysis
  * AUM analysis
  * Scheme performance
  * Aggregation and ranking
* Documented the complete data cleaning and SQL workflow.

### Day 3: Exploratory Data Analysis (EDA)

Created **11 analytical visualizations** including:

* Fund house distribution
* Category-wise fund analysis
* Sub-category analysis
* Risk category distribution
* AUM comparison
* Scheme performance analysis
* NAV trend visualization
* Investor transaction analysis
* Portfolio concentration analysis
* Benchmark comparison
* Summary analytical charts

Generated business insights from the visualizations to understand market trends, fund performance, and investor behavior.

### Day 4: Performance Analytics

Performed detailed **mutual fund performance analysis** using historical NAV and benchmark datasets.

Key analyses completed:

* Return calculations (absolute and percentage returns)
* Rolling return analysis
* CAGR estimation
* Volatility analysis
* Risk-adjusted performance comparison
* Fund ranking based on performance metrics
* Benchmark comparison
* Performance trend visualization
* Category-wise performance evaluation
* Identification of top and bottom performing schemes

Generated performance insights to evaluate fund consistency, risk-return characteristics, and comparative fund performance across categories.
## Dashboard (Power BI)

Developed a four-page interactive Power BI dashboard for mutual fund analytics.

### Day 5: Dashboard pages

* **Industry overview:** KPI cards, AUM trend, AUM by fund house
* **Fund performance:** Risk vs return scatter plot, NAV trend, fund scorecard
* **Investor analytics:** State-wise transaction analysis, transaction type split, age-group SIP analysis
* **SIP & market trends:** SIP inflows vs Nifty 50, category inflow heatmap, top inflow categories

### Key features

* Interactive slicers
* Data relationships using AMFI code
* Professional dashboard layout
* Exportable PDF and presentation-ready visuals


## Key Features

* Automated data ingestion
* Live NAV API integration
* Data preprocessing pipeline
* SQLite database integration
* SQL-based analytics
* Exploratory data analysis
* Mutual fund performance analytics
* Interactive and static visualizations
* Version-controlled project workflow

## Author

**Bandi Bharath**

Data Analyst Intern | AIML Student

GitHub: https://github.com/Bharathreddy560
