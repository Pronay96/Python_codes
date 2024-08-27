def create_player(player_id, player_name, matches_played, runs_scored):
    dict_players = {"Id": player_id, "Name": player_name, "Matches Played": matches_played, "Runs Scored": runs_scored}
    return dict_players


def display_player(players_details):
    if not players_details:
        print("\nNo player details found\n")
    else:
        for i in range(len(players_details)):
            if players_details[i]["Runs Scored"] >= 100:
                print(f"\nPlayer {i+1} :")
                print(f"Id: {players_details[i]["Id"]}")
                print(f"Name: {players_details[i]["Name"]}")
                print(f"Matches_Played: {players_details[i]["Matches Played"]}")
                print(f"Runs_Scored: {players_details[i]["Runs Scored"]}")
            else:
                print("\nNo player details found\n")


def main():
    list_dic = []
    while True:
        print("1. Create Player")
        print("2. Display Player details")
        print("3. Exit")
        choice = int(input("\nEnter the option: "))
        if choice == 1:
            id1 = input("\nPlayer id: ")
            name = input("Player name: ")
            matches = int(input("Matched played: "))
            score = int(input("Runs scored: "))
            player_dict = create_player(id1, name, matches, score)
            list_dic.append(player_dict)
        if choice == 2:
            display_player(list_dic)
        if choice == 3:
            print("\nThank you")
            break


main()
