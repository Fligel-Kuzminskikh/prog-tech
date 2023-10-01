from os.path import getctime
from datetime import datetime
from time import time
import pandas as pd

pd.options.display.float_format = '{:.0f}'.format


def upload_files_database():
    files_database = pd.read_csv("C:\\Users\\User\\prog-tech\\data\\files.csv")
    return files_database


def print_top_files_size(files_database):
    print(files_database.sort_values("size_in_gigabytes", ascending=False).head(10)[['name', 'size_in_gigabytes']])


def list_top_ten_files_size():
    current_time = time()
    try:
        time_created = getctime("C:\\Users\\User\\prog-tech\\data\\files.csv")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_created)
        if delta.days >= 2:
            print("Database on files should be updated!")
        files_database = upload_files_database()
        print_top_files_size(files_database=files_database)
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__list_top_ten_files_size__':
    list_top_ten_files_size()
