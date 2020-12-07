from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

# to import data credentials.
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# initialise db
db = SQLAlchemy()


class Project(db.Model):
    __table_name__ = "Projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String, unique=True)
    link = db.Column(db.String, unique=True)

    def __repr__(self):
        return "<Project %r>" % self.name


db.init_app(app)
