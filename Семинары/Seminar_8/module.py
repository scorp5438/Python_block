def Quest_data():
    '''
    Функция добавляет данные в справочник.\n
    Не принимает никаких данных.\n
    Запрашивает имя и фамилию и вызывает функцию Writing\n
    '''
    name = input("Введиите Фамилию Имя: ")
    number = input("Введите номер телефона: ")
    Writing(name, number)


def Writing(name=None, number=None):
    '''
    Записывает новые данные в файл.\n
    Принимает два параметра:\n
    name (По умолчанию = None)\n
    number (По умолчанию = None)\n
    вызываеся функцией Quest_data, которая и передает данные в эту функцию.\n
    Ничего не возвращает.
    '''
    if name != None:
        with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
            phone_book.write(f'|{name:-<25}|{number:^16}|\n')
    replaces = input("Добавить еще данные: y/n\nВведите ответ: ")
    if replaces.lower() == 'y':
        Quest_data()
    elif replaces.lower() == 'n':
        restart = input("\nНажмите y - чтобы вернуться в начальное меню: ")
        if restart.lower() == 'y':
            import main
            main.Quest()
    else:
        print(f"\nВведены некорректные данные \"{replaces}\", повторите ввод...\n")
        Writing()


def Opening():
    '''
    Открывает файл и выводит содержимое в терминал.\n
    Не принимает никаких данных.\n
    Функция возвращает список, созданный из данных взятых из файла.
    '''
    Guide = list()
    with open('python блок\Семинары\Seminar_8\Phone_book.txt', 'r', encoding='utf-8') as phone_book:
        for i in phone_book.readlines():
            Guide.append(i.strip().strip('|').split('|'))
    return Guide


def Search(Guide, option, data):
    '''
    Функция совершает поиск по файлу.\n
    Принмает параметры:\n
    Guide = список, сформированный функцией Opening.\n
    option = параметр поиска: 1 - по фамилии/имени, 2 - по номеру телефона.\n
    data = аргументы для поиска: телефон или имя.\n
    Функция ничего не возвращает, но выводит все найденные данные на экран.\n
    Если ничего не найдено, выводит надпись: Данного значения "{data}" нет
    '''
    Check = 0
    list_num = Opening()
    print(f'\n|{'|'.join(list_num[0])}|')
    if option == '1':
        for i in Guide:
            if data.lower() in i[0].lower():
                print(f'|{'|'.join(i)}|')
                Check += 1
    elif option == '2':
        for i in Guide:
            if data == i[1].strip():
                print(f'|{'|'.join(i)}|')
                Check += 1
    if Check == 0:
        print(f'\nДанного значения "{data}" нет')
    restart = input("\nНажмите y - чтобы вернуться в начальное меню: ")
    if restart.lower() == 'y':
        import main
        main.Quest()


def Deliting(name=None, number=None):
    '''
    Функция удаляет данные из файла по заданным аргументам.\n
    Принимает параметры:\n
    name (По умолчанию = None) Имя\n
    number (По умолчанию = None) Номер телефона\n
    Ищет искомый объект по фамилии/имени и номеру телефона и удаляет его.\n
    Функция ничего не возвращает, принимает данные из функции Create_del_list.\n
    '''
    list_num = Opening()
    with open('python блок\Семинары\Seminar_8\phone_book.txt', 'w', encoding='utf-8') as phone_book:
        phone_book.write(f'|{'Фамилия Имя':^25}|{'Номер телефана':^16}|\n')
    for i in list_num[1:]:
        if name is not None and number is None:
            if name.lower() in i[0].lower():
                continue
            else:
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{i[0]:-<25}|{i[1]:^16}|\n')
        elif name is not None and number is not None:
            if name.lower() in i[0].lower() and number == i[1].strip():
                continue
            else:
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{i[0]:-<25}|{i[1]:^16}|\n')
    print("Данные удалены успешно")
    restart = input("\nНажмите y - чтобы вернуться в начальное меню: ")
    if restart.lower() == 'y':
        import main
        main.Quest()


