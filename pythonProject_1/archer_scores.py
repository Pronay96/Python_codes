def select_archer(score_list):
    dict_sc = {}
    list_dic = []
    for score in score_list:
        list1 = score.split(',')[0]
        list2 = score.split(',')[1:]
        list_sc = [int(i) for i in list2]
        key, sum1 = [], 0
        new_list = []
        if sum(list_sc) >= 50:
            key = list1
            for i in list_sc:
                sum1 = sum1+i
                new_list.append(i)
                if sum1 >= 50:
                    break
        if key:
            dict_sc = {key: new_list}
            list_dic.append(dict_sc)
    return list_dic


def extract_id(selected_list):
    archer_id = []
    for arc_id in selected_list:
        for value in arc_id:
            for key in arc_id:
                archer_id.append(key)
    return archer_id


def main():
    archer_score = []
    no = int(input("Enter the no of archers:\n"))
    print("Enter the archer id and 10 scores of round1 as comma separated values:\n")
    for i in range(no):
        archer_score.append(input())
    select_list = select_archer(archer_score)
    if select_list is not None and len(select_list) == 0:
        print("No one selected")
    else:
        selected_archers = extract_id(select_list)
        print("Selected Archer Id's:")
        for archer_id in selected_archers:
            print(archer_id)


if __name__ == '__main__':
    main()
