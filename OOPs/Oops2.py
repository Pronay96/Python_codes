class Computer:  # Blueprint

    # Prebuilt special method for variable initialization, gets called automatically for each object
    def __init__(self, cpu,
                 ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):  # Behavior (Methods/Functions)
        print("Config is ", self.cpu, self.ram)


# Creating objects with constructors
com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)

# Calling methods using objects
com1.config()
com2.config()

print(type(com1))
