from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import compute
#import model

class InputForm(Form):
    r = FloatField()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/form1", methods=["GET", "POST"])
def index():
    form = InputForm(request.form)
    if request.method == "POST":
        r = form.r.data
        s = compute(r)
        print("aaa")
        return render_template("viewoutput.html", form = form, s = s)
    else:
        return render_template("viewoutput.html", form = form)

if __name__ == "__main__":
  app.run()
