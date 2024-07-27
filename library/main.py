"""
- основной файл для работы с библиотекой
"""
from bookshelf import BookShelf


class Library:
    def __init__(self):
        self.bookshelf = BookShelf()

    def __hello(self):
        text = "Добрый пожаловать в нашу библиотеку\n" + self.__help()
        return text

    @staticmethod
    def __help():
        text = """
            1 - help;
            2 - Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”;
            3 - Удаление книги: Пользователь вводит id книги, которую нужно удалить;
            4 - Поиск книги: Пользователь может искать книги по title, author или year;
            5 - Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status;
            6 - Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”);
            При наборе пустого символа программа прекращает работу
        """
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
        except ValueError:
            return
        if bool(status) is False:
            self.bookshelf.set_book(title=title, author=author, year=year)
        else:
            self.bookshelf.set_book(title=title, author=author, year=year, status=status)

    def run(self):
        print(self.__hello())
        while True:
            command_to_execute = input(
                "Наберите команду (цифра от 1 до 6 или нажмите ввод для окончания работы программы): ")
            if command_to_execute and command_to_execute not in ("1", "2", "3", "4", "5", "6"):
                print("Нет такой команды на выполнение")
                continue
            if not bool(command_to_execute):
                print("До свидания")
                break
            if command_to_execute == "1":
                print(self.__help())
                continue
            if command_to_execute == "2":
                self.__set_book_2()
                continue


if __name__ == "__main__":
    library = Library()
    library.run()
