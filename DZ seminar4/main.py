'''
Задача 1: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5'

# set1 = set(var2.split())
# set2 = set(var3.split())
# set3 = sorted(set(set1).intersection(set2))

# print(set3)

'''
Задача 2: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
'''

# circule = [29, 9, 16, 27, 19, 6, 20, 15, 14, 30]

# circule.append(circule[0])
# circule.insert(0, circule[-2])

# res = sum(circule[0:3])
# for i in range(1, len(circule)-2):
#     temp = sum(circule[0 + i:3 + i])
#     if temp > res:
#         res = temp
# print(res)

'''
Задача 2 Оптимизированный вариант
'''


# circule = [29, 9, 16, 27, 19, 6, 20, 15, 14, 30]

# circule.append(circule[0])
# circule.insert(0, circule[-2])

# res = sum(circule[0:3])
# temp = sum(circule[0:3])

# for i in range(0, len(circule)-3):
#     temp = temp - circule[i] + circule[i+3]
#     if temp > res:
#         res = temp
# print(res)

'''
Тест скорости
'''

# from time import time
# from random import randint

# circule = []
# for i in range(1000):
#     num = randint(1,30)
#     circule.append(num)

# start1 = time()

# temp = 0
# count = 0
# maxNumber=0

# while count < len(circule):
#     temp = circule[-1]
#     circule.pop(-1)
#     circule.insert(0,temp)
#     count+=1
#     a=circule[1]+circule[2]+circule[3]
#     if a>maxNumber:
#         maxNumber = a
# print(maxNumber)

# end1 = time()

# print(end1 - start1)

# start = time()

# circule.append(circule[0])
# circule.insert(0, circule[-2])

# res = sum(circule[0:3])
# temp = sum(circule[0:3])

# for i in range(0, len(circule)-3):
#     temp = temp - circule[i] + circule[i+3]
#     if temp > res:
#         res = temp
# print(res)

# end = time()

# print(end - start)


