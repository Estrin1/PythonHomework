"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза
может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются
друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите
 “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
    **Вывод:** Парам пам-пам
"""
puh = input("Введите кричалку: ")
print(puh)
list_glas = ["и", "э", "а", "о", "у", "ы", "е", "я", "ю"]
count = 0
set1 = set()
for el in puh:
    print(el, end=" ")
    if el == " ":
        set1.add(count)
        count = 0

    for x in list_glas:
        if x in el:
            count += 1
            print(count)

if len(set1) != 1 or max(set1) == 0 :
    print(f"{set1}. Пам парам")
else:
    print(f"{set1}. Парам пам-пам")
