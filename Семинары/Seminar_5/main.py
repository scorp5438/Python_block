'''
Требуется найти N-е число Фибоначчи
'''

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(9))

# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)
# print(list1[len(list1)-1])


'''
Найти факториал числа Х через рекурсию
'''


# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)


# print(factorial(5))

'''
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''

# a = '1 1 5 5 5 2 5 5 5 1'
# temp = a.split()
# # a = a.replace(max(temp), min(temp))


# def find_min_max(arr):
#     min = arr[0]
#     max = arr[0]
#     for i in arr:
#         if i < min:
#             min = i
#         elif i > max:
#             max = i
#     return min, max


# res = find_min_max(temp)
# print(a)
# a = a.replace(res[1], res[0])
# print(a)

'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''

# def Prime_number(n):
#     return 'yes' if len([i for i in range(2,n) if n % i == 0]) == 0 else 'no'

# for i in range(26):
#     print(f'i = {i} is prime: {Prime_number(i)}')

'''
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''

# x = 4


# def reverse(n):
#     if n == 0:
#         return '+'
#     a = input("Введите число: ")
#     return reverse(n - 1) + a


# print(reverse(x))


