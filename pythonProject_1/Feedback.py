def feedback():
    list1 = []
    list2 = []
    n = int(input("Enter size of list: "))

    if n <= 0:
        print("Invalid List Size")
        return

    for i in range(0, n):
        element = int(input())
        if element < 0:
            print("Invalid Input")
            return
        list1.append(element)

    for j in range(0, n):
        element = int(input())
        if element < 0:
            print("Invalid Input")
            return
        list2.append(element)

    new_list = []
    for i in range(0, n):
        if list1[i] == list2[i]:
            new_list.append('equal')
        else:
            new_list.append(list1[i]-list2[i])

    #print(list1)
    #print(list2)
    print(new_list)


feedback()