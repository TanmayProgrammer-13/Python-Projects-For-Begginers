#Importing Calender Module
import calendar
#Taking Data Of Year By User
Year = int(input("Enter The Year To Display Calender: "))
#Taking Data Of Month 
Month = int(input("Enter the Month: "))
print(calendar.month(Year,Month))
