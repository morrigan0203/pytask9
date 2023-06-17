""" Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор. Он должен проверять входят ли переданные в 
функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. Если не входят, вызывать функцию со случайными числами из диапазонов.
 """

from typing import Callable
import random
from functools import wraps

def deco(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100

    @wraps(func)
    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count > MAX_COUNT:
            input_count = random.randint(MIN_COUNT, MAX_COUNT)
        if MIN_NUM > input_num or input_num > MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_count, input_num)

    return wrapper

@deco
def two_numbers2(count_try: int, num: int) -> Callable[[], None]:
    def random_numbers():
        for i in range(1, count_try + 1):
            user_input = input('Введите число для отгадывания от 1 до 100: ')
            if int(user_input) == num:
                print(f'Вы угадали с {i} попытки')
                break
        else:
            print('Вы не угадали')

    return random_numbers

if __name__=="__main__":
    res = two_numbers2(11, 200)
    res()
