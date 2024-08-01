import json
import csv
from pathlib import Path

__all__ = ['csv_to_json']
def csv_to_json(from_path: Path, to_path: Path) -> None:
    result = []
    with open(from_path, 'r', encoding='utf-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, row in enumerate(csv_read):
            if i != 0:
                level, id, name = row
                data = {
                    "level": int(level),
                    "id": f'{int(id):010}',
                    "name": name.title(),
                    "hash": hash(f'{name.title()}{int(id):010}')
                }
                result.append((data))
    with open(to_path, 'w', encoding='utf-8') as f_write:
        json.dump(result, f_write, indent=4, ensure_ascii=False)




if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_user.json'))
