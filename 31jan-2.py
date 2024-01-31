elcount = int(input("Введіть кількість елементів: "))
list = []

for i in range (elcount):
    list.append(int(input(f"Введіть число №{i+1}:")))

look = int(input("Введіть число для пошуку: "))

available = list.count(look)

for i in range (available):
    list.remove(look)

print(f"Число {look} було видалено зі списку {available} разів")