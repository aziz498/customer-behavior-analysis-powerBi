:Overview
This project analyzes customer shopping behaviour to understand revenue patterns, subscription impact, and product performance.
The analysis helps businesses make data-driven decisions related to marketing, customer retention, and sales optimization.

The project follows a complete BI workflow:
-Data cleaning using Python
-Data modeling and analysis using SQL
-Interactive dashboard using Power BI
-Business Objective
-Identify high-value customer segments
-Analyze the impact of subscriptions on spending
-Understand product category performance
-Evaluate purchasing trends across age groups


:Dataset Summary

-Source: Kaggle
-Records: 3,900
-Columns: 18
-Data Includes:
 Customer details (age, gender, location, subscription status)
 Purchase information (item, category, size, color, season, amount)
 Shopping behaviour (discounts, frequency, reviews, shipping type)
-Missing Data:
 37 missing values in the review rating column


:Data Cleaning & Preparation

-Filled missing review ratings using median values by product category
-Removed duplicate records during SQL data loading
-Created new features such as:
 Age groups
 Purchase frequency labels
 Review rating categories
 Removed redundant columns to keep data clean and efficient
-Tools Used: Python (Pandas)


:Data Modeling

A fact-dimension (star schema) was designed for efficient analysis.
-Dimension Tables
 Dim_Customer: Customer demographics and subscription details
 Dim_Item: Product attributes such as category, size, and color
 Dim_Order_Details: Order and delivery information

-Fact Table
 Fact_Sales: Transaction-level data including purchase amount, reviews, and previous purchases


:SQL Analysis

Key business questions answered:

-Revenue comparison by gender
-Spending behavior of subscribed vs non-subscribed customers
-Top-rated products
-Customer segmentation (New, Returning, Loyal)
-Revenue contribution by age group
-Relationship between repeat purchases and subscriptions


:Power BI Dashboard

An interactive dashboard was built to visualize:

-Revenue trends
-Customer segments
-Subscription impact
-Product category performance
-Age group analysis

"Key Insights & Recommendations

-Increase subscriptions: Most customers are non-subscribers; targeted offers can improve retention
-Focus on top categories: Clothing and Accessories generate the highest revenue
-Target high-value age groups: Young adults and middle-aged customers drive most sales
-Improve low-performing categories: Footwear and Outerwear need better pricing or promotions
-Enhance customer experience: Improving product quality and delivery can increase review ratings and repeat purchases


