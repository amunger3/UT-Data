#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Data Analysis Sample
Using pandas, numpy, and matplotlib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from datetime import datetime, timedelta
import random
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LinearRegression
import os
import warnings

model = RandomForestRegressor()

from sklearn.ensemble import RandomForestClassifier

# Now you can use the RandomForestClassifier
clf = RandomForestClassifier()

# Ignore all warnings
warnings.filterwarnings("ignore")

# Set plotting style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("viridis")
np.random.seed(42)  # For reproducibility

# Create save directory if it doesn't exist
SAVE_DIR = "data_analysis_results"
os.makedirs(SAVE_DIR, exist_ok=True)

###########################################
# Part 1: Data Generation and Preparation #
###########################################

def generate_sample_data(n_samples=1000):
    """
    Generate a sample dataset with various data types and patterns
    """
    print("Generating sample data...")
    
    # Date range
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = [(start_date + timedelta(days=x)) for x in range((end_date - start_date).days + 1)]
    
    # Randomly sample dates
    sample_dates = sorted(random.sample(date_range, n_samples))
    
    # Generate customer IDs
    customer_ids = [f'CUST_{i:05d}' for i in range(1, 101)]
    
    # Generate data
    data = {
        'date': sample_dates,
        'customer_id': [random.choice(customer_ids) for _ in range(n_samples)],
        'transaction_amount': np.random.exponential(scale=100, size=n_samples),
        'items_purchased': np.random.randint(1, 20, size=n_samples),
        'store_location': [random.choice(['North', 'South', 'East', 'West', 'Central']) for _ in range(n_samples)],
        'payment_method': [random.choice(['Credit', 'Debit', 'Cash', 'Mobile']) for _ in range(n_samples)],
        'customer_rating': np.random.randint(1, 6, size=n_samples),
        'discount_applied': np.random.choice([True, False], size=n_samples, p=[0.3, 0.7]),
        'return_customer': np.random.choice([True, False], size=n_samples, p=[0.6, 0.4]),
    }
    
    # Add some patterns and correlations
    for i in range(n_samples):
        # Customers who buy more items tend to spend more
        data['transaction_amount'][i] *= (0.8 + data['items_purchased'][i] / 10)
        
        # Higher discounts for larger transactions
        if data['transaction_amount'][i] > 150:
            data['discount_applied'][i] = np.random.choice([True, False], p=[0.8, 0.2])
        
        # Rating correlation with discount
        if data['discount_applied'][i]:
            data['customer_rating'][i] = min(5, data['customer_rating'][i] + np.random.choice([0, 1], p=[0.6, 0.4]))
    
    # Generate seasonal patterns in transaction amount
    for i, date in enumerate(data['date']):
        # Summer sales boost
        if 6 <= date.month <= 8:
            data['transaction_amount'][i] *= 1.2
        # Holiday season boost
        elif date.month == 12 or date.month == 1:
            data['transaction_amount'][i] *= 1.5
        # Weekend boost
        if date.weekday() >= 5:  # Saturday or Sunday
            data['transaction_amount'][i] *= 1.3
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add derived features
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day_of_week'] = df['date'].dt.dayofweek
    df['is_weekend'] = df['day_of_week'] >= 5
    df['season'] = df['month'].apply(lambda x: 'Winter' if x in [12, 1, 2] else
                                     'Spring' if x in [3, 4, 5] else
                                     'Summer' if x in [6, 7, 8] else 'Fall')
    
    # Add some missing values for practical handling
    random_indices = np.random.choice(range(n_samples), int(n_samples * 0.05), replace=False)
    df.loc[random_indices, 'customer_rating'] = np.nan
    
    random_indices = np.random.choice(range(n_samples), int(n_samples * 0.03), replace=False)
    df.loc[random_indices, 'payment_method'] = np.nan
    
    print(f"Sample data generated with {n_samples} rows.")
    return df

