# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int (input('Bведите число: '))
# a = 1
# print(f"Набор произведений чисел от 1 до {N}:")
# for i in range(1, N + 1):
#     a = a * i
#     if i == N:
#         print(a)
#     else:
#         print(a, end=', ')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# list comprehension

from itertools import accumulate
import operator

n = int(input('Введите число: '))

list(accumulate([a for a in range(1, n + 1)], operator.mul))

print(f"Набор произведений чисел от 1 до {n}: {list(accumulate([a for a in range(1, n + 1)], operator.mul))}")