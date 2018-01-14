from flask import request, render_template, url_for, flash, redirect

@app.route("/")
def index():
    return render_template("index.html")
