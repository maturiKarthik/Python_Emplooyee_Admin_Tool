import tkFont
from Tkinter import Label

from Config import dict_label


class LabelWidget:

    def __init__(self):
        pass

    @staticmethod
    def create_label(root):
        for labels in dict_label:
            fonts = tkFont.Font(family=labels["font_type"], size=labels["font_size"])
            label = Label(root, text=labels["title"], font=fonts,
                          padx=labels["padx"], pady=labels["pady"])
            label.grid(row=labels["row"], column=labels["col"])
