import math
import os
import random
import re
import sys
import time
import datetime


def dateandtime(val, tup):
    lst = []
    if val == 1:
        date_tuple = datetime.date(*tup)
        lst.append(date_tuple)
        formated_date = date_tuple.strftime("%d/%m/%Y")
        lst.append(formated_date)

    if val == 2:
        date1 = datetime.date.fromtimestamp(*tup)
        lst.append(date1)

    if val == 3:
        date3 = datetime.time(*tup)
        lst.append(date3)
        time = datetime.time.strftime(date3, "%I")
        lst.append(time)

    if val == 4:
        date_tuple1 = datetime.date(*tup)
        weekday = datetime.date.weekday(date_tuple1)
        print(weekday)
        if weekday == 0:
            lst.append("Monday")
        elif weekday == 1:
            lst.append("Tuesday")
        elif weekday == 2:
            lst.append("Wednesday")
        elif weekday == 3:
            lst.append("Thursday")
        elif weekday == 4:
            lst.append("Friday")
        elif weekday == 5:
            lst.append("Saturday")
        else:
            lst.append("Sunday")

        month_name = date_tuple1.strftime('%B')
        lst.append(month_name)

        day_of_year = date_tuple1.timetuple().tm_yday
        lst.append(day_of_year)

    if val == 5:
        date_obj = datetime.datetime(*tup)
        lst.append(date_obj)

    return lst


if __name__ == '__main__':
    val = int(input().strip())

    if val == 1 or val == 4 or val == 3:
        qw1_count = 3
    if val == 2:
        qw1_count = 1
    if val == 5:
        qw1_count = 6
    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    tup = tuple(qw1)

    ans = dateandtime(val, tup)

    print(ans)
