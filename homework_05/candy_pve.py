from random import getrandbits, randint


def get_name(p1, p2, f):  # очередность
    return p1 if f else p2


def input_move(value):
    f = True
    while f:
        x = input('Введите количество конфет, которое хотите взять: ')
        try:
            x = int(x)
            if x > value or x < 1:
                print('Можно взять от 1 до 28 конфет включительно. Попробуйте еще раз.')
            else:
                f = not f
        except ValueError:
            print('Вы ввели вовсе не число. Попробуйте еще раз')
    return x


def main():

    greeting = 'Приветствую вас в игре "2021 конфета"!\n' \
               'Правила просты: На столе лежит 2021 конфета,\n' \
               'игроки поочереди берут не более 28 конфет за один ход.\n' \
               'Тот, кто сделает последний ход - забирает все конфеты себе и выигрывает.'
    print(greeting)

    player1 = input('Как зовут первого игрока? Введите имя: ')
    player2 = 'Bot'
    flag = bool(getrandbits(1))

    candy_count = 2021
    max_take = 28
    print(f'Случайным образом компьютер выбрал, что первым ходит {get_name(player1, player2, flag)}')
    print('Начнем игру!'
          '')
    while candy_count > 28:
        name = get_name(player1, player2, flag)
        print(f'Ходит {name}')
        if name == 'Bot':
            take = randint(1, 29)
        else:
            take = input_move(max_take)
        candy_count -= take
        print(f'{name} взял {take} конфет. На столе осталось {candy_count}')
        flag = not flag

    print(f'Последний ход за {get_name(player1, player2, flag)} и он забирает все оставшиеся'
          f' конфеты и конфеты оппонента.\n'
          f'Поздравляем с победой!')


main()
