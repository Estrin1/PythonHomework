"""
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задач
"""

# str1 = 'a a a b c a a d c d d'

# list_1 = list(str1.split())
# print (list_1)
# for i in list_1:
#     count = 0
#     for i  in range(1,len(list_1)):
#         if i  == k:
#          count += 1
#         list_1.insert(count, i)
# print(list_1)

# arr = """She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells""".split()
# a = set(arr)
# print(f"{len(a)}")

"""
Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых 
чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым 
встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и 
выиграл спор. За помощью товарищи обратились к Вам, студентам.
"""
import random
a = list()
b = True
while b == True:
    if a.append(int(input("Введите число: "))) == 0:
        b = False



print(max(a))

