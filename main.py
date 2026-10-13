from task_service import (
    add_task,
    get_tasks,
    delete_task,
    complete_task
)


print("WELCOME TO TASKFLOW MANAGER")


def view_task():
    print("\nYour Tasks")

    tasks = get_tasks()

    if len(tasks) == 0:
        print("No Tasks Available")
        return

    for i, task in enumerate(tasks, start=1):

        task_id, name, completed = task

        if completed:
            status = "✓"
        else:
            status = " "

        print(f"{i}. {name} [{status}]")


def delete_task_ui():

    tasks = get_tasks()

    if len(tasks) == 0:
        print("No Tasks Available")
        return

    print("\nYour Tasks")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task[1]}")

    choice = int(
        input("Which Task do you want to delete? ")
    )

    if choice < 1 or choice > len(tasks):
        print("Please Try Again!")
        return

    task_id = tasks[choice - 1][0]

    print("Are you sure you want to delete the Task?")
    ch = input("Y/N: ")

    if ch == 'Y' or ch == 'y':

        delete_task(task_id)

        print("Task deleted successfully!")


def complete_task_ui():

    tasks = get_tasks()

    if len(tasks) == 0:
        print("No Tasks Available")
        return

    print("\nYour Tasks")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task[1]}")

    choice = int(
        input("Which Task do you want to complete? ")
    )

    if choice < 1 or choice > len(tasks):
        print("Please Try Again!")
        return

    task_id = tasks[choice - 1][0]

    complete_task(task_id)

    print("Task marked as completed!")


while True:

    print("\n1. Add TASK")
    print("2. View TASK")
    print("3. Delete TASK")
    print("4. Complete TASK")
    print("5. EXIT")

    choice = int(
        input("Enter Your Choice: ")
    )

    if choice == 1:

        task = input("Enter Your Task: ")

        add_task(task)

        print("Task Added Successfully")

    elif choice == 2:

        view_task()

    elif choice == 3:

        delete_task_ui()

    elif choice == 4:

        complete_task_ui()

    elif choice == 5:

        print("Thank you for using TaskFlow!")
        break

    else:

        print("Invalid Choice. Try Again.")