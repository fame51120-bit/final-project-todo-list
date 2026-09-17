# 📝 Final Project: DevOps Todo List App
> Containerized Flask App with Multi-stage Docker, Security & Performance Optimization

**Live:** https://github.com/fame51120-bit/final-project-todo-list
**Student:** fame51120-bit | Woolf University

### 🏗️ Architecture Diagram
[User] -> [Flask App:10000] -> [tasks.json]
            |
     [Docker python:3.11-slim ~68MB Multi-stage]

### ✅ Prerequisites
- Docker Desktop
- Python 3.11+
- Git

### 🚀 Installation
git clone https://github.com/fame51120-bit/final-project-todo-list.git
cd final-project-todo-list
docker build -t todo-app.
docker run -p 10000:10000 todo-app
Open http://localhost:10000

### 📖 Usage
- Add Task / Delete Task
- Reports: /security.html and /performance.html

### 🔒 Security (Activity 2)
- Non-root user appuser
- Slim image
- Doc: security.html

### ⚡ Performance (Activity 3)
- Before 187MB -> After 68MB (ลด 63.6%)
- RPS 245 -> 512 req/s
- Doc: performance.html

### 📂 Project Structure
app.py, Dockerfile, requirements.txt, security.html, performance.html, tasks.json
