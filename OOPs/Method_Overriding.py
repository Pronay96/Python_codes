class Parent_House():

    def address(self):
        print("House address is Sodpur")

class My_House(Parent_House):

    def address(self):
        print("House address is Newtown")


parents_house = Parent_House()
my_house = My_House()

print("Parents House:")
parents_house.address()
print("My House:")
my_house.address()