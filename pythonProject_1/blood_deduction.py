def create_list(factors):
    list1 = factors.split(",")
    return list1


def deduce_blood_group(blood_details):
    # 0=A-antigen 2=anti-A antibody
    # 1=B-antigen 3=anti-B antibody
    # Incorrect combo
    blood_type = ""
    if blood_details[0] == 'y' and blood_details[2] == 'y':
        return False
    if blood_details[1] == 'y' and blood_details[3] == 'y':
        return False
    # A group combo
    if blood_details[0] == 'y' and blood_details[3] == 'y':
        if blood_details[4] == '+':
            blood_type = 'A+'
        elif blood_details[4] == '-':
            blood_type = 'A-'
    # B group combo
    if blood_details[1] == 'y' and blood_details[2] == 'y':
        if blood_details[4] == '+':
            blood_type = 'B+'
        elif blood_details[4] == '-':
            blood_type = 'B-'
    # AB group combo
    if blood_details[0] == 'y' and blood_details[1] == 'y':
        if blood_details[4] == '+':
            blood_type = 'AB+'
        elif blood_details[4] == '-':
            blood_type = 'AB-'
    # O group combo
    if blood_details[2] == 'y' and blood_details[3] == 'y':
        if blood_details[4] == '+':
            blood_type = 'O+'
        elif blood_details[4] == '-':
            blood_type = 'O-'
    return blood_type


def main():
    patient_inp = input("Enter y/n for A antigens, y/n for B antigens, y/n for anti-A antibodies, y/n for anti-B "
                        "antibodies, and +/- for Rh factor (as comma separated values):")
    blood_list = create_list(patient_inp)
    blood_group = deduce_blood_group(blood_list)
    if blood_group:
        print(f"Deduced blood group: {blood_group}")
    else:
        print("Incorrect combination of antigens/antibodies entry")

main()
