from Common import *

book = excel.Workbook()

sheet = book.active

sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

sheet['A2'] = 1
sheet['B2'] = 2

book.save('Excel1.xlsx')