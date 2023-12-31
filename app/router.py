from main import app
from pydantic.error_wrappers import ValidationError
import schemas
import services
from flask import render_template, request, redirect, url_for, session


@app.route("/update_bank/<uuid:id>", methods=["GET", "POST"])
def update_bank(id):
    if "username" not in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        bank = schemas.BankSchema(
            id=request.form.get("id"),
            bank_name=request.form.get("bank_name"),
            bik=request.form.get("bik"),
            kor_score=request.form.get("kor_score"),
            swift=request.form.get("swift"),
            iban=request.form.get("iban"),
            user_id=session["uuid"],
        )
        services.BankCRUD.update(bank)
        return redirect(url_for("home"))
    return render_template(
        "update_bank.html",
        bank_req=services.BankManager.get_bank_by_id(id),
    )


@app.route("/add_bank", methods=["GET", "POST"])
def add_bank():
    if "username" not in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        bank = schemas.BankSchema(
            bank_name=request.form.get("bank_name"),
            bik=request.form.get("bik"),
            kor_score=request.form.get("kor_score"),
            swift=request.form.get("swift"),
            iban=request.form.get("iban"),
            user_id=session["uuid"],
        )
        services.BankCRUD.create(bank)
        return redirect(url_for("home"))
    return render_template("add_bank.html")


@app.route("/delete_bank", methods=["GET", "POST"])
def delete_bank():
    if "username" not in session:
        return redirect(url_for("home"))
    if request.method == "POST" and "username" in session:
        bank_to_delete = request.form.get("bank_to_delete")
        services.BankCRUD.delete(bank_to_delete)
        return redirect(url_for("home"))

    return render_template(
        "delete_bank.html", user_banks=services.UserManager.get_banks(session["uuid"])
    )


@app.route("/", methods=["GET", "POST"])
def home():
    if "username" in session:
        if request.method == "POST":
            services.UserManager.set_active_bank(
                request.form.get(session["username"]), session["uuid"]
            )
        return render_template(
            "index.html",
            username=session["username"],
            user_banks=services.UserManager.get_banks(session["uuid"]),
        )
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
            session["uuid"] = services.UserManager.get_by_name_not_bool(
                userform.username
            ).id
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
            register_schema = schemas.RegisterSchema(
                username=request.form["username"],
                password=request.form["password"],
            )
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
    session.pop("uuid", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
