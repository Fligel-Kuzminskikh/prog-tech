from tkinter import *
from tkinter import ttk
from utils.get_n_files import get_n_files
from utils.list_top_ten_extensions_n import list_top_ten_extensions_n
from utils.list_top_ten_files_size import list_top_ten_files_size

tk = Tk()

top_ten_extensions_n = list_top_ten_extensions_n()
column_names = top_ten_extensions_n.columns.to_list()
top_ten_extensions_n["№"] = list(top_ten_extensions_n.index)
top_ten_extensions_n = top_ten_extensions_n[["№"]+column_names]
top_ten_files_size = list_top_ten_files_size()
column_names_2 = top_ten_files_size.columns.to_list()
top_ten_files_size["№"] = list(top_ten_files_size.index)
top_ten_files_size = top_ten_files_size[["№"]+column_names_2]
top_ten_files_size["№"] = top_ten_files_size["№"] + 1
top_ten_extensions_n["№"] = top_ten_extensions_n["№"] + 1

column_names = ("№", "Расширение", "Количество файлов")
top_ten_extensions_n_list = top_ten_extensions_n.values.tolist()
top_ten_extensions_n_list = [tuple(sublist) for sublist in top_ten_extensions_n_list]
column_names_2 = ("№", "Имя файла", "Размер в битах")
top_ten_files_size_list = top_ten_files_size.values.tolist()
top_ten_files_size_list = [tuple(sublist) for sublist in top_ten_files_size_list]
path = StringVar()
n_files = StringVar()
time_last_modified = StringVar()
path_str = "Жёсткий диск"
n_files_str, time_last_modified_str = get_n_files()

label = Label(tk, textvariable=n_files,
              font=("Courier", "14"))
label_2 = Label(tk, textvariable=time_last_modified,
                font=("Courier", "14"))
label_3 = Label(tk, textvariable=path,
                font=("Courier", "14"), underline=0)

path.set(path_str)
label_3.pack()
n_files.set(("Количество файлов:" + " " + str(n_files_str)))
label.pack()
time_last_modified.set(("Время последнего обновления:" + " " + str(time_last_modified_str)))
label_2.pack()


def show_sizes():
    _tk_2 = Tk()
    _tk_2.title("Топ-10 файлов по размеру")
    tree_2 = ttk.Treeview(_tk_2, columns=column_names_2, show="headings")
    tree_2.pack(fill=BOTH, expand=1)

    tree_2.heading("№", text="№", anchor=W)
    tree_2.heading("Имя файла", text="Имя файла", anchor=W)
    tree_2.heading("Размер в битах", text="Размер в битах", anchor=W)

    tree_2.column("#1", stretch=NO, width=125)
    tree_2.column("#2", stretch=NO, width=125)
    tree_2.column("#3", stretch=NO, width=125)

    for file_size_list in top_ten_files_size_list:
        tree_2.insert("", END, values=file_size_list)


def show_extensions():
    _tk = Tk()
    _tk.title("Топ-10 расширений по количеству файлов")
    tree = ttk.Treeview(_tk, columns=column_names, show="headings")
    tree.pack(fill=BOTH, expand=1)

    tree.heading("№", text="№", anchor=W)
    tree.heading("Расширение", text="Расширение", anchor=W)
    tree.heading("Количество файлов", text="Количество файлов", anchor=W)

    tree.column("#1", stretch=NO, width=125)
    tree.column("#2", stretch=NO, width=125)
    tree.column("#3", stretch=NO, width=125)

    for extensions_n_list in top_ten_extensions_n_list:
        tree.insert("", END, values=extensions_n_list)


menubar = Menu(tk)
menu_extensions = Menu(menubar)
menu_sizes = Menu(menubar)
menubar.add_cascade(menu=menu_extensions, label='Топ-10 расширений по количеству файлов')
menubar.add_cascade(menu=menu_sizes, label='Топ-10 файлов по размеру')
menu_extensions.add_command(label='Показать статистику', command=show_extensions)
menu_sizes.add_command(label='Показать статистику', command=show_sizes)
tk['menu'] = menubar


tk.title("Коллектор")
tk.geometry("500x150")

tk.mainloop()
