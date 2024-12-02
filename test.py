import pandas as pd

# Data Retrieval
def load_csv(file_path):
    return pd.read_csv(file_path)

# Data Processing
def filter_data(df, region=None, category=None):
    if region:
        df = df[df['store_region'] == region]
    if category:
        df = df[df['product_category'] == category]
    return df

# Sales Aggregation
def aggregate_sales(sales_df, product_df, store_df):
    # Merge data from multiple sources
    merged_df = sales_df.merge(product_df, on='product_code').merge(store_df, on='store_code')
    
    # Add calculated columns
    merged_df['sales_amount'] = merged_df['sales_qty'] * merged_df['price']
    merged_df['sales_cost'] = merged_df['sales_qty'] * merged_df['cost']
    merged_df['profit'] = merged_df['sales_amount'] - merged_df['sales_cost']
    
    # Aggregate by store region
    by_region = merged_df.groupby('store_region').agg({
        'sales_qty': 'sum',
        'sales_amount': 'sum',
        'sales_cost': 'sum',
        'profit': 'sum'
    }).reset_index()
    
    # Aggregate by product category
    by_category = merged_df.groupby('product_category').agg({
        'sales_qty': 'sum',
        'sales_amount': 'sum',
        'sales_cost': 'sum',
        'profit': 'sum'
    }).reset_index()
    
    return by_region, by_category

# Export aggregated data to Excel
def export_to_excel(by_region, by_category, output_file):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        by_region.to_excel(writer, sheet_name='Sales by Region', index=False)
        by_category.to_excel(writer, sheet_name='Sales by Category', index=False)

# Main Execution
def main():
    sales_file = 'sales.csv'
    product_file = 'product.csv'
    store_file = 'store.csv'
    
    sales_df = load_csv(sales_file)
    product_df = load_csv(product_file)
    store_df = load_csv(store_file)
    
    # Aggregate and export
    region_agg, category_agg = aggregate_sales(sales_df, product_df, store_df)
    export_to_excel(region_agg, category_agg, 'aggregated_sales.xlsx')

if __name__ == "__main__":
    main()
