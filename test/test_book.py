import unittest
from utils import Book

class TestBookClass(unittest.TestCase):

    def test_qr_show(self):
        book = Book("Test Book", "1234", 5)
        # Тут можно добавить тесты для метода qr_show

    def test_reserve_book(self):
        book = Book("Test Book", "110234", 5)
        book_info = ("Test Book", "Author", "1234", 5)
        prov_test = None1111111111111111111111111
        # Тут можно добавить тесты для метода reserve_book

if __name__ == '__main__':
    unittest.main()