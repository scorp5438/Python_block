# list1 = []
# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)
# print(list1[5-1])


'''
Угадыватель числа
'''

# list1 = [1, 4, 7, 8, 9, 5, 2, 1, 4, 0, 4]
# def qick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#     less = [i for i in arr[1:] if i <= pivot]
#     greater = [i for i in arr[1:] if i > pivot]
#     return qick_sort(less) + [pivot] + qick_sort(greater)


# print(qick_sort(list1))


'''
В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
'''

# my_list = [1, 2, 3, 5, 8, 15, 23, 38]

# func = lambda x: x*x

# res = [(i, func(i)) for i in my_list if i % 2 == 0]
# res = [(i, i*i) for i in my_list if i % 2 == 0]

# print(res)

'''
**************************************************************************************
'''

# my_list = [i for i in range(1, 20)]

# print(my_list)

# my_list = list(map(lambda x: x + 10, my_list))
# print(my_list)

'''
**************************************************************************************
'''

# data = '5 48 415 45 87 1 5 65 415'
# # print(data)

# data = list(map(int, data.split()))
# data = [int(i) for i in data.split()]
# # print(data)

# print(data)

'''
**************************************************************************************
'''

# list1 = [1, 2, 5, 4, 8, 4, 8, 9]


# # def func2(x): return x % 2 == 0
# func2 = lambda x: x % 2 == 0

# # def func1(x): return x * x
# func1 = lambda x: x * x 

# list1 = map(func2, list1)

# for i in list1:
#     print(func1(i))

# list1 = list(filter(func2, list1))
# print(list1)

# print(map(func1, list1))

# for i in list1:
#     print(f"[{func1(i)}]")


