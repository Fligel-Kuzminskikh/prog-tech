from os.path import getctime
from datetime import datetime
from time import time
import pandas as pd


def upload_files_database():
    files_database = pd.read_csv("C:\\Users\\User\\prog-tech\\data\\files.csv")
    return files_database


def print_n_files(files_database):
    print("There are", files_database.shape[0], "files on hard drive")


def get_n_files():
    current_time = time()
    try:
        time_created = getctime("C:\\Users\\User\\prog-tech\\data\\files.csv")
        delta = datetime.fromtimestamp(current_time) - datetime.fromtimestamp(time_created)
        if delta.days >= 2:
            print("Database on files should be updated!")
        files_database = upload_files_database()
        print_n_files(files_database=files_database)
    except:
        print("Database on hard drive's files is not created!")


if __name__ == '__get_n_files__':
    get_n_files()
