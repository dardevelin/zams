from flask import request, render_template, url_for, flash, redirect

from .database import session
from . import app

@app.route("/")
def index():
    return render_template("index.html")
