# Sales Aggregation Script

This project processes sales data from multiple CSV sources, aggregates it by store region and product category, and exports the results to an Excel file.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Required Libraries**:
  - Pandas: `pip install pandas`
  - Openpyxl: `pip install openpyxl`

## File Structure

Prepare the following CSV files in your project directory:

1. **sales.csv**
   ```csv
   transaction_date,sales_qty,product_code,store_code
   2024-01-01,120,P001,S001
   2024-01-02,85,P002,S002
   ...
