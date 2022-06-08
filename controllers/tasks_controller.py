from flask import Flask, render_template
from flask import Blueprint
from repositories import task_repository

tasks_blueprint = Blueprint("tasks", __name__)


@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks=tasks)


# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'
