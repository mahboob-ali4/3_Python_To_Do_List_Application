# 2. Build a basic to-do list application that allows users to add tasks, mark them as complete, and remove them.
def to_do_list_app_menu():
    print("\n ------------------------------ TO-DO LIST APPLICATION ------------------------------")
    print("\nPress 1 to add a new task: ")
    print("Press 2 to display all the tasks: ")
    print("Press 3 to update a task: ")
    print("Press 4 to remove a task: ")
    print("Press 5 to exit the application: ")

def user_choice():
    return input("Please enter your choice: ")

tasks = []
def new_task_addition():
    adding_task = input("Please enter name of your new task: ")
    task_status = "not done"
    new_tasks = [adding_task, task_status]
    tasks.append(new_tasks)
    if new_tasks:
        print(new_tasks)
        print("YOUR TASK HAS BEEN ADDED SUCESSFULLY!")

def display_tasks():
    for task in tasks:
        print(task)
    print(f"YOU HAVE TOTAL {len(tasks)} TASKS PENDING.")

def update_tasks():
    search_task_by_index = int(input("Enter the task number starting from 0: "))
    specified_task = tasks[search_task_by_index]
    print(specified_task)
    task_as_done = input("Update this task: ")
    specified_task[1] = task_as_done
    print("YOUR TASK HAS BEEN UPDATED SUCCESSFULLY!")
    print(tasks)

def remove_task():
    task_to_remove = int(input("Enter the task number to remove starting from 0: "))
    tasks.pop(task_to_remove)
    print("YOU REMOVED A TASK SUCCESSFULLY!")
    print(tasks)
    print(f"NOW, YOU HAVE A TOTAL OF {len(tasks)} TASKS PENDING.")

def exit_function():
    print("YOU EXIT THE APPLICATION.")


while True:
    to_do_list_app_menu()
    choice = user_choice()

    if choice == "1":
        new_task_addition()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        update_tasks()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        exit_function()
        break
    else:
        print("PLEASE, MAKE A VALID CHOICE.")