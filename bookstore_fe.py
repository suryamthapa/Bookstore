"""
So, this is the front end of the dictionary project.
I am using the tkinter as instructed in the video which is the reference of this project.
(Don't hesitate to take the help of tutorials.)
----------
Learnings:
----------
1. about tkinter user interface
Like kivy, it is also a gui offered built in by python.
Specially, it is used to build the desktop applications.
It gives the old look. But customizing is very easy for a begineer.
While in kivy, it is difficult to operate things. You must have some knowledge 
on OOP if you want to start building applications in kivy.
2. The concepts about front end display and user interfaces.
"""

# Importing tkinter
from tkinter import *
# Importing the backend file of this project.
from bookstore_be import *

window = Tk()
window.geometry()
window.title("Book Store")
# print(dir(window))

# TO add an entry


def add():
    title = title_var.get()
    author = author_var.get()
    try:
        year = year_var.get()
        isbn = isbn_var.get()
        insert(title, author, year, isbn)
        text.insert(END, "ADDED SUCCESSFULLY!")
        text.delete(0, "end")
    except:
        text.delete(0, "end")
        text.insert(END, "You have given invalid ISBN or Year.")

# To view the existing entries


def view_command():
    result = view()
    text.delete(0, "end")
    for row in result:
        text.insert(END, row)
# To search the existing entries


def search_command():
    title = title_var.get()
    author = author_var.get()
    try:
        year = year_var.get()
        isbn = isbn_var.get()
        result = search(title, author, year, isbn)
        text.delete(0, "end")
        for row in result:
            text.insert(END, row)
    except:
        text.delete(0, "end")
        text.insert(END, "You have given invalid ISBN or Year.")
# To update an entry


def update_command():
    try:
        id_of = selected[0]
        new_title = title_var.get()
        new_author = author_var.get()
        new_year = year_var.get()
        new_isbn = isbn_var.get()
        update(id_of, new_title, new_author, new_year, new_isbn)
        text.delete(0, "end")
        text.insert(END, "UPDATED SUCCESSFULLY!")
    except:
        text.delete(0, "end")
        text.insert(END, "INCOMPLETE INFORMATION!")
# To select the row in the list box


def row_selection(event):
    """
    The basic idea is to select the row,
    which we want to update/delete.
    When we click over a row in the list box,
    it will be selected.
    Specially, listbox provides the capability to 
    get access to the selected rows.
    using curselection() we can access the contents of the row.
    """
    index = text.curselection()[0]
    global selected
    selected = text.get(index)
    # Deleting the existing texts
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    isbn_entry.delete(0, END)
    # Writing the respective entry
    title_entry.insert(END, selected[1])
    author_entry.insert(END, selected[2])
    year_entry.insert(END, selected[3])
    isbn_entry.insert(END, selected[4])
# To delete an entry


def delete_command():
    id_of = selected[0]
    delete(id_of)


# title label
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
# title entry
title_var = StringVar()
title_entry = Entry(window, textvariable=title_var)
title_entry.grid(row=0, column=1)
# author label
l2 = Label(window, text="Author")
l2.grid(row=0, column=3)
# author entry
author_var = StringVar()
author_entry = Entry(window, textvariable=author_var)
author_entry.grid(row=0, column=4)
# year label
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
# year entry
year_var = StringVar()
year_entry = Entry(window, textvariable=year_var)
year_entry.grid(row=1, column=1)
# isbn label
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=3)
# isbn entry
isbn_var = StringVar()
isbn_entry = Entry(window, textvariable=isbn_var)
isbn_entry.grid(row=1, column=4)
# scroll bar
sb1 = Scrollbar(window, width=30)
sb1.grid(row=3, column=3, rowspan=5)
# List box to display the entries
text = Listbox(window, height=10, width=30)
text.grid(row=3, rowspan=6, columnspan=2)
# Configuration
# Connecting the the scroll bar with listbox
text.configure(yscrollcommand=sb1)
sb1.configure(command=text.yview)
text.bind("<<ListboxSelect>>", row_selection)
# Buttons
view_all = Button(window, text="View All", command=view_command)
view_all.grid(row=3, column=4)
search_entry = Button(window, text="Search Entry", command=search_command)
search_entry.grid(row=4, column=4)
add_entry = Button(window, text="Add Entry", command=add)
add_entry.grid(row=5, column=4)
up_sel = Button(window, text="Update Selected", command=update_command)
up_sel.grid(row=6, column=4)
del_sel = Button(window, text="Delete Selected", command=delete_command)
del_sel.grid(row=7, column=4)
close = Button(window, text="Close", command=window.destroy)
close.grid(row=8, column=4)
# Running the main loop of the window
window.mainloop()
