import time;
import datetime
import calendar
ticks = time.time()
now = datetime.datetime.now()

# print("Number of ticks since 12:00am, Jan 1,1970: ",ticks,end="\n")
# cal = calendar.month(now.year, now.month)
# print ("Here is the calendar:",end="\n")
# print (cal)

date = input('Wanna see calendar? type a date on this format: dd/mm/yyyy: ')
date = date.split("/")
day   = int(date[0])
month = int(date[1])
year  = int(date[2])
print ("Here is the calendar:",end="\n")
print (calendar.month(year,month))
