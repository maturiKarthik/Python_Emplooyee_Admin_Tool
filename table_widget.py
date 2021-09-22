from Config import dict_table
from Tkinter import Label


class TableWidget:

    def __init__(self):
        pass

    @staticmethod
    def create_table(root):
        for table in range(len(dict_table)):
            col_name = list(dict_table[0].keys())
            for col_index in range(len(col_name)):
                Label(root, text=dict_table[table][col_name[col_index]], padx=5, pady=5, borderwidth=5).grid(
                    row=table + 1,
                    column=col_index)

    @staticmethod
    def create_table_cols(root):
        col_name = list(dict_table[0].keys())
        for title_index in range(len(col_name)):
            Label(root, bg="gray", text=str(col_name[title_index]).upper(), padx=5, pady=5, borderwidth=5).grid(row=0,
                                                                                                                column=title_index)
