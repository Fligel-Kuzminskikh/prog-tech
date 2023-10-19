import os

from numpy import nan
from tqdm import tqdm
from os.path import join
from re import findall
from pandas import pandas as pd
from filesmeta import dispatcher
pd.options.display.float_format = '{:.0f}'.format


class Collector:
    dispatcher = dispatcher.Dispatcher()
    meta_data_pdf = pd.DataFrame()
    meta_data_images = pd.DataFrame()
    meta_data_ms_office = pd.DataFrame()
    # Writes hard drive's path
    #path_hard_drive = "\\"
    path_hard_drive = "C:\\Users\\User\\Desktop\\Практика"
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
                self.dispatcher.worker_all.filepath = joint_file
                self.list_sizes.append(self.dispatcher.worker_all.get_size())
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
                self.dispatcher.worker_all.filepath = joint_file
                self.list_dates_created.append(self.dispatcher.worker_all.get_time_creation())
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
                self.dispatcher.worker_all.filepath = joint_file
                self.list_dates_changed.append(self.dispatcher.worker_all.get_time_modification())
            # In case of error, it writes numpy's nan
            except:
                self.list_dates_changed.append(nan)

    def get_meta_data_pdf(self):
        for file in tqdm(zip(self.list_paths, self.list_names)):
            try:
                joint_file = join(file[0], file[1])
                if findall(pattern=r"\.pdf$", string=joint_file):
                    self.dispatcher.worker_pdf.pdf_paths.append(joint_file)
            except:
                pass
        self.meta_data_pdf = self.dispatcher.worker_pdf.get_pdf_meta_data()

    def get_meta_data_images(self):
        for file in tqdm(zip(self.list_paths, self.list_names)):
            try:
                joint_file = join(file[0], file[1])
                if findall(pattern=r"\.[Jj][Pp][Gg]$|\.[Pp][Nn][Gg]$", string=joint_file):
                    self.dispatcher.worker_images.image_paths.append(joint_file)
            except:
                pass
        self.meta_data_images = self.dispatcher.worker_images.get_exif_data()

    def get_metadata_ms_office(self):
        for file in tqdm(zip(self.list_paths, self.list_names)):
            try:
                joint_file = join(file[0], file[1])
                if findall(pattern=r"\.docx$", string=joint_file):
                    self.dispatcher.worker_ms_office.docx_paths.append(joint_file)
                elif findall(pattern=r"\.pptx$", string=joint_file):
                    self.dispatcher.worker_ms_office.docx_paths.append(joint_file)
                elif findall(pattern=r"\.xl[st][xm]$", string=joint_file):
                    self.dispatcher.worker_ms_office.xl_paths.append(joint_file)
            except:
                pass
        self.meta_data_ms_office = self.dispatcher.worker_ms_office.get_metadata_ms_office()

    # Creates data-set and saves it as .csv file
    def create_files_database(self):
        # Create pandas dataframe that stores lists with necessary data on files
        files_database = pd.DataFrame(data={"name": self.list_names, "path": self.list_paths,
                                            "size_in_gigabytes": self.list_sizes,
                                            "date_created": self.list_dates_created,
                                            "date_last_changed": self.list_dates_changed})
        files_database["filepath"] = files_database["path"] + "\\" + files_database["name"]
        files_database = files_database.merge(right=self.meta_data_pdf, how="left", left_on="filepath",
                                              right_on="pdf_path")
        files_database = files_database.merge(right=self.meta_data_images, how="left", left_on="filepath",
                                              right_on="image_path")
        files_database = files_database.merge(right=self.meta_data_ms_office, how="left", on="filepath")
        files_database.drop(columns=["filepath", "image_path", "pdf_path"], inplace=True)
        # Saves dataframe as .csv file
        files_database.to_csv(path_or_buf="data/files.csv", header=True, index=False, decimal=".", sep=",",
                              encoding="utf-8")
