# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask("Splinter Website")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
