from os.path import getctime
from datetime import datetime
from time import time
import pandas as pd


def upload_files_database():
    files_database = pd.read_csv("C:\\Users\\User\\prog-tech\\data\\files.csv")
    return files_database


def get_files_extension_print_top_ten_extensions(files_database):
    files_database['extension'] = files_database.name.str.extract(r"((?<=\.)[A-Za-z]+$)")
    print("extension", "\t", "n")
    print(files_database.extension.value_counts()[:10])


def list_top_ten_extensions_n():
    current_time = time()
    try:
        time_created = getctime("C:\\Users\\User\\prog-tech\\data\\files.csv")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_created)
        if delta.days >= 2:
            print("Database on files should be updated!")
        files_database = upload_files_database()
        get_files_extension_print_top_ten_extensions(files_database=files_database)
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__list_top_ten_extensions_n__':
    list_top_ten_extensions_n()
