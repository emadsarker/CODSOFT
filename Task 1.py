tasks = []
def addtask():
    task=input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
def listtasks():
    if not tasks:
        print("There are no tasks.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")
def deletetask():
    listtasks()
    try:
        tasktodelete=int(input("Enter the task number to delete: "))
        if tasktodelete>=0 and tasktodelete < len(tasks):
            removed_task=tasks.pop(tasktodelete)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print(f"Task number {tasktodelete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
if __name__ == "__main__":
    print("** Welcome to the To-Do List **")
    while True:
        print("Please select one option:")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        choice=input("Enter your option:")
        if choice=="1":
            addtask()
        elif choice=="2":
            deletetask()
        elif choice=="3":
            listtasks()
        elif choice=="4":
            print("Exiting the program.")
            break
        else:
            print("Invalid input.Please select a valid option.")
