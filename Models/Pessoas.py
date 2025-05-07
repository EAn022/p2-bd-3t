# Models/Pessoas.py
from abc import ABC, abstractmethod

# Classe abstrata
class Pessoas(ABC):
    def __init__(self, id, nome, cpf, data_nasc):
        self._id = id  # Atributo privado
        self._nome = nome  # Atributo privado
        self._cpf = cpf # Atributo privado
        self._data_nasc = data_nasc # Atributo privado
 
    # Método get para o atributo id
    def get_id(self):
        return self._id

    # Método set para o atributo id
    def set_id(self, codigo):
        self._id = codigo
    
    # Método get para o atributo nome
    def get_nome(self):
        return self._nome

    # Método set para o atributo nome
    def set_nome(self, nome):
        self._nome = nome
    
    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_data_nasc(self):
        return self._data_nasc

    def set_data_nasc(self, data_nasc):
        self._data_nasc = data_nasc