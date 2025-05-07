todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print("Task added.")

def remove_task(index):
    try:
        todo_list.pop(index - 1)
        print("Task removed.")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        index = int(input("Enter task number to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")