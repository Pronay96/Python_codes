def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not Leap Year"


def month_name(no):
    mon_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                'November', 'December']

    if 1 <= no <= 12:
        return mon_name[no - 1]
    else:
        return "Invalid Month"


def day_in_month(month, year):
    dict_leap = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    dict_non_leap = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                     'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

    leap = is_leap(year)
    if leap == "Leap Year":
        return dict_leap.get(month)
    else:
        return dict_non_leap.get(month)
