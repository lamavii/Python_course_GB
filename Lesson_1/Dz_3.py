# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10

# Загадываем число
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Приветствую! Я загадал число от", LOWER_LIMIT, "до", UPPER_LIMIT)

for _ in range(attempts):
    guess = int(input("Попробуйте угадать число: "))

    if guess < num:
        print("Загаданное число больше")
    elif guess > num:
        print("Загаданное число меньше")
    else:
        print("Поздравляю! Вы угадали число", num)
        break
else:
    print("Увы! Попытки закончились. Было загадано число", num)