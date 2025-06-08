from Models.Pessoas import Pessoas

class Paciente(Pessoas):
    def __init__(self, id, id_pessoa, nome, CPF, data_nasc):
        super().__init__(id_pessoa, nome, CPF, data_nasc)
        self._id = id
        self._id_pessoa = id_pessoa
    
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    def get_IdPessoa(self):
        return self._id_pessoa
        
    def set_IdPessoa(self, id_pessoa):
        self._id_pessoa = id_pessoa