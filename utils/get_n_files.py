from os.path import getmtime
from datetime import datetime
from time import time
import pandas as pd
import sqlite3


def print_n_files():
    connection = sqlite3.connect("data/db.db")
    n_files = int(pd.read_sql_query("""SELECT COUNT(*)
                                       FROM files""", connection).iloc[0, 0])
    connection.close()
    print("There are", n_files, "files on hard drive")


def get_n_files():
    current_time = time()
    try:
        time_last_modified = getmtime("data/db.db")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_last_modified)
        if delta.days >= 2:
            print("Database on files should be updated!")
        print_n_files()
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__get_n_files__':
    get_n_files()
