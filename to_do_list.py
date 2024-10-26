tasks = []
def add_task():
    t = input("Enter a new task: \n")
    tasks.append(t)
    print("This task is added.\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        print("Your tasks: \n")
        for i, t in enumerate(tasks, 1):
            print(i,".", t)
        print()

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 1<= task_number <= len(tasks):
        removed = tasks.pop(task_number-1)
        print("task",removed,"is deleted. \n")
    else:
        print("Invalid task number. \n")

def menu():
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("invalid choice!")

if __name__ == "__main__":
    menu()
