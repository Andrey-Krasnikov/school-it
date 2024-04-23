from tkinter import *
from random import choice
passwords = []

def start():
    passwords.clear()
    passwordl = int(entry.get())
    for i in range(10):
        newpass = ""
        for d in range(passwordl):
            newpass += choice('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')
        passwords.append(newpass)
    showpasses()

def showpasses():
    print(passwords)
    listbox.delete(0, END)
    for password in passwords:
        listbox.insert(END,password)


def save():
    file = open("passlist.txt", "w")
    for i in range(10):
        file.write(passwords[i] + "\n")
    file.close()



window = Tk()
window.geometry("800x600")
window.configure(bg="light blue")

label = Label(text="Після натискання на кнопку буде згенеровано\n 10 надійних паролів", fg="yellow", bg="light blue", font=("Arial", 24))
label.pack()

lengthpass = Label(text="Довжина пароля", fg="yellow", bg="light blue", font=("Arial", 16))
lengthpass.place(x=100, y=150)

entry = Entry(font=("Arial", 12))
entry.place(x=100, y=190)

listbox = Listbox(width=40, height=21)
listbox.place(x=400, y=150)

startbt = Button(text="start", command=start, width=15, height=2)
startbt.place(x=400, y=505)

savebt = Button(text="save", command=save, width=15, height=2)
savebt.place(x=530, y=505)

window.mainloop()
