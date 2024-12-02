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
2. **product.csv**
3. **store.csv**

## Setup Instructions

Follow these steps to set up and run the Sales Aggregation Script:

### **Clone the Repository**
   Open your terminal or command prompt, then run:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository 
   ```

## Output
After execution, an Excel file named aggregated_sales.xlsx will be generated in the script directory.
This file contains two sheets:
Sales by Region
Sales by Product Category


## Output

After running the script, an Excel file named **`aggregated_sales.xlsx`** will be generated in the project directory. This file contains two sheets:

### 1. **Sales by Region**
   This sheet provides aggregated sales data grouped by store region.

### 2. **Sales by Product Category**
   This sheet provides aggregated sales data grouped by product category.

## File Structure
   - **aggregated_sales.xlsx**
     - **Sheet 1:** Sales by Region
     - **Sheet 2:** Sales by Product Category

