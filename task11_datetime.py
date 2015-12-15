import sys
import datetime

date = sys.argv[1]
str_dates = date.split('-')
year = int(str_dates[0])
mm = int(str_dates[1])
dd = int(str_dates[2])
date_input = datetime.datetime(year, mm, dd)
date_now = datetime.datetime.now()
timedelta = date_now - date_input
tmdl_hours = timedelta.seconds / 3600
tmdl_min = (timedelta.seconds - tmdl_hours * 3600 ) / 60
tmdl_sec = (timedelta.seconds - tmdl_hours * 3600 - tmdl_min * 60 ) % 60
print("The time delta from {} untill now is {} days, {} hours, {} minutess, {} seconds".format(date, timedelta.days, tmdl_hours, tmdl_min, tmdl_sec))



