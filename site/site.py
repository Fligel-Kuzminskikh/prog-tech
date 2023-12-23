from flask import Flask
from datetime import datetime
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    current_date_time = datetime.now()
    filenames = get_filenames()
    return render_template("main.html", current_date_time=current_date_time, filenames=filenames)


def get_filenames():
    return ["a.html", "forme.txt", "доклад.docx"]


@app.route("/about")
def hello_word():
    return "<h1>О проекте</h1><p>Нашему сайту около 15 минут</p>"


app.run(port=1488)
