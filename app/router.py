from main import app
from flask import render_template, flash, redirect, url_for, request
from wtforms import Form, StringField, PasswordField, validators
from sqlalchemy import Column, Integer, String
from forms import RegistrationForm, LoginForm


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        print(request.form["email"])
        print(request.form["password"])
        return redirect(url_for("success", email=request.form["email"]))
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    # создаем экземпляр класса формы
    form = RegistrationForm(request.form)
    # если HTTP-метод POST и данные формы валидны
    if request.method == "POST" and form.validate():
        flash("Спасибо за регистрацию")
        # return redirect(url_for("login"))
    # если HTTP-метод GET, то просто отрисовываем форму
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
