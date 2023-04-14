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
companylable.place(x=500, y=20)

azs_pc = Canvas(bg="white", width=250, height=250)
azs_pc.place(x=510, y=70)
azs_pc.create_image(0, 0, anchor=NW, image=img)

azc_list = ["KVORUM", "OKKO", "SHELL", "SOCAR", "WOG"]
selected = StringVar()
selected.set(azc_list[0])

def on_select(value):
    global dp_price, a92_price, a95_price, gaz_price, img, company
    print(f"Вибрано: {value}")

    if value == "KVORUM":
        dp_price = 33.25
        a92_price = 34.95
        a95_price = 33.65
        gaz_price = 18.9
        img = PhotoImage(file="fuelprice_imgs/azs_kvorum.png")
    elif value == "OKKO":
        dp_price = 38.99
        a92_price = 36.75
        a95_price = 35.99
        gaz_price = 19.65
        img = PhotoImage(file="fuelprice_imgs/azs_okko.png")
    elif value == "SHELL":
        dp_price = 35.52
        a92_price = 35.95
        a95_price = 35.25
        gaz_price = 19.15
        img = PhotoImage(file="fuelprice_imgs/azs_shell.png")
    elif value == "SOCAR":
        dp_price = 38.50
        a92_price = 39.98
        a95_price = 36.77
        gaz_price = 14.80
        img = PhotoImage(file="fuelprice_imgs/azs_socar.png")
    elif value == "WOG":
        dp_price = 37.99
        a92_price = 36.00
        a95_price = 34.99
        gaz_price = 18.99
        img = PhotoImage(file="fuelprice_imgs/azs_wog.png")


    rb1.configure(text=f"ДП - {dp_price}")
    rb2.configure(text=f"А-92 - {a92_price}")
    rb3.configure(text=f"А-95 - {a95_price}")
    rb4.configure(text=f"ГАЗ - {gaz_price}")
    azs_pc.create_image(0, 0, anchor=NW, image=img)
    company = value
    companylable.configure(text=f"Компанія: {company}", font=("Gotham pro", 22), bg=stbg, fg="white")



azc = OptionMenu(window, selected, *azc_list, command=on_select)
azc.config(font=("Gotham pro", 22), bg=stbg, fg="white", width=10, height=1)
azc.place(x=508, y=350)

fuel = IntVar()

rb1 = Radiobutton(window, text=f"ДП - {dp_price}", font=("Gotham pro", 14), variable=fuel, value=1, bg=stbg, fg="white", selectcolor="black")
rb2 = Radiobutton(window, text=f"А-92 - {a92_price}", font=("Gotham pro", 14), variable=fuel, value=2, bg=stbg, fg="white", selectcolor="black")
rb3 = Radiobutton(window, text=f"А-95 - {a95_price}", font=("Gotham pro", 14), variable=fuel, value=3, bg=stbg, fg="white", selectcolor="black")
rb4 = Radiobutton(window, text=f"ГАЗ - {gaz_price}", font=("Gotham pro", 14), variable=fuel, value=4, bg=stbg, fg="white", selectcolor="black")


rb1.place(x=565, y=430)
rb2.place(x=565, y=460)
rb3.place(x=565, y=490)
rb4.place(x=565, y=520)

f_amount = Label(text="Обсяг палива", font=("Gotham pro", 14), bg=stbg, fg="white")
f_amount.place(x=770, y=430)

e_amount = Entry(font=("Gotham pro", 14), width=10)
e_amount.place(x=770, y=469)


discount = StringVar()
discount.set("0%")

discount_label = Label(text="Обсяг знижки:", font=("Gotham pro", 14), bg=stbg, fg="white")
discount_label.place(x=355, y=430)

discount_menu = OptionMenu(window, discount, "0%", "10%", "20%", "30%")
discount_menu.config(font=("Gotham pro", 14), bg=stbg, fg="white", width=8, height=1)
discount_menu.place(x=355, y=460)

def count():
    global dp_price, a92_price, a95_price, gaz_price
    full_amount = float(e_amount.get())
    fuel_type = fuel.get()
    if fuel_type == 1:
        fuel_price = dp_price
    elif fuel_type == 2:
        fuel_price = a92_price
    elif fuel_type == 3:
        fuel_price = a95_price
    elif fuel_type == 4:
        fuel_price = gaz_price
    discount1 = int(discount.get().strip("%"))
    discount2 = 1 - discount1 / 100
    totalprice = full_amount * fuel_price * discount2
    totalprice = round(totalprice, 2)
    total.configure(text=f"{totalprice} ГРН", font=("Gotham pro", 17), bg=stbg, fg="white")

e_calculate = Button(text="Обчислити вартість", font=("Gotham pro", 17), bg=stbg, fg="white", command=count)
e_calculate.place(x=508, y=600)

total = Label(text="0 ГРН", font=("Gotham pro", 17), bg=stbg, fg="white")
total.place(x=595, y=660)

window.mainloop()