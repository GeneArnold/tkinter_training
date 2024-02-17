import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# button
def button_func(param):
    print(param)
    print(radio_var.get())


button_string = tk.StringVar(value="A button with str var")
# button = ttk.Button(window, text='A simple button', command=button_func)
button = ttk.Button(window, text='A simple button', command=lambda: button_func("Button"), textvariable= button_string)
button.pack()

# checkbutton
# check_var = tk.BooleanVar()
check_var = tk.IntVar()
# check_var = tk.StringVar()
check1 = tk.Checkbutton(
    window,
    text='checkbox 1',
    variable=check_var,
    command=lambda: print(check_var.get()),
    onvalue=10,
    offvalue=5
)
check1.pack()

# radio buttons
radio_var = tk.StringVar(value="2")
radio1 = tk.Radiobutton(
    window,
    text='Radiobutton 1',
    value='one',
    command=lambda:print(radio_var.get()),
    variable=radio_var
)
radio1.pack()

radio2 = tk.Radiobutton(window, text='Radiobutton 2', value = 2,variable=radio_var)
radio2.pack()



#run
window.mainloop()