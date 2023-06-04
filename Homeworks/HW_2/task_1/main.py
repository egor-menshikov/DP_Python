# 1. Игра Fizz-Buzz
# Есть детская игра FizzBuzz, где нужно называть числа подряд, соблюдая всего три правила:
# Если число делится на 3, вместо него надо сказать «Fizz».
# Если число делится на 5, вместо него надо сказать «Buzz».
# А если число делится одновременно на 3 и на 5, то надо вместо него сказать «FizzBuzz».
# На вход подается число num, нужно вывести числа или слова по порядку от 1 до num (включительно) согласно правилам игры

def fizz_buzz():
    list_ = [_ for _ in range(1, int(input('Введите последнее число последовательности: ')) + 1)]
    for item in list_:
        if not item % 3 and not item % 5:
            print('FizzBuzz', end= ' ')
        elif not item % 3:
            print('Fizz', end= ' ')
        elif not item % 5:
            print('Buzz', end= ' ')
        else:
            print(item, end= ' ')
fizz_buzz()