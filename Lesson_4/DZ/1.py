# 1. Напишите функцию для транспонирования матрицы

def change_matrix(matrix:list[list[int]]) -> list[list[int]]:
    return list(zip(*matrix))

print(change_matrix())