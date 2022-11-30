# from tkinter import *

# функции игры

# Приветствие

def welcome():
    print("-------------------")
    print(' Добро пожаловать')
    print('     в игру ')
    print('"Крестики-Нолики"')
    print("-------------------")
    print('Выбор ячейки по координатам X Y')
    print('ввод X и Y через пробел')
    print('строки X')
    print('столбцы Y')
    return


# Игровое поле

def show_fld(f):
    print('   0  1  2')
    for i in range(len(f)):
        str_fld = f"{i}  {'  '.join(f[i])} "
        print(str_fld)


# проверка ввода

def inpt(f):
    while True:
        location = input('Введите координаты хода: ').split()
        if len(location) != 2:
            print('Введите 2 значения: Х и У')
            continue
        x, y = location
        if not (x.isdigit()) or not (y.isdigit()):
            print('Х и У должны быть числами, повторите ввод')
            continue
        x, y = int(x), int(y)
        if not (0 <= x <= 2) or not (0 <= y <= 2):
            print('Х и У должны быть в диапозоне от 0 до 2:')
            continue
        if f[x][y] != ' ':
            print('Ячейка уже занята, необходимо задать другие Х и У')
            continue
        return x, y


# определение победителя

def winner(f, w):
    for i in range(len(f)):
        symbol1 = []
        symbol2 = []
        for j in range(len(f[i])):
            symbol1.append(f[i][j])
            symbol2.append(f[j][i])
        if symbol1 == [w, w, w] or symbol2 == [w, w, w]:
            return True

    symbol1 = []
    symbol2 = []
    for i in range(len(f)):
        symbol1.append(f[i][i])
        symbol2.append(f[i][len(f) - i - 1])
    if symbol1 == [w, w, w] or symbol2 == [w, w, w]:
        return True

    return False


# алгоритм игры

welcome()

field = [[' '] * 3 for _ in range(3)]

for count in range(9):
    show_fld(field)
    if count % 2 == 0:
        print('Ходит крестик')
        user = 'X'
    else:
        print('Ходит нолик')
        user = 'O'

    x, y = inpt(field)
    field[x][y] = user

    if winner(field, user):
        show_fld(field)
        print()
        print(f'{user} победил!')
        break
    if count == 8:
        show_fld(field)
        print('Ничья!')
