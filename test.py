import tkinter as tk
from tkinter import IntVar
class Test:
    def __init__(self, student):
        #Створення вікна
        self.student = student
        window = tk.Tk()
        window.title("Тест з інформатики")
        window.geometry("900x900+510+240")
        window.resizable(width=False, height=False)
        window.config(bg="white")
        #Назва тесту
        window.title = tk.Label(text="Тест з Інформатики", font=("Gotham Pro Medium", 20), bg="white")
        window.title.place(x=320, y=20)
        #Покажемо тести на екрані з використанням RadioButton:
        self.a1 = IntVar()
        question1_label = tk.Label(text="1. Що таке OOP?", font=("Arial", 12), bg="white")
        question1_label.place(x=30, y=60)
        question1_option1 = tk.Radiobutton(text="одна з парадигм програмування, яка розглядає програму як множину «об'єктів», що взаємодіють між собою", value=1, variable=self.a1, bg="white")
        question1_option1.place(x=30, y=80)

        question1_option2 = tk.Radiobutton(text="це спосіб програмування, який використовується тільки для створення ігор та візуальних ефектів.", value=2, variable=self.a1, bg="white")
        question1_option2.place(x=30, y=100)

        question1_option3 = tk.Radiobutton(text="це зовсім нова мова програмування, яка не має жодного відношення до традиційних мов програмування, таких як C або Java.", value=3, variable=self.a1, bg="white")
        question1_option3.place(x=30, y=120)

        question1_option4 = tk.Radiobutton(text="одна з парадигм програмування, яка розглядає програму як множину «об'єктів», що взаємодіють між собою", value=4, variable=self.a1, bg="white")
        question1_option4.place(x=30, y=140)

        self.a2 = IntVar()
        question2_label = tk.Label(text="2. Що таке інкапсуляція в ООП?", font=("Arial", 12), bg="white")
        question2_label.place(x=30, y=180)

        question2_option1 = tk.Radiobutton(
            text="це засіб забезпечення захисту даних від прямого доступу з зовнішнього середовища",
            value=1, variable=self.a2, bg="white")
        question2_option1.place(x=30, y=200)

        question2_option2 = tk.Radiobutton(
            text="це техніка програмування, за допомогою якої створюються об'єкти, які можуть існувати в різних станах.",
            value=2, variable=self.a2, bg="white")
        question2_option2.place(x=30, y=220)

        question2_option3 = tk.Radiobutton(
            text="це методологія, яка дозволяє програмістам використовувати готові компоненти, щоб зменшити кількість коду, що потрібно написати.",
            value=3, variable=self.a2, bg="white")
        question2_option3.place(x=30, y=240)

        question2_option4 = tk.Radiobutton(
            text="це просто інший термін для поліморфізму, який означає, що об'єкт може мати різні форми в залежності від контексту, в якому він використовується.",
            value=4, variable=self.a2, bg="white")
        question2_option4.place(x=30, y=260)

        self.a3 = IntVar()
        question3_label = tk.Label(text="3. Що таке поліморфізм в ООП?", font=("Arial", 12), bg="white")
        question3_label.place(x=30, y=300)

        question3_option1 = tk.Radiobutton(
            text="це здатність об'єктів виконувати різні дії в залежності від контексту, в якому вони використовуються.",
            value=1, variable=self.a3, bg="white")
        question3_option1.place(x=30, y=320)

        question3_option2 = tk.Radiobutton(
            text="це метод програмування, за допомогою якого можна об'єднувати кілька функцій в одну, що працює для різних типів даних.",
            value=2, variable=self.a3, bg="white")
        question3_option2.place(x=30, y=340)

        question3_option3 = tk.Radiobutton(
            text="це технологія, яка дозволяє розподіляти ресурси між об'єктами в залежності від їх потреб",
            value=3, variable=self.a3, bg="white")
        question3_option3.place(x=30, y=360)

        question3_option4 = tk.Radiobutton(
            text="це тільки для досвідчених програмістів.",
            value=4, variable=self.a3, bg="white")
        question3_option4.place(x=30, y=380)
        #2 питання з checkbutton
        self.a4v1 = IntVar()
        self.a4v2 = IntVar()
        self.a4v3 = IntVar()
        self.a4v4 = IntVar()
        question4_label = tk.Label(text="4. Що таке поліморфізм в ООП?", font=("Arial", 12), bg="white")
        question4_label.place(x=30, y=420)

        question4_option1 = tk.Checkbutton(
            text="це механізм, який дозволяє скрити складність деталей реалізації, надаючи простий та зрозумілий інтерфейс для користувачів.",
            onvalue=1, offvalue=0, variable=self.a4v1, bg="white")
        question4_option1.place(x=30, y=440) #+

        question4_option2 = tk.Checkbutton(
            text="це процес зведення декількох класів в один, для того щоб зменшити кількість коду, який потрібно написати",
            onvalue=1, offvalue=0, variable=self.a4v2, bg="white")
        question4_option2.place(x=30, y=460)

        question4_option3 = tk.Checkbutton(
            text="це техніка програмування, яка дозволяє користувачеві працювати з даними, не вдаючись до деталей їх реалізації",
            onvalue=1, offvalue=0, variable=self.a4v3, bg="white")
        question4_option3.place(x=30, y=480) #+

        question4_option4 = tk.Checkbutton(
            text="це лише теоретичне поняття, яке не має практичного застосування в програмуванні.",
            onvalue=1, offvalue=0, bg="white", variable=self.a4v4)
        question4_option4.place(x=30, y=500)

        #пит2/5 checkbox

        self.a5v1 = IntVar()
        self.a5v2 = IntVar()
        self.a5v3 = IntVar()
        self.a5v4 = IntVar()
        question5_label = tk.Label(text="5. Що таке наслідування в ООП?", font=("Arial", 12), bg="white")
        question5_label.place(x=30, y=540)

        question5_option1 = tk.Checkbutton(
            text="це процес передачі властивостей інтерфейсу одного класу до іншого класу.",
            onvalue=1, offvalue=0, variable=self.a5v1, bg="white")
        question5_option1.place(x=30, y=560) #+

        question5_option2 = tk.Checkbutton(
            text="це засіб забезпечення контролю над доступом до властивостей класу.",
            onvalue=1, offvalue=0, variable=self.a5v2, bg="white")
        question5_option2.place(x=30, y=580)

        question5_option3 = tk.Checkbutton(
            text="це засіб збільшення кількості доступних методів в класі.",
            onvalue=1, offvalue=0, variable=self.a5v3, bg="white")
        question5_option3.place(x=30, y=600)

        question5_option4 = tk.Checkbutton(
            text="це процес створення нового класу на основі існуючого класу з додаванням або видаленням деяких властивостей.",
            onvalue=1, offvalue=0, bg="white", variable=self.a5v4) #+
        question5_option4.place(x=30, y=620)

        #розташуємо кнопку перевірку оцінки, та лейбл, в який напишемо оцінку

        Check = tk.Button(
            text="Перевірити оцінку",
            bg="white", font="Arial", width=20, height=2, command=self.review)
        Check.place(x=30, y=670)

        self.resultT = tk.Label(text="Результат: ?", font=("Arial Medium", 20), bg="white")
        self.resultT.place(x=240, y=675)


        window.mainloop()
    def review(self):
        self.result = 1
        if self.a1.get() == 1:
            self.result = self.result+1
        if self.a2.get() == 1:
            self.result = self.result+1
        if self.a3.get() == 1:
            self.result = self.result+1
        #тепер пропишемо перевірку чекбоксів
        if self.a4v1.get() and self.a4v3.get() == 1:
            self.result = self.result+4
        elif self.a4v1.get() or self.a4v3.get() == 1:
            self.result = self.result+2
        if self.a5v1.get() and self.a5v4.get() == 1:
            self.result = self.result+4
        elif self.a5v1.get() or self.a5v4.get() == 1:
            self.result = self.result+2
        self.writeIn()
        print(f"DEBUG: {self.result}")
        #запишемо це значення через конфіг
        self.resultT.config(text=f"Результат: {self.result}", font=("Arial Medium", 20), bg="white")

    def writeIn(self):
        #зробимо функцію, куди будуть кидатися результати студентів. це допоможе уникнути "підбору" правильного варінту, та зробить легшим процесс оцінювання.
        with open("results.txt", "w") as f:
            print(f"Студент: {self.student} ; Оцінка за тест: {self.result} \n", file=f)
Start = Test("Krasnikov")