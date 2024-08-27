def main():
    participants = []

    num_participants = int(input("Enter the no.of participants details to be created: "))

    if num_participants <= 0:
        print("Invalid input")
        display_participants(participants)
        return

    for i in range(num_participants):
        name = input("Enter participant's name: ")
        age = int(input("Enter participant's age: "))
        state = input("Enter participant's state: ")

        if age <= 10 or age > 80:
            print("Invalid input")
            display_participants(participants)
            return

        participant_info = {'Name': name, 'Age': age, 'State': state}
        participants.append(participant_info)

    display_participants(participants)

    # State Count
    state_count = {}

    for participant in participants:
        state = participant['State']
        state_count[state] = state_count.get(state, 0) + 1

    for state, count in state_count.items():
        print(f"State: {state} Count: {count}")

def display_participants(participants):
    if participants:
        for participant in participants:
            print(participant)
    return

if __name__ == '__main__':
    main()