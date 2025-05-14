class Consulta:
    def __init__(self, id, id_paciente, id_medico, data_consulta, observacoes):
        self._id = id 
        self._id_paciente = id_paciente 
        self._id_medico = id_medico
        self._data_consulta = data_consulta
        self._observacoes = observacoes

    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    
    def get_id_paciente(self):
        return self._id_paciente
    
    def set_id_paciente(self, id_paciente):
        self._id_paciente = id_paciente

    
    def get_id_medico(self):
        return self._id_medico
    
    def set_id_medico(self, id_medico):
        self._id_medico = id_medico
    
    
    def get_data_consulta(self):
        return self._data_consulta
    
    def set_data_consulta(self, data_consulta):
        self._data_consulta - data_consulta

    
    def get_observacoes(self):
        return self._observacoes
    
    def set_observacoes(self, observacoes):
        self._observacoes = observacoes

        