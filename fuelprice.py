from tkinter import *
from tkinter import Radiobutton

window = Tk()
window.title("Ціни на паливо")
window.geometry("1300x800")
window.configure(bg="#2c3e50")

company = "KVORUM"

dp_price = 33.25
a92_price = 34.95
a95_price = 33.65
gaz_price = 18.9

img = PhotoImage(file="fuelprice_imgs/azs_kvorum.png")

stbg = "#2c3e50"



companylable = Label(text=f"Компанія: {company}", font=("Gotham pro", 22), bg=stbg, fg="white")
companylable.place(x=490, y=20)

azs_pc = Canvas(bg="white", width=250, height=250)
azs_pc.place(x=510, y=70)
azs_pc.create_image(0, 0, anchor=NW, image=img)

azc_list = ["KVORUM", "OKKO", "SHELL", "SOCAR", "WOG"]
selected = StringVar()
selected.set(azc_list[0])

def on_select(value):
    print(f"Вибрано: {value}")

    #if value == "KVORUM"
    pass

azc = OptionMenu(window, selected, *azc_list, command=on_select)
azc.config(font=("Gotham pro", 22), bg=stbg, fg="white", width=10, height=1)
azc.place(x=508, y=350)

fuel = IntVar()

rb1 = Radiobutton(window, text=f"ДП - {dp_price}", font=("Gotham pro", 14), variable=fuel, value=1, bg=stbg, fg="white", selectcolor="black")
rb2 = Radiobutton(window, text=f"А-92 - {a92_price}", font=("Gotham pro", 14), variable=fuel, value=2, bg=stbg, fg="white", selectcolor="black")
rb3 = Radiobutton(window, text=f"А-95 - {a95_price}", font=("Gotham pro", 14), variable=fuel, value=3, bg=stbg, fg="white", selectcolor="black")
rb4 = Radiobutton(window, text=f"ГАЗ - {gaz_price}", font=("Gotham pro", 14), variable=fuel, value=4, bg=stbg, fg="white", selectcolor="black")


rb1.place(x=508, y=430)
rb2.place(x=508, y=460)
rb3.place(x=508, y=490)
rb4.place(x=508, y=520)





window.mainloop()
