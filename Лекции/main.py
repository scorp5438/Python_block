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
