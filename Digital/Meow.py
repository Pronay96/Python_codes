import sys

file_name = 'C:/Users/PRONAY/Desktop/Python/python_file.py'

try:
    with open(file_name, 'rt') as file:
        for line in file:
            print(line)

except:
    print(f"Could not open the file {file_name}")
    sys.exit(1)

sum = 10+20

print(sum)