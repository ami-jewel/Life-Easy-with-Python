Here is a excel dataset "RK-Courier-"<br>
We need to modify few of it's column value.

## Work procedure as below:
### 1. Remove hyphens from Mob column (01716-009099)
### 2. Add '88' before each mobile number, ensuring no duplicate '88' if already present (8801716009099)
### 3. Format the 'cdate' column to d-m-yy (24-06-2024)
### 4. Add a new column 'product_type'and fill-up with the value 'trade_license'
### 5. Finally save to new Excel file.

## GUI interface using TKinter
Tkinter is the most commonly used library for developing GUI.<br>
We use it for choose any type of file from the system/PC

## Install important library
from tkinter import Tk
from tkinter.filedialog import askopenfilename

## Finaly save the file to new Excel file
output_path = 'RK-Courier-25.06.2025_Modified.xlsx'
df.to_excel(output_path, index=False)
