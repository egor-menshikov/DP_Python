# 5. Дана строка текста, необходимо сформировать из нее две новых строки
# из символов которые стоят на четных позициях и на нечетных

text = input('Введите строку:\n')
even = ''
odd = ''
for i in range(len(text)):
    if not i % 2:
        even += text[i]
    else:
        odd += text[i]
print(even, odd)