class Student:

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s


s1 = Student()

print("Sum of 3 parameters:",s1.sum(5, 9, 8))
print("Sum of 2 parameters:",s1.sum(5, 9))
print("Sum of 1 parameters:",s1.sum(5))
