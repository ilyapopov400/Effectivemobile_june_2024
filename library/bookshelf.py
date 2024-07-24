"""
- работа с БД библиотеки
"""
import json
import os


class BookShelf:
    DB = "db.json"  # файл с json
    """
    - класс для работы с БД библиотеки
    """

    def __init__(self):
        self.db = self.__class__.DB
        if not os.path.exists(self.db):  # создаем файл при его отсутствии
            with open(file=self.db, mode="w") as f:
                content = dict()
                json.dump(content, f)

    def set_book(self, title: str, author: str, year: int, status: bool):
        """
        - записываем в БД книгу
        :param title:
        :param author:
        :param year:
        :param status:
        :return:
        """
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

    def del_book(self, id: int):
        """
        - удаляем из БД книгу по идентификатору ID
        :param id:
        :return:
        """
        id = str(id)
        with open(file=self.db, mode="r") as f:
            data = f.read()
            data = json.loads(data)

        with open(file=self.db, mode="w") as f:
            try:
                data.pop(id)
                print("Книга с идентификатором {} удалена".format(id))
            except KeyError:
                print("Нет книги с идентификатором {}".format(id))
            json.dump(data, f, indent=2)


if __name__ == "__main__":
    bookshelf = BookShelf()
    bookshelf.set_book(title="man", author="Ilya", year=1975, status=True)
    bookshelf.del_book(id=1)
