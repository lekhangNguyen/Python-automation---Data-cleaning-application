# Data Cleaning Project

This Python project performs data cleaning on CSV and Excel files by handling missing values, removing duplicate records, and saving the cleaned data to a new file. The script also checks and removes any duplicate files generated during multiple runs of the program.

## Features

- Supports `.csv` and `.xlsx` file formats.
- Handles missing values by:
  - Filling missing numeric values with the mean.
  - Dropping rows with missing non-numeric values.
- Identifies and removes duplicate rows.
- Saves duplicate records and the cleaned dataset as separate `.csv` files.
- Removes previously generated duplicate and cleaned files before saving new ones to avoid file duplication.

## Prerequisites

Before running this project, you need to install the following Python packages:

- **pandas**: For handling and manipulating data.
- **os**: A built-in module for interacting with the file system.
- **openpyxlsx**: To read and write Excel files.
  You can install `pandas` via `pip`:

```bash
pip install pandas
pip install openpyxl
```

## Usage

1. Clone or download the repository.
2. Ensure you have installed the necessary dependencies (see Prerequisites).
3. Place your dataset in the same folder as the script or provide the correct path to it.

### Running the Script

Run the script using Python:

```bash
python data_cleaning.py
```

The script will prompt you to provide:

- The file path of the dataset.
- A name for the dataset (this will be used in naming the output files).

Example input:

```
Please enter dataset path: sales.xlsx
Please enter dataset name: sales
```

### Output Files

The script generates the following files:

- **sales_duplicates.csv**: Contains the duplicate rows from the dataset.
- **sales_Cleaned_data.csv**: Contains the cleaned dataset with duplicates removed and missing values handled.

If you run the script multiple times, it will automatically delete any previously generated files to prevent duplication.

### Example Code

Below is a simplified version of the code:

```python
# import dependencies
import pandas as pd
import os

# Function to check if a file already exists and remove it
def remove_existing_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Existing file '{file_name}' removed.")

# Main function
def data_cleaning(data_path, data_name):
    # Checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path!")
        return
    else:
        # Checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data = pd.read_csv(data_path, encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file!')
            data = pd.read_excel(data_path)
        else:
            print('Unknown type!')
            return

    # Showing number of records
    print(f'DATASET CONTAINS:\n{data.shape[0]} ROWS\n{data.shape[1]} COLUMNS\n')

    # Cleaning process

    # Checking duplicate
    duplicates = data.duplicated()
    total_duplicate = data.duplicated().sum()

    print(f'DATASET TOTAL DUPLICATE RECORDS:\n{total_duplicate}\n')

    # Saving the duplicates (only create files when there's a duplicate value)
    if total_duplicate > 0:
        duplicate_file_name = f'{data_name}_duplicates.csv'
        # Remove existing duplicate file
        remove_existing_file(duplicate_file_name)
        # Save new duplicates file
        duplicate_record = data[duplicates]
        duplicate_record.to_csv(duplicate_file_name, index=None)
        print(f"Duplicate records saved to '{duplicate_file_name}'")

    # Deleting duplicates
    df = data.drop_duplicates()

    # Find missing values
    total_missing_value = df.isnull().sum().sum()  # Total missing values
    missing_value_column = df.isnull().sum()  # Total missing values in each column

    print(f'DATASET HAS TOTAL:\n{total_missing_value} missing values\n')
    print(f'DATASET CONTAINS MISSING VALUE BY COLUMNS\n{missing_value_column}')

    # Dealing with missing values
    columns = df.columns
    for col in columns:
        # Filling mean for numeric columns
        if df[col].dtype in (int, float):
            df[col] = df[col].fillna(df[col].mean())
        else:
            # Dropping rows with missing non-numeric columns
            df.dropna(subset=[col], inplace=True)

    print(f'DATASET IS CLEANED!\nNumber of Rows: {df.shape[0]}\nNumber of Columns: {df.shape[1]}')

    # Saving the cleaned dataset
    cleaned_file_name = f'{data_name}_Cleaned_data.csv'
    # Remove existing cleaned file
    remove_existing_file(cleaned_file_name)
    # Save new cleaned dataset
    df.to_csv(cleaned_file_name, index=None)
    print(f"Cleaned dataset saved to '{cleaned_file_name}'")

if __name__ == "__main__":
    data_path = input("Please enter dataset path: ")
    data_name = input("Please enter dataset name: ")

    # Calling the function
    data_cleaning(data_path, data_name)
```

### Notes

- Ensure your dataset file path and name are correct when prompted by the script.
- If there are no duplicates or missing values, the respective sections will not generate files.
- The script is designed to handle only `.csv` and `.xlsx` files; other formats will result in an error message.

### License

This project is licensed under the MIT License

### Instructions:

- Replace the project name and description to reflect the specific purpose of your project.
- Add a license section if necessary, or customize it based on your needs.
