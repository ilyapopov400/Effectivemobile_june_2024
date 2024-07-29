"""
- основной файл для работы с библиотекой
"""
from bookshelf import BookShelf


class LibraryEngine:
    def __init__(self):
        self.bookshelf = BookShelf()
        self.command_dict = {
            "1": self.__help_1,
            "2": self.__set_book_2,
            "3": self.__del_book_3,
        }

    def __hello(self):
        text = "Добрый пожаловать в нашу библиотеку\n" + self.__help_1()
        return text

    @staticmethod
    def __help_1():
        text = """
            1 - help;
            2 - Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”;
            3 - Удаление книги: Пользователь вводит id книги, которую нужно удалить;
            4 - Поиск книги: Пользователь может искать книги по title, author или year;
            5 - Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status;
            6 - Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”);
            При наборе пустого символа программа прекращает работу
        """
        print(text)
        return text

    def __set_book_2(self) -> None:
        """
        - записываем книгу в библиотеку
        :return: None
        """
        title = input("название книги: ")
        author = input("автор книги: ")
        year = input("год издания: ")
        status = input("статус книги: 'in stock', 'out stock', (необязательный параметр, по умолчанию 'in stock'): ")
        try:
            year = int(year)
            if bool(status) is False:
                self.bookshelf.set_book(title=title, author=author, year=year)
            else:
                self.bookshelf.set_book(title=title, author=author, year=year, status=status)
        except ValueError:
            print("Неверные или недостаточные данные")
            return

    def __del_book_3(self):
        """
        - удаляем книгу из библиотеки по "id"
        :return:
        """
        id_list = list(self.bookshelf.get_data_from_db())
        if not bool(id_list):
            print("В библиотеке нет книг")
            return
        id_list = ", ".join(id_list)

        print("В библиотеке есть книги с ID: ", id_list)

        id_for_del = input("Наберите ID для удаляемой книги: ")
        try:
            self.bookshelf.del_book(id=int(id_for_del))
        except ValueError:
            print("Неверные данные")
            return

    def run(self):
        print(self.__hello())
        while True:
            command_to_execute = input(
                "Наберите команду (цифра от 1 до 6 или нажмите ввод для окончания работы программы): ")
            if not bool(command_to_execute):
                print("До свидания")
                break
            if command_to_execute not in ("1", "2", "3", "4", "5", "6"):
                print("Нет такой команды на выполнение")
                continue

            self.command_dict.get(command_to_execute)()  # вызов метода для исполнения


if __name__ == "__main__":
    library = LibraryEngine()
    library.run()
