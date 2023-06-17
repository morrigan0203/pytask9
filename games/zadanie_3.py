""" Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она возвращает. 
При повторном вызове файл должен расширяться, а не перезаписываться.
●	Каждый ключевой параметр сохраните как отдельный ключ json словаря.
●	Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
●	Имя файла должно совпадать с именем декорируемой функции. """


import json
from typing import Callable
from functools import wraps


def deco(func: Callable):
    with open(f'{func.__name__}.json', 'r') as f:
        final_dict_arr = json.load(f)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        final_dict = {}
        res = func(*args, **kwargs)
        for i in range(len(args)):
            final_dict.update({str(i): args[i]})
        final_dict.update({"res":res})
        final_dict.update({**kwargs})
        final_dict_arr.append(final_dict)
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict_arr, f, indent=2)

    return wrapper


@deco
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__=="__main__":
    multy(6, 7, temp=2, r=3, c=2, d=5)

