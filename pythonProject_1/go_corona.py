def vaccine():

    while True:
        tot_people = int(input("Enter the total no.of people in the ares: "))

        if tot_people <= 0:
            print("Invalid Input")
            return

        single_dose = int(input("Single-dose count: "))

        if single_dose <= 0 or single_dose > tot_people:
            print("Invalid Input")
            return

        double_dose = int(input("Double-dose count: "))

        if double_dose <= 0 or double_dose > tot_people:
            print("Invalid Input")
            return

        if (double_dose+single_dose) > 0:
            print("Invalid Input")
            return

        non_vac = tot_people - (single_dose + double_dose)

        print(f"Non vaccinated people count: {non_vac}")

        vac_percnt = (double_dose / tot_people) * 100

        print(f"Total vaccinated percentage of people: {vac_percnt:.2f}")

        check = int(input("Do you want to continue (1) for yes (0) for no: "))

        if check != 0 or check != 1:
            print("Invalid Input")
            return

        elif check == 0:
            return

        else:
            continue

vaccine()