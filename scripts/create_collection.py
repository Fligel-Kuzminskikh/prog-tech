import sys

sys.path = ["C:\\Users\\User\\prog-tech"] + sys.path

from staff import collector

# Initializes collector object
c = collector.Collector()


# Collects data on files in hard drive
def collect_files_data():
    c.get_list_files_names_paths()
    c.get_list_sizes()
    c.get_list_dates_created()
    c.get_list_dates_last_modified()
    c.get_meta_data_pdf()
    c.get_meta_data_images()
    c.get_metadata_ms_office()


# Initiates create_collection function
def create_collection():
    collect_files_data()
    # Creates files.csv after data are collected
    c.create_files_database()


# Executes create_collection
if __name__ == '__create_collection__':
    create_collection()
