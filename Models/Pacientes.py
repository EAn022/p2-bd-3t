from Models.Pessoas import Pessoas

class Pacientes(Pessoas):
    def __init__(self, id, nome, data_nasc, CPF):
        super().__init__(nome, data_nasc, CPF)
        self._id = id
    
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id