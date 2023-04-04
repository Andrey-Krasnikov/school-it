import tkinter as tk

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




window.mainloop()