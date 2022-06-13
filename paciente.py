class Paciente(Pessoa, Dados):
    
    def _init_(self, plano_saude, acompanhante, tempo_internacao, exames, contato_emergencia, nome, idade, endereco, telefone, email, tipo_sanguineo, alergia, uso_ilicito, uso_medicamento):
        super()._init__init_(nome, idade, endereco, telefone, email)
        super()._init__init_(tipo_sanguineo, alergia, uso_ilicito, uso_medicamento)
        self._plano_saude = plano_saude
        self._acompanhante = acompanhante
        self._tempo_internacao = tempo_internacao
        self._telefone = telefone
        self._email = email
        self._exames = exames
        self._contato_emergencia = contato_emergencia
        