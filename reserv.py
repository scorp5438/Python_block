# def Quest_data():
#     name = input("Введиите Фамилию Имя: ")
#     number = input("Введите номер телефона: ")
#     Writing(name, number)


# def Writing(name=None, number=None):
#     if name != None:
#         with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
#             phone_book.write(f'{name:-<25}| {number:<10}\n')
#     replaces = input("Добавить еще данные: y/n\nВведите ответ: ")
#     if replaces.lower() == 'y':
#         Quest_data()
#     elif replaces.lower() == 'n':
#         return None
#     else:
#         print(f"Введены некорректные данные \"{replaces}\", повторите ввод...")
#         Writing()


# def Opening():
#     Guide = list()
#     with open('python блок\Семинары\Seminar_8\Phone_book.txt', 'r', encoding='utf-8') as phone_book:
#         for i in phone_book.readlines()[1:]:
#             Guide.append(i.strip().split('|'))
#     return Guide


# def Quest():
#     operations = input(
#         "Выбирите операцию\n1 - Показать справочник \n2 - Добивить значение"
#         "\n3 - Найти данные\n4 - Удалить значение\n5 - Заменить значение\nВведите комадну: ")
#     if operations == '1':
#         print()
#         for i in Opening():
#             print(f'|{'|'.join(i)}|')
#         restart = input("Нажмите y - чтобы продолжиить: ")
#         if restart.lower() == 'y':
#             Quest()
#     elif operations == '2':
#         Quest_data()
#     elif operations == '3':
#         find = input(
#             "Выбирете вариант поиска:\n1 - По фамилии/имени\n2 - По номеру\nВведите комадну: ")
#         if find == '1':
#             name = input("Введите фамилию/имя: ")
#             return Search(Opening(), find, name)
#         elif find == '2':
#             number = input("Введит номер телефона: ")
#             return Search(Opening(), find, number)
#         else:
#             print(f"Введены некорректные данные \"{find}\", повторите ввод...\n")
#             Quest()
#     elif operations == '4':
#         name_del = input("Введите фамилию имя, кого необходимо удалить: ")
#         Create_del_list(Opening(), name_del)
#     elif operations == '5':
#         name_change = input("Введите фамилию имя, кого необходимо заменить: ")
#         Create_change_list(Opening(), name_change)

# Quest()
# def Search(Guide, option, data):
#     Check = 0
#     print()
#     if option == '1':
#         for i in Guide:
#             if data in i[0]:
#                 print(f'{''.join(i)}')
#                 Check += 1
#     elif option == '2':
#         for i in Guide:
#             if data in i[1]:
#                 print(f'{''.join(i)}')
#                 Check += 1
#         if Check == 0:
#             print(f'Данного значения "{data}" нет')


print('--(зачеркнутый текст)--')