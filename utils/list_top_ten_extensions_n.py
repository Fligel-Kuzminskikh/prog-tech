from os.path import getctime
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
    print(top_ten_extensions_n)


def list_top_ten_extensions_n():
    current_time = time()
    try:
        time_created = getctime("data/db.db")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_created)
        if delta.days >= 2:
            print("Database on files should be updated!")
        get_files_extension_print_top_ten_extensions()
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__list_top_ten_extensions_n__':
    list_top_ten_extensions_n()
