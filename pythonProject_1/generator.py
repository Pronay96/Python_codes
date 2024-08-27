def find_lucky_number(name, table):
    sum1 = 0
    for char in name:
        if char in table[0]:
            ind = table[0].index(char)
            var = table[1][ind]
            # sum1 = sum1 + var
            yield var


def main():
    table = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z'], [1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3, 4, 5, 7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7]]
    name = input("Enter your name: ")
    if name.islower():
        print("Your lucky number is:0")
        print("Invalid Name")
        return
    name_up = name.upper()
    res = find_lucky_number(name_up, table)
    if res:
        res = list(res)
        res = sum(res)
        print(f"Your lucky number is : {res}")

main()
