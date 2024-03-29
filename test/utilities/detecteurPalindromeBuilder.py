from langueFrancaise import LangueFrancaise
from momentJournee import MomentJournee
from src.detecteurPalindrome import DetecteurPalindrome
from utilities.langueStub import LangueStub

class DetecteurPalindromeBuilder:
    __langue = LangueFrancaise()
    __momentJournee = MomentJournee.Default

    @classmethod
    def buildDefault(self):
        return DetecteurPalindromeBuilder.build(self)

    def build(self):
        return DetecteurPalindrome(self.__langue, self.__momentJournee)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self

    def ayantPourMomentJournee(self, momentJournee):
        self.__momentJournee = momentJournee
        return self