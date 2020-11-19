from flask import Flask, render_template
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
