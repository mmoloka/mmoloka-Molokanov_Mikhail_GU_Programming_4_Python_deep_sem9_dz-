import json
import os
from typing import Callable

def deco_2(func: Callable):
    data = []
    for obj in os.listdir():
        if os.path.isfile(obj) and obj == f'{func.__name__}.json':
            with open(obj, 'r', encoding='utf-8') as f:
                data = json.load(f)
    def wrapper_2(*args):
        result = func(*args)
        json_dict = {'args': args, 'res': result}
        data.append(json_dict)
        with open('result.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return result
    return wrapper_2 

@deco_2
def quadratic_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        return 'Действительных корней нет'
    
if __name__ == '__main__':
    quadratic_equation(-4, 28, -49)  
    quadratic_equation(-6, 0, 54)
    quadratic_equation(3, -4, 94)      