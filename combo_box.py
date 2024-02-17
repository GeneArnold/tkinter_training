import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.title('Combo and Spin')
window.geometry('800x500')

# create widgets

# Combox
items = ["Ice cream","Cookies","Pizza"]
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
# combo.configure(values=items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text=f"Selected value: {food_string.get()}"))

combo_label = ttk.Label(window, text="A Label")
combo_label.pack()


# Spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window, 
                   from_=3, 
                   to = 20, 
                   increment= 3, 
                   command= lambda: print(spin_int.get()),
                   textvariable=spin_int)

# spin['value'] = (1,2,3,4,5)
spin.bind('<<Increment>>', lambda event: print("UP"))
spin.bind('<<Decrement>>', lambda event: print("DOWN"))
spin.pack()

#run
window.mainloop()