def preprocess_data(df):
    """
    Preprocess the dataset: handle missing values, convert data types, etc.
    """
    print("\nPreprocessing data...")
    
    # Make a copy to avoid modifying the original
    df_processed = df.copy()
    
    # Convert date column to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(df_processed['date']):
        df_processed['date'] = pd.to_datetime(df_processed['date'])
    
    # Handle missing values
    df_processed['customer_rating'].fillna(df_processed['customer_rating'].median(), inplace=True)
    df_processed['payment_method'].fillna(df_processed['payment_method'].mode()[0], inplace=True)
    
    # Create features for time-based analysis
    df_processed['month_year'] = df_processed['date'].dt.to_period('M')
    
    # Feature engineering
    df_processed['transaction_size'] = pd.qcut(
        df_processed['transaction_amount'], 
        q=4, 
        labels=['Small', 'Medium', 'Large', 'Very Large']
    )
    
    # Encode categorical variables for modeling
    df_processed['store_location_encoded'] = df_processed['store_location'].map({
        'North': 0, 'South': 1, 'East': 2, 'West': 3, 'Central': 4
    })
    
    df_processed['payment_method_encoded'] = df_processed['payment_method'].map({
        'Credit': 0, 'Debit': 1, 'Cash': 2, 'Mobile': 3
    })
    
    # Boolean to int
    df_processed['discount_applied_int'] = df_processed['discount_applied'].astype(int)
    df_processed['return_customer_int'] = df_processed['return_customer'].astype(int)
    df_processed['is_weekend_int'] = df_processed['is_weekend'].astype(int)
    
    # Calculate days since first purchase for each customer
    customer_first_purchase = df_processed.groupby('customer_id')['date'].min()
    df_processed['first_purchase_date'] = df_processed['customer_id'].map(customer_first_purchase)
    df_processed['days_since_first_purchase'] = (df_processed['date'] - df_processed['first_purchase_date']).dt.days
    
    print("Data preprocessing completed.")
    return df_processed

#############################
# Part 2: Exploratory Analysis #
#############################

def explore_data(df):
    """
    Perform exploratory data analysis
    """
    print("\nPerforming exploratory data analysis...")
    
    # Basic descriptive statistics
    print("\nBasic Statistics:")
    print(df.describe().round(2))
    
    # Data types and missing values
    print("\nData Types and Missing Values:")
    data_info = pd.DataFrame({
        'Data Type': df.dtypes,
        'Non-Null Count': df.count(),
        'Missing Values': df.isnull().sum(),
        'Missing Percentage': (df.isnull().sum() / len(df) * 100).round(2)
    })
    print(data_info)
    
    # Categorical variables distribution
    print("\nCategorical Variables Distribution:")
    for col in ['store_location', 'payment_method', 'season', 'transaction_size']:
        print(f"\n{col} Distribution:")
        print(df[col].value_counts(normalize=True).round(4) * 100)
    
    # Numerical variables correlation
    print("\nCorrelation Matrix:")
    numeric_columns = df.select_dtypes(include=['number']).columns
    correlation_matrix = df[numeric_columns].corr().round(2)
    print(correlation_matrix)
    
    # Customer segmentation
    print("\nCustomer Segments:")
    customer_segments = df.groupby('customer_id').agg({
        'transaction_amount': ['count', 'mean', 'sum'],
        'items_purchased': ['mean', 'sum'],
        'customer_rating': 'mean',
        'return_customer': 'mean'
    })
    customer_segments.columns = [f'{col[0]}_{col[1]}' for col in customer_segments.columns]
    print(customer_segments.describe().round(2))
    
    # Time-based analysis
    print("\nMonthly Trends:")
    monthly_trends = df.groupby('month_year').agg({
        'transaction_amount': ['count', 'mean', 'sum'],
        'customer_rating': 'mean'
    })
    monthly_trends.columns = [f'{col[0]}_{col[1]}' for col in monthly_trends.columns]
    print(monthly_trends.head())
    
    # Store performance
    print("\nStore Location Performance:")
    store_performance = df.groupby('store_location').agg({
        'transaction_amount': ['count', 'mean', 'sum'],
        'customer_rating': 'mean',
        'return_customer': 'mean'
    })
    store_performance.columns = [f'{col[0]}_{col[1]}' for col in store_performance.columns]
    print(store_performance)
    
    print("Exploratory analysis completed.")
    return correlation_matrix, customer_segments, monthly_trends, store_performance

