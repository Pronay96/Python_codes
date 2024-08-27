def display(pa):
    print(f"The password is: {pa}")

def password_generator(fn,ln):
    if len(fn) < 4:
        print("First Name cannot be less than 4 charecters")
        return
    if len(ln) <= 3:
        print("Last Name cannot be less than 3 charecters")
        return

    temp = str(len(fn))+str(len(ln))
    password = fn.lower()+ln.lower()+temp
    display(password)


first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

password_generator(first_name,last_name)