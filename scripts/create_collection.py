import sys

sys.path = ["C:\\Users\\User\\prog-tech"] + sys.path

from staff import collector


c = collector.Collector()


def create_collection():
    """Creates "files" table in "db.db" database after data are collected."""
    c.create_collected_files_database()


# Executes create_collection
if __name__ == '__create_collection__':
    create_collection()
