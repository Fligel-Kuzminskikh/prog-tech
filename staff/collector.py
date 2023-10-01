import os

from numpy import nan
from tqdm import tqdm
from os.path import join, getsize, getctime, getmtime
from pandas import pandas as pd
pd.options.display.float_format = '{:.0f}'.format


class Collector:
    # Writes hard drive's path
    path_hard_drive = "\\"
    #path_hard_drive = "C:\\Users\\User\\Desktop\\Практика"
    # Initiates lists for files' names, paths, sizes, and dates when files were created and last changed
    list_names = list()
    list_paths = list()
    list_sizes = list()
    list_dates_created = list()
    list_dates_changed = list()

    # Extracts files' names and paths
    def get_list_files_names_paths(self):
        print("\n")
        print("Collecting files' names and paths")
        print("\n")
        # Iterates over directories in given root (hard drive)
        for root, dirs, files in tqdm(os.walk(self.path_hard_drive)):
            # Saves found names and paths in lists
            self.list_names += [name for name in files]
            self.list_paths += [root]*len(files)

    # Extracts files' sizes in gigabytes
    def get_list_sizes(self):
        print("\n")
        print("Collecting files' sizes")
        print("\n")
        # Iterates over files
        for file in tqdm(zip(self.list_paths, self.list_names)):
            # Tries to extract file's size and save into list in gigabytes
            try:
                joint_file = join(file[0], file[1])
                self.list_sizes.append(getsize(joint_file)/1000000000)
            # In case of error, it writes numpy's nan
            except:
                self.list_sizes.append(nan)

    # Extracts files' creation date
    def get_list_dates_created(self):
        print("\n")
        print("Collecting files' creation dates")
        print("\n")
        for file in tqdm(zip(self.list_paths, self.list_names)):
            # Tries to extract file's creation date and save into list
            try:
                joint_file = join(file[0], file[1])
                self.list_dates_created.append(getctime(joint_file))
            # In case of error, it writes numpy's nan
            except:
                self.list_dates_created.append(nan)

    # Extracts files' modification date
    def get_list_dates_last_modified(self):
        print("\n")
        print("Collecting files' last change dates")
        print("\n")
        for file in tqdm(zip(self.list_paths, self.list_names)):
            # Tries to extract file's modification date and save into list
            try:
                joint_file = join(file[0], file[1])
                self.list_dates_changed.append(getmtime(joint_file))
            # In case of error, it writes numpy's nan
            except:
                self.list_dates_changed.append(nan)

    # Creates data-set and saves it as .csv file
    def create_files_database(self):
        # Create pandas dataframe that stores lists with necessary data on files
        files_database = pd.DataFrame(data={"name": self.list_names, "path": self.list_paths,
                                            "size_in_gigabytes": self.list_sizes,
                                            "date_created": self.list_dates_created,
                                            "date_last_changed": self.list_dates_changed})
        # Saves dataframe as .csv file
        files_database.to_csv(path_or_buf="data/files.csv", header=True, index=False, decimal=".", sep=",",
                              encoding="utf-8")
