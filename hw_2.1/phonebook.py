contacts = dict()


def add_record():
    '''Добавить номер и имя человека'''
    name = input('Имя: ')
    number = input('Номер: ')
    if name not in contacts.keys():
        contacts[name] = [number, ]
    else:
        contacts[name].append(number)

def print_by_name():
    '''Вывести номера человека по имени'''
    name = input('Имя: ')
    if name not in contacts.keys():
        print('Человек не найден!')
        return
    [print_two(name, number) for number in contacts[name]]

def remove_person():
    '''Удалить человека по имени'''
    name = input('Имя: ')
    if name not in contacts.keys():
        print('Человек не найден!')
        return
    contacts.pop(name)

def print_book():
    '''Вывод книги'''
    [[print_two(name, number) for number in numbers] for name, numbers in contacts.items()]

def print_two(string1, string2):
    '''formatted print with two arguments'''
    print(f'{string1}    {string2}')


if __name__ == '__main__':
    actions = [add_record, print_by_name, remove_person]
    while True:
        print()
        for action in actions:
            print(f'{actions.index(action)+1} - {action.__doc__}')
        try:
            actions[int(input())-1]()
        # Вывод книги по невалидному выбору пункта меню
        except ValueError, IndexError:
            print_book()



