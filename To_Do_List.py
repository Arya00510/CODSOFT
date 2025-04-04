import datetime

todo = {}

def add_task():
    task = input("Enter your task: ").strip()
    if task:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        todo[time] = task
        print(f"Task added at {time}")
    else:
        print("Empty task not allowed.")

def show_tasks():
    if not todo:
        print("No tasks to show.")
        return
    print("\n--- TO-DO LIST ---")
    for idx, (time, task) in enumerate(todo.items(), start=1):
        print(f"{idx}. [{time}] {task}")

def delete_task():
    show_tasks()
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(todo):
            key = list(todo.keys())[number - 1]
            print(f"Deleted: {todo[key]}")
            del todo[key]
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

while True:
    print("\n1. Add Task  2. Show Tasks  3. Delete Task  4. Exit")
    ch = input("Choice: ")
    if ch == '1':
        add_task()
    elif ch == '2':
        show_tasks()
    elif ch == '3':
        delete_task()
    elif ch == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option.")