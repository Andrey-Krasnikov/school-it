from random import randint

count = int(input("Введіть к-кість чисел: "))
list = []
find = int(input("Введіть шукане у списку:"))
res = 0

for i in range(count):
    num = randint(0,100)
    list.append(num)
    if num==find:
        res+=1


print(f"Мін.число: {min(list)}, Макс.число: {max(list)}, Число {find} зустрічається у списку {res} разів.")