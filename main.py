import json
import os

class Task:
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["description"], data["due_date"], data["completed"])

TASKS_FILE = "tasks.json"

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4, ensure_ascii=False)

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task.from_dict(d) for d in data]
    except:
        return []

def main():
    tasks = load_tasks()
    while True:
        print("\n=== My To-Do List ===")
        print("1. View all tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        if not tasks:
            print("\n(No tasks yet)")
        else:
            for i, t in enumerate(tasks, 1):
                status = "[Done]" if t.completed else "[Todo]"
                print(f"{i}. {status} {t.description} (Due: {t.due_date})")

        choice = input("\nChoose menu (1-5): ")

        if choice == "1":
            continue
        elif choice == "2":
            desc = input("Task name: ")
            due = input("Due date (ex. 20/09/2026): ")
            tasks.append(Task(desc, due))
            save_tasks(tasks)
            print("Task added!")
        elif choice == "3":
            try:
                num = int(input("Which task is done? Number: "))
                tasks[num-1].mark_completed()
                save_tasks(tasks)
                print("Great! Completed!")
            except:
                print("Invalid number")
        elif choice == "4":
            try:
                num = int(input("Delete which task? Number: "))
                tasks.pop(num-1)
                save_tasks(tasks)
                print("Deleted")
            except:
                print("Invalid number")
        elif choice == "5":
            print("Bye bye!")
            break
        else:
            print("Please choose 1-5")

if __name__ == "__main__":
    main()