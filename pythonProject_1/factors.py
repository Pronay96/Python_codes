def factors(num):
    lst1 = []
    for i in range(1, num+1):
        if num % i == 0:
            lst1.append(i)

    print(*lst1, sep=",")


number = int(input("Enter a number: "))

factors(number)