# todo.py
tasks = []

def show_menu():
    print("\n--- To Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice.")
