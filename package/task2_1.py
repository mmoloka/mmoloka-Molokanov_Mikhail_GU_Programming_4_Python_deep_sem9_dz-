import csv
from random import randint
from typing import Callable

# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

def deco_1(func: Callable):
    def wrapper_1(csv_file: str):
        with open(csv_file, 'r', newline='') as f:
            csv_reader = csv.reader(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            result = []
            for line in csv_reader:
                a = line[0]
                b = line[1]
                c = line[2]
                result.append(func(a, b, c))
        return result
    return wrapper_1        

@deco_1
def quadratic_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        return 'Действительных корней нет'
    
def generator_numbers_in_csv(csv_file: str, count_lines: int) -> None:
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, dialect='excel') 
        for _ in range(count_lines):
            a = randint(-999, 999)
            b = randint(-999, 999)
            c = randint(-999, 999)
            line = [a, b, c]
            csv_writer.writerow(line)

if __name__ == '__main__':
    generator_numbers_in_csv('three_numbers.csv', 110)
    print(quadratic_equation('three_numbers.csv'))
