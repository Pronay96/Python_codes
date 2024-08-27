def add_task(task, todo_list):
    todo_list.append(task)
    return todo_list


def mark_task_complete(index, todo_list):
    if index > len(todo_list) or len(todo_list) == 0:
        print("Invalid Input")
    else:
        todo_list.pop(index)
        for values in todo_list:
            print(values)


def main():
    todo_list = []
    while True:
        choice = int(input("Enter a command (1 to add a task, 2 to mark a task complete, 3 to quit):"))
        if choice == 1:
            task = input("Enter the task to add: ")
            todo_list = add_task(task, todo_list)
            print(todo_list)
        elif choice == 2:
            ind1 = int(input("Enter the index of the task to mark as complete:"))
            mark_task_complete(ind1, todo_list)
        elif choice == 3:
            break
        else:
            print("Invalid command")
            break

main()