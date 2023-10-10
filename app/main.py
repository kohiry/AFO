from flask import Flask
from config import DBConfig

app = Flask(__name__, template_folder="/templates")
app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_url()



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
