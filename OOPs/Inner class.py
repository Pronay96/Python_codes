class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.CPU = "AMD Ryzen"
            self.RAM = 8

        def show(self):
            print(self.brand, self.CPU, self.RAM)


s1 = Student("Pronay", 28)
s2 = Student("Riju", 14)

s1.show()
s2.show()

print("Directly accessing attributes from inside lap object")
print(s1.lap.CPU)
print(s2.lap.RAM)

lap1 = s1.lap
lap2 = s2.lap

print("Creating object from lap object")
lap1.show()
lap2.show()