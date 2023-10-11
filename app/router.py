from main import app
from pydantic.error_wrappers import ValidationError
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
    if request.method == "POST" and "username" not in session:
        userform = schemas.LoginSchema(
            username=request.form["username"], password=request.form["password"]
        )
        if services.UserCheck.check(userform):
            session["username"] = userform.username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password")

    elif request.method == "POST" and "username" in session:
        return render_template("login.html", error="Please logout in home page.")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST" and "username" not in session:
        if not services.UserManager.get_by_name(request.form["username"]):
            try:
                register_schema = schemas.RegisterSchema(
                    username=request.form["username"],
                    email=request.form["email"],
                    password=request.form["password"],
                )
            except ValidationError:
                return render_template("register.html", error="email incorrect")
            services.UserCRUD.register_to_user(register_schema)
            return redirect(url_for("login"))

        else:
            return render_template("register.html", error="This username in database")
    elif request.method == "POST" and "username" in session:
        return render_template("register.html", error="Please logout in home page.")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
