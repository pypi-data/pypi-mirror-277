# tests/test_core.py

import unittest
from stringutils.core import to_snake_case, to_camel_case, remove_special_characters, normalize_whitespace

class TestStringUtils(unittest.TestCase):
    def test_to_snake_case(self):
        self.assertEqual(to_snake_case('CamelCaseString'), 'camel_case_string')

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case('snake_case_string'), 'snakeCaseString')

    def test_remove_special_characters(self):
        self.assertEqual(remove_special_characters('Hello, World!'), 'Hello World')

    def test_normalize_whitespace(self):
        self.assertEqual(normalize_whitespace('Hello   World'), 'Hello World')

if __name__ == '__main__':
    unittest.main()
