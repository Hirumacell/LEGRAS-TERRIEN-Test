import os
import unittest

from src.detecteurPalindrome import DetecteurPalindrome
from src.langueFrancaise import LangueFrancaise
from src.langueAnglaise import LangueAnglaise
from utilities.detecteurPalindromeBuilder import DetecteurPalindromeBuilder

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

    def test_bien_dit(self):
        # ETANT DONNE un palindrome
        # ET que l'utilisateur parle français
        langue = LangueFrancaise()
        palindrome = 'radar'

        # QUAND on le fournit au détecteur
        resultat = DetecteurPalindromeBuilder().ayantPourLangue(langue).build().detecter(palindrome)

        # ALORS on obtient cette chaine suivie de "Bien dit !"
        attendu = palindrome + os.linesep + 'Bien dit !'
        self.assertIn(attendu, resultat)

    def test_well_said(self):
        # ETANT DONNE un palindrome
        # ET que l'utilisateur parle anglais
        langue = LangueAnglaise()
        palindrome = 'radar'

        # QUAND on le fournit au détecteur
        resultat = DetecteurPalindromeBuilder().ayantPourLangue(langue).build().detecter(palindrome)

        # ALORS on obtient cette chaine suivie de "Well Said !"
        attendu = palindrome + os.linesep + 'Well Said !'
        self.assertIn(attendu, resultat)

    def test_absence_bien_dit(self):
        # ETANT DONNE un non-palindrome
        for chaine in cas_test_non_palindrome:
            with self.subTest(chaine):
                # QUAND on le fournit au détecteur
                resultat = DetecteurPalindromeBuilder().build().detecter(chaine)

                # ALORS "Bien dit !" n'apparaît pas
                self.assertNotIn('Bien dit !', resultat)

    def test_bonjour(self):
        # ETANT DONNE une chaine
        chaine = 'test'

        # QUAND je demande si elle est un palindrome
        resultat = DetecteurPalindromeBuilder.build().detecter(chaine)

        # ALORS la première ligne est "Bonjour"
        premiere_ligne = resultat.split(os.linesep)[0]
        self.assertEqual('Bonjour', premiere_ligne)

    def test_AuRevoir(self):
        # ETANT DONNE une chaine
        chaine = 'test'

        # QUAND je demande si elle est un palindrome
        resultat = DetecteurPalindromeBuilder().build().detecter(chaine)

        # ALORS la dernière ligne est "Au revoir"
        derniere_ligne = resultat.split(os.linesep)[-1]
        self.assertEqual('Au revoir', derniere_ligne)

    def test_bonjour2(self):
        # ETANT DONNE une chaine
        cas = ['kayak','test']

        for chaine in cas:
            # QUAND je demande si elle est un palindrome
            resultat = DetecteurPalindromeBuilder.build().detecter(chaine)

            # ALORS la première ligne est "Bonjour"
            premiere_ligne = resultat.split(os.linesep)[0]
            self.assertEqual('Bonjour', premiere_ligne)

if __name__ == '__main__':
    unittest.main()