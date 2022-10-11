# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Number = int(input('Введите натуральное число > 0: '))
# if Number > 0:
#     result = {}
#     total = 0
#     for key in range(1, Number+1):
#         result[key] = round((1+1/key)**key, 2)
#         total += float(result[key])
#     print(f"Список из {Number} чисел заданной последовательности (1+1/{Number})^{Number}: {result}")
#     print(f"Cумма элементов из списка выше: {round(total, 2)}")
# else:
#     print("Ошибка ввода!")

# lambda

n = int(input('Введите натуральное число > 0: '))

function_calculator = lambda n: round((1+1/n)**n, 2)

if n > 0:
    result = []
    for i in range(1, n+1):
        result.append(function_calculator(i))
    total = 0
    for j in result:
        total += j
    print(f"Список из {n} чисел заданной последовательности (1+1/{n})^{n}: {result}")
    print(f"Cумма элементов из списка выше: {round(total, 2)}")
else:
    print("Ошибка ввода!")