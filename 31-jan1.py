elcount = int(input("Введіть кількість елементів: "))
list = []

for i in range (elcount):
    list.append(int(input(f"Введіть число №{i+1}:")))

list.sort()
print("Ваш список у порядку зростання:", *list)
list.sort(reverse=True)
print("Ваш список у порядку спадання:", *list)