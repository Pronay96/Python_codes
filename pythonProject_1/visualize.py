from bar import *

def main():
    num_star = int(input("number of times the symbol '*' should display: "))
    num_hyphen = int(input("number of times the symbol '-' should display: "))
    num_hash = int(input("number of times the symbol '#' should display: "))

    draw_bar(num_star, num_hyphen, num_hash)

    return

if __name__ == '__main__':
    main()