def calculate_score(score_values):
    cnt = 0
    check = 0.5*(sum(score_values)/len(score_values))
    for score in score_values:
        if score >= check:
            cnt += 1
        if score == 0:
            return 0
    return cnt


def main():
    size = int(input("Enter the size of the scorecard: "))
    score_list = []
    print("Enter the score values:")
    for i in range(size):
        score = float(input())
        score_list.append(score)
    count = calculate_score(score_list)
    print(f"The score values that are equal to or above 50% of the average score: {count}")


main()