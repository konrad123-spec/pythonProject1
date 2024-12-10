import pandas as pd

data = [
    {"Name": "Aditya", "Height": 179},
    {"Name": "Saneer", "Height": 179},
    {"Name": "Daarwin", "Height": 179},
    {"Name": "Aditya", "Height": 179}
]

df = pd.DataFrame(data)

print(df)

writer = pd.ExcelWriter('excel_with_dict.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='first_sheet', index=False)
writer.close()
