



# 🛒 Super Store Sales & Operations Analysis

This project provides a concise yet impactful exploratory data analysis (EDA) of a retail Super Store dataset. The primary goal is to understand store performance metrics—such as revenue, customer count, and inventory availability—and uncover patterns that can inform better retail decisions.

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Dataset Summary](#dataset-summary)
- [Business Objectives](#business-objectives)
- [Tools and Technologies](#tools-and-technologies)
- [Analysis Workflow](#analysis-workflow)
  - [1. Data Inspection](#1-data-inspection)
  - [2. Data Cleaning & Type Conversion](#2-data-cleaning--type-conversion)
  - [3. Univariate Analysis](#3-univariate-analysis)
  - [4. Bivariate & Correlation Analysis](#4-bivariate--correlation-analysis)
- [Key Insights](#key-insights)
- [Visualizations](#visualizations)
- [Conclusion](#conclusion)
- [Author](#author)

---

## 📊 Project Overview

Retail stores generate vast amounts of sales and operations data. This project explores patterns across store locations, performance metrics, and inventory counts. It demonstrates data manipulation, statistical description, and visual storytelling using Python.

---

## 🗃 Dataset Summary

- **File Name:** Stores.csv
- **Number of Records:** Varies
- **Key Fields:**
  - `Store ID`
  - `Store_Area`
  - `Items_Available`
  - `Daily_Customer_Count`
  - `Store_Sales`
  - `Furnished` (Boolean indicator)
  - `Price`

---

## 🎯 Business Objectives

- Identify top-performing stores by revenue
- Determine customer traffic patterns by store
- Understand correlation between store features and performance (e.g., size, item availability)
- Provide actionable insights for business stakeholders (marketing, operations, expansion)

---

## 🛠 Tools and Technologies

- **Language:** Python
- **Libraries:** 
  - pandas
  - numpy
  - seaborn
  - matplotlib
- **Environment:** Jupyter Notebook

---

## 🔍 Analysis Workflow

### 1. Data Inspection
- Loaded and displayed first few rows using `pandas`
- Verified data shape, column names, and data types
- Checked for null values and duplicate entries

### 2. Data Cleaning & Type Conversion
- Converted `Store ID` from float to integer
- Ensured consistency in data types for accurate analysis

### 3. Univariate Analysis
- Calculated revenue by store and ranked top 10
- Counted daily customer visits by store ID
- Ranked stores by `Store_Area`
- Used bar charts and pie charts for easy interpretation

### 4. Bivariate & Correlation Analysis
- Visualized relationship between `Items_Available` and `Daily_Customer_Count` using scatter plots
- Explored correlation between store attributes and sales behavior
- Used regression plots for price vs furnished apartments

---

## 💡 Key Insights

- **Store Performance:** Top 10 stores by revenue exhibit significantly higher customer counts.
- **Customer Behavior:** Stores with more items available tend to attract more customers.
- **Store Area Impact:** Larger stores tend to contribute more to total revenue.
- **Inventory vs Demand:** There's a positive correlation between item availability and daily footfall.

---

## 📈 Visualizations

- Bar Chart: Top 10 Store IDs by Revenue
- Horizontal Bar Chart: Top Store IDs by Daily Customers
- Pie Chart: Top Store Areas
- Scatter Plot: Customer Count vs Items Available
- Regression Plot: Price vs Furnishing Status

---

## ✅ Conclusion

This analysis demonstrates how basic EDA can help uncover meaningful insights in retail operations. It highlights the analyst’s ability to clean and interpret data, answer key business questions, and generate visual narratives that guide strategic decisions.

---

## 👩‍💻 Author

**Precious Celestine**  
*Data Analyst | Excel | SQL | Power BI | Python*  
[LinkedIn](https://www.linkedin.com/in/preciouscelestine) | [GitHub](https://github.com/preciouscelestine)

---

> ⚠️ Disclaimer: This dataset is used for learning purposes and may not reflect real commercial activity.

