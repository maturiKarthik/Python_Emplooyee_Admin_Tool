import Tkconstants
import Tkinter
import random
from Tkinter import *
from label_widget import *
from entry_widget import *
from table_widget import *
from Config import dict_table


def get_value_from_entry(event):
    new_emp = {
        "name": EntryWidget.entry_obj[0].get(),
        "address": EntryWidget.entry_obj[1].get(),
        "telephone": EntryWidget.entry_obj[2].get(),
        "email": EntryWidget.entry_obj[3].get(),
        "id": EntryWidget.entry_obj[4].get()
    }
    dict_table.append(new_emp)
    TableWidget.create_table_cols(scrollable_frame)
    TableWidget.create_table(scrollable_frame)
    EntryWidget.clear_all_entry()


# Creates random Id
def set_random_id(event):
    id = random.randint(1000, 9000)
    EntryWidget.clear_one_entry(4)
    EntryWidget.entry_obj[4].insert(0, 'FR' + str(id))


window = Tkinter.Tk()
window.title("Admin Management Tool")
window.geometry("1300x400")
# Start of Frame Left
frame_left = LabelFrame(window, text="Enter Employee", padx=5, pady=5, borderwidth=5)
frame_left.grid(row=0, column=0, padx=15, pady=15)
# widgets to be displayed on left panel
LabelWidget.create_label(frame_left)
EntryWidget.create_entries(frame_left)
# Button Submit
button_submit = Tkinter.Button(frame_left, text="Submit", highlightbackground='#3E4149')
button_submit.grid(row=7, column=1)
button_submit.bind('<Button-1>', get_value_from_entry)
# # Button Random ID
button_random = Tkinter.Button(frame_left, text="Gen_ID", highlightbackground='blue')
button_random.grid(row=4, column=2)
button_random.bind("<Button-1>", set_random_id)
# ELF => End  Left Panel

# Right Panel widget
frame_right = LabelFrame(window, text="Employee List", width=1600, height=690, borderwidth=5)
frame_right.grid_propagate(0)
frame_right.grid(row=0, column=1, padx=15, pady=15, sticky="E")

canvas = Canvas(frame_right)
scrollbar = Scrollbar(frame_right, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

TableWidget.create_table_cols(scrollable_frame)
TableWidget.create_table(scrollable_frame)

frame_right.grid(column=1, row=0)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# End of Right panel
window.mainloop()
