import tkinter as tk
from tkinter import END

window = tk.Tk()
window.title("Калькулятор")
window.geometry("350x353")
window.resizable(width=False, height=False)
window.config(bg="black", padx=15, pady=20)

for i in range(4):
    window.grid_columnconfigure(i, minsize=80)

entry = tk.Entry(font="Arial, 20")
entry.grid(column=0, row=0, columnspan=4,stick="we")
entry.insert(0,"0")

def do_operation(sym):
    b= entry.get()
    entry.delete(0, END)
    if sym== "/" and b[-1] =="0": entry.insert(0, "Ділити на нуль може тільки Кернес")
    elif sym=="=":
        if "/" in b and b[-1] =="0": entry.insert(0, "Ділити на нуль може тільки Кернес")
        else:
            entry.insert(0,str(eval(b)))
    else:
        entry.insert(0, str(eval(b))+sym)

def calc(sym):
    if sym=="CE":
        entry.delete(0, END)
        entry.insert(0, "0")
    elif sym=="<-":
        entry.delete(len(entry.get())-1)
        if entry.get()=="":
            entry.insert(0, "0")
    elif sym=="." and entry.get().count(".")==0:entry.insert(END,".")
    elif sym in "-+*/":
        s=entry.get()
        if s[-1] in "-+*/":
            s = s[0:-1]+sym
            entry.delete(0, END)
            entry.insert(0, s)
        elif "+" in s or "-" in s or "/" in s or "*" in s: do_operation(sym)
        else:
            s = s+sym
            entry.delete(0, END)
            entry.insert(0, s)

    elif sym=="=":
        k=entry.get()
        if k[-1] in "-+*/":
            ch=k[0:-1]
            k=k+ch
            entry.delete(0,END)
            entry.insert(0,str(eval(k)))
        else:
            do_operation(sym)
    else:
        if entry.get()=="0":entry.delete(0,END)
        if sym in "0123456789":entry.insert(END,sym)

bt1 = tk.Button(font=("Arial", 20), text="+", command=lambda:calc("+")).grid(column=0,row=1,stick="we")
bt2 = tk.Button(font=("Arial", 20), text="-", command=lambda:calc("-")).grid(column=1,row=1,stick="we")
bt3 = tk.Button(font=("Arial", 20), text="*", command=lambda:calc("*")).grid(column=2,row=1,stick="we")
bt4 = tk.Button(font=("Arial", 20), text="/", command=lambda:calc("/")).grid(column=3,row=1,stick="we")

bt1 = tk.Button(font=("Arial", 20), text="1", command=lambda:calc("1")).grid(column=0,row=2,stick="we")
bt2 = tk.Button(font=("Arial", 20), text="2", command=lambda:calc("2")).grid(column=1,row=2,stick="we")
bt3 = tk.Button(font=("Arial", 20), text="3", command=lambda:calc("3")).grid(column=2,row=2,stick="we")
bt4 = tk.Button(font=("Arial", 20), text="CE", command=lambda:calc("CE")).grid(column=3,row=2,stick="we")

bt1 = tk.Button(font=("Arial", 20), text="4", command=lambda:calc("4")).grid(column=0,row=3,stick="we")
bt2 = tk.Button(font=("Arial", 20), text="5", command=lambda:calc("5")).grid(column=1,row=3,stick="we")
bt3 = tk.Button(font=("Arial", 20), text="6", command=lambda:calc("6")).grid(column=2,row=3,stick="we")
bt4 = tk.Button(font=("Arial", 20), text="<-", command=lambda:calc("<-")).grid(column=3,row=3,stick="we")

bt1 = tk.Button(font=("Arial", 20), text="7", command=lambda:calc("7")).grid(column=0,row=4,stick="we")
bt2 = tk.Button(font=("Arial", 20), text="8", command=lambda:calc("8")).grid(column=1,row=4,stick="we")
bt3 = tk.Button(font=("Arial", 20), text="9", command=lambda:calc("9")).grid(column=2,row=4,stick="we")
bt4 = tk.Button(font=("Arial", 20), text=",", command=lambda:calc(".")).grid(column=3,row=4,stick="we")

bt3 = tk.Button(font=("Arial", 20), text="0", command=lambda:calc("0")).grid(column=0,row=5,stick="we")
bt4 = tk.Button(font=("Arial", 20), text="=", command=lambda:calc("=")).grid(column=1,row=5,stick="we",columnspan=3)



window.mainloop()