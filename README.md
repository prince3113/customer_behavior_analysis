Project Overview

This project analyzes customer shopping behavior using transactional data from 3,900 purchases across multiple product categories. The goal is to uncover insights into spending patterns, customer segmentation, product preferences, and subscription behavior to support data-driven business decisions.

Dataset Summary
Total Records: 3,900
Columns: 18
Missing Values: 37 (in Review Rating)
Key Features:
Customer demographics (Age, Gender, Location, Subscription Status)
Purchase details (Item, Category, Amount, Season, Size, Color)
Shopping behavior (Discount, Promo Code, Frequency, Shipping Type)

Data Cleaning & Preparation (Python)
Loaded dataset using pandas
Handled missing values using median imputation by category
Standardized column names to snake_case
Feature Engineering:
age_group
purchase_frequency_days
Removed redundant column: promo_code_used
Integrated cleaned data into PostgreSQL

SQL Analysis (Business Insights)

Performed advanced queries to extract insights:

Revenue comparison by gender
High-spending customers using discounts
Top 5 products by rating
Shipping type vs spending (Express vs Standard)
Subscribers vs Non-subscribers analysis
Discount-dependent products
Customer segmentation (New, Returning, Loyal)
Top products per category
Repeat buyers & subscription behavior
Revenue by age group

Key Insights
Male customers generated ~2x more revenue than females
Express shipping users spend slightly more on average
Majority customers fall under the Loyal segment (3000+)
Discounts significantly influence purchasing behavior
Young adults contribute the highest revenue

Power BI Dashboard

An interactive dashboard was built to visualize:

Customer distribution
Revenue trends
Category-wise sales
Subscription insights
Age group analysis

Business Recommendations
Boost subscriptions with exclusive benefits
Implement customer loyalty programs
Optimize discount strategies
Focus marketing on high-revenue segments
Promote top-rated & best-selling products

Tech Stack
Python (Pandas, NumPy)
SQL (PostgreSQL)
Power BI
Data Analysis & Visualization

How to run
# Clone the repository
git clone https://github.com/prince3113/customer_behavior_analysis.git

# Install dependencies
pip install pandas numpy

Project Files
Dataset (CSV)
Python Scripts
SQL Queries
Power BI Dashboard (.pbix)
Project Report & PPT
