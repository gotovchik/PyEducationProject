"""Создайте программу для игры в "Крестики-нолики" """
table = list(range(1, 10))
win_positions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                 (1, 4, 7), (2, 5, 8), (3, 6, 9),
                 (1, 5, 9), (3, 5, 7)]


def draw_table():  # рисуем игральный стол
    print('-------------')
    for i in range(3):
        print('|', table[0 + i * 3], '|', table[1 + i * 3], '|', table[2 + i * 3], '|')
        print('-------------')


def user_input(symbol):  # обработка ввода пользователя
    while True:
        place = int(input(f'В какое место ставим {symbol}? '))
        if place not in table:
            print('Вы ввели неправильный номер клетки или клетка уже занята. Попробуйте еще раз!')
            continue
        table[place - 1] = symbol
        break


def check_win():  # проверка выигрышных позиций
    for i in win_positions:
        if table[i[0] - 1] == table[i[1] - 1] == table[i[2] - 1]:
            return table[i[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_table()
        if counter % 2 == 0:
            user_input('X')
        else:
            user_input('O')
        if counter > 3:
            win = check_win()
            if win:
                draw_table()
                print(f'Победил {win}')
                break
        counter += 1
        if counter > 8:
            draw_table()
            print('Ничья!')
            break


main()
