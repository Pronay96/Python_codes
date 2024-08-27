class Computer:  # Blueprint

    def config(self):  # Behavior (Methods/Functions)
        print("i5, 16gb, 1TB")


# com1 is a variable which needs to be mentioned as object type.
# In java to initialize the type of com1 object, we need to construct the object with the constructor of the class.
com1 = Computer()  # Object (com1) Constructor (Computer())

print(type(com1))

Computer.config(com1)  # Calling config with passing com1 as parameter

com1.config()  # Calling config for com1 using object and com1 acts as parameter but in back of screen
