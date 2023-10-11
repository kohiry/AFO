from main import app
from flask import render_template, request, redirect, url_for, session


@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    else:
        return render_template("index.html")


@app.route("/login")
def login():
    if request.method == "POST":
        username = request.form["username"]
        pwd = request.form["pwd"]


if __name__ == "__main__":
    app.run(debug=True)
