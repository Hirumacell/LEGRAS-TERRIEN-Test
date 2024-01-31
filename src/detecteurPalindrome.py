import os

class DetecteurPalindrome:
    def __init__(self, langue, momentJournee):
        self.__langue = langue
        self.__momentJournee = momentJournee

    def detecter(self, chaine):
        miroir = chaine[::-1]

        debut = self.bonjour() + os.linesep + miroir + os.linesep

        return (debut + self.bien_dit() if chaine == miroir else debut) + self.aurevoir()

    def bonjour(self):
        return self.__langue.bonjour(self.__momentJournee)

    def bien_dit(self):
        return self.__langue.feliciter()

    def aurevoir(self):
        return self.__langue.aurevoir(self.__momentJournee)