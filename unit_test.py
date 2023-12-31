import unittest
import datetime
from main import is_palindrome, bienDit, get_salutation, auRevoir

class TestPalindromeScript(unittest.TestCase):

    def test_isPalindrome(self):
        for chaine in ["kayak", "", "a", "Kayak"]:

            resultat = is_palindrome(chaine)
            returnResult = bienDit(chaine)

            self.assertTrue(resultat)

    def test_isNotPalindrome(self):
        word = "yakak"

        resultat = is_palindrome(word)

        self.assertFalse(resultat)

    def test_Miroir(self):
        # ETANT DONNE
        word = "yakak"

        # QUAND
        result = bienDit(word)

        # ALORS
        inversion = word[::-1]
        self.assertEqual(inversion, result)

    def test_BienDit(self):
        word = "kayak"

        result = bienDit(word)

        resultSearch = "Bien dit!"
        self.assertEqual(resultSearch, result)

    def test_Salutation(self):
        for langue in ["fr", "en"]:
            if (langue == "fr"):
                result = get_salutation(langue)

                hour = datetime.datetime.now().hour

                if (6 <= hour < 18):
                    resultSearch = "Bonjour!"

                    self.assertEqual(resultSearch, result)
                else:
                    resultSearch = "Bonsoir!"

                    self.assertEqual(resultSearch, result)
            else:
                result = get_salutation(langue)

                hour = datetime.datetime.now().hour

                if (6 <= hour < 12):
                    resultSearch = "Good morning!"

                    self.assertEqual(resultSearch, result)
                elif (12 <= hour < 18):
                    resultSearch = "Good afternoon!"

                    self.assertEqual(resultSearch, result)
                else:
                    resultSearch = "Good evening!"

                    self.assertEqual(resultSearch, result)

    def test_AuRevoir(self):
        for langue in ["fr", "en"]:
            if (langue == "fr"):
                result = auRevoir(langue)

                hour = datetime.datetime.now().hour

                if (18 <= hour < 24):
                    resultSearch = "Bonne soirée!"

                    self.assertEqual(resultSearch, result)
                else:
                    resultSearch = "Bonne journée!"

                    self.assertEqual(resultSearch, result)
            else:
                result = auRevoir(langue)

                hour = datetime.datetime.now().hour

                if (18 <= hour < 24):
                    resultSearch = "Good night!"

                    self.assertEqual(resultSearch, result)
                else:
                    resultSearch = "Good day!"

                    self.assertEqual(resultSearch, result)


if __name__ == '__main__':
    unittest.main()