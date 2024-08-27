class Car:
    # Static/Class Variable (if changed will be changed for all the objects as it is available to all objects)
    wheels = 4

    def __init__(self):
        self.mill = 10  # Instance Variable
        self.comp = "BMW"  # Instance Variable


c1 = Car()
c2 = Car()

# Printing the Instance Variables
print("Printing the Instance Variables:")
print(c1.comp, c1.mill)
print(c2.comp, c2.mill)

# Since comp and mill are instance variables we can change then anywhere in the code for any object
c1.mill = 12
c2.comp = "Ferrari"
print("Updated instance variables:")
print(c1.comp, c1.mill)
print(c2.comp, c2.mill)

# Printing the Class variable, same for all the objects
print("Printing the Class variable:")
print(c1.wheels)
print(c2.wheels)

# If we now change the value of wheels, it will not be changed for any individual object
# The value of wheels will change for all the object
Car.wheels = 10
print("Printing after updating the Class variables:")
print(c1.comp, c1.wheels)
print(c2.comp, c2.wheels)
print(Car.wheels)
