# Создайте функцию генератор чисел Фибоначчи


def fibonachi(number: int = 11) -> int:
    a, b = 0, 1
    while number > 0:
        yield a
        a, b, = b, a + b
        number -= 1


for i in fibonachi():
    print(i)