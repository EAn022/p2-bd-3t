from Models.Funcionarios import Funcionario

class Medico(Funcionario):
    def __init__(self, id, id_funcionario, salario, cargo, nome, CPF, data_nasc, crm, especialidade):
        super().__init__(id_funcionario, None, salario, cargo, nome, CPF, data_nasc)
        self._id = id  
        self._id_funcionario = id_funcionario  
        self._crm = crm
        self._especialidade = especialidade

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_id_funcionario(self):
        return self._id_funcionario

    def set_id_funcionario(self, id_funcionario):
        self._id_funcionario = id_funcionario

    def get_crm(self):
        return self._crm

    def set_crm(self, crm):
        self._crm = crm

    def get_especialidade(self):
        return self._especialidade

    def set_especialidade(self, especialidade):
        self._especialidade = especialidade
