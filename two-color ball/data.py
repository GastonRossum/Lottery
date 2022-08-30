# 常用功能
import xlrd
import numpy as np
import pandas as pd
from collections import Counter
# 打开实验数据表格
book = xlrd.open_workbook(r'/Daily/Lottery/data/alll.xls')
# 选择页数为第1页
sheet1 = book.sheets()[0]

# # 数据总行数
# nrows = sheet1.nrows
# print('数据总行数：', nrows)
#
# # 数据总列数
# ncols = sheet1.ncols
# print('表格总列数：', ncols)

# # 获取表中第三行的数据
# x = sheet1.row_values(2)
# print('第3行: ', x)

# 获取表中第二列的数据
y = sheet1.col_values(8)
y = np.array(y).astype(dtype=int).tolist()  #
# y.dtype = 'int8'
result = pd.value_counts(y).sort_index()
d2 = Counter(y)
sorted_x = sorted(d2.items(), key=lambda x: x[1], reverse=True) # 将元素出现次数进行排序
print('红球1：', y)
print(sorted_x)
# print(result)

# # 获取表中第二列且不要第一个值的数据
# y_noone = sheet1.col_values(1)[1:]
# print('第二列且不要第一个值： ', y_noone)
# # 获取第3行第3列的单元格的数据
# x_3_y_3 = sheet1.cell(2, 2).value
# print('第3行第3列的单元格的值：', x_3_y_3)

