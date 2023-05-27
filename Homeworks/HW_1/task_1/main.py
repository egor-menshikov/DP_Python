# 1. На вход подается число с плавающей точкой, выведите первую цифра дробной части

data = [i for i in input('enter a float number:\n').split('.')]
print(data[1][0])