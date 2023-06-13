"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""
n = int(input("Введите количество элементов в множестве: set_n"))
m = int(input("Введите количество элементов в множестве: set_m"))
set_n = set(input(f"Введите {n} элементов в множестве: set_n"))
set_m = set(input(f"Введите {m}элементов в множестве: set_m"))
print(f"{sorted(set_m.union(set_n))}")