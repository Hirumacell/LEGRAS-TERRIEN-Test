import locale
import time

from momentJournee import MomentJournee
from langueFrancaise import LangueFrancaise
from langueAnglaise import LangueAnglaise
from detecteurPalindrome import DetecteurPalindrome

class DetecteurPalindromeEtape4:

    def __init__(self):
        self.__langue == LangueFrancaise
        if locale.getdefaultlocale()[0] == 'en-EN':
            self.__langue = LangueAnglaise

        hour = time.localtime().tm_hour
        self.__momentJournee = MomentJournee.Inconnue
        if 6 <= hour <= 12:
            self.__momentJournee = MomentJournee.Matin
        if 13 <= hour <= 17:
            self.__momentJournee = MomentJournee.Apres_midi
        if 18 <= hour <= 23:
            self.__momentJournee = MomentJournee.Soir
        else:
            self.__momentJournee = MomentJournee.Nuit

    def detecter(self):
        MotDetecte = input("Donner un mot :")
        Detecteur = DetecteurPalindrome(self.__langue, self.__momentJournee)
        return Detecteur.detecter(MotDetecte)

Palindrome =  DetecteurPalindromeEtape4()
print(Palindrome.detecter())




