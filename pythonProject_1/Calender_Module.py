import math
import os
import random
import re
import sys
import calendar
import datetime


def usingcalendar(datetuple):
    year, month, date = datetuple

    if calendar.isleap(year):
        month = 2

    # Printing the calender
    print(calendar.month(year, month))

    # Printing 7 days from the last week
    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    month_dates = list(cal.itermonthdates(year, month))
    last_monday_ind = max(i for i, d in enumerate(month_dates) if d.weekday() == 0)
    last_week = month_dates[last_monday_ind: last_monday_ind + 7]
    print(last_week)

    # Printing the frequent day
    day = datetime.datetime(year, month, 1)
    starting_day = day.strftime('%A')
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    count = [4 for i in range(0, 7)]
    pos = -1
    for i in range(0, 7):
        if starting_day == days[i]:
            pos = i
            break
    print(days[pos])


if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    tup = tuple(qw1)

    usingcalendar(tup)
