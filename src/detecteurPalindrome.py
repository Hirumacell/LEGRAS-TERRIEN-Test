import os

class DetecteurPalindrome:
    def __init__(self, langue):
        self.__langue = langue

    def detecter(self, chaine):
        miroir = chaine[::-1]

        debut = ('Bonjour'
                 + os.linesep
                 + miroir
                 + os.linesep)

        return (debut + self.__langue.feliciter() if chaine == miroir else debut) + "Au revoir"