import pandas as pd
from pandas import ExcelWriter

height_data = [
    {"Name": "Aditya", "Height": 179},
    {"Name": "Saneer", "Height": 179},
    {"Name": "Daarwin", "Height": 179},
    {"Name": "Aditya", "Height": 179}
]

weight_data = [
    {"Name": "Aditya", "Weight": 70},
    {"Name": "Saneer", "Weight": 80},
    {"Name": "Daarwin", "Weight": 60},
    {"Name": "Aditya", "Weight": 50}
]

marks_data = [
    {"Name": "Aditya", "marks": 179},
    {"Name": "Saneer", "marks": 179},
    {"Name": "Daarwin", "marks": 179},
    {"Name": "Aditya", "marks": 179}
]

height_data_df = pd.DataFrame(height_data)
weight_data_df = pd.DataFrame(weight_data)
marks_data_df = pd.DataFrame(marks_data)
writer = ExcelWriter('data/excel_with_multiple_sheets.xlsx', engine='xlsxwriter')

height_data_df.to_excel(writer,sheet_name='height', index=False)
weight_data_df.to_excel(writer,sheet_name='weight', index=False)
marks_data_df.to_excel(writer,sheet_name='marks', index=False)
writer.close()





