import unittest
from main import LibraryEngine as Lib


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.library_engine1 = Lib()
        self.library_engine2 = Lib()

    def test_something(self):
        """
        - создается один объект класса LibraryEngine
        :return:
        """

        self.assertEqual(id(self.library_engine1), id(self.library_engine2),
                         "создается несколько объектов класса LibraryEngine")


if __name__ == '__main__':
    unittest.main()
