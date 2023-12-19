from secrets import randbelow as random
'''
Задача 1
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai.
Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
'''

# my_list = []
# x = random(10)

# count = 0
# len_list = int(input("Ведите количество элементов массива: "))
# print(f"Введите елементы массива(цифры)")

# while len_list > 0:
#     elem = int(input())
#     my_list.append(elem)
#     len_list -= 1

# print(len(my_list))
# print(*my_list)
# print(x)
# for i in my_list:
#     if i == x:
#         count += 1
# print(count)

'''
Задача 1 второй вариант решения
'''

# my_list = []
# x = random(10)

# len_list = int(input("Ведите количество элементов массива: "))
# print(f"Введите елементы массива(цифры)")

# while len_list > 0:
#     elem = int(input())
#     my_list.append(elem)
#     len_list -= 1

# print(len(my_list))
# print(*my_list)
# print(x)
# print(my_list.count(x))

'''
Задача 2
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai.
Последняя строка
содержит число X
5
1 2 3 4 5
6
-> 5
1 2 3 5
'''

# my_list = []
# x = random(5)

# len_list = int(input("Ведите количество элементов массива: "))
# print(f"Введите елементы массива(цифры)")

# while len_list > 0:
#     elem = int(input())
#     my_list.append(elem)
#     len_list -= 1

# diff = abs(x - my_list[0])
# num = my_list[0]

# for i in my_list:
#     if abs(x - i) < diff:
#         diff = abs(x - i)
#         num = i

# print(len(my_list))
# print(my_list)
# print(x)
# print(num)

'''
Задача 2 второй вариант
'''

# my_list = []
# x = random(5)

# len_list = int(input("Ведите количество элементов массива: "))
# print(f"Введите елементы массива(цифры)")

# while len_list > 0:
#     elem = int(input())
#     my_list.append(elem)
#     len_list -= 1

# diff = abs(x - my_list[0])
# num = my_list[0]
# res = []

# for i in my_list:
#     if abs(x - i) <= diff:
#         diff = abs(x - i)
# for i in my_list:
#     if abs(x - i) == diff:
#         res.append(i)

# print(len(my_list))
# print(my_list)
# print(x)
# print(*set(res))
# print(*res)

'''
Задача 3
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.
Ввод:
ноутбук
Вывод:
12
'''

# one_points = "AEIOULNSTR_АВЕИНОРСТ"
# two_points = "DG_ДКЛМПУ"
# three_points = "BCMP_БГЁЬЯ"
# four_points = "FHVWY_ЙЫ"
# five_points = "K_ЖЗХЦЧ"
# eight_points = "JX_ШЭЮ"
# ten_points = "QZ_ФЩЪ"

# word = input("Введите слово: ")
# points = 0
# for alpha in word:
#     print(alpha)
#     if alpha.upper() in one_points:
#         points += 1
#     elif alpha.upper() in two_points:
#         points += 2
#     elif alpha.upper() in three_points:
#         points += 3
#     elif alpha.upper() in four_points:
#         points += 4
#     elif alpha.upper() in five_points:
#         points += 5
#     elif alpha.upper() in eight_points:
#         points += 8
#     elif alpha.upper() in ten_points:
#         points += 10
# print(points)

'''
Задача 3 второй вариант решения
'''
# letters = {
#     1: "AEIOULNSTRАВЕИНОРСТ",
#     2: "DGДКЛМПУ",
#     3: "BCMPБГЁЬЯ",
#     4: "FHVWYЙЫ",
#     5: "KЖЗХЦЧ",
#     8: "JXШЭЮ",
#     10: "QZФЩЪ",
# }

# word = input("Введите слово: ")
# points = 0


# for i in word:
#     for k, v in letters.items():
#         if i.upper() in v:
#             points += k
# print(points)
