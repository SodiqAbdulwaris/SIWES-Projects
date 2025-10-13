
from MyTasks import tasks, save_tasks

class ToDoList:
    def __init__(self):
        self.tasks = tasks
        self.save_tasks = save_tasks

    def view(self):
        if not self.tasks:
            print("No Tasks Available")
        else:
            for i, task in enumerate (self.tasks, start=1):
                if task["status"]:
                    status = "✔️"
                else:
                    status = "❌"
                print(f"{i}. {task['title']} -> {status}")
    
    def add(self):
        AddTask = input("What do you want to do? ")
        self.tasks.append({"title": AddTask, "status": False})
        save_tasks()
        print("Task Added Successfully")

    def mark(self):
        incomplete_tasks = [task for task in self.tasks if not task["status"]]

        if not incomplete_tasks:
            print("🎉 All tasks are already marked as done!")
            return

        print("\nIncomplete Tasks:")
        for i, task in enumerate(incomplete_tasks, start=1):
            print(f"{i}. {task['title']} -> ❌")

        try:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(incomplete_tasks):
                actual_index = self.tasks.index(incomplete_tasks[task_num - 1])
                self.tasks[actual_index]["status"] = True

                self.save_tasks()

                print(f"✅ Task '{incomplete_tasks[task_num - 1]['title']}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


    def delete(self):
        self.view()  
        if self.tasks:  
            try:
                TaskNum = int(input("Enter task number to delete: "))
                if 1 <= TaskNum <= len(self.tasks):
                    deleted_task = self.tasks.pop(TaskNum - 1)
                    save_tasks()
                    print(f"Task '{deleted_task['title']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


