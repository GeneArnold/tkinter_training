import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/tkinter-event-binding/

def button_func():
    print("Button pressed")

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")


# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text="This is a label")
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# ttk button
button = ttk.Button(master=window,text="A button",command=button_func)
button.pack()

# events
#window.bind("<Command-a>", lambda event:print("an event"))
window.bind("<Command-a>", lambda event:print(event))

window.bind("<KeyPress>", lambda event:print(event.char))

#window.bind("<Motion>", get_pos)
text.bind("<Motion>", get_pos)

button.bind("<Command-b>", get_pos)

entry.bind("<FocusIn>", lambda event:print('entry selected'))
entry.bind("<FocusOut>", lambda event:print('entry deselected'))

#run
window.mainloop()