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

    def __init__(self) -> None:
        self.db = self.__class__.DB
        if not os.path.exists(self.db):  # создаем файл при его отсутствии
            with open(file=self.db, mode="w") as f:
                content = dict()
                json.dump(content, f)

    def get_data_from_db(self) -> dict:
        """

        :return: словарь с данными из файла json с БД
        """
        with open(file=self.db, mode="r") as f:
            data = f.read()
            data = json.loads(data)
        return data

    def set_book(self, title: str, author: str, year: int, status: str = "in stock") -> None:
        """
        - записываем в БД книгу
        :param title:
        :param author:
        :param year:
        :param status:
        :return:
        """
        data = self.get_data_from_db()
        if status not in ("in stock", "out stock"):
            raise ValueError("status может принимать значения только 'in stock', 'out stock'")
        if not all((
                bool(title), bool(author), bool(year))
        ):
            raise ValueError("Недостаточно передано данных")

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

    def del_book(self, id: int) -> None:
        """
        - удаляем из БД книгу по идентификатору ID
        :param id:
        :return:
        """
        id = str(id)
        data = self.get_data_from_db()

        with open(file=self.db, mode="w") as f:
            try:
                data.pop(id)
                print("Книга с идентификатором {} удалена".format(id))
            except KeyError:
                print("Нет книги с идентификатором {}".format(id))
            json.dump(data, f, indent=2)

    def get_book(self, title: str = None, author: str = None, year: int = None, status: str = None) -> list:
        """
        - поиск книги по параметрам
        :param title:
        :param author:
        :param year:
        :param status:
        :return: list
        """
        result_id, result = set(), list()
        data = self.get_data_from_db()
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

    def show_books(self) -> list:
        """
        - возвращает список всех книг в виде dict
        :return: list
        """
        data = self.get_data_from_db()
        return list(data.values())

    def changing_book_processing(self, id: int, new_status: str = "in stock") -> None:  # TODO
        """
        - Пользователь вводит id книги и новый статус (“в наличии” или “выдана”)
        :param id: int
        :return:
        """
        if new_status not in ("in stock", "out stock"):
            raise ValueError("status может принимать значения только 'in stock', 'out stock'")
        data = self.get_data_from_db()
        data_list = list(data.values())
        result = list(filter(lambda x: x.get("id") == id, data_list))
        if not result:
            print("книга с идентификатором {} отсутствует".format(id))
            return
        book = result[0]
        book["status"] = new_status
        data[str(id)] = book
        with open(file=self.db, mode="w") as f:
            json.dump(data, f, indent=2)


if __name__ == "__main__":
    bookshelf = BookShelf()
    # bookshelf.set_book(title="man", author="Ilya", year=1975, status='in stock')
    # bookshelf.set_book(title="woman", author="Vera", year=1971, status='out stock')
    # bookshelf.set_book(title="girl", author="Dasha", year=2002)

    # bookshelf.del_book(id=1)
    # print(*bookshelf.get_book(title="man", status='out stock'), sep="\n")
    # print(*bookshelf.show_books(), sep="\n")
    bookshelf.changing_book_processing(id=2, new_status="out stock")
