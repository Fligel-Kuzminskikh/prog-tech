from os.path import getctime
from datetime import datetime
from time import time
import pandas as pd
import sqlite3

pd.options.display.float_format = '{:.0f}'.format


def print_top_files_size():
    connection = sqlite3.connect("data/db.db")
    top_ten_files_size = pd.read_sql_query("""SELECT name, size_in_gigabytes
                                              FROM files
                                              ORDER BY size_in_gigabytes DESC
                                              LIMIT 10""", connection)
    connection.close()
    print(top_ten_files_size)


def list_top_ten_files_size():
    current_time = time()
    try:
        time_created = getctime("data/db.db")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_created)
        if delta.days >= 2:
            print("Database on files should be updated!")
        print_top_files_size()
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__list_top_ten_files_size__':
    list_top_ten_files_size()
