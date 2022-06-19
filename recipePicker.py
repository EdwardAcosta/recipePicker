import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import pyglet

bg_colour = "#3d6466"

def load_frame2():
    print("Button has been pressed!")


# initiallize app with basic settings
root = tk.Tk()
root.title("Recipe Picker")
root.eval("tk::PlaceWindow . center")


# place app in the center of the screen (alternative approach to root.eval())
#x = root.winfo_screenwidth() // 2
#y = int(root.winfo_screenheight() * 0.1)
#root.geometry('500x600+' + str(x) + '+' + str(y))


frame1=tk.Frame(root, width=500, height=600,bg=bg_colour)
frame1.grid(row=0,column=0)
frame1.pack_propagate(False)


#Frame1 widgets
logo_img=ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
logo_widget= tk.Label(frame1, image=logo_img,bg=bg_colour)
logo_widget.image = logo_img
logo_widget.pack()

tk.Label(frame1,
 text="ready for your random recipe?",
 bg=bg_colour,
 fg="white",
 font=("TkMenuFont", 14)
 ).pack()

# button widget
tk.Button(
    frame1,
    text="Shuffle",
    font=("TkHeadingFont",20),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda:load_frame2()).pack()
    









# run app
root.mainloop()