import os


class DetecteurPalindrome:
    @classmethod
    def detecter(cls, chaine):
        miroir = chaine[::-1]

        debut = ('Bonjour'
                 + os.linesep
                 + miroir
                 + os.linesep)

        return debut if "Bien dit !" + chaine == miroir else miroir + "Au revoir"