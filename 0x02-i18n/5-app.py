#!/usr/bin/env python3
"""force_local_with_url_parameter
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """FLask Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """local selector"""
    langs = app.config['LANGUAGES']
    requested_lang = request.args.get('locale')
    user_lang = g.user.get('locale') if g.user else None

    if user_lang in langs:
        if requested_lang and langs:
            return requested_lang
        return user_lang
    if requested_lang in langs:
        return requested_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_local():
    "inject locale in templates"
    return {'locale': get_locale()}


def get_user(user_id):
    """get a logged in from a mock database"""
    user_id = int(user_id) if user_id else None
    if user_id not in users.keys():
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """executed before a request"""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@app.route('/')
def index():
    """index page"""
    user = getattr(g, 'user', None)
    username = user.get('name') if user else None
    return render_template('5-index.html', username=username)


if __name__ == "__main__":
    app.run(debug=True)
