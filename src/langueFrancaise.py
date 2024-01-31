from src.momentJournee import MomentJournee

class LangueFrancaise:
    def feliciter(self):
        return "Bien dit !"

    def bonjour(self, momentJournee):
        if(momentJournee == MomentJournee.Matin):
            return "Bonjour"
        elif(momentJournee == MomentJournee.Apres_midi):
            return "Bon après-midi"
        elif(momentJournee == MomentJournee.Soir):
            return "Bonsoir"
        elif(momentJournee == MomentJournee.Nuit):
            return "Bonne nuit"
        else:
            return "Bonjour"

    def aurevoir(self, momentJournee):
        if(momentJournee == MomentJournee.Matin):
            return "Au revoir"
        elif(momentJournee == MomentJournee.Apres_midi):
            return "Au revoir"
        elif(momentJournee == MomentJournee.Soir):
            return "Bonne nuit"
        elif(momentJournee == MomentJournee.Nuit):
            return "Bonne nuit"
        else:
            return "Au revoir"