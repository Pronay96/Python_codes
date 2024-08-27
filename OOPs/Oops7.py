# Operator Overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m3 = self.m1 + other.m1
        m4 = self.m2 + other.m2
        s4 = Student(m3, m4)
        return s4

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = Student(71, 94)
s2 = Student(65, 80)

s3 = s1 + s2  # s1+s2 = Student.__add__(s1,s2)

print(s3.m1, s3.m2)

if s1 > s2:  # s1>s2 = Student.__gt__(s1,s2)
    print("S1 wins")
else:
    print("S2 wins")
