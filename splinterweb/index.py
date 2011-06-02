# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flaskext.babel import Babel

app = Flask("Splinter Website")
babel = Babel(app, default_locale='en')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<language>")
def set_language(language):
    if language in babel.list_translations():
        app.config['BABEL_DEFAULT_LOCALE'] = language
    return index()

if __name__ == '__main__':
    app.run(debug=True)
