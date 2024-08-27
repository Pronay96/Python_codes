def archer():

    scores = 0
    tot_score = 0
    x = 0  # Flag variable

    print("Scores: \n")

    while tot_score <= 100:

        scores = int(input())

        if scores < 0:
            print("There is no negetive score")
            return

        tot_score += scores
        x += 1

        if tot_score >= 100:
            print(f"The number of turns : {x}")
            return


archer()
