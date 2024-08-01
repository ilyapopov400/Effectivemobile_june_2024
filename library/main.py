"""
- основной файл для работы с библиотекой
Программа запускается через LibraryEngine.run() и выполняется в бесконечном цикле.
Прерывание осуществляется через ввод пустой строки
"""
from bookshelf import BookShelf


class LibraryEngine:
    __instance = None

    def __new__(cls, *args, **kwargs):
        """
        - используем паттерн Singleton для создания только одного объекта этого класса
        :param args:
        :param kwargs:
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        self.__class__.__instance = None

    def __init__(self):
        self.bookshelf = BookShelf()
        self.command_dict = {
            "1": self.__help_1,
            "2": self.__set_book_2,
            "3": self.__del_book_3,
            "4": self.__get_book_4,
            "5": self.__show_5,
            "6": self.__changing_book_processing_6,

        }

    @staticmethod
    def hello():
        text = "Добрый пожаловать в нашу библиотеку\n"
        print(text)

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

    @staticmethod
    def show_one_book(book):
        """
        - данные об одной книге
        :return:
        """
        id_book = book.get("id")
        title = book.get("title")
        author = book.get("author")
        year = book.get("year")
        status = book.get("status")
        if status == "in stock":
            status = "в наличие"
        else:
            status = "выдана"
        return "id: {}, название: {}, автор: {}, год выпуска: {}, наличие в библиотеке: {}".format(id_book, title,
                                                                                                   author, year, status)

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

    def __get_book_4(self):
        """
        - поиск книги: Пользователь может искать книги по title, author, year или status
        :return:
        """
        len_book = len(self.bookshelf.get_data_from_db())
        print("Сейчас в библиотеке {} книг".format(len_book))
        if len_book == 0:
            print("Подождите, сейчас книг в библиотеке нет")
            return
        title = input("Введите название книги или нажмите ввод: ")
        author = input("Введите имя автора книги или нажмите ввод: ")
        year = input("Введите год издания книги или нажмите ввод: ")
        status = input("Введите статус книги или нажмите ввод: ")
        if not title:
            title = None
        if not author:
            author = None
        if not year:
            year = None
        if not any(
                (title, author, year, status)
        ):
            print("Неверные или недостаточные данные")
            return
        if year:
            try:
                year = int(year)
            except ValueError:
                return
        if status and status not in ('in stock', 'out stock'):
            print("status может принимать значения только 'in stock', 'out stock'")
            return

        result = self.bookshelf.get_book(title=title, author=author, year=year, status=status)
        print("Найденные книги:")
        if not result:
            print("По Вашему запросу книг не найдено")
            return
        for book in result:
            print(self.show_one_book(book=book))

    def __show_5(self):
        """
        - Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status
        :return:
        """
        data = self.bookshelf.get_data_from_db().values()
        if not data:
            print("Нет книг в библиотеке")
            return
        print("Книги в библиотеке:")
        for book in data:
            print(self.show_one_book(book=book))

    def __changing_book_processing_6(self):
        """
        - Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”);
        :return:
        """
        id_list = list(self.bookshelf.get_data_from_db())
        if not bool(id_list):
            print("В библиотеке нет книг")
            return

        print("В библиотеке есть книги с ID: ", ", ".join(id_list))

        id_for_changing = input("Наберите ID для изменяемой книги: ")
        if id_for_changing not in id_list:
            print("Неверное значение для ID")
            return
        book_for_changing = self.bookshelf.get_data_from_db().get(id_for_changing)
        print("Изменяемая книга: \n", self.show_one_book(book=book_for_changing))
        status_new = input("Наберите новый статус для изменяемой книги: 1 - 'в наличие', 2 - 'выдана'): ")
        if status_new == "1":
            self.bookshelf.changing_book_processing(id=int(id_for_changing), new_status="in stock")
        elif status_new == "2":
            self.bookshelf.changing_book_processing(id=int(id_for_changing), new_status="out stock")
        else:
            print("Неверно выбрано значение")


def mane():
    """
    - обрабатываем вводные данные пользователя

    :return:
    """
    library = LibraryEngine()
    library.hello()
    library.command_dict.get("1")()
    while True:
        command_to_execute = input(
            "Наберите команду (цифра от 1 до {} или нажмите ввод для окончания работы программы): ".format(
                len(library.command_dict)))
        if not bool(command_to_execute):
            print("До свидания")
            break

        if command_to_execute not in (map(str, range(1, len(library.command_dict) + 1))):
            print("Нет такой команды на выполнение")
            continue

        library.command_dict.get(command_to_execute)()  # вызов метода для исполнения


if __name__ == "__main__":
    mane()
