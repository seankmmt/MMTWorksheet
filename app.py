#requisites
from flask import Flask, Blueprint, render_template, abort, Markup
from jinja2 import TemplateNotFound

#logic package imports

app = Flask(__name__)

# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
#app.config.from_object('config.DevConfig')

@app.route("/")
def index():
    return  render_template('index.html')


if __name__=='__main__':
    app.run(debug=False)