'''
This is our GUI file (the main file to run)

A program that stores this book information:

Title
Author
Year
ISBN

User can:

View all records
Search an entry
Update entry
Delete entry
Close
'''

from tkinter import *
from backend import Database # import Database class from backend script

# create a Database object
database = Database("books.db")

'''
Where we write our command (wrapper) functions
'''
def get_selected_row(event):
    try: # try to execute indented block
        global selected_tuple # makes this a global variable
        index = list1.curselection()[0] # as prints out tuple
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2]) # grab the author name
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3]) # grab the year
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4]) # grab the isbn
    except IndexError: # except when there is an index error
        pass # do nothing

def view_command():
    list1.delete(0, END) # ensures we delete everything from 0 to last row
                         # so as to not print duplicates (edge case)
    for row in database.view():
        list1.insert(END, row) # new rows will be put at the END of the listbox

def search_command():
    list1.delete(0, END) # empty the list
    for row in database.search(title_text.get(), author_text.get(),\
                              year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(),\
                   year_text.get(), isbn_text.get())
    list1.delete(0, END)
    # let user know the add was successful by displaying entry information
    list1.insert(END, (title_text.get(), author_text.get(),\
                 year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(),\
                 year_text.get(), isbn_text.get())
                 
'''
END command functions
'''

window = Tk() # creates a window

window.wm_title("Book Store") # adds title to window's title bar

''' Create labels '''
# create a Title label
l1 = Label(window, text = "Title")

# use grid method to set its place in the window
l1.grid(row = 0, column = 0)

# create Author label
l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

# create Year label
l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

# create ISBN label
l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

''' Add entry fields '''
title_text = StringVar() # this line is required!
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar() # this line is required!
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar() # this line is required!
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar() # this line is required!
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

''' Create list box '''
list1 = Listbox(window, height = 6, width = 35)
#list1.grid(row = 2, column = 0) # Note: this format occupies only the first cell!
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

''' Create scrollbar '''
sb1 = Scrollbar(window) # window parameter attaches our object to window
sb1.grid(row = 2, column = 2, rowspan = 6) # helps to draw a grid to visualize

list1.configure(yscrollcommand = sb1.set) # vertical scroll bar set to sb1
sb1.configure(command = list1.yview) # we pass a command parameter, which means
                                     # when we scroll the bar, the vertical view
                                     # of the list will change
list1.bind('<<ListboxSelect>>', get_selected_row)

''' Create buttons '''
b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop() # keeps window open until closed by user
