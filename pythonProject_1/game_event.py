def find_each_round_winner(team1, team2):
    new_list = []
    for i in range(len(team1)):
        if team1[i] > team2[i]:
            new_list.append('Team1')
        if team1[i] < team2[i]:
            new_list.append('Team2')
        if team1[i] == team2[i]:
            new_list.append('Equal')
    return new_list


def count_winners(winner_list):
    cnt1 = 0
    cnt2 = 0
    cnt_eq = 0
    for wins in winner_list:
        if wins == 'Team1':
            cnt1 += 1
        if wins == 'Team2':
            cnt2 += 1
        if wins == 'Equal':
            cnt_eq += 1
    winner_dict = {"Team1": cnt1, "Team2": cnt2, "Equal": cnt_eq}
    return winner_dict


def main():
    rounds = int(input("Enter the no of rounds: "))
    if rounds <= 0:
        print("Invalid rounds")
        return
    team1 = []
    team2 = []
    print("Enter the team 1 points: ")
    for i in range(rounds):
        points = int(input())
        team1.append(points)
    print("Enter the team 2 points: ")
    for i in range(rounds):
        points = int(input())
        team2.append(points)
    round_winner = find_each_round_winner(team1, team2)
    winners_dict = count_winners(round_winner)
    print(round_winner)
    for key, value in winners_dict.items():
        print(f"{key}: {value}")

main()