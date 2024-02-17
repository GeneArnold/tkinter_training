import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# create a window
window = tk.Tk()
window.title('Sliders')
window.geometry('600x400')

scale_float = tk.DoubleVar(value=15)

# slider
scale = ttk.Scale(window,
                from_= 0, 
                to = 25, 
                command=lambda value: print(scale_float.get()),
                length=300,
                orient='horizontal',
                variable=scale_float
            )
scale.pack()

# progress bar
progress = ttk.Progressbar(window, 
                variable=scale_float,
                maximum=25,
                length=300,
                orient='horizontal',
                mode='determinate'
            )

#progress.start()

progress.pack()


# scrolledtext
scrolled_text = scrolledtext. ScrolledText(window, width=50, height = 20)
scrolled_text.pack()

#run
window.mainloop()