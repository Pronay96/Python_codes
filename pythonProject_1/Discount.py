def calculate_discount(input_string):
    hh_num = input_string.split(':')[0]  # it will not be in a list
    hh_type = input_string.split(':')[1]

    # Sum of house numbers (123= 1+2+3)
    sum1 = 0
    for i in range(len(hh_num)):
        m = int(hh_num[i])  # it will convert value at index i to int
        sum1 += m

    cost_dis = None
    if hh_type == '2BHK':
        if sum1 % 2 == 0:
            cost_dis = 3700000 * 0.05

        else:
            cost_dis = 3900000 * 0.04

    final = cost_dis

    if hh_type == '3BHK':
        if sum1 % 2 == 0:
            cost_dis = 4900000 * 0.07

        else:
            cost_dis = 5100000 * 0.08

    final = cost_dis

    return final


def main():
    detail = input("Enter the details:\n")
    cd = calculate_discount(detail)
    print(cd)


if __name__ == '__main__':
    main()
