'''
Задача №47. Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.
Пример ввода и вывода данных представлены на следующем
слайде

Ввод:
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print('ok')
else:
 print('fail')
Вывод:
ok
'''

# transformation = lambda x: x

# values = [45, 54, 65, 4, 65, 4, 6, 54, 6, 54, 65, 4, 6] # или любой другой список
# transormed_values = list(map(transformation, values))

# if values == transormed_values:
#    print('ok')
# else:
#  print('fail')

'''
Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна
Пример ввода и вывода данных представлены на
следующем слайде

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''

from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

func = lambda x, y: pi * x * y

def find_farthest_orbit(list_of_orbits):
    res = max([[func(i, j), i, j] for i, j in list_of_orbits if i != j])
    res = max([[pi * i * j, i, j] for i, j in list_of_orbits if i != j])
    return res[1:]
    # res = max([i for i in list_of_orbits], key=lambda x: pi * x[0] * x[1] * (x[0] != x[1]))
    # return res

print(*find_farthest_orbit(orbits))


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*max(orbits, key=lambda x: x[0] * x[1] * (x[0] != x[1])))

'''Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

Вывод:
same
'''
# values = [1, 1, 1, 1, 1]


# def same_by(operation, arr):
#     res = list(filter(operation, arr))
#     return True if len(res) == 0 or arr == res else False


# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
