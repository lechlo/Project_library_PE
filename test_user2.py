import unittest
from utils import User

class TestUserClass(unittest.TestCase):
    """Класс для тестирования функций класса User.
    """

    def test_user_creation(self):
        """Тест для проверки создания пользователя.
        """

        user = User("John", "Doe", "Ser", "13.04.2001", "johndoe@example.com", "студент")
        self.assertEqual(user.name, "John")
        self.assertEqual(user.fam, "Doe")
        self.assertEqual(user.oth, "Ser")
        self.assertEqual(user.date, "13.04.2001")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertEqual(user.status, "студент")

    def test_change_password(self):
        """Тест для проверки изменения пароля пользователя.
        """

        user = User("John", "Doe", "Ser", "13.04.2001", "johndoe@example.com", "студент")
        user.change_password("newpassword456")
        self.assertEqual(user.password, "newpassword456")

    def test_user_borrow_book(self):
        """Тест для проверки алгоритма аренды книги пользователем.
        """

        user = User("John", "Doe", "Ser", "13.04.2001", "johndoe@example.com", "студент")
        book_info = ("Test Book", "Author", "1234", 5)
        result = user.borrow_book(book_info)
        self.assertTrue(result)  # Assuming borrow_book returns True on success

if __name__ == '__main__':
    unittest.main()