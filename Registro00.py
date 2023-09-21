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
        alternativa=input('Aperte no número ao lado da ação desejada \n[0]Cadastrar [1]Login  [2]Terminar\n')

        if alternativa=='0' or alternativa=='Cadastrar' or alternativa=='Cadastro':
            
            cadastro.append(RegUsuario())
            cadastro[i].nome=input('Nome: ')
            cadastro[i].cpf= int(input(' CPF: '))
            cadastro[i].email=(input('Email: '))
            print('\nSenha: ')
            Senha=input('***** ')
            print('\nConfirme:')
            confirmar=input('***** ')

            if Senha==confirmar:
                cadastro[i].senha=Senha
                print('Cadastro conclído')
                print(cadastro)
                i+=1
                retornar=0


        if alternativa=='1' or alternativa=='Login':
            login=input('email: ')
            key=input('Senha: ')

            for a in range(i):
                if login in cadastro[a].email and key in cadastro[a].senha:
                    print('Bem Vindo!')
                    retornar=1
        
        if alternativa=='2' or alternativa=='Terminar' or alternativa=='02':
            certeza=input('Confirmar ação [sim] ou [voltar]')

            if certeza=='sim':
                break

            if certeza=='voltar':
                retornar=0
        
    elif retornar==1:

        Objetivo=input('Aperte no número ao lado da ação desejada \n [1]Saldo  [2]Médias [3]Transações [4]Vizualisar Dados [5]Sair da conta\n')

        if Objetivo=='1':
            

            infSaldo=input('Informe o saldo')

        if Objetivo=='5' or Objetivo == '[5]':
            retornar=0

        elif Objetivo!='1' or Objetivo!='2' or Objetivo!='3' or Objetivo!='4' or Objetivo!='5':
            print('Digite valor válido!')
            retornar=1


    else:
        print('Digite valor válido!')
        retornar=0

#Saídas provisórias
print('Usuários cadastrados: ',cadastro)
print(RegUsuario)