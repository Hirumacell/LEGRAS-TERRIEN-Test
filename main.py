import locale
from datetime import datetime

from detecteurPalindrome import DetecteurPalindrome
from src.momentJournee import MomentJournee
from src.langueFrancaise import LangueFrancaise
from src.langueAnglaise import LangueAnglaise

# Relier la langue à celle du système
class LangueAdapter:
    def __init__(self):
        langue_systeme = locale.getlocale()
        if langue_systeme[0] == "en_GB":
            self.__langue = LangueAnglaise()
        else:
            self.__langue = LangueFrancaise()

    def get_langue(self):
        return self.__langue

#Relier le moment de la journée à celui du système
class MomentJourneeAdapter:
    def __init__(self):
        heure = datetime.now().hour
        if heure < 12:
            self.__momentJournee = MomentJournee.Matin
        elif heure < 18:
            self.__momentJournee = MomentJournee.Apres_midi
        elif heure < 22:
            self.__momentJournee = MomentJournee.Soir
        else:
            self.__momentJournee = MomentJournee.Nuit

    def get_momentJournee(self):
        return self.__momentJournee


#Relier L’entrée et la sortie à la console
class ConsoleAdapter:
    def __init__(self):
        self.__input = input
        self.__print = print

    def get_momentJournee(self):
        return self.__momentJournee

    def get_input(self):
        return self.__input("Entrez une chaine : ")


if __name__ == '__main__':
    langue = LangueAdapter().get_langue()
    momentJournee = MomentJourneeAdapter().get_momentJournee()
    console = ConsoleAdapter()
    chaine = console.get_input()
    detecteur = DetecteurPalindrome(langue, momentJournee)
    resultat = detecteur.detecter(chaine)
    print(resultat)