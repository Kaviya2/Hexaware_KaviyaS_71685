#Time and Date

import datetime
mytime = datetime.datetime.now()
print(mytime)#current time
print(mytime.hour)#current hour
print(mytime.minute)#min
print(mytime.second)#sec


import calendar
cale=calendar.month(2022,5)#mentioned month calendar
print(cale)
print("=====")
print(calendar.prcal(2022))#whole year calendar
