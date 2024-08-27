def fibonacci(number):
    if number < 1 or number > 12:
        print("Invalid Month")
        return

    prev1 = 0
    prev2 = 1
    fib_num = 0

    for x in range(1, number+1):
        if x > 2:
            fib_num = prev1+prev2
            prev1 = prev2
            prev2 = fib_num
            print(fib_num, end=" ")
        if x == 2:
            fib_num = prev2
            print(fib_num, end=" ")
        if x == 1:
            fib_num = prev1
            print(fib_num, end=" ")

    print("")
    print(f"The amoeba size is {fib_num}")

mon = int(input("Enter the month as numeric value: "))

fibonacci(mon)