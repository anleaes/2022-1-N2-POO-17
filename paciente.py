class Paciente:
    
    def __init__(self, pessoa, dados, plano_saude, acompanhante, tempo_internacao, dieta, exames, contato_emergencia):
        self._pessoa = pessoa
        self._dados = dados
        self._plano_saude = plano_saude
        self._acompanhante = acompanhante
        self._tempo_internacao = tempo_internacao
        self._dieta = dieta
        self._exames = exames
        self._contato_emergencia = contato_emergencia
        