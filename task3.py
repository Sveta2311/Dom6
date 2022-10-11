# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# N = int (input('Bведите число (размер списка) > 0: '))
# if N > 0:
#     import random
#     list = random.sample(range(100), N)
#     print(f"Сгенерированный список: {list}")
#     if N == 1:
#         print("В списке нет элементов, стоящих на нечетных позициях!")
#     else:
#         print("Элементы списка, стоящие на нечетной позиции: ")
#     for i in range(1, len(list), 2):
#             if i == N-1 or i == N-2:
#                 print(list[i])
#             else:
#                 print(list[i], end=", ")
#     else:
#         print(f"Сумма элементов списка, стоящих на нечетной позиции: {sum(list[1::2])}") 
# else:
#     print("Ошибка ввода!")

# filter

import random
n = int (input('Bведите число (размер списка) > 0: '))
if n > 0:
    list1 = random.sample(range(100), n)
    print(f"Сгенерированный список: {list1}")
    if n == 1:
        print("В списке нет элементов, стоящих на нечетных позициях!")
        exit()
    else:
        def filter_odd_indices(a):
            if list1.index(a)%2 == 1:
                return True
            else:
                return False

    out_filter = list(filter(filter_odd_indices, list1))

    print("Элементы списка, стоящие на нечетной позиции:",out_filter)
    print("Сумма элементов списка, стоящих на нечетной позиции:",sum(out_filter))

else:
    print("Ошибка ввода!")
