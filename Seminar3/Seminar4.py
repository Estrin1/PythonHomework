# from random import randint
#
# n=int(input('Сколько у вас кустов: '))
# berries=[]
# for i in range(n):
#     berries.append(randint(0, 5))
# print(berries)
# max=max(berries)
# print(f'Максимальное число ягод на кусте {berries.index(max)} с количество {max} ягод')
# #print(max+berries.index(max))
# #print(berries.index(max))
# #print(berries.index(max)-1)
# n = int(input("input number:  "))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#          return fib(n-1)+ fib(n -2)
#
#
# print(fib(n))
"""Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
ЫInput: 5 -> 1 3 3 3 4

Output: 1 3 3 3 """
from random import randint


def recreverse(n):
    if n == 1:
        return False

    elif:
        print(recreverse(n - 1))
