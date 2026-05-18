def add_tasks(tasks):
    tsk_no = int(input("Enter how many tasks you want to add: "))
    for tsk in range(1, tsk_no+1):
        task = input((f"Enter task number {tsk}: "))
        tasks.append(task)
    print(f"Added {tsk_no} tasks!")
def view_tasks(tasks):
    tsks_avl = len(tasks)
    print(f"You have {tsks_avl} tasks: ")
    for tsk in tasks:
        print(f"[ ] {tsk}")
print("-----TO DO LIST-----")
tasks = []
user_choice = 0
while user_choice != 3:
    print("To-Do List Operations: ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Exit")
    user_choice = int(input("Select your actions: "))
    match user_choice:
        case 1:
            add_tasks(tasks)
        case 2:
            view_tasks(tasks)
        case 3:
            print("Exiting....!")
            break
        case _:
            print("Choose only from the given options!")