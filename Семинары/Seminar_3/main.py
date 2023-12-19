'''
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# new_list =[]
# x = set()

# # print(len(set(my_list)))

# for elem in my_list:
#     if elem not in new_list:
#     # if new_list.count(elem) == 0:
#         new_list.append(elem)
#     # x.add(elem)
# print(len(new_list))
# print(new_list)

'''
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.
'''

# my_list = [1, 2, 3, 4, 5]
# k = 2
# k = k % len(my_list)

# while k > 0:
#     temp = my_list.pop()
#     my_list.insert(0, temp)
#     k -= 1
# print(my_list)

# k=2
# lst1 = [1,2,3,4,5]
# print(lst1[-k:],lst1[:-k])


# new_list = [*my_list[len(my_list)-k:], *my_list[0:len(my_list)-k]]

# print(new_list)