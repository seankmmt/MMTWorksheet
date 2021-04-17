from wtforms import Form, FloatField, validators
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, abort, url_for, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

class InputForm(Form):
    r = FloatField()

app = Flask(__name__)
app.config["DEBUG"] = True

# Ensure templates are auto-reloaded -------------------------------------------
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.secret_key = "Seung-min_Yu_Sean_Kim_MMT_Math_Worksheet_Generator_Website"
#------------------------------------------------------------------------
#db = SQLAlchemy(app)

#class Comment(db.Model):
#
#    __tablename__ = "comments"
#
#    id = db.Column(db.Integer, primary_key=True)
#    content = db.Column(db.String(4096))

@app.route('/')
def index():
    """The "main" page of the website"""
    return render_template("index.html", error=False)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Login page of the website"""
    return render_template("login.html", error=True)

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register the user"""
    return render_template("register.html", error=False)


@app.route('/pre-algebra')
def prealgebra():
    """pre-algebra"""
    return render_template("pre-algebra.html", error=False)


if __name__ == "__main__":
  app.run()
