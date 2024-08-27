def factorial(num):

    fact = 1

    for i in range(num, 1, -1):
        fact = fact * i

    return fact


number = int(input("Enter a number: "))

print(f"The factorial is {factorial(number)}")