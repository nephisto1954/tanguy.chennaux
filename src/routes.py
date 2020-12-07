from flask import Flask, render_template, url_for, request
from src import app, Project, db


@app.route("/")
@app.route("/home")
def homepage():
    title = "Homepage"
    return render_template("Homepage.html", title=title)


@app.route("/about")
def about():
    title = "About"
    return render_template("About.html", title=title)


@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("Contact.html", title=title)


@app.route("/projects")
def all_projects():
    title = "Projects"
    return render_template("Projects.html", title=title)


@app.route("/projects/new", methods=["get", "post"])
def new():

    title = "Add a new project"

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        link = request.form["link"]

        project = Project(name=name, description=description, link=link)
        db.session.add(project)
        db.session.commit()
        return render_template("New.html", title=title)


@app.route("/projects/<project_name>")
def projects(project_name):
    project = Project.query.filter_by(name=project_name).first()

    if project is None:
        return "No project found"
    else:
        return project.description


@app.route("/stack")
def stack():
    title = "Stack"
    return render_template("Stack.html", title=title)
