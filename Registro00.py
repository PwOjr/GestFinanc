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
saldo=0


while True:

    if retornar==0:
        login=str
        LogCAD=input('Aperte no número ao lado da ação desejada \n[0]Cadastrar [1]Login  [2]Terminar\n')
        i+=1

        if LogCAD=='0' or LogCAD=='Cadastrar' or LogCAD=='Cadastro':
            retornar=2
            cadastro.append(RegUsuario)
            Usuario.nome= input('nome: ')
            Usuario.cpf= int(input(' CPF: '))
            Usuario.email=(input('Email '))
            print('\nSenha:')
            Usuario.senha=input('***** ')
            print('\nConfirme:')
            Usuario.confsenha=input('***** ')

            if Usuario.senha==Usuario.confsenha:
                cadastro.append(Usuario)
                print('Cadastro conclído')
                print(cadastro)
                retornar=0


        if LogCAD=='1' or LogCAD=='Login':
            login=input('email: ')
            key=input('Senha')
            retornar=1

            if login in Usuario.email and key in Usuario.senha and retornar==1:
                print('Bem Vindo!')
                retornar=3
        
    if retornar==3:

        Objetivo=input('Aperte no número ao lado da ação desejada \n [1]Saldo  [2]Médias [3]Transações [4]Vizualisar Dados [5]Sair da conta\n')

        if Objetivo=='1':
            

            infSaldo=input('Informe o saldo')

        if Objetivo=='5' or Objetivo == '[5]':
            retornar=0

        elif Objetivo!='1' or Objetivo!='2' or Objetivo!='3' or Objetivo!='4' or Objetivo!='5':
            print('Digite valor válido!')
            retornar=3
            #Não consegui voltar em 'objetivo' utilizando a variável retornar

        if LogCAD=='2' or LogCAD=='Terminar' or LogCAD=='02':
            certeza=input('Confirmar ação [sim] ou [voltar]')

            if certeza=='sim':
                break

            if certeza=='voltar':
                retornar=0

    else:
        print('Digite valor válido!')
        retornar=0

#Saídas provisórias
print('Informações do usuário:', Usuario)
print('Usuários cadastrados: ',cadastro)
print(RegUsuario)