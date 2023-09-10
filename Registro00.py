#Projeto_Integrador

#Parte inicial do código, em que trabalharemos apenas com o Cadastro. 
#Caso já exista uma conta, será solicitado o login e assim encerrará o código

from dataclasses import dataclass
@dataclass

#Atributos da minha classe
class RegUsuario:
    nome: str =''
    email: str=''
    cpf: int = 0
    senha: str=''
    confsenha: str=''

#criando objeto (usuário) pertecente a classe Registro de Usuário
Usuario=RegUsuario()

#Vetor responsável por cadastrar as informações de cada usuário.
cadastro=[]

#Contador
i=0

#Meio para locomover livrimente dentro do laço de repetição.
retornar=0


while True:

    if retornar==0:
        login=str
        LogCAD=input('Aperte no número ao lado da ação desejada \n [0]Login [1]Cadastrar  [2]Terminar\n')
        i+=1

        if LogCAD=='0' or LogCAD=='Login':
            login=str(input('email: '))
            retornar=1

            if login in cadastro:
                print('Bem Vindo!')
                retornar=3 

            else:
                print('Email não registrado')
                retornar=0


        if LogCAD=='1' or LogCAD=='Cadastrar' or LogCAD=='Cadastro':
            retornar=2
            cadastro.append(RegUsuario)
            Usuario.nome= str(input('nome: '))
            Usuario.cpf= int(input(' CPF: '))
            Usuario.email=str(input('Email '))
            print('\nSenha:')
            Usuario.senha=str(input('***** '))
            print('\nConfirme:')
            Usuario.confsenha=str(input('***** '))

            if Usuario.senha==Usuario.confsenha:
                cadastro.append(Usuario)
                print('Cadastro conclído')
                print(cadastro)
                retornar=0

        if LogCAD=='2' or LogCAD=='Terminar' or LogCAD=='02':
            certeza=input('Confirmar ação [sim] ou [voltar]')

            if certeza=='sim':
                break

            if certeza=='voltar':
                retornar=0

#Saídas provisórias
print('Informações do usuário:', Usuario)
print('Usuários cadastrados: ',cadastro)
print(RegUsuario)