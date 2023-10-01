from datetime import datetime

start_time = datetime.now()

import os

from os.path import join


def get_list_files():
    list_files = list()
    for root, dirs, files in os.walk("\\"):
        list_files += [join(root, file) for file in files]
    return list_files


def print_n_files(list_files):
    print("There are", len(list_files), "files on the hard drive")


def main():
    print_n_files(list_files=get_list_files())
    print("Execution took", datetime.now() - start_time)


if __name__ == '__main__':
    main()
