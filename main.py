def add_tasks(tasks):
    tsk_no = int(input("Enter how many tasks you want to add: "))
    for tsk in range(1, tsk_no+1):
        task = input((f"Enter task number {tsk}: "))
        tasks.append(task)
    print(f"Added {tsk_no} tasks!")
def view_tasks(tasks):
    tsks_avl = len(tasks)
    print(f"You have {tsks_avl} tasks: ")
    if tsks_avl == 0:
            print("No available tasks!")
            return
    for index, tsk in enumerate(tasks, start = 1):
        print(f"{index}. [ ] {tsk}")
def remove_tasks(tasks):
    tsks_avl = len(tasks)
    print(f"You have {tsks_avl} tasks: ")
    if tsks_avl == 0:
        print("No available tasks!")
        return
    for index, tsk in enumerate(tasks, start = 1):
        print(f"{index}. [ ] {tsk}")
    task_no = int(input("Enter the task number you want to remove: "))
    while task_no > tsks_avl or task_no <= 0:
        print("Enter available task index!")
        task_no = int(input("Enter the task number you want to remove: "))
    indx = task_no - 1
    print(f"Removed task {task_no}: {tasks[indx]}!")
    tasks.pop(indx)
def menu():
    print("-----TO DO LIST-----")
    tasks = []
    user_choice = 0
    while user_choice != 4:
        print("To-Do List Operations: ")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Exit")
        user_choice = int(input("Select your actions: "))
        match user_choice:
            case 1:
                add_tasks(tasks)
            case 2:
                view_tasks(tasks)
            case 3:
                remove_tasks(tasks)
            case 4:
                print("Exiting....!")
                break
            case _:
                print("Choose only from the given options!")
menu()