import os

class DetecteurPalindrome:
    def __init__(self, langue, momentJournee):
        self.__langue = langue
        self.__momentJournee = momentJournee

    def detecter(self, chaine):
        miroir = chaine[::-1]

        debut = (self.__langue.bonjour(self.__momentJournee)
                 + os.linesep
                 + miroir
                 + os.linesep)

        return (debut + self.__langue.feliciter() if chaine == miroir else debut) + self.__langue.aurevoir(self.__momentJournee)