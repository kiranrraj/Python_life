from openpyxl import load_workbook

wb = load_workbook(filename='sample.xlsx')
sheet = wb['PI']
print(sheet['F5'].value)