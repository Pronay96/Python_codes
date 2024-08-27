class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __str__(self):
        return f"{self.m1}, {self.m2}"
        # return "{}, {}".format(self.m1, self.m2)

s1 = Student(78, 89)
s2 = Student(49, 92)

print(s1)
print(s2)
