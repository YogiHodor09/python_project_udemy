import unittest
import cap_text

'''
unittest.TestCase - Inherited the TestCase method from unittest class
'''


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap_text.capitalize_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monti python'
        result = cap_text.capitalize_text(text)
        self.assertEqual(result, 'Monti Python')


if __name__ == '__main__':
    unittest.main()
