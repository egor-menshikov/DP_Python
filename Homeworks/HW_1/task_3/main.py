# На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное.

number = input('Введите число:\n')
num_list = [int(item) for item in number if item.isdigit()]
print(sum(num_list))
