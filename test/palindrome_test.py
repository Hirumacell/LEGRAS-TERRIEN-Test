import os
import unittest

from src.langueFrancaise import LangueFrancaise
from src.langueAnglaise import LangueAnglaise
from utilities.detecteurPalindromeBuilder import DetecteurPalindromeBuilder
from utilities.langueSpy import LangueSpy

cas_test_non_palindrome = ['test', 'epsi']


class MyTestCase(unittest.TestCase):

    def test_miroir(self):
        # ETANT DONNE une chaine
        for chaine in cas_test_non_palindrome:
            with self.subTest(chaine):
                # QUAND je demande si elle est un palindrome
                detecteur = DetecteurPalindromeBuilder().build()
                resultat = detecteur.detecter(chaine)

                # ALORS j'obtiens cette chaine en miroir
                attendu = chaine[::-1]
                self.assertIn(attendu, resultat)


    def test_felicitation(self):
        cas = [[LangueFrancaise(), "Bien dit !"], [LangueAnglaise(), "Well said !"]]

        for param in cas:
            with self.subTest(param[0]):
                langue = param[0]
                palindrome = 'kayak'

                resultat = DetecteurPalindromeBuilder().ayantPourLangue(langue).build().detecter(palindrome)

                attendu = palindrome + os.linesep + param[1]
                self.assertIn(attendu, resultat)


    def test_absence_bien_dit(self):
        # ETANT DONNE un non-palindrome
        for chaine in cas_test_non_palindrome:
            with self.subTest(chaine):
                # QUAND on le fournit au détecteur
                langue = LangueSpy()
                resultat = DetecteurPalindromeBuilder().ayantPourLangue(langue).build().detecter(chaine)

                # ALORS "Bien dit !" n'apparaît pas
                self.assertFalse(langue.felicitationsConsultees())


    def test_AuRevoir(self):
        cas = [[LangueFrancaise(), "Au revoir"], [LangueAnglaise(), "Goodbye"]]
        for param in cas:
            with self.subTest(param[0]):
                langue = param[0]
                chaine = 'test'

                resultat = DetecteurPalindromeBuilder().ayantPourLangue(langue).build().detecter(chaine)

                derniere_ligne = resultat.split(os.linesep)[-1]
                self.assertEqual(param[1], derniere_ligne)


    def test_bonjour(self):
        cas = [[LangueFrancaise(), "Bonjour"], [LangueAnglaise(), "Hello"]]

        for param in cas:
            with self.subTest(param[0]):
                langue = param[0]
                casChaine = ['kayak', 'test']
                for chaine in casChaine:
                    with self.subTest(chaine):
                        resultat = DetecteurPalindromeBuilder().ayantPourLangue(langue).build().detecter(chaine)

                        premiere_ligne = resultat.split(os.linesep)[0]
                        self.assertEqual(param[1], premiere_ligne)



if __name__ == '__main__':
    unittest.main()