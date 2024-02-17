import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Frames and parenting')
window.geometry('600x400')

# frame
frame = ttk.Frame(window, width = 150, height = 200, borderwidth=1, relief=tk.SOLID)
frame.pack_propagate(False) # Switch to size frame by the above settings or have it size based on its children
frame.pack(side="left")

# master setting
label = ttk.Label(frame, text="Label in frame")
label.pack()

button = ttk.Button(frame, text="Button in frame")
button.pack()

# example
label2 = ttk.Label(window, text="Label outside frame")
label2.pack(side="left")

#run
window.mainloop()