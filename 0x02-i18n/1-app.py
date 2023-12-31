#!/usr/bin/env python3
"""
flask_babel app
"""
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config(object):
    """config for your Flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """render template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
