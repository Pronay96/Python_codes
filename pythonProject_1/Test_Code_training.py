def primegenerator(num, val):
    lst = []
    for value in range(2, num):
        for i in range(2, value):
            if value % i == 0:
                break
        else:
            lst.append(value)
    print(lst)

    if val == 0:
        for j in range(1,len(lst),2):
            yield lst[j]
    if val == 1:
        for k in range(0, len(lst), 2):
            yield lst[k]


if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i, end=" ")
