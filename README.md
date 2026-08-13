# Mutual Fund Analytics Capstone Project

A complete end-to-end data analytics project that analyzes mutual fund performance, investor behavior, portfolio risk, and fund recommendations using Python, SQL, and interactive visualizations.

## Project overview

This project was developed as part of the Bluestock Fintech Data Analytics Capstone Program. The project builds a complete analytics pipeline for mutual fund data, starting from raw data ingestion and cleaning, followed by exploratory data analysis, performance analytics, risk analytics, investor behavior analysis, and dashboard reporting.

The project uses Python, SQL, SQLite, and visualization libraries to generate actionable investment insights.

## Business objective

The primary objective of this project is to evaluate mutual fund performance and investor behavior to support better investment decision-making. The project focuses on:

* Identifying high-performing funds
* Measuring downside risk
* Understanding investor investment patterns
* Detecting SIP discontinuity risk
* Building a simple fund recommendation engine
* Comparing portfolio concentration across funds

## Project objectives

The project was completed across multiple phases:

* Data ingestion and validation
* Data cleaning and preprocessing
* SQL database creation
* Exploratory data analysis
* Performance analytics
* Advanced risk analytics
* Investor analytics
* Dashboard development
* Final reporting and presentation

## Project architecture

Raw CSV datasets
↓
Data cleaning & preprocessing
↓
SQLite database
↓
Exploratory data analysis
↓
Performance & risk analytics
↓
Investor analytics
↓
Interactive dashboard
↓
Business insights & recommendations

## Project structure

mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebook/
│   ├── performance_analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── var_cvar_report.csv
│   ├── rolling_sharpe_chart.png
│   └── performance reports
│
├── dashboard/
│   └── dashboard.pdf
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── recommender.py
├── requirements.txt
├── README.md
└── run_pipeline.py

## Dataset descriptions

The project uses ten primary datasets:

| Dataset               | Description                     |
| --------------------- | ------------------------------- |
| Fund Master           | Scheme information and metadata |
| NAV History           | Historical NAV values           |
| AUM by Fund House     | Assets under management         |
| Monthly SIP Inflows   | SIP investment trends           |
| Category Inflows      | Fund category inflows           |
| Industry Folio Count  | Investor participation          |
| Scheme Performance    | Return metrics                  |
| Investor Transactions | SIP and lump-sum investments    |
| Portfolio Holdings    | Stock and sector allocations    |
| Benchmark Indices     | Market benchmark 
performance    |

## Installation and setup

### Clone the repository

git clone https://github.com/Bharathreddy560/mutual-funds.git

cd mutual-funds

### Create virtual environment

python -m venv venv

### Activate virtual environment

Windows:

venv\Scripts\activate

### Install dependencies

pip install -r requirements.txt

## How to run the project

Run the complete analytics pipeline:

python run_pipeline.py

Run the fund recommender:

python recommender.py

Open the dashboard:

dashboard/dashboard.pdf

## Analytics performed

### Exploratory data analysis

* NAV trend analysis
* SIP growth analysis
* Investor demographic analysis
* Geographic distribution analysis
* Correlation analysis

### Performance analytics

* CAGR
* Sharpe ratio
* Sortino ratio
* Alpha and Beta
* Maximum drawdown
* Tracking error

### Advanced risk analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-day Sharpe ratio
* Sector concentration (HHI)

### Investor analytics

* Cohort analysis
* SIP continuity analysis
* At-risk investor detection

### Recommendation engine

* Risk-based fund recommendation
* Sharpe ratio ranking
* Low / Moderate / High risk mapping

## Key findings

* Large-cap funds delivered superior risk-adjusted performance.
* Small-cap funds exhibited the highest downside risk.
* The 2024 investor cohort contributed the largest investment volume.
* More than 1,300 investors were identified as at-risk due to irregular SIP continuity.
* Sector concentration varied significantly across equity funds.
* Rolling Sharpe analysis highlighted periods of changing fund efficiency.

## Technologies used

* Python
* Pandas
* NumPy
* Matplotlib
* Plotly
* SQLite
* SQL
* Jupyter Notebook
* Git
* GitHub
## Final project deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Advanced_Analytics.ipynb
* recommender.py
* run_pipeline.py
* Dashboard
* Performance and risk analytics reports

## Project completion status

All major project objectives have been completed, including ETL, SQL database creation, exploratory data analysis, performance analytics, advanced risk analytics, investor analytics, dashboard development, reporting, and presentation.

## Repository

GitHub: https://github.com/Bharathreddy560/mutual-funds


## Author

**Bandi Bharath**

Bluestock Fintech Data Analytics Capstone Project

GitHub: https://github.com/Bharathreddy560/mutual-funds









