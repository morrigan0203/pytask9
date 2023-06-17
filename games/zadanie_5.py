""" Объедините функции из прошлых задач. Функцию угадайку задекорируйте декораторами для сохранения параметров, 
декоратором контроля значений и декоратором для многократного запуска. Выберите верный порядок декораторов. """

import random
from typing import Callable 

import zadanie_3 as z3
import zadanie_4 as z4
import zadanie_2 as z2

@z4.count(3)
@z2.deco
@z3.deco
def two_numbers(count_try: int, num: int):
    print("5.", count_try, num)
    for i in range(1, count_try + 1):
        user_input = input('Введите число для отгадывания от 1 до 100 : ')
        if int(user_input) == num:
            print(f'Вы угадали с {i} попытки')
            return True
    else:
        print('Вы не угадали')
    return False


if __name__ == '__main__':
    #print(1)
    res = two_numbers(30, 200)

