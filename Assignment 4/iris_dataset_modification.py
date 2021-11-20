from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

rb = open_workbook(r"./iris_dataset.xlsx")
wb = copy(rb)
s = wb.get_sheet(0)
class_label = 1
for row in range(0, 150):
    if row > 49:
        class_label = 2
    if row > 99:
        class_label = 3

    s.write(row, 4, class_label)

wb.save("modified_iris_dataset.xls")