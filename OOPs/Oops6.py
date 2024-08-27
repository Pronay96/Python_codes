#Inheritance
class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

# If B does not inherit A, we can only access feature3 and feature4
class B:

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# When C inherits A, we can access feature 5 and 6 as well as now we can use feature 1 and 2
# So, if there are methods in some other class we want to use in recent class
# We can inherit them in the recent class to access those methods as well
# C becomes child/sub class and A becomes parent/super class
class C(A):

    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")

# Multilevel inheritance
# D inherits C inherits A
# So, D can access C and A both, but A or C can not access D
class D(C):
    def feature7(self):
        print("Feature 7 working")

    def feature8(self):
        print("Feature 8 working")

# Multiple inheritance
# Here E can access both from A and B
class E(A,B):
    def feature9(self):
        print("Feature 7 working")

    def feature10(self):
        print("Feature 8 working")



a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

print("Without inheritance")
#Calling from class A
a1.feature1()
a1.feature2()

#Calling from class B
b1.feature3()
b1.feature4()

print("\n")

print("With inheritance")

c1.feature1()
c1.feature2()
c1.feature5()
c1.feature6()

print("\n")

print("With multi-level inheritance")
d1.feature1()
d1.feature2()
d1.feature5()
d1.feature6()
d1.feature7()
d1.feature8()

print("\n")

print("With multiple inheritance")
e1.feature1()
e1.feature2()
e1.feature3()
e1.feature4()
e1.feature9()
e1.feature10()