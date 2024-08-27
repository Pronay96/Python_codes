import sys

sys.setrecursionlimit(2000)
print(f"Recursion limit is: {sys.getrecursionlimit()}")

i = 0


def greet():
    global i
    i += 1
    print(i, "Hello")
    greet()


greet()
