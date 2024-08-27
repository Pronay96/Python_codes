def palindrome(num):
    rev = num[::-1]
    print(f"The reversed number is {rev}")

    if rev == num:
        print("Palindrome")
    else:
        print("Not Palindrome")


number = input("Enter a value: ")
palindrome(number)
