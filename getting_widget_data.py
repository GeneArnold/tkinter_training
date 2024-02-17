import tkinter as tk
from tkinter import ttk

def button_func():
	# get content of entry
	# print(entry.get())

	entry_text = entry.get()

	# update the label
	# label.configure(text = 'some other text')
	# This is the perferred method
	label['text'] = entry_text
	entry['state'] = 'disabled'

	# to see all the options
	# print(label.configure())

# window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("150x150")

# widgets
# label does not have a get data function
label = ttk.Label(master=window,text="My Label")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window,text="My Button",command=button_func)
button.pack()

# run
window.mainloop()
