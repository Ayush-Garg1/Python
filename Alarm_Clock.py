import os
import datetime
import time

d, mo, y = input("Enter date /'in format DD/MM/YYYY/' : ").split('/')
h, m, s = input("Enter Time /'in Format HH:MM:SS/' : ").split(":")
schedule = datetime.date(int(y), int(mo), int(d))
while True:
    if (time.localtime().tm_hour == int(h) and time.localtime().tm_min == int(m) and time.localtime().tm_sec == int(s)
            and datetime.date.today() == schedule):
        print("Wake Up Buddy....")
        break
