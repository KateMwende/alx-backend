#!/usr/bin/env python3
"""
Use Babel
"""
from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config(object):
    """configure app with babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """render a template"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """choose language"""
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    

if __name__ == '__main__':
    app.run()
