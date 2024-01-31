from momentJournee import MomentJournee

class LangueFrancaise:
    def feliciter(self):
        return "Bien dit !"

    def bonjour(self, momentJournee):
        match momentJournee:
            case MomentJournee.Matin:
                return "Bonjour"
            case MomentJournee.Apres_midi:
                return "Bonjour"
            case MomentJournee.Soir:
                return "Bonsoir"
            case MomentJournee.Nuit:
                return "Bonsoir"
        return "Bonjour"

    def aurevoir(self, momentJournee):
        match momentJournee:
            case MomentJournee.Matin:
                return "Bonne journée"
            case MomentJournee.Apres_midi:
                return "Bon après-midi"
            case MomentJournee.Soir:
                return "Bonne soirée"
            case MomentJournee.Nuit:
                return "Bonne nuit"
        return "Au revoir"