# 2. Какого цвета клетка
# На вход подается обозначение шахматной клетки, необходимо вывести ее цвет

def chess_color():
    user_input = input('Введите координаты шахматной клетки: ').casefold()
    letters = 'abcdefgh'
    position = letters.index(user_input[0]) + int(user_input[1]) + 1
    if not position % 2:
        print('Black')
    else:
        print('White')


chess_color()
