#!/usr/bin/env python3
"""parametrize template
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """FLask Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """local selector"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_local():
    "inject locale in templates"
    return {'locale': get_locale()}


@app.route('/')
def index():
    """index page"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
