def create_ratings(input_string):
    list_info = input_string.split(",")
    rating_dict = {}
    for rating in list_info:
        key = rating.split(":")[0]
        value = rating.split(":")[1]
        rating_dict[key] = value
    return rating_dict


def count_rating(rating_dict):
    list1, list2 = [], []
    for key, value in rating_dict.items():
        if 0 <= int(value) <= 5:
            list1.append(key)
        else:
            list2.append(key)
    return list1, list2


def main():
    dict_trainer = {}
    count_rating1 = ()
    trainer_info = input("Enter the ratings (as comma-separated values):")
    dict_trainer = create_ratings(trainer_info)
    # print(dict_trainer)
    count_rating1 = count_rating(dict_trainer)
    # print(count_rating1)
    if len(count_rating1[0]) == 0 and len(count_rating1[1]) == 0:
        print("The list of trainers with ratings between 0-5: Nil")
        print("The list of trainers with ratings between 6 and above: Nil")
    if len(count_rating1[0]) != 0 and len(count_rating1[1]) != 0:
        print(f"The list of trainers with ratings between 0-5: {count_rating1[0]}")
        print(f"The list of trainers with ratings between 6 and above: {count_rating1[1]}")
    if len(count_rating1[0]) == 0 and len(count_rating1[1]) != 0:
        print("The list of trainers with ratings between 0-5: Nil")
        print(f"The list of trainers with ratings between 6 and above: {count_rating1[1]}")
    if len(count_rating1[0]) != 0 and len(count_rating1[1]) == 0:
        print(f"The list of trainers with ratings between 0-5: {count_rating1[0]}")
        print("The list of trainers with ratings between 6 and above: Nil")

main()
