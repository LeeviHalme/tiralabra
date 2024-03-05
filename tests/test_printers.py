import unittest
from src.utils.printers import print_help_page, print_logo

# these tests are not very useful,
# because they both return void and
# do side effects that can't be tested
class TestPrinters(unittest.TestCase):
    def test_print_help_page(self):
        print_help_page()

    def test_print_logo(self):
        print_logo()
