from datetime import datetime

start_time = datetime.now()

import os

from numpy import nan
from os.path import join, getsize
import pandas as pd
pd.options.display.float_format = '{:.0f}'.format


def get_list_files():
    list_files = list()
    for root, dirs, files in os.walk("\\"):
        list_files += [join(root, file) for file in files]
    return list_files


def get_list_sizes(list_files):
    list_sizes = list()
    for file in list_files:
        try:
            list_sizes.append(getsize(file))
        except:
            list_sizes.append(nan)
    return list_sizes


def get_top_files_size(list_files, list_sizes):
    return pd.DataFrame({"file": list_files, "size": list_sizes}).sort_values("size", ascending=False).head(10)


def print_top_files_size(top):
    print("file", "\t", "size")
    for file_size in zip(top["file"], top["size"]):
        print(file_size[0], "\t", file_size[1])


def main():
    list_files = get_list_files()
    list_sizes = get_list_sizes(list_files=list_files)
    top = get_top_files_size(list_files=list_files, list_sizes=list_sizes)
    print_top_files_size(top)
    print("Execution took", datetime.now() - start_time)

if __name__ == '__main__':
    main()
