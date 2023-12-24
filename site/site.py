import sys

sys.path = ["C:\\Users\\User\\prog-tech"] + sys.path

from flask import Flask
from datetime import datetime
from flask import render_template
from utils.get_n_files import get_n_files
from utils.list_top_ten_extensions_n import list_top_ten_extensions_n
from utils.list_top_ten_files_size import list_top_ten_files_size

app = Flask(__name__)


@app.route("/")
def main():
    # current_date_time = datetime.now()
    # filenames = get_filenames()
    n_files, time_last_modified = get_n_files()
    return render_template("main.html", n_files=n_files, time_last_modified=time_last_modified)
    # current_date_time=current_date_time, filenames=filenames)


@app.route("/extensions")
def extensions():
    top_ten_extensions_n = list_top_ten_extensions_n().values.tolist()
    # return "<h1>О проекте</h1><p>Нашему сайту около 15 минут</p>"
    return render_template("extensions.html", top_ten_extensions_n=top_ten_extensions_n)


@app.route("/sizes")
def extensions():
    top_ten_extensions_n = list_top_ten_extensions_n().values.tolist()
    # return "<h1>О проекте</h1><p>Нашему сайту около 15 минут</p>"
    return render_template("sizes.html", top_ten_extensions_n=top_ten_extensions_n)


app.run(port=1488)
