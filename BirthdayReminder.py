# Reading an excel file using Python
import xlrd
import datetime

## This program is created for sending Birthday reminders

# Give the location of the file

loc = ("E:\AKANKSHA\Edyoda - Python\Python programs\BirthdayReminder.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)

# reading the first sheet of workbook
sheet = wb.sheet_by_index(0)

i = 0
# To read the all rows row

def checkBirthday(date) :
        date = str(date).replace("\"","").split("-",2)
        return date

while(i < 7) :
        rowsVal = sheet.row_values(i)
        date = checkBirthday(rowsVal[1])
        # print(date[1:2])
        today_month = "0" + str(datetime.date.today().month)
        today_day = ""+str(datetime.date.today().day)
        birthday_day = date[0:1]
        birthday_month = date[0:2]
        if (birthday_month.__contains__(today_month) and birthday_day.__contains__(today_day)):
                print("happy birthday ---> "+rowsVal[0])
        i = i + 1


