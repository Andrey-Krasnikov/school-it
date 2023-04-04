import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Автобусні рейси")
window.geometry("900x900+510+240")
window.resizable(width=False, height=False)
window.config(bg="white")


#header
window.title = tk.Label(text="Вкажіть кількість пасажирів:", font=("Gotham Pro Medium", 20), bg="white")
window.title.place(x=140, y=20)

window.count = tk.Entry()
window.count.place(x=570, y=30)

#body

window.auto1 = Canvas(width="200", height="150")
window.auto1.place(x=166, y= 100)
img1 = PhotoImage(file="av1.png")
window.auto1.create_image(100,75,image=img1)

window.auto2 = Canvas(width="200", height="150")
window.auto2.place(x=566, y= 100)


window.mainloop()