def Change(name=None, new_name=None, number=None, new_number=None):
    '''
    Функция вносит изменения в файл.\n
    принимает параметры:\n
    name (По умолчанию = None) Имя.\n
    new_name (По умолчанию = None) Новое имя.\n
    number (По умолчанию = None) Номер телефона.\n
    new_number (По умолчанию = None) Новый номер телефона.\n
    У функции есть 3 режима:\n
    1 Изменить фамилию имя.\n
    2 Изменить номер.\n
    3 Изменить всю запись.\n
    Ничего не возвращает, данные принимает из функции Setting_change.
    '''
    list_num = Opening()
    with open('python блок\Семинары\Seminar_8\phone_book.txt', 'w', encoding='utf-8') as phone_book:
        phone_book.write(f'|{'Фамилия Имя':^25}|{'Номер телефана':^16}|\n')
    for i in list_num[1:]:
        if name is not None and new_name is not None and number is not None and new_number is None:
            if name.lower() in i[0].lower() and number == i[1].strip():
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{new_name:-<25}|{i[1]:^16}|\n')
            else:
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{i[0]:-<25}|{i[1]:^16}|\n')
        elif name is not None and new_name is None and number is not None and new_number is not None:
            if name.lower() in i[0].lower() and number == i[1].strip():
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{i[0]:-<25}|{new_number:^16}|\n')
            else:
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{i[0]:-<25}|{i[1]:^16}|\n')
        elif name is not None and new_name is not None and number is not None and new_number is not None:
            if name.lower() in i[0].lower() and number == i[1].strip():
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{new_name:-<25}|{new_number:^16}|\n')
            else:
                with open('python блок\Семинары\Seminar_8\phone_book.txt', 'a', encoding='utf-8') as phone_book:
                    phone_book.write(f'|{i[0]:-<25}|{i[1]:^16}|\n')
    print("Данные изменены успешно")
    restart = input("\nНажмите y - чтобы вернуться в начальное меню: ")
    if restart.lower() == 'y':
        import main
        main.Quest()


def Create_del_list(Guide, data):
    '''
    Функция проверяет данные для удаления:\n
    Если принимаемый аргумент встречает несколько раз,\n
    необходимо выбрать объект удаления.\n
    Если данные не найдены, выводится надпись:\n
    Такой записи нет...\n
    Принимает параметры:\n
    Guide = список, сформированный функцией Opening.\n
    data = искомый аргумент (фамилия/имя)\n
    Вызывает функцию Deliting
    Возвращает список объектов на удаление
    '''
    delete_list = []
    for i in Guide:
        if data.lower() in i[0].lower():
            delete_list.append(i)
    if len(delete_list) > 1:
        for i in delete_list:
            print(f'{i}')
        num_del = input("\nНайдено несколько записей, укажите телефон: ")
        # Заменил num_del in j на num_del == j.strip()
        if len([j for i in delete_list for j in i if num_del == j.strip()]) == 1:
            Deliting(data, num_del)
        # Заменил num_del in j на num_del == j.strip()
        elif len([j for i in delete_list for j in i if num_del == j.strip()]) == 0:
            print("\nНомер не найден, повторите ввод...\n")
            Create_del_list(Guide, data)
    elif len(delete_list) == 1:
        Deliting(data)
    else:
        print("Такой записи нет...")
    # return delete_list


def Create_change_list(Guide, data):
    '''
    Функция проверяет данные для редактирования:\n
    Если принимаемый аргумент встречает несколько раз,\n
    необходимо выбрать объект для редактирования.\n
    Если данные не найдены, выводится надпись:\n
    Такой записи нет...\n
    Принимает параметры:\n
    Guide = список, сформированный функцией Opening.\n
    data = искомый аргумент (фамилия/имя).
    Ничего не возвращает.\n
    '''
    change_list = []
    for i in Guide:
        if data.lower() in i[0].lower():
            change_list.append(i)
    if len(change_list) > 1:
        for i in change_list:
            print(f'{i}')
        num_change = input("\nНайдено несколько записей, укажите телефон: ")
        if len([j for i in change_list for j in i if num_change == j.strip()]) == 1:
            Setting_change(data, num_change)
        elif len([j for i in change_list for j in i if num_change == j.strip()]) == 0:
            print("\nНомер не найден, повторите ввод...\n")
            Create_change_list(Guide, data)
    elif len(change_list) == 1:
        Setting_change(data, change_list[0][1].strip())
    else:
        print("Такой записи нет...")


def Setting_change(name, number):
    '''
    Функция настраивает параметры изменений.\n
    Есть 3 варианта:\n
    1 Изменить фамилию имя.\n
    2 Изменить номер.\n
    3 Изменить всю запись.\n
    Принимает параметры:\n
    name = Имя.\n
    number = Номер телефона.\n
    Ничего не возвращает
    Вызывает функцию Change
    '''
    option = input(
        "Что хотите изменить\n1 - Фамилию имя\n2 - Номер телефона\n3 - Всю запись целоиком\nВведите команду: ")
    if option == '1':
        new_name = input("Введите новую фамилию имя: ")
        Change(name=name, new_name=new_name, number=number)
    elif option == '2':
        new_number = input("Введите новый номер: ")
        Change(name=name, number=number, new_number=new_number)
    elif option == '3':
        new_name = input("Введите новую фамилию имя: ")
        new_number = input("Введите новый номер: ")
        Change(name, new_name, number, new_number)
    else:
        print(f"\nВведены некорректные данные \"{option}\"...\n")
        Setting_change(name, number)
