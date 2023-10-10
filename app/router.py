from main import app


@app.route("/")
@app.route("/index")
def hello_world():
    return "aboba"


if __name__ == "__main__":
    app.run(debug=True)
