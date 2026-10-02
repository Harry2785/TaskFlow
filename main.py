print("WELCOME TO TASKFLOW MANAGER")
tasks=[]

def add_task():
    task=input("Enter Your Task: ")
    new_task = {
        "name": task,
        "completed": False
    }
    tasks.append(new_task)
    print("Task Added Succesfully")
def view_task():
    print("\n Your Tasks")
    if len(tasks)==0:
        print("No Tasks Available")
    else:
        for i, task in enumerate(tasks, start=1):
            if task["completed"]:
               status = "✓"
            else:
                status = " "
            print(f"{i}. {task['name']} [{status}]")

def delete_task():
    if len(tasks)==0:
        print("No Tasks Available")
    else:

        for i, task in enumerate(tasks, start=1):
            print(i, task["name"])

        del_task = int(input("Which Task do you want to delete? "))
        if del_task<1 or del_task>len(tasks):
            print("Please Try Again! ")
        else:

            print("Are you sure you want to delete the Task?")
            ch = input("Y/N: ")

            if ch == 'Y' or ch == 'y':
                tasks.pop(del_task - 1)

                print("\nYour Updated TaskFlow")

                for i, task in enumerate(tasks, start=1):
                    print(i, task["name"])

def complete_task():
    if len(tasks) == 0:
        print("No Tasks Available")

    else:
        for i, task in enumerate(tasks, start=1):
            print(i, task["name"])

        completed = int(input("Which Task do you want to complete? "))

        if completed < 1 or completed > len(tasks):
            print("Please Try Again!")

        else:
            tasks[completed - 1]["completed"] = True
            print("Task marked as completed!")

while True:
    print("1. Add TASK")
    print("2. View TASK")
    print("3. Delete TASK")
    print("4. Complete TASK")
    print("5. EXIT")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        add_task()
    elif choice ==2:
        view_task()
    elif choice==3:
         delete_task()
    elif choice==4:
        complete_task()
    elif choice == 5:
        print("Thank you for using TaskFlow!")
        break

    else:
        print("Invalid Choice. Try Again.")

