import os

from flask import Flask

# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev'
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/')
def hello():
    return """<!DOCTYPE html>
        <html>
        <head>
	        <meta charset="utf-8"/>
	        <title>Flask example Biography</title>
        </head>
        <body>
	        <h1>About Me</h1>
		        <div>Hello my name is Seán. I am a 3rd year student at Technological University Dublin.
		        Visit (the current IP address)/contanct-me to contact me.</div>

        </body>
        </html>"""

@app.route('contact-me')
def contact():
    return """<a href="mailto:c18332623@mytudublin.ie">Click to send me an email.</a>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0")
