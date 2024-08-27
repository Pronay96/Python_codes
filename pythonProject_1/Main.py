def calculate_bill(units):
    if units < 0:
        print("Invalid Unit")
        return

    total_bill = 0

    # First 50 units
    if units <= 50:
        total_bill += units * 0.50
    else:
        total_bill += 50 * 0.50
        units -= 50

        # Next 100 units
        if units <= 100:
            total_bill += units * 0.75
        else:
            total_bill += 100 * 0.75
            units -= 100

            # Next 100 units
            if units <= 100:
                total_bill += units * 1.20
            else:
                total_bill += 100 * 1.20
                units -= 100

                # Units above 250
                total_bill += units * 1.50

    # Adding surcharge of 20%
    total_bill += total_bill * 0.20

    print(f"Total electricity bill for {units} units is Rs. {total_bill:.2f}")

# Main program
units_consumed = int(input("Enter the total units consumed: "))
calculate_bill(units_consumed)