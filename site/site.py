import sys

sys.path = ["C:\\Users\\User\\prog-tech"] + sys.path

from flask import Flask
from datetime import datetime
from flask import render_template
from utils.get_n_files import get_n_files

app = Flask(__name__)


@app.route("/")
def hello_world():
    # current_date_time = datetime.now()
    # filenames = get_filenames()
    n_files, time_last_modified = get_n_files()
    return render_template("main.html", n_files=n_files, time_last_modified=time_last_modified)
    # current_date_time=current_date_time, filenames=filenames)


def get_filenames():
    return ["a.html", "forme.txt", "доклад.docx"]


@app.route("/extensions")
def hello_word():
    # return "<h1>О проекте</h1><p>Нашему сайту около 15 минут</p>"
    return render_template("extensions.html")


app.run(port=1488)
