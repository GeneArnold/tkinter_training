# https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
# https://www.tutorialspoint.com/python/tk_menu.htm

import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Menu')
window.geometry('600x400')

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu)
file_menu.add_command(label="New", command=lambda: print("New"))
file_menu.add_separator()
file_menu.add_command(label="Open", command=lambda: print("Open"))
menu.add_cascade(label="File", menu=file_menu)

# another sub menu
help_check_string = tk.StringVar(value='on')
help_menu = tk.Menu(menu)
help_menu.add_command(label="Help Entry", command=lambda:print(help_check_string.get()))
help_menu.add_checkbutton(label="Check", onvalue='on', offvalue='off', variable=help_check_string)

menu.add_cascade(label="Help", menu=help_menu)

window.configure(menu = menu)

# menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()

button_sub_menu = tk.Menu(menu_button)
button_sub_menu.add_command(label="entry", command=lambda:print("one"))

#menu_button.configure(menu=button_sub_menu)
menu_button['menu'] = button_sub_menu

#run
window.mainloop()