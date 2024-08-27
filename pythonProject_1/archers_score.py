def create_list(input_string):
    list1 = []
    avg_sc = input_string.split(':')
    for x in avg_sc:
        score = int(x)
        list1.append(score)
    return list1

def find_player_count(list_score):
    dict1 = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for i in list_score:
        if i > 50:
            dict1['A'] +=1

        elif 40 < i <= 50:
            dict1['B'] += 1

        elif 25 < i <= 40:
            dict1['C'] += 1

        else:
            dict1['D'] += 1

    return dict1


def main():
    input_string = input("Enter the average scores (as colon-seperated values):")
    score_list = create_list(input_string)
    print(score_list)
    result_dict = find_player_count(score_list)
    print("Grade count:")
    if type(result_dict) == dict:
        for key,val in result_dict.items():
            print(key,":",val)

    return

if __name__ == '__main__':
    main()