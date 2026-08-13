"""
Data cleaning and SQLite database creation.

This script cleans mutual fund datasets,
handles missing values, standardizes formats,
and creates the project database.

Author: Bandi Bharath
"""
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

# -----------------------------
# STEP 1: Clean NAV history data
# -----------------------------

nav = pd.read_csv("data/raw/02_nav_history.csv")

print(nav.dtypes)

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

print(nav.dtypes)

# Sort data
nav = nav.sort_values(["amfi_code", "date"])

print(nav.head())

# Check missing values
print(nav.isnull().sum())

# Check duplicate rows
print(nav.duplicated().sum())

# Remove duplicates
nav = nav.drop_duplicates()

# Save cleaned NAV data
nav.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV history cleaned successfully!")


# ---------------------------------------
# STEP 2: Clean investor transaction data
# ---------------------------------------

tx = pd.read_csv("data/raw/08_investor_transactions.csv")

print(tx.head())

print(tx.dtypes)

# Convert transaction date
tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])

print(tx.dtypes)

# Standardize transaction type
tx["transaction_type"] = tx["transaction_type"].str.strip().str.title()

tx["transaction_type"] = tx["transaction_type"].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

print(tx["transaction_type"].unique())

# Check invalid amounts
print(tx[tx["amount_inr"] <= 0])

# Keep only valid amounts
tx = tx[tx["amount_inr"] > 0]

# Check minimum amount
print(tx["amount_inr"].min())

# Check KYC values
print(tx["kyc_status"].unique())

# Save cleaned transaction data
tx.to_csv("data/processed/investor_transactions_cleaned.csv", index=False)

print("Investor transactions cleaned successfully!")


# -----------------------------------
# STEP 3: Create SQLite database
# -----------------------------------

engine = create_engine("sqlite:///bluestock_mf.db")

print("Database connection created successfully!")


# -----------------------------------
# STEP 4: Load data into SQLite
# -----------------------------------

# Load NAV table
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("NAV data loaded into SQLite successfully!")

# Load transaction table
tx.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Transaction data loaded into SQLite successfully!")


# -----------------------------------
# STEP 5: Verify row counts using SQL
# -----------------------------------

conn = sqlite3.connect("bluestock_mf.db")

# Count NAV rows
nav_count = pd.read_sql(
    "SELECT COUNT(*) AS total_rows FROM fact_nav;",
    conn
)

print("Fact NAV table:")
print(nav_count)

# Count transaction rows
tx_count = pd.read_sql(
    "SELECT COUNT(*) AS total_rows FROM fact_transactions;",
    conn
)

print("Fact Transactions table:")
print(tx_count)
# Show first 5 rows from fact_nav

result = pd.read_sql(
    "SELECT * FROM fact_nav LIMIT 5;",
    conn
)

print(result)
# Count transactions by type

result = pd.read_sql(
    """
    SELECT transaction_type,
           COUNT(*) AS total_transactions
    FROM fact_transactions
    GROUP BY transaction_type;
    """,
    conn
)

print(result)
# Sort transaction types by highest count

result = pd.read_sql(
    """
    SELECT transaction_type,
           COUNT(*) AS total_transactions
    FROM fact_transactions
    GROUP BY transaction_type
    ORDER BY total_transactions DESC;
    """,
    conn
)

print(result)
# Top 5 highest transaction amounts

result = pd.read_sql(
    """
    SELECT investor_id,
           transaction_type,
           amount_inr
    FROM fact_transactions
    ORDER BY amount_inr DESC
    LIMIT 5;
    """,
    conn
)

print(result)
# Top 5 SIP transactions above Rs. 10,000

result = pd.read_sql(
    """
    SELECT investor_id,
           transaction_date,
           amount_inr
    FROM fact_transactions
    WHERE transaction_type = 'SIP'
      AND amount_inr > 10000
    ORDER BY amount_inr DESC
    LIMIT 5;
    """,
    conn
)

print(result)
# Monthly transaction count

result = pd.read_sql(
    """
    SELECT strftime('%Y-%m', transaction_date) AS month,
           COUNT(*) AS total_transactions
    FROM fact_transactions
    GROUP BY month
    ORDER BY month;
    """,
    conn
)

print(result)
# Close the connection
conn.close()

print("Database verification completed successfully!")