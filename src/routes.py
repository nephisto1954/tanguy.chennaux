from flask import Flask, render_template, url_for
from src import app


@app.route("/")
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
def projects():
    title = "Projects"
    return render_template("Projects.html", title=title)


@app.route("/stack")
def stack():
    title = "Stack"
    return render_template("Stack.html", title=title)
