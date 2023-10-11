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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not services.UserManager.get_by_name(request.form["username"]):
            register_schema = schemas.RegisterSchema(
                username=request.form["username"],
                email=request.form["email"],
                password=request.form["password"],
            )
            services.UserCRUD.register_to_user(register_schema)
            return redirect(url_for("login"))

        else:
            return render_template("register.html", error="This username in database")
    else:
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
