#import the xlrd module
import xlrd

#Open the spreadsheet file (or workbook)
workbook = xlrd.open_workbook("Book1.xlsx")

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
