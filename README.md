# 🛍️ Amazon Product Sales Analysis (2025)

This project performs a complete end-to-end data analysis workflow on the **Amazon Products Sales Dataset (42K+ Items – 2025)**.
It includes detailed **data cleaning**, **feature engineering**, **exploratory data analysis (EDA)**, and an **interactive Streamlit dashboard** that visualizes key business insights.

---

## 📘 Dataset Information

* **Source:** [Kaggle – Amazon Products Sales Dataset (42K+ Items – 2025)](https://www.kaggle.com/datasets/ikramshah512/amazon-products-sales-dataset-42k-items-2025)
* **Data Period:** Collected and published in **2025**, reflecting listings from **late 2024 to early 2025**
* **Dataset Size:** 42,675 rows × 18 columns

The dataset contains product-level information extracted from an Amazon-like e-commerce platform.
Each record represents a unique product listing with features related to pricing, discounting, sales performance, and customer feedback.

---

## 📊 Dataset Columns Overview

| Column Name        | Description                                                          |
| ------------------ | -------------------------------------------------------------------- |
| `product_title`    | Name/Title of the product                                            |
| `product_category` | Category under which the product is listed                           |
| `discounted_price` | Current selling price after discount                                 |
| `original_price`   | Original listed price                                                |
| `discount_rate`    | Calculated percentage discount between original and discounted price |
| `product_rating`   | Average user rating (out of 5 stars)                                 |
| `review_count`     | Number of user reviews for the product                               |
| `sales_last_month` | Number of items sold in the past month                               |
| `price_segment`    | Categorized price level (Low / Medium / High / Premium)              |
| `best_seller`      | Indicates if the product is a best seller                            |
| `eco_badge`        | Indicates if the product has an eco-friendly badge                   |
| `coupon_available` | Shows whether a discount coupon is available                         |
| `sponsored`        | Marks if the product is a sponsored listing                          |
| `product_url`      | Link to the product listing (not used in analysis)                   |
| `image_url`        | Product image URL (not used in analysis)                             |
| `buy_box_status`   | Indicates whether the product was currently in Amazon’s Buy Box      |
| `has_discount`     | Shows if the product had any active discount or price reduction at the time of collection.|
| `collection_day`   | The day of the month when the product information was collected      |
| `collection_week`  | The week number during which the data was collected                  |
| `collection_month` | The month of data collection                                         |

---

## 🧹 Notebook 1: Data Cleaning & Feature Engineering

**File:** `notebooks/data_cleaning.ipynb`

This notebook performs comprehensive **data cleaning** and **feature engineering** on the raw dataset.

### Key Steps

* Inspected all columns and data types
* Removed redundant whitespaces, symbols, and text artifacts
* Standardized numerical fields (`discount_rate`, `discounted_price`, `original_price`)
* Converted percentage and currency strings to numeric values
* Created a new column:  
  - **price segmentation** (Low / Medium / High / Premium)
  - **has_discount** → Indicates whether the product had an active discount.
  - **collection_day**, **collection_week**, **collection_month** → Represent the day, week, and month when the data was collected.
  - **product_category** by title 
* Checked for missing values and inconsistencies (but did not perform imputation)
* Saved the cleaned dataset as:
  📁 `data/amazon_sales_2025_cleaned.csv`

---

## 📈 Notebook 2: Exploratory Data Analysis (EDA)

**File:** `notebooks/data_analysis.ipynb`

This notebook explores **product performance patterns**, **sales trends**, and **pricing behaviors** through visual analysis.

### Key Analytical Steps

* General overview of product ratings, reviews, and discounts
* Missing value and correlation heatmap analysis
* Distribution plots for prices, discounts, and ratings
* Univariate Analysis:
  * Product Rating Distribution
  * Discount Rate Distribution
  * Price Segment Distribution
  * Eco-Badge Distribution
  * Product Category Distribution
* Bivariate analyses:
  * `discount_rate` vs `sales_last_month`
  * `product_rating` vs `discounted_price`
  * `review_count` vs `sales_last_month`
  * `price_segment` vs `sales_last_month`
 
### Objective

The goal of this analysis was to uncover **how factors such as price, rating, and discount** affect product sales and popularity.

---

## 💻 Streamlit Dashboard

**File:** `app/app.py`  

[Streamlit App Link](https://amazon-sales-ml-project.streamlit.app)


The interactive dashboard visualizes the key insights extracted from the cleaned dataset.
Users can explore **categories**, **price segments**, and **product performance** dynamically through filters.

### Dashboard Features

* 🧭 Sidebar filters for category, price segment, best seller, coupon, and eco badge
* 💡 KPI cards showing key metrics:

  * Total products
  * Average rating
  * Average discount rate
  * Average monthly sales
* 🥧 Pie charts for categorical distributions
* 📊 Bar and scatter plots for:

  * Top-selling categories
  * Discount vs sales
  * Reviews vs sales
  * Price vs rating
  * Average rating vs discount (per category)

---

## ⚙️ Tech Stack

| Category          | Tools / Libraries           |
| ----------------- | --------------------------- |
| **Language**      | Python 3.10                 |
| **Data Analysis** | pandas, numpy               |
| **Visualization** | matplotlib, seaborn, plotly |
| **Web App**       | Streamlit                   |
| **Environment**   | Jupyter Notebook, VS Code   |

---

## 📂 Project Structure

```
amazon-product-sales-ML-project/
│
├── app/
│   └── app.py
│
├── data/
│   ├── amazon_sales_2025_analyzed.csv
│   ├── amazon_sales_2025_raw.csv
│   └── amazon_sales_2025_cleaned.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── data_analysis.ipynb
│
├── requirements.txt
└── README.md
```

---

## 🧠 Insights Summary

* Products with higher discounts usually have more sales.
* Best Seller items tend to get better ratings and more reviews.
* Sponsored and coupon products get more visibility but don’t affect ratings much.
* Eco Badge (eco-friendly) products have steady, moderate demand.

---

## 📘 Note

This project was created for learning and analysis purposes only.  
All data was taken from Kaggle’s public dataset and is not intended for commercial use.

