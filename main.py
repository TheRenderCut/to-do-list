def add_tasks(tasks):
    tsk_no = int(input("Enter how many tasks you want to add: "))
    for tsk in range(1, tsk_no+1):
        task = input((f"Enter task number {tsk}: "))
        new_task = {
            "task": task,
            "completed": False
        }
        tasks.append(new_task)
    print(f"Added {tsk_no} tasks!")
def view_tasks(tasks):
    tsks_avl = len(tasks)
    print(f"You have {tsks_avl} tasks: ")
    if tsks_avl == 0:
            print("No available tasks!")
            return
    for index, tsk in enumerate(tasks, start = 1):
        if tsk['completed']:
            print(f"{index}. [X] {tsk['task']}")
        else:
            print(f"{index}. [ ] {tsk['task']}")
def remove_tasks(tasks):
    view_tasks(tasks)
    tsks_avl = len(tasks)
    if tsks_avl == 0:
        return
    task_no = int(input("Enter the task number you want to remove: "))
    while task_no > tsks_avl or task_no <= 0:
        print("Enter available task index!")
        task_no = int(input("Enter the task number you want to remove: "))
    indx = task_no - 1
    print(f"Removed task {task_no}: {tasks[indx]['task']}!")
    tasks.pop(indx)
def modify_taskstatus(tasks):
    view_tasks(tasks)
    tsks_avl = len(tasks)
    if tsks_avl == 0:
        return
    task_no = int(input("Enter the task number you have completed: "))
    while task_no > tsks_avl or task_no <= 0:
        print("Enter available task index!")
        task_no = int(input("Enter the task number you want to remove: "))
    indx_no = task_no - 1
    tasks[indx_no]['completed'] = True
def load_tasks(tasks):
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                split_task = line.split("|")
                if split_task[1].strip() == "True":
                    split_task[1] = True
                else:
                    split_task[1] = False
                new_task = {
                    "task": split_task[0],
                    "completed": split_task[1]
                }
                tasks.append(new_task)
    except:
        return
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for tsk in tasks:
            file.write(tsk['task'] + "|" + str(tsk['completed']) + "\n")
def menu():
    print("-----TO DO LIST-----")
    tasks = []
    user_choice = 0
    load_tasks(tasks)
    while user_choice != 5:
        print("To-Do List Operations: ")
        print("1. Add Task")
        print("2. View Task")
        print("3. Remove Task")
        print("4. Modify Task Status")
        print("5. Exit")
        user_choice = int(input("Select your actions: "))
        match user_choice:
            case 1:
                add_tasks(tasks)
            case 2:
                view_tasks(tasks)
            case 3:
                remove_tasks(tasks)
            case 4:
                modify_taskstatus(tasks)
            case 5:
                save_tasks(tasks)
                print("Exiting....!")
                break
            case _:
                print("Choose only from the given options!")
menu()