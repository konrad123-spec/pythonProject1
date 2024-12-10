import pandas as pd

# pip install pandas
# pip install xlsxwriter

writer = pd.ExcelWriter('empty_file.xlsx', engine='xlsxwriter')

empty_dataframe = pd.DataFrame()

empty_dataframe.to_excel(writer,sheet_name='empty')
writer.close()

data = [["Aditya",179],
       ['Sameer',181],
       ['Darwin',178],
       ["Joel",167]]

column_names = ["Name", "Hight"]

df = pd.DataFrame(data, column_names)
writer = pd.ExcelWriter('data/excel_with_list.xlsx', engine='xlsxwriter')


