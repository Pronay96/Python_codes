def is_ugly(number_list):
    number_list = map(int, number_list)
    count = 0
    for num in number_list:
        if num <= 0:
            print("Invalid Input")
        temp = num
        for fctr in [2, 3, 5]:
            while temp % fctr == 0:
                temp = temp//fctr
        if temp == 1:
            print(num)
            count += 1
    if count == 0:
        print("No ugly numbers found")


def main():
    ugly_numb = input("Enter the numbers (as comma-separated values): ")
    # numb_list = list(map(int, ugly_numb.split(",")))
    numb_list = ugly_numb.split(",")
    is_ugly(numb_list)


main()