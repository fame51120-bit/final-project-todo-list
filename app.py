from flask import Flask, request, jsonify, render_template_string
import json
import os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

# สร้างไฟล์ถ้ายังไม่มี
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as f:
        json.dump([], f)

def load_tasks():
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Todo List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head><body class="bg-light"><div class="container mt-5" style="max-width:700px">
    <div class="card shadow p-4">
    <h2>📝 Todo List - Final Project</h2>
    <div class="input-group mt-3"><input id="taskInput" class="form-control" placeholder="New task..."><button class="btn btn-primary" onclick="addTask()">Add</button></div>
    <ul id="taskList" class="list-group mt-3"></ul>
    <hr><a href="/security.html" class="btn btn-outline-dark btn-sm">Security Report</a> <a href="/performance.html" class="btn btn-outline-success btn-sm">Performance Report</a>
    </div></div>
    <script>
    async function load(){ let res=await fetch('/tasks'); let tasks=await res.json(); let list=document.getElementById('taskList'); list.innerHTML=''; tasks.forEach((t,i)=>{ list.innerHTML+=`<li class="list-group-item d-flex justify-content-between">${t}<button class="btn btn-danger btn-sm" onclick="delTask(${i})">x</button></li>`; }); }
    async function addTask(){ let input=document.getElementById('taskInput'); if(!input.value) return; await fetch('/tasks',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({task:input.value})}); input.value=''; load(); }
    async function delTask(i){ await fetch('/tasks/'+i,{method:'DELETE'}); load(); }
    load();
    </script></body></html>
    """)

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks = load_tasks()
    tasks.append(data.get("task",""))
    save_tasks(tasks)
    return jsonify({"status":"ok"})

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return jsonify({"status":"deleted"})

@app.route("/security.html")
def security():
    with open("security.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/performance.html")
def performance():
    with open("performance.html", "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
