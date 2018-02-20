#import the xlrd module
import xlrd
import xlwt

#Open the spreadsheet file (or workbook)
workbook = xlrd.open_workbook("Book1.xlsx")

print("workbook nsheets : {0}".format(workbook.nsheets))
print("workbook sheet names : ", workbook.sheet_names())

first_sheet=workbook.sheet_by_index(0)
print("row values : ", first_sheet.row_values(0))
cell=first_sheet.cell(4,1)
print("Cell(4,1) : ", cell)

print("==> col values : ", first_sheet.col_values(0))

# To write to excel
print("** xlwt import ")
workbook2 =  xlwt.Workbook(encoding = "utf-8")
sheet1=workbook2.add_sheet("Python Sheet1")
sheet2=workbook2.add_sheet("Python Sheet2")
sheet3=workbook2.add_sheet("Python Sheet3")

sheet1.write(0,0, "This is Sheet 1")
sheet2.write(10,0, "This is Sheet 2")
sheet3.write(0,10, "This is Sheet 3")

workbook2.save("Pythonspreadsheet1.xlsx")
print("Workbook2 created <Pythonspreadsheet1.xlsx")


#Open a sheet:
#if you know the name of the sheet, you can open it by running the following:
worksheet = workbook.sheet_by_name("Users")

#if you are not sure of the name of the sheet,
# you can open the first worksheet by it's index as follows:
worksheet = workbook.sheet_by_index(0)

#once you have selected the worksheet,
#you can extract the value of a particular data cell as follows:
print("the value at row 4 and column 2 is : {0}".format(worksheet.cell(4,2).value))

#if you want to know the number of sheets,
#use the property nsheets on the workbook object:
sheet_count = workbook.nsheets
print("the total number of sheets : {0}".format(sheet_count))

#if you wan to have a list of the names of the sheets present in the file,
#use the function sheet_names() on the workbook object
sheets_name = workbook.sheet_names()
print("sheet names: {0}".format(sheets_name))

#to find the total number of rows and columns in the sheet use the property nrows and ncols with
#the sheet object
total_rows = worksheet.nrows
total_cols = worksheet.ncols
print("number of rows : {0}, and number of columns : {0}".format(total_rows,total_cols))

#final tip:
#let's loop in every record in the worksheet and store them in a list then display the final list:
table = list()
record = list()
for x in range(total_rows):
    for y in range(total_cols):
        record.append(worksheet.cell(x,y).value)
    table.append(record)
    record = []
    x +=1
print("Printing table : \n", table)

