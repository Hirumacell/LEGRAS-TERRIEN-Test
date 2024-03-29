from test.utilities.langueStub import LangueStub


class LangueSpy(LangueStub):
    __felicitatiosConsultees = False

    def felicitationsConsultees(self):
        return self.__felicitatiosConsultees

    def feliciter(self):
        self.__felicitatiosConsultees = True

    def bonjour(self):
        self.__felicitatiosConsultees = True

    def aurevoir(self):
        self.__felicitatiosConsultees = True
