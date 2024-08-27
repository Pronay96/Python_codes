def main():
    list1 = []
    list2 = []

    #Enrolment quantity
    enrolment = int(input("Number of Students: "))
    if enrolment < 1 or enrolment > 30:
        print("Invalid Input")
        return

    #Input of name and reg_id
    for i in range (enrolment):
        print(f"Student {i+1}: ")
        name = input("Name: ")
        reg_no = input("Reg No: ")
        if len(reg_no) != 7:
            print("Invalid input")
            return

        #Tuple/List of Tuple
        tup1 = (name,int(reg_no))
        list1.append(tup1)

    #Map list of tuple to list of list
    list2 = list(map(list, list1))

    #Create username and password
    for lower in range(len(list2)):
        uname = (list2[lower][0].lower().replace(" ",""))
        temp = str(list2[lower][1])
        passwrd = uname+temp[-3:]
        list2[lower].append(uname)
        list2[lower].append(passwrd)

    #Map list of list to list of tuple
    list2 = tuple(map(tuple,list2))

    #Printing list1 with name and reg_id
    print("List of student enrolled: ")
    print("('NAME','REG NO')")
    for i in range(enrolment):
        print(list1[i])

    #Printing list2 with all creds
    print("List of students with login credentials: ")
    print("('NAME','REG NO','UNAME','PASSWORD')")
    for i in range(enrolment):
        print(list2[i])

main()