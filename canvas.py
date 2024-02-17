import tkinter as tk
from tkinter import ttk

# create a window
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

# canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

#canvas.create_rectangle((50,20,100,200), fill='red', width=10, dash=(1,2))

canvas.create_rectangle((50,20,100,200), fill='red', outline='green', width=10, dash=(1,2))


#canvas.create_line((0,0,100,150), fill='blue')

#canvas.create_oval((200,0,300,100), fill='green')

# canvas.create_polygon((0,0,100,200,300,50), fill='orange')

# canvas.create_arc((200,0,300,100), 
#                   fill='purple', 
#                   start=45, 
#                   style = tk.ARC, 
#                   outline='red', 
#                   width=10)


#canvas.create_text((50,50), text="Some text", fill="green")

#run
window.mainloop()