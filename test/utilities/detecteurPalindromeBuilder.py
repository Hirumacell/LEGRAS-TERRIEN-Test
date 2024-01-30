from src.detecteurPalindrome import DetecteurPalindrome
from langueStub import LangueStub

class DetecteurPalindromeBuilder:
    __langue = LangueStub()

    def build(self):
        return DetecteurPalindrome(self.__langue)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self