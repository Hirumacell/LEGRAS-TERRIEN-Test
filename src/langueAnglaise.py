from momentJournee import *

class LangueAnglaise:
    def feliciter(self):
        return "Well said !"

    def bonjour(self, momentJournee):
        if(momentJournee == MomentJournee.Matin):
            return "Good morning"
        elif(momentJournee == MomentJournee.Apres_midi):
            return "Good afternoon"
        elif(momentJournee == MomentJournee.Soir):
            return "Good evening"
        elif(momentJournee == MomentJournee.Nuit):
            return "Good night"
        else:
            return "Good morning"

    def aurevoir(self, momentJournee):
        if(momentJournee == MomentJournee.Matin):
            return "Goodbye"
        elif(momentJournee == MomentJournee.Apres_midi):
            return "Goodbye"
        elif(momentJournee == MomentJournee.Soir):
            return "Good night"
        elif(momentJournee == MomentJournee.Nuit):
            return "Good night"
        else:
            return "Goodbye"