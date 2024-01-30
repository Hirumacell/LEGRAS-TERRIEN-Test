from langueStub import LangueStub as langueStub


class LangueSpy(langueStub):
    __felicitatiosConsultees = False

    def felicitationsConsultees(self):
        return self.__felicitatiosConsultees

    def feliciter(self):
        self.__felicitatiosConsultees = True

    def bonjour(self):
        self.__felicitatiosConsultees = True

    def aurevoir(self):
        self.__felicitatiosConsultees = True
