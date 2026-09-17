from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>✅ My To-Do List is Live on Cloud!</h1>
    <p>Project: final-project-todo-list</p>
    <p>Owner: fame51120-bit</p>
    <p>DevOps & Cloud Deployment Successful</p>
    <hr>
    <a href='/tasks'>ดู tasks.json</a>
    """

@app.route("/tasks")
def tasks():
    try:
        with open("tasks.json") as f:
            return f.read()
    except:
        return "[]"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
