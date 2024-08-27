class Students:
    school = "GNIT"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Instance Method since we are passing self, so this method works when called for any object
    # This takes the object for which it is called as self
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_marks(self):  # Instance Method Accessors
        return self.m1

    def set_marks(self, value):  # Instance Method Mutators
        self.m1 = value

    # Class Methods are used when we will be working with class variables
    # Any operation on class variable will be effective for all and any objects
    @classmethod
    def get_School(cls):  # Since we are using class method, instead of using self(object), we use class(cls)
        return cls.school

    # Static Method is used when we do not want to associate with any of the instance/class variables
    @staticmethod
    def info():  # Do not give any parameter as we do not want this method to work for any class(cls)/object(self)
        print("This is Student class.. in Oops5 module")
    # Static is used suppose to operate on object of other class
    # Factorial of a number which has nothing to do with the variables of this class


s1 = Students(70, 69, 71)
s2 = Students(51, 83, 90)

# Print marks and average
print(s1.school, s1.m1, s1.m2, s1.m3, s1.avg())
print(s2.school, s2.m1, s2.m2, s2.m3, s2.avg())

# Print Instance Method Accessor function
print(s1.get_marks())
print(s2.get_marks())

# Print Instance Method Mutator Method
s1.set_marks(89)
s2.set_marks(61)
print(s1.get_marks())
print(s2.get_marks())

# Print class Method
# If we do not pass cls as parameter here,we will see error.
# To avoid error we need to use a decorator before the class method (@classmethod)
print(Students.get_School())

# To avoid error we need to use a decorator before the static method (@staticmethod)
Students.info()
