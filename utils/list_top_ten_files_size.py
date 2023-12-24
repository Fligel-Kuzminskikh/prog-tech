from os.path import getmtime
from datetime import datetime
from time import time
import pandas as pd
import sqlite3

pd.options.display.float_format = '{:.0f}'.format


def print_top_files_size():
    connection = sqlite3.connect("data/db.db")
    top_ten_files_size = pd.read_sql_query("""SELECT name, size_in_bytes
                                              FROM files
                                              ORDER BY size_in_bytes DESC
                                              LIMIT 10""", connection)
    connection.close()
    # print(top_ten_files_size)
    return top_ten_files_size


def list_top_ten_files_size():
    current_time = time()
    try:
        time_last_modified = getmtime("data/db.db")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_last_modified)
        if delta.days >= 2:
            print("Database on files should be updated!")
        return print_top_files_size()
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__list_top_ten_files_size__':
    list_top_ten_files_size()
