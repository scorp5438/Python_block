'''
Задача 1: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2
'''

coins = [1, 1, 1, 1, 0, 0, 1]
# coins = []
# add = True
# print("Введите числа 1 или 0. Для выхода нажмите 'q': ")
# while add:
#     coin = input()
#     try:
#         if int(coin) == 1 or int(coin) == 0:
#             coins.append(int(coin))
#     except ValueError:
#         if coin == 'q':
#             add = False
#         else:
#             print("Введено некорректное значение, повторите ввод")
#             add = True

# print(f"\nМассив с монетами:{coins}\nМинимальное кол-во монет:")

# res = [coins.count(1), coins.count(0)]
# print(min(res))

'''
Задача 1 второй вариант решения
'''

# coins = [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
# coins = []
# add = True
# print("Введите числа 1 или 0. Для выхода нажмите '2': ")
# while add:
#     coin = input()
#     try:
#         if int(coin) == 1 or int(coin) == 0:
#             coins.append(int(coin))
#     except ValueError:
#         if coin == 'q':
#             add = False
#         else:
#             print("Введено некорректное значение, повторите ввод")
#             add = True

# print(f"\nМассив с монетами:{coins}\nМинимальное кол-во монет:")
# a = 0
# b = 0

# for i in coins:
#     if i == 0:
#         a += 1
#     else:
#         b += 1
# if a < b:
#     print(a)
# else:
#     print(b)

'''
Задача 2: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
12 35 -> 7 5
11 30 -> 5 6
19 60 -> 4 15
65 699 -> 23 42
1794 803825 -> 869 925
'''

# s = 12
# p = 27
# my_list = []
# for i in range(2, p):
#     if p % i == 0 and p // i == s - i:
#         my_list.append(i)
# if(len(my_list) == 1):
#     my_list.append(my_list[0])
# print(*my_list)

'''
Задача 3: Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
10 -> 1 2 4 8
'''

# n = 10
# count = 0

# my_list = []
# def My_Func(c):
#     if 2 ** c < n: my_list.append(2 ** c)
#     return my_list if 2 ** c > n else My_Func(c + 1)

# print(My_Func(count))
# print(*my_list)

'''
Задача 3 второй вариант решения
'''

# n = 18
# temp = 1
# count = 1

# while temp <= n:
#     print(temp, end = " ")
#     temp = 2 ** count
#     count += 1