# TN37DE1034,Livi,AA9920126787787,Two wheeler,2
def validate_license_number(vehicle_details):
    licence_no = vehicle_details.split(",")[2]
    if (len(licence_no) == 15 and licence_no.startswith("AA") and int(licence_no[2:4]) == 99 and
            1990 <= int(licence_no[4:8]) <= 2022 and licence_no[8:].isdigit()):
        return True
    else:
        return False


def generate_parking_id (vehicle_details):
    vehicle_no = vehicle_details.split(",")[0]
    customer_name = vehicle_details.split(",")[1]
    licence_no = vehicle_details.split(",")[2]
    vehicle_type = vehicle_details.split(",")[3]
    duration = int(vehicle_details.split(",")[4])
    amount = 0
    parking_id = ""
    if vehicle_type.lower() == "two wheeler":
        parking_id += "A"
        amount = float(duration * 20)
    if vehicle_type.lower() == "four wheeler":
        parking_id += "B"
        amount = float(duration * 30)
    digit = list(map(int, licence_no[-7:].strip()))
    parking_id += str(sum(digit))
    parking_id += customer_name[0]
    parking_dict = {"Name": customer_name, "Parking Id": parking_id, "Amount": amount}
    return parking_dict


def main():
    vehicle_details = input("Enter the Details:\n")
    val_licence_no = validate_license_number(vehicle_details)
    if val_licence_no:
        parking_details = generate_parking_id(vehicle_details)
        print(parking_details)
    else:
        print("Invalid input")
        return


main()