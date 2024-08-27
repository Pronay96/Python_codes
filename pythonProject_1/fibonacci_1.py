# WAP to find the number where the fibonacci series last value should be less than the number of elements
def fibonacci(number):

    a = 0
    b = 1
    fib_num = 0

    if number < 1:
        print("Invalid Input.")

    elif number == 1:
        print(a, end=' ')

    else:
        print(a, end=' ')
        print(b, end=' ')
        for i in range(2, number):
            fib_num = a + b
            a = b
            b = fib_num
            if fib_num <= number:
                print(fib_num, end=' ')


mon = int(input("Enter a value: "))

fibonacci(mon)
