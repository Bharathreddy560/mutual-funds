# Data dictionary

## Database: bluestock_mf.db

This database contains cleaned mutual fund NAV data and investor transaction data.

---

## Table: fact_nav

Stores historical NAV (Net Asset Value) records.

| Column    | Data Type | Description                         |
| --------- | --------- | ----------------------------------- |
| amfi_code | INTEGER   | AMFI scheme code of the mutual fund |
| date      | DATE      | NAV date                            |
| nav       | REAL      | Net Asset Value of the scheme       |

Example:

| amfi_code | date       | nav      |
| --------- | ---------- | -------- |
| 100016    | 2022-01-03 | 520.4608 |

---

## Table: fact_transactions

Stores investor transaction records.

| Column             | Data Type | Description                             |
| ------------------ | --------- | --------------------------------------- |
| investor_id        | TEXT      | Unique investor ID                      |
| transaction_date   | DATE      | Date of the transaction                 |
| amfi_code          | INTEGER   | Mutual fund AMFI code                   |
| transaction_type   | TEXT      | SIP, Lumpsum, or Redemption             |
| amount_inr         | INTEGER   | Transaction amount in Indian Rupees     |
| state              | TEXT      | Investor state                          |
| city               | TEXT      | Investor city                           |
| city_tier          | TEXT      | City classification (Tier 1/2/3)        |
| age_group          | TEXT      | Investor age group                      |
| gender             | TEXT      | Investor gender                         |
| annual_income_lakh | REAL      | Annual income in lakhs                  |
| payment_mode       | TEXT      | UPI, Cheque, Net Banking, Mandate, etc. |
| kyc_status         | TEXT      | Verified or Pending                     |

Example:

| investor_id | transaction_type | amount_inr |
| ----------- | ---------------- | ---------- |
| INV003054   | SIP              | 5000       |

---

## Data cleaning performed

### fact_nav

* Converted date to datetime
* Sorted by amfi_code and date
* Removed duplicate rows
* Validated NAV values
* Saved cleaned dataset

### fact_transactions

* Converted transaction_date to datetime
* Standardized transaction_type values
* Removed invalid transaction amounts
* Validated KYC values
* Saved cleaned dataset

---

## Database summary

* fact_nav: 46,000 rows
* fact_transactions: 32,778 rows

Created as part of the Day 2 Mutual Fund Analytics internship project.
