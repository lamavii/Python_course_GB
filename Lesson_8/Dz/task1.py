from pathlib import Path
import json

__all__ = ['input_user']

def input_user(path: Path) -> None:
    unique_id = set()
    if not path.is_file():
        data = {str(level): {} for level in range(1, 8)}
    else:
        with open(path, 'r', encoding='utf-8') as file_read:
            data = json.load(file_read)
            # unique_id = {id for id_name in data.values() for id in id_name.keys()}
            for id_name in data.values():
                unique_id.update(id_name.keys())

    while name := input('Enter user_name: '):
        level = input('Enter level from 1 to 7: ')
        user_id = input('Enter user_id: ')
        if user_id not in unique_id:
            unique_id.add(user_id)
            data[level].update({user_id: name})
            with open(path, 'w', encoding='utf-8') as file_write:
                json.dump(data, file_write, indent=4, ensure_ascii=False)
        else:
            print('Such user is exist already!!!')


if __name__ == '__main__':
    input_user(Path('users.json'))
