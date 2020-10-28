import os

from flask import Flask


def __init__(self):
    def create_app(test_config=None):
        # create and configure the app
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        # a simple page that says hello
        @app.route('/')
        def hello():
            open('index.html', 'r', 'utf-8')

        @app.route('contact-me')
        def contact():
            return """<a href="mailto:c18332623@mytudublin.ie">Click to send me an email.</a>"""

        return app



