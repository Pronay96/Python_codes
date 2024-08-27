def find_winner(sales_rep1, sales_rep2):
    cnt_rep1, cnt_rep2 = 0, 0
    for i in range(len(sales_rep1)):
        if sales_rep1[i] > sales_rep2[i]:
            cnt_rep1 += 1
        if sales_rep2[i] > sales_rep1[i]:
            cnt_rep2 +=1
    if cnt_rep1 > cnt_rep2:
        return "Sales Representative 1 is the winner"
    if cnt_rep2 > cnt_rep1:
        return "Sales Representative 2 is the winner"
    if cnt_rep1 == cnt_rep2:
        return "Both are winners"


def main():
    emp1 = []
    emp2 = []
    no_of_days = int(input("Enter the number of days: "))
    print("Enter daily sales for Sales Representative 1:")
    for i in range(no_of_days):
        sales = int(input())
        emp1.append(sales)
    print("Enter daily sales for Sales Representative 2:")
    for i in range(no_of_days):
        sales = int(input())
        emp2.append(sales)
    output = find_winner(emp1,emp2)
    print(output)


main()