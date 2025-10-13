import json, os

if not os.path.exists("OOPToDoList\\tasks.json"):
    with open("OOPToDoList\\tasks.json", "w") as file:
        json.dump([], file)

def load_tasks():
    if os.path.exists("OOPToDoList\\tasks.json"):
        with open("OOPToDoList\\tasks.json", "r") as file:
            return json.load(file)
    return []

tasks = load_tasks()

def save_tasks():
    with open("OOPToDoList\\tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


