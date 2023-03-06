def get_data():
    with open('hw/phone.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return (data)


def print_data(data):
    for i in data:
        print(i)


def add_data(data):
    print('Введите ФИО: ')
    name = input()
    print('Введите номер телефона: ')
    phone_nmbr = input()
    if len(data) > 0:
        data.pop()
    data.append(f'{name} ')
    data.append(f'{phone_nmbr}\n')


def write_data(data):
    file = open('hw/phone.txt', 'w', encoding='utf-8')
    # data = str(data)
    file.writelines(data)


def find_contact():
    flag = 1
    print('Введите имя или номер: ')
    name = input()
    for line in text:
        if name in line:
            flag = 0
            print(line)
    if flag:
        print('Такого контакта нет')


def change_contact():
    with open('hw/phone.txt', 'r', encoding='utf-8') as f:
        old_data = f.read()
    print('Введите, что заменить (полное ФИО или номер): ')
    old_info = input()
    print('Введите, на что заменить: ')
    new_info = input()
    new_data = old_data.replace(old_info, new_info)
    with open('hw/phone.txt', 'w', encoding='utf-8') as file:
        file.writelines(new_data)


def menu():
    print('МЕНЮ')
    print('Если хотите добавить контакт, нажмите 1')
    print('Если хотите найти контакт, нажмите 2')
    print('Если хотите редактировать контакт, нажмите 3')
    print('Если хотите увидеть весь справочник, нажмите 4')
    print('Чтобы закончить работу, нажмите 0')
    a = int(input())
    if a == 1:
        add_data(text)
        write_data(text)
        print('\n')
        menu()
    if a == 2:
        find_contact()
        print('\n')
        menu()
    if a == 3:
        change_contact()
        print('\n')
        menu()
    if a == 4:
        get_data()
        print_data(text)
        print('\n')
        menu()
    if a == 0:
        quit()


text = get_data()
menu()
