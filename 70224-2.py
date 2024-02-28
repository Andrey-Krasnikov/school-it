from random import randint

count = int(input("Введіть к-кість чисел: "))
sp = []
t = int(input("Введіть число для вставки:"))
for i in range(count):
    num = randint(50, 250)
    sp.append(num)

print(f"Несортований список: {sp}")

sp.sort()

for i in range(len(sp)):
    if sp[i] >= t:
        sp.insert(i, t)
        break
else:
    sp.append(t)  #якщо всі числа менше ніж т

print(f"Список з корективами: {sp}")
