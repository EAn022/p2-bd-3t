from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, id, id_pessoa, salario, cargo):
        self._id = id
        self._salario = salario
        self._cargo = cargo
    
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
