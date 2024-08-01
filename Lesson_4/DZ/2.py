# 2. Напишите функцию принимающую на вход только ключевые параметры
# и возвращающую словарь, где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


# my_dict = {1:'one', 2:['two'], '3':('three',)}

def func(**kwargs) -> dict:
    new_dict = {}
    for key, value in kwargs.items():
        if not isinstance(value, (list, set, dict)):
            new_dict[value] = key
        else:
            new_dict[str(value)] = key
    return new_dict


print(func(one=1, two=['2'], three=(3,)))
