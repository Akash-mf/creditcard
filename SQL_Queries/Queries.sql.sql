-- SQL Queries for Analysis
-- You can write SQL queries to analyze various aspects of credit card data, like transaction trends, average spending, and customer behavior.

-- Customer Spending Summary
-- Query to get total spending per customer.


SELECT 
    customer_id,
    SUM(total_spent) AS total_spent
FROM 
    transactions
GROUP BY 
    customer_id
ORDER BY 
    total_spent DESC;

-- Monthly Spending Trend
-- Query to analyze monthly spending trends.


SELECT 
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(total_spent) AS monthly_spending
FROM 
    transactions
GROUP BY 
    month
ORDER BY 
    month;

-- Top Spenders
-- Query to find the top 10 customers by total spending.


SELECT 
    customer_id,
    SUM(total_spent) AS total_spent
FROM 
    transactions
GROUP BY 
    customer_id
ORDER BY 
    total_spent DESC
LIMIT 10;

-- Transaction Frequency by Customer
-- Query to analyze the frequency of transactions by customer.


SELECT 
    customer_id,
    COUNT(*) AS transaction_count
FROM 
    transactions
GROUP BY 
    customer_id
ORDER BY 
    transaction_count DESC;
