# 2. На вход подается целое число, необходимо поменять местами первую и последняя цифру в числе
number = input('Введите целое число:\n')
list_ = list(number)
list_[0], list_[-1] = list_[-1], list_[0]
number = ''
for i in list_:
    number += i
print(number)