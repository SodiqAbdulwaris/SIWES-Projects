
from MyTasks import tasks, save_tasks

def view():
    if not tasks:
        print("No Tasks Available")
    else:
        for i, task in enumerate (tasks, start=1):
            if task["status"]:
                status = "✔️"
            else:
                status = "❌"
            print(f"{i}. {task['title']} -> {status}")

def add():
    AddTask = input("What do you want to do? ")
    tasks.append({"title": AddTask, "status": False})
    save_tasks()
    print("Task Added Successfully")

def mark():
    
    for i, task in enumerate (tasks, start=1):
            if task["status"]:
                status = "✔️"
            else:
                status = "❌"
            if status == "❌":
                print(f"{i}. {task['title']} -> {status}")
    
    if tasks:
        try:
            TaskNum = int(input("Enter task number to mark as done: "))
            if 1 <= TaskNum <= len(tasks):
                tasks[TaskNum - 1]["status"] = True
                save_tasks()
                print(f"Task '{tasks[TaskNum - 1]['title']}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def delete():
    view()  
    if tasks:  
        try:
            TaskNum = int(input("Enter task number to delete: "))
            if 1 <= TaskNum <= len(tasks):
                deleted_task = tasks.pop(TaskNum - 1)
                save_tasks()
                print(f"Task '{deleted_task['title']}' deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("---TO-DO LIST---")
        print("1. View Task")
        print("2. Add Task")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. EXIT")
        UserChoice = int(input("Choose an option: "))

        if UserChoice == 1:
            view()
        elif UserChoice == 2:
            add()
        elif UserChoice == 3:
            mark()
        elif UserChoice == 4:
            delete()
        elif UserChoice == 5:
            print("Exiting....")
            break

if __name__ == "__main__":
    main()
