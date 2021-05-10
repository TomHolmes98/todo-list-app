from application import app, db
from application.models import tasks

@app.route("/")
@app.route("/home")
def home():
    all_tasks = tasks.query.all()
    return str(all_tasks)

@app.route("/create")
def create():
    new_todo = tasks(description = "New task")
    db.session.add(new_todo)
    db.session.commit()
    return "New task added"

@app.route("/complete/<int:id>")
def complete(id):
    task = tasks.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return "Task is now complete"

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = tasks.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return f"Task {id} is now incomplete"

@app.route("/update/<int:id>")
def update(new_description):
    task = tasks.query.order_by(tasks.id.desc()).first()
    task.description = new_description
    db.session.commit()
    return f"Most recent task was updated with the description: {new_description}"

@app.route("/delete/<int:id>")
def delete(id):
    task = tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    return f"Task {id} was deleted."
    


