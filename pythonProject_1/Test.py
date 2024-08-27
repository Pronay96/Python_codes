a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter age:"))
    print(k)

except ZeroDivisionError as e:
    print("Second input is incorrect, please insert correct value:", e)

except ValueError as e:
    print("Please check the age:", e)

except Exception as e:
    print("Unknown Exception:", e)

finally:
    print("Resource close")
