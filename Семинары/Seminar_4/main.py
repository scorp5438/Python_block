'''
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''

# string = "a a a b c a a d c d d"
# new_str = ''

# for i in string.split():
#     new_str += f"{i}_{str(new_str.count(i) + 1)} "
# print(new_str)

'''
Второй вариант
'''

# string = "a a a b c a a d c d d"
# string = string.split()
# new_str = ''

# for i in range(len(string)):
#     new_str += f"{string[i]}_{string[:i+1].count(string[i])} "
# print(new_str)

'''
Третий вариант
'''

# string = "a a a b c a a d c d d".split()
# new_dict = {}

# for i in string:
#     if i not in new_dict:
#         print(i, end=' ')
#     else:
#         print(f"{i}_{new_dict[i]}", end=' ')
#     new_dict[i] = 1 + new_dict.get(i, 0)

'''
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
'''

# string = "She sells sea shells on the sea shore The shells \
# that she sells are sea shells I'm sure.So if she sells sea  \
# shells on the sea shore I'm sure that the shells are sea \
#  shore shells"

'''
Первый вариант
'''

# print(len(set(string.split())))

'''
Второй вариант
'''

# print(len(set(i.lower() for i in string.split())))

'''
Третий вариант
'''

# result = []
# for i in string.replace('.', ' ').split():
#     if i.lower() not in result:
#         result.append(i.lower())
# print(len(result))

'''
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Ваня:
n = int(input())
max_number = 1000   1 ошибка, значение должно быть 0
while n != 0:      
 n = int(input())
 if max_number > n: 2 верное, верное условие n > max_number
 max_number = n
print(max_number)

Петя:
n = int(input())
max_number = -1
while n < 0:        1 ошибка, верное условие n > 0
 n = int(input())
 if max_number < n: 2 ошибка, верное условие n > max_number
 n = max_number     3 ошибка, верно max_number = n
print(n)            4 ошибка, верно print(max_number)
'''


'''
Вводятся номера телефонов в одну строчку через пробел \
с разными кодами стран: +7, +6, +2, +4 и т.д. \
Необходимо составить словарь d, где ключи - это коды +7, +6, +2 и т.п., \
а значения - список номеров \
(следующих в том же порядке, что и во входной строке) \
с соответствующими кодами. Полученный словарь вывести командой:
print(*sorted(d.items()))
Sample Input:
+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 \
+21234567110 +71232267890
Sample Output:
('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) \
    ('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854', '+71232267890'])
'''

# d = {'+2': ['+21235777890', '+21234567110'],
#      '+6': ['+61234576890'],
#      '+7': ['+71234567890', '+71234567854', '+71232267890'],
#      '+5': ['+52134567890'],
#      }

# number = "+7 +6 +2 +5"

# num_list = number.split()
# result = []
# for i in num_list:
#     if d.get(i):
#         result.append((i, d[i]))
# print(*sorted(result))