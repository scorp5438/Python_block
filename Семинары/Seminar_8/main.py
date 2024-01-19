from module import *


def Quest():
    '''
    Главное меню программы.\n
    Функция позволяет выбрать один из нескольких вариантов использования.
    Ничего не принимает.\n
    Ничего не возвращает.\n
    Вызывает функции (в зависимости от варианта использования):
    Opening, Quest_data, Search, Create_del_list, Create_change_list.
    '''
    operations = input(
        "Выбирите операцию\n1 - Показать справочник \n2 - Добавить значение"
        "\n3 - Найти данные\n4 - Удалить значение\n5 - Заменить значение\nВведите комадну: ")
    if operations == '1':
        print()
        for i in Opening():
            print(f'|{'|'.join(i)}|')
        restart = input("Нажмите y - чтобы продолжиить: ")
        if restart.lower() == 'y':
            Quest()
    elif operations == '2':
        Quest_data()
    elif operations == '3':
        find = input(
            "Выбирете вариант поиска:\n1 - По фамилии/имени\n2 - По номеру\nВведите комадну: ")
        if find == '1':
            name = input("Введите фамилию/имя: ")
            return Search(Opening(), find, name)
        elif find == '2':
            number = input("Введит номер телефона: ")
            return Search(Opening(), find, number)
        else:
            print(f"\nВведены некорректные данные \"{find}\", повторите ввод...\n")
            Quest()
    elif operations == '4':
        name_del = input("Введите фамилию имя, кого необходимо удалить: ")
        Create_del_list(Opening(), name_del)
    elif operations == '5':
        name_change = input("Введите фамилию имя, кого необходимо заменить: ")
        Create_change_list(Opening(), name_change)
    else:
        print(f"\nНекорректная команда \"{operations}\" повторите ввод...\n")
        Quest()


Quest()