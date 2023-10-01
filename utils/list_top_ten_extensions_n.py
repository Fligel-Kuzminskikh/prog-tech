from datetime import datetime

start_time = datetime.now()

import os

from os.path import join
import pandas as pd


def get_list_files():
    list_files = list()
    for root, dirs, files in os.walk("\\"):
        list_files += [join(root, file) for file in files]
    return list_files


def get_files_extension(list_files):
    files = pd.DataFrame({"file": list_files})
    files['extension'] = files.file.str.extract(r"((?<=\.)[A-Za-z]+$)")
    return files


def print_top_ten_files_extensions(files_extensions):
    print("extension", "\t", "n")
    print(files_extensions.extension.value_counts()[:10])


def main():
    list_files = get_list_files()
    files_extensions = get_files_extension(list_files=list_files)
    print_top_ten_files_extensions(files_extensions=files_extensions)
    print("Execution took", datetime.now() - start_time)


if __name__ == '__main__':
    main()
