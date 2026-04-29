tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(i, ".", t)

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(i, ".", t)
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print("Removed:", removed)
                else:
                    print("Invalid number.")
            except ValueError:
                print("Enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")