#############################
# Part 3: Data Visualization #
#############################

def create_visualizations(df, correlation_matrix, customer_segments, monthly_trends, store_performance):

    """
    Create visualizations for the dataset
    """
    print("\nCreating visualizations...")
    
    # Set up the plotting environment
    sns.set(style="whitegrid", font_scale=1.2)
    
    # 1. Distribution of transaction amounts
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(df['transaction_amount'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribution of Transaction Amounts')
    ax.set_xlabel('Transaction Amount ($)')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/transaction_amount_distribution.png", dpi=300)
    plt.close()
    
    # 2. Transaction amount by store location
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(x='store_location', y='transaction_amount', data=df, ax=ax)
    ax.set_title('Transaction Amount by Store Location')
    ax.set_xlabel('Store Location')
    ax.set_ylabel('Transaction Amount ($)')
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/transaction_by_location.png", dpi=300)
    plt.close()
    
    # 3. Correlation heatmap
    plt.figure(figsize=(14, 10))
    mask = np.zeros_like(correlation_matrix, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, annot=True, fmt='.2f')
    plt.title('Correlation Matrix of Numerical Variables')
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/correlation_heatmap.png", dpi=300)
    plt.close()
    
    # 4. Monthly transaction trends
    monthly_data = monthly_trends.reset_index()
    monthly_data['month_year_str'] = monthly_data['month_year'].dt.strftime('%Y-%m')
    
    fig, ax1 = plt.subplots(figsize=(14, 7))
    
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Total Transaction Amount ($)', color='tab:blue')
    ax1.plot(monthly_data['month_year_str'], monthly_data['transaction_amount_sum'], 
             marker='o', linestyle='-', color='tab:blue', label='Total Amount')
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('Number of Transactions', color='tab:red')
    ax2.plot(monthly_data['month_year_str'], monthly_data['transaction_amount_count'], 
             marker='s', linestyle='--', color='tab:red', label='Transaction Count')
    ax2.tick_params(axis='y', labelcolor='tab:red')
    
    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    plt.title('Monthly Transaction Trends')
    plt.xticks(rotation=45)
    fig.tight_layout()
    plt.savefig(f"{SAVE_DIR}/monthly_trends.png", dpi=300)
    plt.close()
    
    # 5. Customer rating distribution by payment method
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.violinplot(x='payment_method', y='customer_rating', data=df, ax=ax)
    ax.set_title('Customer Rating Distribution by Payment Method')
    ax.set_xlabel('Payment Method')
    ax.set_ylabel('Customer Rating')
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/rating_by_payment.png", dpi=300)
    plt.close()
    
    # 6. Items purchased vs transaction amount with discount applied
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x='items_purchased', y='transaction_amount', 
                   hue='discount_applied', size='customer_rating',
                   sizes=(20, 200), data=df.sample(n=500), ax=ax)
    ax.set_title('Items Purchased vs Transaction Amount')
    ax.set_xlabel('Number of Items Purchased')
    ax.set_ylabel('Transaction Amount ($)')
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/items_vs_amount.png", dpi=300)
    plt.close()
    
    # 7. Store performance comparison
    store_perf = store_performance.reset_index()
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Transaction count
    sns.barplot(x='store_location', y='transaction_amount_count', data=store_perf, ax=axes[0])
    axes[0].set_title('Number of Transactions by Store')
    axes[0].set_ylabel('Number of Transactions')
    
    # Average transaction
    sns.barplot(x='store_location', y='transaction_amount_mean', data=store_perf, ax=axes[1])
    axes[1].set_title('Average Transaction Amount by Store')
    axes[1].set_ylabel('Average Amount ($)')
    
    # Customer rating
    sns.barplot(x='store_location', y='customer_rating_mean', data=store_perf, ax=axes[2])
    axes[2].set_title('Average Customer Rating by Store')
    axes[2].set_ylabel('Average Rating')
    
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/store_performance.png", dpi=300)
    plt.close()
    
    # 8. Seasonal patterns
    seasonal_data = df.groupby('season').agg({
        'transaction_amount': ['count', 'mean', 'sum'],
        'items_purchased': 'mean',
        'customer_rating': 'mean'
    })
    seasonal_data.columns = [f'{col[0]}_{col[1]}' for col in seasonal_data.columns]
    seasonal_data = seasonal_data.reset_index()
    
    # Order seasons correctly
    season_order = ['Winter', 'Spring', 'Summer', 'Fall']
    seasonal_data['season'] = pd.Categorical(seasonal_data['season'], categories=season_order, ordered=True)
    seasonal_data = seasonal_data.sort_values('season')
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # Transaction count by season
    sns.barplot(x='season', y='transaction_amount_count', data=seasonal_data, ax=axes[0, 0])
    axes[0, 0].set_title('Number of Transactions by Season')
    axes[0, 0].set_ylabel('Number of Transactions')
    
    # Average transaction amount by season
    sns.barplot(x='season', y='transaction_amount_mean', data=seasonal_data, ax=axes[0, 1])
    axes[0, 1].set_title('Average Transaction Amount by Season')
    axes[0, 1].set_ylabel('Average Amount ($)')
    
    # Total revenue by season
    sns.barplot(x='season', y='transaction_amount_sum', data=seasonal_data, ax=axes[1, 0])
    axes[1, 0].set_title('Total Revenue by Season')
    axes[1, 0].set_ylabel('Total Revenue ($)')
    
    # Average customer rating by season
    sns.barplot(x='season', y='customer_rating_mean', data=seasonal_data, ax=axes[1, 1])
    axes[1, 1].set_title('Average Customer Rating by Season')
    axes[1, 1].set_ylabel('Average Rating')
    
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/seasonal_patterns.png", dpi=300)
    plt.close()
    
    # 9. Day of week patterns
    df['day_name'] = df['date'].dt.day_name()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['day_name'] = pd.Categorical(df['day_name'], categories=day_order, ordered=True)
    
    daily_data = df.groupby('day_name').agg({
        'transaction_amount': ['count', 'mean', 'sum'],
        'items_purchased': 'mean'
    })
    daily_data.columns = [f'{col[0]}_{col[1]}' for col in daily_data.columns]
    daily_data = daily_data.reset_index()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Transaction count by day
    sns.barplot(x='day_name', y='transaction_amount_count', data=daily_data, ax=ax1)
    ax1.set_title('Number of Transactions by Day of Week')
    ax1.set_ylabel('Number of Transactions')
    ax1.set_xlabel('')
    
    # Average transaction amount by day
    sns.barplot(x='day_name', y='transaction_amount_mean', data=daily_data, ax=ax2)
    ax2.set_title('Average Transaction Amount by Day of Week')
    ax2.set_ylabel('Average Amount ($)')
    ax2.set_xlabel('Day of Week')
    
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/day_of_week_patterns.png", dpi=300)
    plt.close()
    
    # 10. Customer Segments - Advanced Visualization
    # Prepare customer data for clustering
    customer_data = customer_segments.copy()
    
    # Select features for clustering
    features = ['transaction_amount_count', 'transaction_amount_mean', 'transaction_amount_sum',
                'items_purchased_mean', 'customer_rating_mean']
    X = customer_data[features].values
    
    # Normalize the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    clusters = kmeans.fit_predict(X_scaled)
    
    # Add cluster info to the data
    customer_data['cluster'] = clusters
    customer_data['pca1'] = X_pca[:, 0]
    customer_data['pca2'] = X_pca[:, 1]
    
    # Visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Create a scatter plot for each cluster
    for cluster_id in range(4):
        cluster_data = customer_data[customer_data['cluster'] == cluster_id]
        ax.scatter(cluster_data['pca1'], cluster_data['pca2'], 
                   s=cluster_data['transaction_amount_sum'] / 100,  # Size based on total spend
                   alpha=0.7, 
                   label=f'Cluster {cluster_id}')
    
    # Add cluster centers
    centers_pca = pca.transform(scaler.transform(kmeans.cluster_centers_))
    ax.scatter(centers_pca[:, 0], centers_pca[:, 1], s=300, c='black', marker='X', label='Cluster Centers')
    
    ax.set_title('Customer Segmentation based on Purchase Behavior')
    ax.set_xlabel(f'Principal Component 1 ({pca.explained_variance_ratio_[0]:.2%} variance)')
    ax.set_ylabel(f'Principal Component 2 ({pca.explained_variance_ratio_[1]:.2%} variance)')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/customer_segmentation.png", dpi=300)
    plt.close()
    
    # 11. Advanced: Interactive dashboard-style visualization
    fig = plt.figure(figsize=(22, 16))
    gs = gridspec.GridSpec(3, 3)
    
    # Transaction amount distribution by payment method
    ax1 = plt.subplot(gs[0, :2])
    sns.boxplot(x='payment_method', y='transaction_amount', data=df, ax=ax1)
    ax1.set_title('Transaction Amount Distribution by Payment Method', fontsize=14)
    ax1.set_xlabel('Payment Method', fontsize=12)
    ax1.set_ylabel('Transaction Amount ($)', fontsize=12)
    
    # Customer rating distribution
    ax2 = plt.subplot(gs[0, 2])
    sns.countplot(x='customer_rating', data=df, palette='viridis', ax=ax2)
    ax2.set_title('Customer Rating Distribution', fontsize=14)
    ax2.set_xlabel('Customer Rating', fontsize=12)
    ax2.set_ylabel('Count', fontsize=12)
    
    # Monthly transaction count and average
    ax3 = plt.subplot(gs[1, :])
    monthly_data_short = monthly_data.tail(12)  # Last 12 months
    
    bar_width = 0.4
    x = np.arange(len(monthly_data_short))
    
    bars1 = ax3.bar(x - bar_width/2, monthly_data_short['transaction_amount_count'], 
                  bar_width, label='Transaction Count')
    ax3.set_ylabel('Number of Transactions', fontsize=12)
    ax3.set_title('Monthly Transaction Trends (Last 12 Months)', fontsize=14)
    
    ax3_twin = ax3.twinx()
    line = ax3_twin.plot(x, monthly_data_short['transaction_amount_mean'], 'ro-', linewidth=2, 
                      label='Avg Transaction Amount')
    ax3_twin.set_ylabel('Average Transaction Amount ($)', fontsize=12, color='r')
    ax3_twin.tick_params(axis='y', colors='r')
    
    ax3.set_xticks(x)
    ax3.set_xticklabels(monthly_data_short['month_year_str'], rotation=45)
    
    # Combine legends
    lines, labels = ax3.get_legend_handles_labels()
    lines2, labels2 = ax3_twin.get_legend_handles_labels()
    ax3.legend(lines + lines2, labels + labels2, loc='upper left')
    
    # Store location performance comparison
    ax4 = plt.subplot(gs[2, 0])
    sns.barplot(x='store_location', y='transaction_amount_mean', data=store_perf, palette='Blues_d', ax=ax4)
    ax4.set_title('Avg Transaction by Store', fontsize=14)
    ax4.set_xlabel('Store Location', fontsize=12)
    ax4.set_ylabel('Average Amount ($)', fontsize=12)
    
    # Customer return rate by store
    ax5 = plt.subplot(gs[2, 1])
    sns.barplot(x='store_location', y='return_customer_mean', data=store_perf, palette='Greens_d', ax=ax5)
    ax5.set_title('Return Customer Rate by Store', fontsize=14)
    ax5.set_xlabel('Store Location', fontsize=12)
    ax5.set_ylabel('Return Rate', fontsize=12)
    
    # Items purchased vs rating
    ax6 = plt.subplot(gs[2, 2])
    sns.regplot(x='items_purchased', y='customer_rating', data=df.sample(300), scatter_kws={'alpha':0.5}, ax=ax6)
    ax6.set_title('Items Purchased vs Customer Rating', fontsize=14)
    ax6.set_xlabel('Items Purchased', fontsize=12)
    ax6.set_ylabel('Customer Rating', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(f"{SAVE_DIR}/dashboard_visualization.png", dpi=300)
    plt.close()
    
    print("Visualizations created and saved to the 'data_analysis_results' directory.")


################################
# Part 4: Advanced Data Analysis #
################################

def perform_advanced_analysis(df):
    """
    Perform advanced analysis including customer segmentation, 
    predictive modeling, and time series analysis
    """
    print("\nPerforming advanced analysis...")
    
    # 1. Customer Segmentation using RFM (Recency, Frequency, Monetary) Analysis
    print("\n1. RFM Customer Segmentation:")
    
    # Get the current date (last date in the dataset + 1 day)
    current_date = df['date'].max() + pd.Timedelta(days=1)
    
    # Calculate RFM metrics
    rfm = df.groupby('customer_id').agg({
        'date': lambda x: (current_date - x.max()).days,  # Recency
        'transaction_amount': ['count', 'sum']  # Frequency, Monetary
    })
    rfm.columns = ['recency', 'frequency', 'monetary']
    
    # Create RFM segments
    rfm['r_quartile'] = pd.qcut(rfm['recency'], 4, labels=False, duplicates='drop')
    rfm['f_quartile'] = pd.qcut(rfm['frequency'], 4, labels=False, duplicates='drop')
    rfm['m_quartile'] = pd.qcut(rfm['monetary'], 4, labels=False, duplicates='drop')
    
    # Invert recency (lower is better)
    rfm['r_quartile'] = 3 - rfm['r_quartile']
    
    # Calculate RFM score
    rfm['rfm_score'] = rfm['r_quartile'] + rfm['f_quartile'] + rfm['m_quartile']
    
    # Create RFM segments
    segment_labels = ['Low-Value', 'Mid-Value', 'High-Value', 'Top Customers']
    rfm['customer_segment'] = pd.qcut(rfm['rfm_score'], 4, labels=segment_labels)
    
    # Print segment statistics
    segment_stats = rfm.groupby('customer_segment').agg({
        'recency': 'mean',
        'frequency': 'mean',
        'monetary': 'mean',
        'rfm_score': 'mean'
    }).round(2)
    print(segment_stats)
    
    # Customer distribution across segments
    segment_counts = rfm['customer_segment'].value_counts()
    print("\nCustomer Distribution across Segments:")
    print(segment_counts)
    
    # 2. Predictive Modeling: Transaction Amount Prediction
    print("\n2. Predictive Modeling - Transaction Amount Prediction:")
    
    # Prepare features and target
    model_data = df[['transaction_amount', 'items_purchased', 'customer_rating', 
                     'discount_applied_int', 'return_customer_int', 'is_weekend_int',
                     'days_since_first_purchase', 'store_location_encoded', 
                     'payment_method_encoded', 'month', 'day_of_week']]
    
    # Handle any remaining missing values
    model_data = model_data.dropna()
    
    # Split features and target
    X = model_data.drop('transaction_amount', axis=1)
    y = model_data['transaction_amount']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train models
    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.fit(X_train, y_train).predict(X_test)
    
    # Random Forest Regression
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    
    # Feature importance (from Random Forest)
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf_model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance.head(5))
    
    # Plot actual vs predicted values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, rf_pred, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
    plt.xlabel('Actual Transaction Amount')
    plt.ylabel('Predicted Transaction Amount')
    plt.title('Random Forest: Actual vs Predicted Transaction Amounts')
    plt.tight_layout()
    plt.show()
    
    return rf_model



my_df = generate_sample_data()
processed_df = preprocess_data(my_df)
correlation_matrix, customer_segments, monthly_trends, store_performance = explore_data(processed_df)
visuals_df = create_visualizations(processed_df, correlation_matrix, customer_segments, monthly_trends, store_performance)
analytics = perform_advanced_analysis(processed_df)

