# 3. Reporting
# For reporting purposes, you can use Python along with libraries like Matplotlib, Seaborn, or Plotly for visualization.

# Transaction Count by Customer (Bar Chart)


import matplotlib.pyplot as plt

# Query to get the transaction count by customer
query = """
SELECT 
    customer_id,
    COUNT(*) AS transaction_count
FROM 
    transactions
GROUP BY 
    customer_id
ORDER BY 
    transaction_count DESC
"""
data = pd.read_sql(query, engine)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(data['customer_id'], data['transaction_count'])
plt.xlabel('Customer ID')
plt.ylabel('Transaction Count')
plt.title('Transaction Count per Customer')
plt.xticks(rotation=90)
plt.show()


# 3.2. Monthly Spending Trend (Line Chart)

# Query to get monthly spending trends
query = """
SELECT 
    DATE_TRUNC('month', transaction_date) AS month,
    SUM(total_spent) AS monthly_spending
FROM 
    transactions
GROUP BY 
    month
ORDER BY 
    month
"""
data = pd.read_sql(query, engine)

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(data['month'], data['monthly_spending'], marker='o')
plt.xlabel('Month')
plt.ylabel('Monthly Spending')
plt.title('Monthly Spending Trend')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

-- 3.3. Top 10 Spenders (Pie Chart)

# Query to get top spenders
query = """
SELECT 
    customer_id,
    SUM(total_spent) AS total_spent
FROM 
    transactions
GROUP BY 
    customer_id
ORDER BY 
    total_spent DESC
LIMIT 10
"""
data = pd.read_sql(query, engine)


# Plotting the pie chart

plt.figure(figsize=(8, 8))
plt.pie(data['total_spent'], labels=data['customer_id'], autopct='%1.1f%%', startangle=90)
plt.title('Top 10 Spenders')
plt.show()

# 4.ETL Scheduling
# You can automate the ETL process using Apache Airflow to schedule and monitor it.


# Example of an Airflow DAG for the ETL process
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_transform_load():
    # ETL code from above (Extract, Transform, Load)
    pass

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

with DAG('credit_card_etl', default_args=default_args, schedule_interval='@daily') as dag:
    etl_task = PythonOperator(
        task_id='etl_task',
        python_callable=extract_transform_load,
    )


# Conclusion
# This project covers:

# ETL: Extract data, transform it, and load it into a database.
# SQL Queries: Aggregate and analyze the data based on customer and transaction metrics.
# Reporting: Visualize trends, spending patterns, and top spenders using Python and SQL.