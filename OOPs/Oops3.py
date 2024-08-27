class Computer:

    def __init__(self):
        self.name = "Pronay"
        self.age = 28

    def update(self):
        self.age = 20

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()  # c1 is an object stored in the heap memory

c2 = Computer()

# id is a function used to find the address of the object in heap memory
print("Address of c1 object in heap memory:", id(c1))
print("Address of c2 object in heap memory:", id(c2))

# Printing name after using constructor and init method called
print("Name/Age after using constructor and init method called for obj c1:", c1.name, c1.age)
print("Name/Age after using constructor and init method called for obj c2:", c2.name, c2.age)

# Printing name after making change in the main code
c2.name = "Harish"
c2.age = 24

print("Name/Age after making change in the main code for obj c2:", c1.name, c1.age)
print("Name/Age after making change in the main code for obj c2:", c2.name, c2.age)

# Printing by calling update method
c1.update()
print("Name/Age after calling update method for obj c1:", c1.name, c1.age)

# Compare age
if c1.compare(c2):
    print("Same Age")
else:
    print("Different Age")
