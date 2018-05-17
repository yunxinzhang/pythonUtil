#pip install xlrd
import xlrd
book = xlrd.open_workbook('test.xlsx')# 打开xls文件
sheet = book.sheet_by_name('Sheet1')
rows = sheet.nrows #获取行数
cols = sheet.ncols #获取列数
# for c in range(cols): #读取每一列的数据
# 	c_values = sheet.col_values(c)
# 	print(c_values)
for r in range(rows): #读取每一行的数据
	r_values = sheet.row_values(r)
	print(r_values[1])
	with open(str(r),"w") as fw:
		fw.write(r_values[1])
print(sheet.cell(1,1)) #读取指定单元格的数据