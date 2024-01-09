'''
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''


# def multiplication(a, b):
#     if b == 0:
#         return 1
#     return a * multiplication(a, b - 1)


# print(multiplication(2, 10))

# x = 2
# y = 10


# def multiplication(a, b):
#     if b == 1:
#         return a
#     return multiplication(x * a, b - 1)


# print(multiplication(x, y))

'''
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4
'''


# def sum(a, b):
#     if b <= 0:
#         return a
#     # return sum(a + 1, b - 1)
#     return a + sum(1, b - 1)


# print(sum(11, 4))
