from random import choice
from envparse import env
import os




def gain():
    get_list = [i for i in range(1, 31)]
    env.read_envfile('setting.env')
    my_money = int(os.getenv('MY_MONEY'))
    while True:
        stavka = int(input("Введите номер слота: "))
        if stavka <= 0:
            print('Вводите в числа в районе 1-30')
            continue
        elif stavka >= 31:
            print('Вводите в числа в районе 1-30')
            continue
        else:
            stavka_baks = int(input("Сумма ставки: "))
            if my_money < stavka_baks:
                print('У вас не так много денег')
                continue
            my_money -= stavka_baks
            if stavka == choice(get_list):
                dengi = stavka_baks * 2
                my_money += dengi
                print('Вы выиграли!')
            else:
                print('Вы проиграли)')
                stavka_baks = 0
            print(f'У вас осталось {my_money}')

            if my_money <= 0:
                print('у вас закончились деньги')
                break

        continue_play = input('Вы хотите продолжить игру? Напишите "Да","Yes" или "Нет","No": ')
        if continue_play.isupper() == 'да' or 'yes':
            continue
        elif continue_play.isupper() == 'нет' or 'no':
            print('До скорой встречи!')
            break
        else:
            print('Пишите корректно')
            continue


