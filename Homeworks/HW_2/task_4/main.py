# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи
# (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
from typing import List


def fibo(n: int) -> int:
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n - 1) + fibo(n - 2)


def fibo_nega_list(num: int) -> list[int]:
    list_fib = [fibo(i) for i in range(num + 1)]
    list_nega = list_fib[:0:-1]
    for i in range(-1, -len(list_nega) - 1, -1):
        if not i % 2:
            list_nega[i] *= -1
    return list_nega + list_fib

fib_num = int(input('Введите число: '))
print(fibo_nega_list(fib_num))

