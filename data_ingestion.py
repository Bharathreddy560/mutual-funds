"""
Mutual Fund Analytics - Data ingestion

Loads all raw mutual fund datasets, validates the data,
and prepares them for the ETL pipeline.

Functions:
- Load raw CSV datasets
- Validate dataset structure
- Perform initial data quality checks

Author: Bandi Bharath
Project: Bluestock Mutual Fund Analytics Capstone
"""
import os
import pandas as pd

# Path to raw data
folder = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

print(f"\nTotal CSV files found: {len(csv_files)}\n")

for file in csv_files:
    path = os.path.join(folder, file)

    print("=" * 70)
    print(f"File: {file}")
    print("=" * 70)

    try:
        df = pd.read_csv(path)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

       

    except Exception as e:
        print(f"Error reading {file}: {e}")

    print("\n")

    # Store fund master dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\n========== UNIQUE FUND HOUSES ==========")
print(fund_master["fund_house"].unique())

print("\n========== UNIQUE CATEGORIES ==========")
print(fund_master["category"].unique())

print("\n========== UNIQUE SUB CATEGORIES ==========")
print(fund_master["sub_category"].unique())

print("\n========== UNIQUE RISK CATEGORIES ==========")
print(fund_master["risk_category"].unique())

# Read datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print("\n========== AMFI CODE VALIDATION ==========")

if len(missing_codes) == 0:
    print("✅ All AMFI codes from Fund Master are present in NAV History.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)