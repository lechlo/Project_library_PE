import unittest
from utils import Book

class TestBookClass(unittest.TestCase):
    """Класс для тестирования функций класса Book.
    """

    def test_qr_show(self):
        """Тест для метода qr_show.
        """

        book = Book("Test Book", "1234", 5)
        # Тут можно добавить тесты для метода qr_show

    def test_reserve_book(self):
        """Тест для метода reserve_book.
        """

        book = Book("Test Book", "1234", 5)
        book_info = ("Test Book", "Author", "1234", 5)
        prov_test = None
        # Тут можно добавить тесты для метода reserve_book

if __name__ == '__main__':
    unittest.main()