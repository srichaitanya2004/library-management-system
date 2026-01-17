import unittest
from src.library import Library


class TestLibrarySprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        self.assertIn(1, lib.books)

    def test_duplicate_book_raises_error(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        with self.assertRaises(ValueError):
            lib.add_book(1, "Java", "James")


if __name__ == "__main__":
    unittest.main()
class TestLibrarySprint2(unittest.TestCase):

    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        lib.borrow_book(1)
        self.assertTrue(lib.books[1]["borrowed"])

    def test_borrow_unavailable_book_raises_error(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        lib.borrow_book(1)
        with self.assertRaises(ValueError):
            lib.borrow_book(1)

    def test_return_book(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        lib.borrow_book(1)
        lib.return_book(1)
        self.assertFalse(lib.books[1]["borrowed"])
class TestLibrarySprint3(unittest.TestCase):

    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        lib = Library()
        lib.add_book(1, "Python", "Guido")
        report = lib.generate_report()
        self.assertIn("Python", report)
