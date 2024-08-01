# Добавьте в пакет, созданный на
# семинаре шахматный модуль. Внутри него напишите код, решающий задачу
# о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей
# так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает на
# вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль. Используйте генератор
# случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random

__all__ = ['queens_safe', 'generate_random_queens']
def attack(x1, y1, x2, y2):
    # Проверка, бьют ли два ферзя друг друга в горизонтальной, вертикальной или диагональной линии
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

def queens_safe(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            if attack(x1, y1, x2, y2):
                return False
    return True

def generate_random_queens():
    successful_queens = []
    while len(successful_queens) < 8:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        if (x, y) not in successful_queens:
            successful_queens.append((x, y))
    return successful_queens

if __name__ == '__main__':
    successful_placements = 0
    while successful_placements < 4:
        successful_queens = generate_random_queens()
        result = queens_safe(successful_queens)
        if result:
            successful_placements += 1
            print(f'Успешная расстановка {successful_queens}')