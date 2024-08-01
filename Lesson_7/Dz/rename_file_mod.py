# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import random
import string
import os

__all__ = ['rename_group']

def create_random_files(quantity: int):
    file_ext = ['txt', 'jpg', 'mov', 'mp3', 'bin', 'csv', 'md', 'doc']
    for _ in range(quantity):
        name = ''.join(random.sample(string.ascii_lowercase, 10)) + '.' + random.choice(file_ext)
        with open(name, 'w', encoding='utf-8') as file:
            file.write(name)


# create_random_files(2)

def rename_group(path: str = os.getcwd(),
                 new_name: str = '',
                 count: int = 1,
                 in_ext: str = '',
                 out_ext: str = '___',
                 limits: tuple = (0, 10)):
    counter = 1
    if os.path.isdir(path):
        for file in os.listdir(path):
            name, ext = file.rsplit('.', 1)
            if ext == in_ext or not in_ext:
                re_name = (f'{name[limits[0]:limits[1]]}'
                           f'{new_name if new_name else ""}'
                           f'{counter:0>{count}}.{out_ext}')
                os.rename(os.path.join(path, file), os.path.join(path, re_name))
                counter += 1
        print(f'Было переименовано {counter - 1}')
    else:
        print('Это не директория!')


if __name__ == '__main__':
    rename_group(new_name='new', in_ext='txt', out_ext='jpeg', count=5, limits=(2, 7))
