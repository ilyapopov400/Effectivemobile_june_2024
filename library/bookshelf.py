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

    def __get_data_from_db(self):
        """

        :return: словарь с данными из файла json с БД
        """
        with open(file=self.db, mode="r") as f:
            data = f.read()
            data = json.loads(data)
        return data

    def set_book(self, title: str, author: str, year: int, status: str = "in stock"):
        """
        - записываем в БД книгу
        :param title:
        :param author:
        :param year:
        :param status:
        :return:
        """
        data = self.__get_data_from_db()
        if status not in ("in stock", "out stock"):
            raise ValueError("status может принимать значения только 'in stock', 'out stock'")

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
        data = self.__get_data_from_db()

        with open(file=self.db, mode="w") as f:
            try:
                data.pop(id)
                print("Книга с идентификатором {} удалена".format(id))
            except KeyError:
                print("Нет книги с идентификатором {}".format(id))
            json.dump(data, f, indent=2)

    def get_book(self, title: str = None, author: str = None, year: int = None, status: str = None):
        """
        - поиск книги по параметрам
        :param title:
        :param author:
        :param year:
        :param status:
        :return:
        """
        result_id, result = set(), list()
        data = self.__get_data_from_db()
        for book in data.values():
            if title == book.get("title"):
                result_id.add(book.get("id"))
            if author == book.get("author"):
                result_id.add(book.get("id"))
            if year == book.get("year"):
                result_id.add(book.get("id"))
            if status == book.get("status"):
                result_id.add(book.get("id"))

        for id in result_id:
            result.append(
                data.get(str(id))
            )

        for _ in range(len(result)):
            for i in range(len(result)):
                book = result[i]
                if title and book.get("title") != title:
                    result.pop(i)
                    break

        for _ in range(len(result)):
            for i in range(len(result)):
                book = result[i]
                if author and book.get("author") != author:
                    result.pop(i)
                    break

        for _ in range(len(result)):
            for i in range(len(result)):
                book = result[i]
                if year and book.get("year") != year:
                    result.pop(i)
                    break

        for _ in range(len(result)):
            for i in range(len(result)):
                book = result[i]
                if status and book.get("status") != status:
                    result.pop(i)
                    break
        return result

    def show_books(self):
        data = self.__get_data_from_db()
        return list(data.values())


if __name__ == "__main__":
    bookshelf = BookShelf()
    # bookshelf.set_book(title="man", author="Ilya", year=1975, status='out stock')
    # bookshelf.del_book(id=2)
    print(*bookshelf.get_book(title="man", status='out stock'), sep="\n")
    # print(*bookshelf.show_books(), sep="\n")
