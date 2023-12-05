import unittest
from main import is_palindrome

class TestPalindromeScript(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertTrue(is_palindrome("kayak"))

    def test_isNotPalindrome(self):
        self.assertFalse(is_palindrome(("yakak")))

    def test_isPalindromeEmpty(self):
        self.assertTrue(is_palindrome(""))

    def test_isPalindromeOneChar(self):
        self.assertTrue(is_palindrome("a"))

    """def test_isPalindromeMaj(self):
        self.assertTrue(is_palindrome("Kayak"))"""


if __name__ == '__main__':
    unittest.main()