# 6. Проверка на палиндром:
#    а. слова
#    б. предложения

text = input('Введите слово:\n')
if text.casefold() == text[::-1].casefold():
    print('Палиндром')
else:
    print('Не палиндром')

sentence = input('Введите предлождение:\n')
sentence = sentence.replace(' ', '')
if sentence.casefold() == sentence[::-1].casefold():
    print('Палиндром')
else:
    print('Не палиндром')
