def dictionary():
    word_dictionary = {}
    list2 = []

    while True:
        word = input("Enter the word: ")
        num = int(input("Enter the no.of meaning: "))

        if num <= 0:
            print("Invalid Input")
            print(word_dictionary)
            return

        list1 = []
        print("Enter meanings:")
        for x in range(num):
            mean = input()
            list1.append(mean)
            word_dictionary = {word: list1}
        list2.append(word_dictionary)

        i = int(input("Do you want to add one more element to the dictionary? If yes press 1,else press 0: "))
        if i == 0:
            break

    for i in range(len(list2)):
        for key, values in list2[i].items():
            print(f"{key}: {values}")


dictionary()
