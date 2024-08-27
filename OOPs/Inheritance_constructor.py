class A:

    def __init__(self):
        print("Inside init of class A")

    def feature1(self):
        print("Feature1-A is working")

    def feature2(self):
        print("Feature2 is working")


class B():

    def __init__(self):
        print("Inside init of class B")

    def feature1(self):
        print("Feature1-B is working")

    def feature4(self):
        print("Feature4 is working")


class C(A, B):

    def __init__(self):
        super().__init__()
        print("Inside init of class C")

    def feature(self):
        super().feature1()
        super().feature2()
        super().feature4()


print("Creating object of class C using constructor")
c1 = C()
c1.feature()