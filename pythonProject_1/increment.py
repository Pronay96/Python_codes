def main():
    #Input no.of employees
    t_num = int(input("Total no of employees: "))
    if t_num <= 0:
        print("Invalid number")
        return

    for i in range (t_num):
        # Input employee details/increament/count
        emp_name = input("Employee name:")
        sal = float(input("Salary:"))
        if sal <= 0:
            print("Invalid salary")
            return

        deg = input("Designation:")

        if (deg == 'Service Advisor'):
            sa = (sal * 0.2) + sal
            print(f"After the increment,{emp_name}'s salary is $ {sa}")
        elif (deg == 'Supervisor'):
            sa = (sal * 0.15) + sal
            print(f"After the increment,{emp_name}'s salary is $ {sa}")
        elif (deg == 'Mechanic'):
            sa = (sal * 0.10) + sal
            print(f"After the increment,{emp_name}'s salary is $ {sa}")
        else:
            sa = (sal * 0.07) + sal
            print(f"After the increment,{emp_name}'s salary is $ {sa}")

        cnt_great = 0
        cnt_less = 0
        if sa > 50000:
            cnt_great += 1

    #Printing counts
    print(f"Employee count:{t_num}")
    print(f"Salary above 50000:{cnt_great}")
    print(f"Salary below or equal to 50000:{t_num-cnt_great}")


main()