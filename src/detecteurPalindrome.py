import os


class DetecteurPalindrome:
    @classmethod
    def detecter(cls, chaine):
        miroir = chaine[::-1]

        debut = ('Bonjour'
                 + os.linesep
                 + miroir
                 + os.linesep)

        return debut + "Bien dit !" if chaine == miroir else debut + "Au revoir"