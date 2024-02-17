import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set("button pressed")


# create a window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('150x150')

# tkinter variable
string_var = tk.StringVar(value="Start Value")

# Create Widgets
label = ttk.Label(window, text='Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(window, textvariable=string_var)
entry.pack()

button = ttk.Button(window, text='button', command=button_func)
button.pack()

# run
window.mainloop()