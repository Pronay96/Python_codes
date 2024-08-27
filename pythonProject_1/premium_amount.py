# Write other functions here
def validate_customer_id(cust_list):
    list1 = []
    for x in cust_list:
        customer_id = x[1]
        if len(customer_id) == 7 and customer_id.startswith("INS") and customer_id[3] == "-" and customer_id[
                                                                                                 4:].isdigit():
            list1.append(list(x))
    return list1


def calculate_total_amount(val_cust_list, veh_type):
    total_prem = 0
    dict1 = {}
    l1, l2 = [], []
    list1 = []
    for value in val_cust_list:
        value1 = value[3]
        if value1 == veh_type:
            veh_no = value[2]
            prem_amt = value[4]
            total_prem = total_prem + int(prem_amt)
            l1.append(veh_no)
            l2.append(prem_amt)
    dict1 = {l1[i]: l2[i] for i in range(len(l1))}
    list1.append(dict1)
    list1.append(total_prem)

    return list1


def main():
    customer_list = []
    customer_count = int(input("No of customers:"))
    tup = ()
    for i in range(customer_count):
        tup = ()
        customer_name, customer_id, vehicle_number, vehicle_type, premium_amount = input().split(',')
        tup = tup + (customer_name, customer_id, vehicle_number, vehicle_type, premium_amount)
        customer_list.append(tup)
    valid_customer_list = validate_customer_id(customer_list)
    if valid_customer_list is not None and len(valid_customer_list) == 0:
        print("No valid customer details found")
    else:
        for x in valid_customer_list:
            print(x)
        vehicle_type = input("Enter the vehicle type:")

        vehicle_dict = calculate_total_amount(valid_customer_list, vehicle_type)
        if vehicle_dict is not None:
            if len(vehicle_dict[0]) != 0:
                print("vehicle No. Amount")
                for key, val in vehicle_dict[0].items():
                    print(key, val)
                print("Total amount", vehicle_dict[1])
            else:
                print("No vehicle found")
    return


if __name__ == '__main__':
    main()
