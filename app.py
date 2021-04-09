from flask import Flask, Blueprint, render_template, abort, Markup
from jinja2 import TemplateNotFound

app = Flask(__name__)

# set to True to inform that the app needs to be re-created
to_reload = False


def get_app():
    print("create app now")
    app = Flask(__name__)

    # to make sure of the new app instance
    now = datetime.now()

    @app.route("/")
    def index():
        return f"hello, the app started at %s" % now

    @app.route('/reload')
    def reload():
        global to_reload
        to_reload = True
        return "reloaded"

    return app


class AppReloader(object):
    def __init__(self, create_app):
        self.create_app = create_app
        self.app = create_app()

    def get_application(self):
        global to_reload
        if to_reload:
            self.app = self.create_app()
            to_reload = False

        return self.app

    def __call__(self, environ, start_response):
        app = self.get_application()
        return app(environ, start_response)


# This application object can be used in any WSGI server
# for example in gunicorn, you can run "gunicorn app"
application = AppReloader(get_app)

if __name__ == '__main__':
    run_simple('localhost', 5000, application,
               use_reloader=True, use_debugger=True, use_evalex=True)