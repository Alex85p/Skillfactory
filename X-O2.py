# X-O game
def welcome():  # Приветствие
    print("-------------------")
    print(' Добро пожаловать')
    print('     в игру ')
    print('"Крустики-Нолики"')
    print("-------------------")
    print('Выбор ячейки осуществляется по координатам X Y')
    print('строки X')
    print('столбцы Y')
    return


def show_fld(f):  # Игровое поле
    print('   0  1  2')
    for i in range(len(f)):
        str_fld = f"{i}  {'  '.join(f[i])} "
        print(str_fld)


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


def winner(f, w):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(f[c[0]][c[1]])
        if symbols == [w, w, w]:
            return True
    return False


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
        print(f'Выиграл {user}!')
        break
    if count == 8:
        show_fld(field)
        print('Ничья!')
