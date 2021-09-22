import Tkinter
from Tkinter import Entry
from Config import dict_entry


class EntryWidget:

    # To get Value from entry use entry_obj[index].get() of predefined function
    entry_obj = []

    def __init__(self):
        pass

    @staticmethod
    def create_entries(root):
        for entries in dict_entry:
            entry = Entry(root)
            entry.grid(row=entries["row"], column=entries["col"], padx=10, pady=10)
            EntryWidget.entry_obj.append(entry)

    @staticmethod
    def clear_all_entry():
        for entries in EntryWidget.entry_obj:
            entries.delete(0, Tkinter.END)

    @staticmethod
    def clear_one_entry(index):
        EntryWidget.entry_obj[index].delete(0, Tkinter.END)