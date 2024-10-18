Here’s the code for the `README.md` file that you can paste directly into your GitHub repository:

```markdown
# Data Cleaning Project

This project is designed to clean datasets by identifying and removing duplicate entries, handling missing values, and saving cleaned versions of the dataset. The script works with both CSV and Excel file formats.

## Features
- Supports **CSV** and **Excel** (`.xlsx`) files.
- Identifies and removes duplicate records.
- Saves duplicate records in a separate file.
- Handles missing values:
  - Fills missing numeric values with the column mean.
  - Drops rows with missing non-numeric (object) values.
- Saves the cleaned dataset to a new file.

## Prerequisites
Before running the script, ensure that you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Pandas](https://pandas.pydata.org/) library (Install using `pip install pandas`)

## Installation
1. Clone this repository or download the script.
2. Install the required dependencies by running:
    ```bash
    pip install pandas
    ```

## How to Use
1. Place your dataset (`.csv` or `.xlsx`) in the same directory as the script, or provide the full path to the file.
2. Run the script using:
    ```bash
    python data_cleaning.py
    ```
3. You will be prompted to enter:
   - **Dataset path**: The file path to your dataset.
   - **Dataset name**: A name that will be used for saving the output files.

Example:

```bash
Please enter dataset path: sales.xlsx
Please enter dataset name: sales
```

4. The script will process the dataset:
   - If duplicate records are found, they will be saved to a file named `<data_name>_duplicates.csv`.
   - The cleaned dataset will be saved as `<data_name>_Cleaned_data.csv`.
   
   If you run the script multiple times, the existing duplicate and cleaned files will be replaced.

## Script Details

### Main Functionality
- **Duplicate Handling**: The script checks for duplicate rows and removes them. Duplicate records are saved to a separate CSV file.
- **Missing Value Handling**:
  - For numeric columns, missing values are replaced with the column's mean.
  - For non-numeric columns, rows with missing values are dropped.

### Example Output
- After running the script on a dataset named `sales.xlsx`, you will get:
  - `sales_duplicates.csv` (if duplicates exist).
  - `sales_Cleaned_data.csv` (the cleaned dataset).

### File Overwriting
If files with the same name already exist (e.g., `sales_duplicates.csv` or `sales_Cleaned_data.csv`), the script will automatically remove them before saving new files to avoid duplicates.

## Example Files

### Input File: `sales.xlsx`
```
| OrderID | Product | Quantity | Price |
|---------|---------|----------|-------|
| 1       | A       | 10       | 100   |
| 2       | B       | 5        | 50    |
| 1       | A       | 10       | 100   |
| 3       | C       | 2        | 30    |
```

### Output Files:
1. **Duplicates File**: `sales_duplicates.csv`
    ```
    | OrderID | Product | Quantity | Price |
    |---------|---------|----------|-------|
    | 1       | A       | 10       | 100   |
    ```

2. **Cleaned Dataset**: `sales_Cleaned_data.csv`
    ```
    | OrderID | Product | Quantity | Price |
    |---------|---------|----------|-------|
    | 1       | A       | 10       | 100   |
    | 2       | B       | 5        | 50    |
    | 3       | C       | 2        | 30    |
    ```

## Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.
```
