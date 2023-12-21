'''
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
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
#     new_str += f"{string[i]}_{str(string[:i+1].count(string[i]))} "
# print(new_str)

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

# string = "She sells sea shells on the sea shore The shells that she sells are sea shells\
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

'''
Первый вариант
'''

# print(len(set(string.split())))

'''
Второй вариант
'''

# print(len(set(i for i in string.split())))

'''
Третий вариант
'''

# result = []
# for i in string.split():
#     if i not in result:
#         result.append(i)
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
max_number = 1000   1 ошибка
while n != 0:       2 ошибка
 n = int(input())
 if max_number > n: 3 ошибка
 max_number = n
print(max_number)

Петя:
n = int(input())
max_number = -1
while n < 0:        1 ошибка
 n = int(input())
 if max_number < n:
 n = max_number     2 ошибка
print(n)            3 ошибка
'''