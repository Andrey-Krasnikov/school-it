booklist = []
pricelist = []
higher = []
n = 0
while True:
    n+=1
    book = input(f"Введіть назву книги #{n}: ")
    if book == ".":
        print("Список книг закритий.")
        break
    booklist.append(book)
    pricelist.append(float(input(f"Введіть ціну книги #{n}: ")))
    print("////////// Щоб закінчити введення, натисніть крапку //////////")

summ = sum(pricelist)
avg = round(summ/len(pricelist), 2)
print(f"Середня вартість всіх книжок в магазині: {avg}\nВсі книжки разом коштують:{summ}\nСписок книжок, ціна яких вища за середню: \n")

for i in range(len(booklist)):
    if pricelist[i] > avg:
        print(f"ін.{i+1}: {booklist[i]} - {pricelist[i]}")