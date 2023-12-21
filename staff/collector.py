import os

from tqdm import tqdm
import pandas as pd
from filesmeta.dispatcher import Dispatcher
import sqlite3
pd.options.display.float_format = '{:.0f}'.format


class Collector:
    dispatcher = Dispatcher()
    # path_hard_drive = "\\"
    data_files = list()
    path_hard_drive = "C:\\Users\\User\\Desktop"

    def collect_data_files(self):
        """Iterates over directories in given root (e.g. hard drive). Extracts files' names, paths, size in gigabytes,
        date of creation, date of last modification and other metadata."""
        print("\n")
        print("Collecting data on files...")
        print("\n")
        for root, _, files in tqdm(os.walk(self.path_hard_drive)):
            for file in files:
                self.dispatcher.path = root
                self.dispatcher.name = file
                yield self.dispatcher.get_metadata_file()

    def create_collected_files_database(self):
        """Creates pandas dataframe that stores dictionaries with necessary data on files. Saves dataframe as .db
        file."""
        files_database = pd.DataFrame(list(self.collect_data_files()))
        query = files_database.dtypes == "object"
        columns = files_database.dtypes[query].index
        for column in columns:
            files_database[column] = files_database[column].astype("str")
        connection = sqlite3.connect("data/db.db")
        files_database.to_sql(name="files", con=connection, if_exists="replace", index=False)
        connection.close()
