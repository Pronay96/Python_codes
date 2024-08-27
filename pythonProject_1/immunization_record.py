def create_record(children_record):
    list_rec_dict = []
    for details in children_record:
        name = details.split(':')[0]
        gender = details.split(':')[1]
        weeks = int(details.split(':')[2])
        contact = details.split(':')[3]
        if 1 <= weeks <= 24:
            dict_record = {"Name": name, "Gender": gender, "Weeks": weeks, "Contact": contact}
            list_rec_dict.append(dict_record)
    return list_rec_dict


def display_record(valid_records, weeks):
    cnt = 0
    for i in range(len(valid_records)):
        if valid_records[i]["Weeks"] <= weeks:
            print(f"\nRecord{i + 1} :")
            print(f"Name: {valid_records[i]["Name"]}")
            print(f"Gender: {valid_records[i]["Gender"]}")
            print(f"Weeks: {valid_records[i]["Weeks"]}")
            print(f"Contact: {valid_records[i]["Contact"]}")
            cnt += 1
    if cnt == 0:
        print(f"\nNo child under {weeks} weeks has booked for the vaccination")
    if cnt == 1:
        print(f"\nThere is 1 child under {weeks} weeks who have booked for the vaccination")
    if cnt > 1:
        print(f"\nThere are {cnt} children under {weeks} weeks who have booked for the vaccination")


def main():
    no_of_children = int(input("Enter the no of children:\n"))
    children_record = []
    print("Enter name, gender, weeks, and contact as colon-separated values:")
    for i in range(no_of_children):
        details = input()
        children_record.append(details)
    created_record_list = create_record(children_record)
    print(created_record_list)
    if created_record_list is not None and len(created_record_list) == 0:
        print("No records available")
    else:
        week = int(input("To display the records based on weeks since birth - Enter the no of weeks(<=24): "))
        display_record(created_record_list, week)


main()
