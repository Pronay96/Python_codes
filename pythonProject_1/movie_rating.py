def check_rating(rating_list):
    cnt1, cnt2 = 0, 0
    for rating in rating_list:
        if 0 <= rating <= 5:
            cnt1 += 1
        if 6 <= rating <= 10:
            cnt2 += 1
    if cnt1 > cnt2:
        return "The highest rating is for 0-5"
    if cnt2 > cnt1:
        return "The highest rating is for 6-10"
    if cnt1 == cnt2:
        return "Ratings are equal"


def main():
    rating_list = []
    viewer_cnt = int(input("Enter the number of viewers: "))
    for i in range(viewer_cnt):
        rating = int(input())
        if 0 <= rating <= 10:
            rating_list.append(rating)
        else:
            print("Invalid Input")
    final = check_rating(rating_list)
    print(final)


main()
