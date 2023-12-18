'''
Задача 1 первый вариант решения
Найдите сумму цифр трехзначного числа n
'''

# from secrets import randbelow as rand
# number = rand(999)

# print(number)

# def Sum(num):
#     res = 0
#     for i in str(number):
#         res += int(i)
#     return res

# print(Sum(number))


'''
Задача 1 второй вариант решения
'''

# from secrets import randbelow as rand
# number = rand(999)

# print(number)

# def Sum(num):
#     return sum([int(i) for i in str(num)])

# print(Sum(number))

'''
Задача 1 третий вариант решения
'''

# from secrets import randbelow as rand
# number = rand(999)

# print(number)

# def Sum(num):
#     res = 0
#     while num > 0:
#         res += num % 10
#         num //= 10
#     return res

# print(Sum(number))

'''
Задача 1 усложненный вариант
Найдите сумму цифр трехзначного числа n, если в результате получилось двухзначное число, то необходимо снова найти их сумму
до тех пор, пока не получится однозначное число 239 —> 2 + 3 + 9 = 14 —> 1 + 4 = 5
'''
# from secrets import randbelow as rand
# number = rand(9999999999999)

# print(number)
# def Sum(num):
#     res = 0
#     for i in str(num):
#         res += int(i)
#     return res if res < 10 else Sum(res)

# print(Sum(number))

'''
Задача 1 усложненный вариант Второй вариант решения
'''
# from secrets import randbelow as rand

# res = 0
# number = rand(9999999999999)
# print(number)

# while number > 0:
#     res += number % 10
#     number //= 10
#     if res >= 10:
#         temp = res
#         res = 0
#         # print(temp)
#         while temp > 0:
#             res += temp % 10
#             temp //= 10 
#             # print(temp)
# print(res)

'''
Задача 2
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.
'''
# n = 24

# def Guravliki():
#     return f"{n//6} {(n//6)*4} {n//6}"
# print(Guravliki())

'''
Задача 3
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.
'''

# n = 385916
# left_num = int(str(n)[:3])
# righr_num = int(str(n)[3:])

'''
Альтернативынй вариант нахождения левого и правого числа
'''
# left_num = n // 1000
# righr_num = n % 1000

# def Sum(n):
#     res = 0
#     for i in str(n):
#         res += int(i)
#     return res

# if Sum(left_num) == Sum(righr_num): print("yes")
# else: print("No")

'''
Определите, можно ли от шоколадки размером a x b долек отломить c долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.
'''
# a = 3
# b = 2
# c = 3

# if c % a == 0 or c % b == 0 and a * b > c: print("yes")
# else: print("no")