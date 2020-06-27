#wapp to wish the user gm/ga/ge
#along with date also display the date and ttime

import datetime
dt = datetime.datetime.now()
date=dt.date()
print("date =",date)
time=dt.time()
print("time =",time)
hour=dt.hour

#for 12 hour
s1=time.strftime('%I:%M:%S %p')
print(s1)



if hour >=6 and hour<12:
    print("good morning")
elif hour>=12 and hour<17:
    print("good afternoon")
else:
    print("good evening")
