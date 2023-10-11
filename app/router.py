from main import app
import schemas
import services
from flask import render_template, request, redirect, url_for, session


@app.route("/")
def home():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    else:
        return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userform = schemas.LoginSchema(
            username=request.form["username"], password=request.form["password"]
        )
        if services.UserCheck.check(userform):
            session["username"] = userform.username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
