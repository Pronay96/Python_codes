def Prime(num):

    if num > 1:
        for i in range(2,(num//2)+1):
            if num % i == 0:
                print(f"{num} is not a Prime Number")
                break
        else:
            print(f"{num} is a Prime Number")


number = int(input("Enter a number: "))
Prime(number)