"""
- работа с БД библиотеки
"""
import json
import os


class BookShelf:
    """
    - класс для работы с БД библиотеки
    """

    def __init__(self, db: str):
        """
        :param db: patch for db.json
        """
        self.db = db
        if not os.path.exists(self.db):  # создаем файл при его отсутствии
            with open(file=self.db, mode="w") as f:
                content = dict()
                json.dump(content, f)

    def set(self, title: str, author: str, year: int, status: bool):
        with open(file=self.db, mode="r") as f:
            data = f.read()
            data = json.loads(data)

        with open(file=self.db, mode="w") as f:
            if not data:
                id = 1
            else:
                id = max(
                    [int(i) for i in data.keys()]
                ) + 1
            content = {
                'id': id,
                'title': title,
                'author': author,
                'year': year,
                'status': status,
            }
            data[id] = content
            json.dump(data, f, indent=2)


if __name__ == "__main__":
    bookshelf = BookShelf(db="db.json")
    bookshelf.set(title="man", author="Ilya", year=1975, status=True)
