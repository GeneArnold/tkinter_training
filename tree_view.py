import tkinter as tk
from tkinter import ttk
from random import choice

# create a window
window = tk.Tk()
window.title('Treeview')
window.geometry('600x400')

# data 
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

# treeview
table = ttk.Treeview(window, columns=('first','last','email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both',expand=True)

# insert values into a table
# table.insert(parent='', index=0, values=('John','Doe','j@email'))

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first[0]}.{last}@email.com"
    data = (first, last, email)
    table.insert(parent='',index=0, values=data)

table.insert(parent='', index=tk.END, values=('XXXXX','YYYYY','ZZZZZ'))

def items_select(_):
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)

# events
table.bind('<<TreeviewSelect>>', items_select)
table.bind("<Delete>", delete_items)




#run
window.mainloop()