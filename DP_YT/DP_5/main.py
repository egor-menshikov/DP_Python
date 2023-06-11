# from typing import Callable
#
#
# def two_sum(a: int, b: int) -> int:
#     return a + b
#
#
# list_ = [(1, 2), (3, 4)]
#
#
# def operation(func: Callable, obj1, obj2):
#     return func(obj1, obj2)
#
#
# print(list(map(two_sum, (a for a, b in list_), (b for a, b in list_))))
# list_2 = list(map(two_sum, (a for a, b in list_), (b for a, b in list_)))
# print(type(list_2[0]))

# _______________________________________________________________________


# import builtins
# help(builtins)


# a = 'sdadadaad'
# b = 'basfa'
# print(sorted(a, reverse=True))

text = [i for i in'safdh137hrf2fj92jgf92gf']
list_ = list(enumerate(sorted(text)))
print(*list_, sep='\n')