# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов
# и директорий.


import os
import json
import csv
import pickle
from pathlib import Path

__all__ = ['dir_traversal']


def dir_traversal(path: Path) -> None:
    data = []

    for root, dirs, files in os.walk(path):
        dir_size = 0

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            data.append({
                'path': file_path,
                'type': 'file',
                'size': file_size,
                'parent_directory': root
            })

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size += get_dir_size(dir_path)
            data.append({
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': root
            })

    save_to_json(data, 'result.json')
    save_to_csv(data, 'result.csv')
    save_to_pickle(data, 'result.pkl')


def get_dir_size(path):
    total_size = 0

    for path, dirs, files in os.walk(path):
        for file in files:
            f_path = os.path.join(path, file)
            total_size += os.path.getsize(f_path)

    return total_size


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def save_to_csv(data, filename):
    headers = ['path', 'type', 'size', 'parent_directory']
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def save_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    dir_traversal(r'/home/zaur/Learning/Data_Engineer/Deep_Python/Homework8/Package') # указываем собственный путь
