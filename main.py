from pessoa import Pessoa
from contato_emergencia import ContatoEmergencia  
from dados import Dados            
from exames import Exames
from laboratorio import Laboratorio
from observacao import Observacao
from profissional import Profissional
from paciente import Paciente

pe1 = Pessoa('Maria',28,'rua tal','222222222','maria@maria.com')
da1 = Dados('O+', 'Sem Alergias', 'Sem uso ilicitos', 'Sem uso de medicamentos')
pr1 = Profissional('Fabio','emfermeiro','55555','FabioSouza')
ob1 = Observacao('baixo','pouco urgente','não precisa','soro')
ce1 = ContatoEmergencia('Joao','6666666','pai','o+')
la = Laboratorio('Exames Sul','Rua central', '88.999.555/2225-55', '51888888888', pr1)
ex1 = Exames('8 horas','imagem','10:00','5',ob1,la) 
pa1 = Paciente(pe1, da1, 'Unimed', 'Lucas','2 horas','Liquidos',ex1, ce1)


print('    PROFISSIONAL\n''NOME: ' + pr1.nome_profissional + '\nCARGO: ' + pr1.cargo + '\nREGISTRO: ' + pr1.registro_profissional + '\nASSINATURA: ' + pr1.assinatura)

print('    LABORARIOO\n''NOME: ' + la.nome_laboratorio + '\nCARGO: ' + la.endereco_laboratorio + '\nCNPJ: ' + la.cnpj + '\nTELEFONE: ' + la.telefone_laboratorio)