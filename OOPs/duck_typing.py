class Pycharm:
    def execute(self):
        print("Inside Pycharm Class:")
        print("----------------------")
        print("Compiling")
        print("Running")


class MyEditor:
    def execute(self):
        print("\nInside MyEditor Class:")
        print("-------------------------")
        print("Spell Check")
        print("Convension Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


# Creating object for the class Pycharm
ide = Pycharm()
# Creating object of the main class Laptop
lap1 = Laptop()
# Calling method code from Laptop class passing an object as argument
lap1.code(ide)

# Creating object for the class MyEditor
ide1 = MyEditor()
# Calling method code from Laptop class passing an object as argument
lap1.code(ide1)
