import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Tab Widget')
window.geometry('600x400')

# Notebook widget
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
label = ttk.Label(tab1, text="Text in tab 1")
label.pack()
button1 = ttk.Button(tab1, text="text")
button1.pack()

tab2 = ttk.Frame(notebook)
entry = ttk.Entry(tab2)
entry.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack()


#run
window.mainloop()