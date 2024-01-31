from momentJournee import *

class LangueAnglaise:
    def feliciter(self):
        return "Well said !"

    def bonjour(self, momentJournee):
        match momentJournee:
            case MomentJournee.Matin:
                return "Good morning"
            case MomentJournee.Apres_midi:
                return "Good afternoon"
            case MomentJournee.Soir:
                return "Good evening"
            case MomentJournee.Nuit:
                return "Good night"
        return "Hello"

    def aurevoir(self, momentJournee):
        match momentJournee:
            case MomentJournee.Nuit:
                return "Good night"
        return "Goodbye"