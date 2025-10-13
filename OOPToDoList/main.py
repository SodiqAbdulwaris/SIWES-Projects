from ToDoListClass import ToDoList

def main():

    lists = ToDoList()

    while True:
        print("---TO-DO LIST---")
        print("1. View Task")
        print("2. Add Task")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. EXIT")
        UserChoice = int(input("Choose an option: "))

        if UserChoice == 1:
            lists.view()
        elif UserChoice == 2:
            lists.add()
        elif UserChoice == 3:
            lists.mark()
        elif UserChoice == 4:
            lists.delete()
        elif UserChoice == 5:
            print("Exiting....")
            break

if __name__ == "__main__":
    main()