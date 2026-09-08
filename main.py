import json, os

class Task:
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date
        self._completed = completed
    def mark_complete(self):
        self._completed = True
    def is_completed(self):
        return self._completed
    def to_dict(self):
        return {"description": self.description, "due_date": self.due_date, "completed": self._completed}
    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['due_date'], data['completed'])

TASKS_FILE = "tasks.json"

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4, ensure_ascii=False)

def load_tasks():
    if not os.path.exists(TASKS_FILE): return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return [Task.from_dict(i) for i in json.load(f)]
    except: return []

def main():
    tasks = load_tasks()
    while True:
        print("\n1.เพิ่มงาน 2.ดูงาน 3.ทำเสร็จ 4.ออก")
        c = input("เลือก: ")
        if c == "1":
            tasks.append(Task(input("ชื่องาน: "), input("วันส่ง: ")))
        elif c == "2":
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t.description} | {t.due_date} | {'เสร็จ' if t.is_completed() else 'ยังไม่เสร็จ'}")
        elif c == "3":
            try:
                tasks[int(input("เลขงาน: "))-1].mark_complete()
            except: pass
        elif c == "4":
            save_tasks(tasks)
            break

if __name__ == "__main__":
    main()
