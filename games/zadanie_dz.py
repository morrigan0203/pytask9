import math
import json
from random import randint
from typing import Callable
from functools import wraps

def read(fileName: str):
    def deco(func: Callable):
        with open(f'{fileName}', 'r') as f:
            params = json.load(f)
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in params:
                func(i["a"],i["b"],i["c"])
        return wrapper
    return deco

def save(fileName: str):
    def deco(func: Callable):
        with open(f'{fileName}', 'r') as f:
            data = json.load(f)
        @wraps(func)
        def wrapper(*args, **kwargs):
            final_dict = {}
            res = func(*args, **kwargs)
            for i in range(len(args)):
                final_dict.update({str(i): args[i]})
            final_dict.update({"res":res})
            final_dict.update({**kwargs})
            data.append(final_dict)
            with open(f'{fileName}', 'w') as f:
                json.dump(data, f, indent=2)
        return wrapper
    return deco

@read("data01.json")
@save("res01.json")
def findRoot(a: int, b: int, c: int):
    """Функция расчета корнец квадратного уравнния"""
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return (x1,x2)
    elif d == 0:
        x1 = -b/(2*a)
        return (x1, None)
    return (None, None)

def genNums(fileName: str, countVars: int):
    data = []
    for i in range(countVars):
        vars = {"a":randint(-100,100),"b":randint(-100,100),"c":randint(-100,100)}
        data.append(vars)
    with open(f'{fileName}', 'w') as f:
        json.dump(data, f, indent=2)


if __name__=="__main__":
    print(findRoot(5,20,10))
    #help(findRoot)
    #genNums('data01', 10)
    