#!/usr/bin/env python3
"""babel_setup
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """FLask Configuration"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, default_locale=Config.LANGUAGES[0], default_timezone='UTC')


@app.route('/')
def index():
    """index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
