# import dependencies
import pandas as pd
import numpy as np
import time
import os
import xlrd
import random
import openpyxl
data_path = 'sales.xlsx'
data_name = ''

#checking if the path exists
if not os.path.exists(data_path):
    print("Incorrect path!")
    #return
else:
    #checking the file type
    if data_path.endswith('.csv'):
        print('Dataset is csv!')
        #ignore errors if any rows have problem
        data = pd.read_csv(data_path,encording_errors ='ignore' )

    elif data_path.endswith('.xlsx'):
        print('Dataset is excel file!')
        data = pd.read_excel(data_path)
            
    else:
        print('Unknown type!')
        #return

#showing number of records
print(f'DATASET CONTAINS:\n{data.shape[0]} ROWS\n{data.shape[1]} COLUMNS\n')

#cleaning

#checking duplicate
duplicates = data.duplicated()
total_duplicate = data.duplicated().sum()

print(f'DATASET TOTAL MISSING VALUES:\n{total_duplicate}\n')

#saving the duplicates (only create files when theres duplicate value)
if total_duplicate > 0:
    duplicate_record= data[duplicates]
    duplicate_record.to_csv(f'{data_name}_duplicates.csv', index=None)

#deleting duplicates
df = data.drop_duplicates()

#find missing values
total_missing_value = df.isnull().sum().sum() #total missing values
missing_value_column = df.isnull().sum() #total missing values in each columns

print(f'DATASET HAS TOTAL:\n{total_missing_value} missing values\n')
print(f'DATASET CONTAINS MISSING VALUE BY COLUMNS\n{missing_value_column}')

#dealing with missing 
#fillna for int and float
#dropna for any object
columns = df.columns
for col in columns:
    #filling mean for numeric columns all rows
    if df[col].dtype in (int, float):
        df[col] = df[col].fillna(df[col].mean())
        print(f'')
    else:
        #dropping all the rows with missing nonnumber col
        df.dropna(subset=col, inplace=True)

print(f'DATA SET IS CLEANED!\nNumber of Rows:{df.shape[0]}\nNumber of Columns:{df.shape[1]}')