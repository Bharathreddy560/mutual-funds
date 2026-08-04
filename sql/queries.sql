-- 1. Total NAV records
SELECT COUNT(*) AS total_nav_records
FROM fact_nav;

-- 2. Total transaction records
SELECT COUNT(*) AS total_transaction_records
FROM fact_transactions;

-- 3. Transaction count by type
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Transaction count by type (highest first)
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;

-- 5. Top 5 highest transactions
SELECT investor_id,
       transaction_type,
       amount_inr
FROM fact_transactions
ORDER BY amount_inr DESC
LIMIT 5;

-- 6. Top 5 SIP transactions
SELECT investor_id,
       transaction_date,
       amount_inr
FROM fact_transactions
WHERE transaction_type = 'SIP'
ORDER BY amount_inr DESC
LIMIT 5;

-- 7. Monthly transaction count
SELECT strftime('%Y-%m', transaction_date) AS month,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY month
ORDER BY month;

-- 8. Average transaction amount by type
SELECT transaction_type,
       AVG(amount_inr) AS average_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Transactions by KYC status
SELECT kyc_status,
       COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status;

-- 10. Top 10 cities by transaction count
SELECT city,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY city
ORDER BY total_transactions DESC
LIMIT 10;