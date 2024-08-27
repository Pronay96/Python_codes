import sys

# Terminal input
# If we want to use terminal to get results and while using we want to give user input, we need to use argv.
# Argv is part of a class sys that needs to be imported
# Argv will take values as a list, so we need index to access it
# INDEX[0] is the name of the file being executed and consecutive once are the inputs

# Printing string
x = sys.argv[1]
y = sys.argv[2]
z = x+y
print(z)

# Printing integer
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print(z)