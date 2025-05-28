from Models.Pessoas import Pessoas

class Funcionario(Pessoas):
    def __init__(self, id, id_pessoa, salario, cargo, nome, CPF, data_nasc):
        super().__init__(id_pessoa, nome, CPF, data_nasc)
        self._id = id
        self._salario = salario
        self._cargo = cargo
        self._id_pessoa = id_pessoa
    
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_salario(self):
        return self._salario
    
    def set_salario(self, salario):
        self._salario = salario

    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_IdPessoa(self):
        return self._id_pessoa
        
    def set_IdPessoa(self, id_pessoa):
        self._id_pessoa = id_pessoa
