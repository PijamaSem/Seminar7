def mode():
    mode = input('Введите режим работы, "w" запись в справочник, "s" сортировка справочника, "r" чтение справочника, Ваш выбор: ')
    return mode

def get_data():
    print('Введите данные: Имя, фамлию, телефон')
    name = input('Введите Имя: ')
    surname = input('Введите Фамилию: ')
    tel_num = input('Введите Телефон: ')
    user_line = (1, name, surname,tel_num)
    return user_line

