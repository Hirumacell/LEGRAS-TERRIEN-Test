from src.detecteurPalindrome import DetecteurPalindrome
from utilities.langueStub import LangueStub

class DetecteurPalindromeBuilder:
    __langue = LangueStub()

    @classmethod
    def buildDefault(self):
        return DetecteurPalindromeBuilder.build(self)

    def build(self):
        return DetecteurPalindrome(self.__langue)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self