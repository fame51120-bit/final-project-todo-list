from flask import Flask, request, redirect, render_template_string, jsonify
import json, os

app = Flask(__name__)
TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>My To-Do List - Secure</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-4" style="max-width:650px">
<div class="card shadow p-4">
<h3 class="text-center">✅ My To-Do List - Secure & Live!</h3>
<p class="text-center text-muted small">fame51120-bit | DevOps & DevSecOps Success</p>
<form method="POST" action="/add" class="d-flex gap-2 my-3">
<input name="task" class="form-control" placeholder="เพิ่มงานใหม่..." required>
<button class="btn btn-primary">เพิ่ม</button>
</form>
<ul class="list-group">
{% for t in todos %}
<li class="list-group-item d-flex justify-content-between align-items-center">{{t}} <a href="/delete/{{loop.index0}}" class="btn btn-sm btn-danger">ลบ</a></li>
{% endfor %}
</ul>
{% if not todos %}<p class="text-center text-muted mt-3">ยังไม่มีงาน</p>{% endif %}
<hr>
<div class="d-flex justify-content-between small">
<a href="/tasks">API: /tasks</a>
<a href="/security.html">🔐 Security Report</a>
</div>
</div>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, todos=load_tasks())

@app.route("/add", methods=["POST"])
def add():
    tasks = load_tasks()
    task = request.form.get("task","").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    tasks = load_tasks()
    if 0 <= id < len(tasks):
        tasks.pop(id)
        save_tasks(tasks)
    return redirect("/")

@app.route("/tasks")
def tasks_api():
    return jsonify(load_tasks())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
