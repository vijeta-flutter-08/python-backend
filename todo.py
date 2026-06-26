todos = []

while True:
    print("\n===== Todo App =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        todos.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(todos) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(todos, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(todos) == 0:
            print("No tasks to delete.")
        else:
            for index, task in enumerate(todos, start=1):
                print(f"{index}. {task}")

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(todos):
                removed = todos.pop(task_number - 1)
                print(f"'{removed}' deleted successfully.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")