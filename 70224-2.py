from random import randint

count = int(input("Введіть к-кість чисел: "))
list = []
t = int(input("Введіть число для вставки:"))
res = 0

for i in range(count):
    num = randint(50,250)
    list.append(num)
print(f"Несортований список:{list}")
sortid = list.sort()

for i in range(len(sortid)):
    if sortid[i] >= t:

