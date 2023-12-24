from os.path import getmtime
from datetime import datetime
from time import time
import pandas as pd
import sqlite3


def get_files_extension_print_top_ten_extensions():
    connection = sqlite3.connect("data/db.db")
    top_ten_extensions_n = pd.read_sql_query("""SELECT extension, COUNT(*) n
                                                FROM files
                                                GROUP BY extension
                                                ORDER BY n DESC
                                                LIMIT 10""", connection)
    connection.close()
    # print(top_ten_extensions_n)
    return top_ten_extensions_n


def list_top_ten_extensions_n():
    current_time = time()
    try:
        time_last_modified = getmtime("data/db.db")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_last_modified)
        if delta.days >= 2:
            print("Database on files should be updated!")
        return get_files_extension_print_top_ten_extensions()
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__list_top_ten_extensions_n__':
    list_top_ten_extensions_n()
