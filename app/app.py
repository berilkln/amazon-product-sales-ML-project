import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(
    page_title="Amazon Product Sales Dashboard 2025",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("data/amazon_sales_2025_analyzed.csv")
    return df

df = load_data()

# --- Title and Description ---
st.title("🛍️ Amazon Product Sales Dashboard - 2025")
st.markdown("""
### 📘 Dataset Overview
This dashboard is based on the **Amazon Products Sales Dataset (42K+ Items - 2025)** published on [Kaggle](https://www.kaggle.com/datasets/ikramshah512/amazon-products-sales-dataset-42k-items-2025).

The dataset contains detailed information on **over 42,000 Amazon products**, covering various categories, prices, ratings, discounts, and sales performance metrics.

Each record represents a unique product listing and includes attributes such as:
- Product title, category, and price information (original & discounted)
- Customer rating and number of reviews
- Monthly sales volume and discount rate
- Best-seller, sponsored, coupon, and eco-badge status indicators

📅 **Data Period:** Collected and published in **2025**, reflecting product listings and performance from **late 2024 to early 2025**.

💾 **Dataset Size:** 42,675 rows × 18 columns  
This dashboard has been developed **for educational and analytical purposes only**.  
""")


# --- Sidebar Filters ---
st.sidebar.header("🔍 Filters")
category = st.sidebar.multiselect("Select Product Category:", df['product_category'].unique())
segment = st.sidebar.multiselect("Select Price Segment:", df['price_segment'].unique())
best_seller = st.sidebar.multiselect("Select Best Seller Status:", df['best_seller'].unique())
coupon_available = st.sidebar.multiselect("Select Coupon Availability:", df['coupon_available'].unique())
eco_badge = st.sidebar.multiselect("Select Eco Badge Availability:", df['eco_badge'].unique())

filtered_df = df.copy()
if category:
    filtered_df = filtered_df[filtered_df['product_category'].isin(category)]
if segment:
    filtered_df = filtered_df[filtered_df['price_segment'].isin(segment)]
if best_seller:
    filtered_df = filtered_df[filtered_df['best_seller'].isin(best_seller)]
if coupon_available:
    filtered_df = filtered_df[filtered_df['coupon_available'].isin(coupon_available)]
if eco_badge:
    filtered_df = filtered_df[filtered_df['eco_badge'].isin(eco_badge)]

# --- KPI Cards ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Products", len(filtered_df))
col2.metric("Average Rating", round(filtered_df['product_rating'].mean(), 2))
col3.metric("Avg. Discount Rate (%)", round(filtered_df['discount_rate'].mean(), 2))
col4.metric("Avg. Monthly Sales", round(filtered_df['sales_last_month'].mean(), 2))

# --- Pie Charts (Categorical Overview) ---
st.markdown("###  Categorical Distributions")

col1, col2, col3 = st.columns(3)

fig1 = px.pie(filtered_df, names='best_seller', title='Best Seller Distribution')
col1.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(filtered_df, names='price_segment', title='Price Segment Distribution')
col2.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(filtered_df, names='sponsored', title='Sponsored Product Ratio')
col3.plotly_chart(fig3, use_container_width=True)


st.markdown("## 📊 Key Insights")

# --- Top 10 Categories by Sales ---
st.markdown("### 🔝 Top 10 Categories by Total Sales")
top_sales = (
    filtered_df.groupby('product_category')['sales_last_month']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(top_sales, x='product_category', y='sales_last_month',
              title='Top 10 Best-Selling Categories',
              text='sales_last_month')
fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside')
st.plotly_chart(fig4, use_container_width=True)



# 1️⃣ Discount Rate vs Monthly Sales
fig5 = px.scatter(filtered_df, 
                   x='discount_rate', 
                   y='sales_last_month',
                   color='product_category',
                   title='Discount Rate vs Monthly Sales',
                   labels={'discount_rate': 'Discount Rate (%)', 'sales_last_month': 'Monthly Sales Volume'})
st.plotly_chart(fig5, use_container_width=True)

# 2️⃣ Reviews vs Sales
fig6 = px.scatter(filtered_df, 
                   x='review_count', 
                   y='sales_last_month',
                   trendline='ols',
                   opacity=0.6,
                   title='Number of Reviews vs Monthly Sales',
                   labels={'review_count': 'Number of Reviews', 'sales_last_month': 'Monthly Sales Volume'})
st.plotly_chart(fig6, use_container_width=True)

# Price vs Rating
fig7 = px.scatter(filtered_df, 
                   x='discounted_price', 
                   y='product_rating',
                   color='product_category',
                   opacity=0.6,
                   title='Discounted Price vs Product Rating',
                   labels={'discounted_price': 'Discounted Price ($)', 'product_rating': 'Product Rating (1–5)'})
st.plotly_chart(fig7, use_container_width=True)

# Price Segment vs Average Sales
avg_sales_segment = (
    filtered_df.groupby('price_segment')['sales_last_month']
    .mean().reset_index()
)
fig8 = px.bar(avg_sales_segment, 
               x='price_segment', 
               y='sales_last_month',
               title='Average Monthly Sales by Price Segment',
               labels={'price_segment': 'Price Segment', 'sales_last_month': 'Avg. Monthly Sales'})
st.plotly_chart(fig8, use_container_width=True)


avg_df = (filtered_df.groupby('product_category')[['discount_rate', 'product_rating']].mean().reset_index())

fig9 = px.scatter(
    avg_df,
    x='discount_rate',
    y='product_rating',
    color='product_category',
    size='product_rating',
    title='Average Rating vs Discount Rate (per Category)',
    labels={
        'discount_rate': 'Average Discount Rate (%)',
        'product_rating': 'Average Product Rating (1–5)'
    }
)
st.plotly_chart(fig9, use_container_width=True)
