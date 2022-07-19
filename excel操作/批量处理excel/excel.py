import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

df1 = pd.read_excel('/Users/nw/Desktop/自动化办公代码/excel操作/批量处理excel/fin_data.xlsx', sheet_name=0, converters={'年':str,'公司':str})

df1.groupby('公司',as_index=False).apply(print)

wb = openpyxl.Workbook()

def writesheet(group):
    data = group.reset_index(drop=True)
    ws = wb.create_sheet(title=data.loc[0,'公司'])
    for r in dataframe_to_rows(data, index=False,header=True):
        ws.append(r)

df1.groupby('公司',as_index=False).apply(writesheet)

wb.save('整理结果.xlsx')

def writesheet(group):
    data = group.reset_index(drop=True)
    data.to_excel('整理文件'+data.loc[0,'公司']+'.xlsx',index=False)

df1.groupby('公司',as_index=False).apply(writesheet)

