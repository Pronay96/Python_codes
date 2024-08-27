def calculate_days(from_date, to_date):
    day_cnt = 0
    from_day = int(from_date.split("/")[0])
    from_month = int(from_date.split("/")[1])
    to_day = int(to_date.split("/")[0])
    to_month = int(to_date.split("/")[1])
    if from_month == to_month:
        day_cnt = to_day - from_day
    else:
        month_cnt = to_month - from_month
        day_cnt = (to_day - from_day) + (month_cnt * 30)
    return day_cnt


def calculate_total_amount(customer_name, room_type, no_of_days):
    total_amount, single, double, triple = 0, 3300, 4000, 4500
    if room_type == "Single":
        if no_of_days <= 3:
            total_amount = single - (single * 0.1)
        else:
            total_amount = single - (single * 0.15)
    if room_type == "Double":
        if no_of_days <= 3:
            total_amount = double - (double * 0.1)
        else:
            total_amount = double - (double * 0.17)
    if room_type == "Triple":
        if no_of_days <= 3:
            total_amount = triple - (triple * 0.1)
        else:
            total_amount = triple - (triple * 0.2)
    dict_hotel = {"Customer Name": customer_name, "No of days": no_of_days, "Total amount": total_amount}
    return dict_hotel


def main():
    info = input("Information:\n")
    room_no = info.split(":")[0]
    customer_name = info.split(":")[1]
    room_type = info.split(":")[2]
    from_date = info.split(":")[3]
    to_date = info.split(":")[4]
    day_count = calculate_days(from_date, to_date)
    print(f"No of Days from calculate_days function: {day_count}")
    output = calculate_total_amount(customer_name, room_type, day_count)
    for key, value in output.items():
        print(f"{key}: {value}")


main()
