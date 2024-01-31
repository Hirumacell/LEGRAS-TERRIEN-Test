import locale
from src.langueFrancaise import LangueFrancaise
from src.langueAnglaise import LangueAnglaise

class LangueAdapter:
    def __init__(self):
        langue_systeme = locale.getlocale()
        if langue_systeme[0] == "en_GB":
            self.__langue = LangueAnglaise
        else:
            self.__langue = LangueFrancaise

    def get_langue(self):
        return self.__langue

if __name__ == '__main__':
    langue = LangueAdapter().get_langue()
    print(langue().bonjour(1))
    print(langue().aurevoir(1))
    print(langue().feliciter())

