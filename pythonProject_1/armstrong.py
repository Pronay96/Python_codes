# Defination : Armstrong number is sum of all the digits in a number to the power of the length of the number
# Armstrong Number example:
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
# 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4
def armstrong(num):
    tmp = 0
    lst1 = [int(value) for value in str(num)]

    for lst_val in lst1:
        tmp = tmp+(lst_val ** len(lst1))

    print(f"The final result is {tmp}")
    if tmp == num:
        print(f"{tmp} is a Armstrong Number")
    else:
        print(f"{tmp} is not Armstrong Number")


number = int(input("Enter a number: "))

armstrong(number)