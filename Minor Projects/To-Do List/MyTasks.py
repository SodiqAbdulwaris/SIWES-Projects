import json, os

def load_tasks():
    if os.path.exists("To-Do List\\tasks.json"):
        with open("To-Do List\\tasks.json", "r") as file:
            return json.load(file)
    return []

tasks = load_tasks()

def save_tasks():
    with open("To-Do List\\tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)



