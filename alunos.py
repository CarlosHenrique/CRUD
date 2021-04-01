#defs de aluno, que criei.
def consultar_aluno():
    x=1
    arq = open("aluno.txt", "r")
    for linha in arq.readlines():
        print(x,'-',linha)
        x+=1
        arq.close()
def cadastrar_aluno():
    arq = open('aluno.txt', 'a')
    arq.write(input('Nome:'))
    arq.write(' | ')
    arq = open('aluno.txt', 'a')
    while True:
        cpf = input('CPF:')
        if cpf.isnumeric() and len(cpf) == 11:
            arq.write(cpf)
            arq = open('relatorio_aluno/{}.txt'.format(cpf),'w') # sempre que cadastrar um novo professor cria um arquivo na pasta de relatorio equivalente ao cpf do professor
            break
        else:
            print('Digite um CPF valido.')
    arq = open('aluno.txt', 'a')
    arq.write(' | ')
    arq.write('\n')
    arq.close()


def atualizar_aluno():
    arq = open('aluno.txt', 'r')#abre o arquivo alunos.txt em modo leitura.
    dic = {}
    lista1 = arq.readlines()#cria uma lista temporaria.
    cpfaluno = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(cpfaluno) < 11:
                cpfaluno += c
        dic[i] = cpfaluno
        cpfaluno = ''
    arq.close()
    cpfinput = input('Digite aqui o CPF: ') # pega o cpf do aluno para encontra-lo na lista.
    if cpfinput in dic.values():
        nome = input('Nome completo: ')  # pega informacao atualizada
        cpf = input('CPF: ')  # informacao atualizada
        arq = open('att.txt', 'w')  # abre arquivo auxiliar
        arq.write(nome)
        arq.write(' | ')
        arq.write(cpf) # escreve os dados novos no arquivo aux
        arq.write(' | ')
        arq.write('\n')
        arq.close()
        arq = open('att.txt', 'r') # abre o arquivo em modo leitura
        aux = arq.readlines() # cria uma variavel que le as linhas do arquivo
        arq.close()
        for i in lista1: # percorre a lista1 com as linhas do arquivo de alunos
            if cpfinput == dic[i]: # se o cpf novo estiver no dicionario onde foi armazenado todos os cpfs
                pos = lista1.index(i) # variavel recebe a posicao do cpf na lista1
                lista1.pop(pos) # apaga o cpf
                lista1.insert(pos, aux[0])#e adiciona o novo cpf na posiçao do anterior 
        arq = open('aluno.txt', 'w') # abre o arquivo de aluno em modo escrita
        for i in lista1:
            arq.write(i)# reescreve os elementos da lista1 atualizados
        arq.close()
        print('Atualizado com sucesso.')
    else:
        print('CPF inválido. Tente novamente')
        
def remover_aluno():
    arq = open('aluno.txt', 'r')#abre o arquivo alunos.txt em modo leitura.
    dic = {}
    lista1 = arq.readlines()#cria uma lista temporaria.
    cpfaluno = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(cpfaluno) < 11:
                cpfaluno += c
        dic[i] = cpfaluno # armazena todos os cpfs que estão na lista1 em um dicionario
        cpfaluno = ''
    arq.close()
    cpfinput = input('Digite seu cpf aqui: ') # pega o cpf do aluno para encontra-lo na lista.
    if cpfinput in dic.values(): # se o cpf que deseja encontrar estiver no dicionario
        for i in lista1: # percorre a lista 1 
            if cpfinput == dic[i]: # se cpf que deseja estiver no dicionario
                pos = lista1.index(i) # pega a posicao na lista1
                lista1.pop(pos) # apaga o cpf a partir da posicao
        arq = open('aluno.txt', 'w') # abre arquivo
        for i in lista1: # reescreve a lista 1 atualizada dentro do arquivo
            arq.write(i)
        arq.close()
        print('Removido com sucesso.')
    else:
        print('CPF inválido. Tente novamente')



def menu_aluno():
    while True:
        opcao = int(input('{} MENU ALUNOS {}\n0.Voltar para Menu Principal\n1.Cadastrar Aluno.\n2.Consultar Alunos.\n3.Remover Aluno.\n4.Atualizar Aluno.\n5.Relatório\n'.format(10*'-',10*'-')))
        if opcao == 0:
            break
        elif opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            consultar_aluno()
        elif opcao == 3:
            remover_aluno()
        elif opcao == 4:
            atualizar_aluno()
        elif opcao == 5:
            relatorio_aluno()
        else:
            print('Opção inválida')
            opcao = int(input('{} MENU {}\n0.Voltar para Menu Principal\n1.Cadastrar Aluno.\n2.Consultar Alunos.\n3.Remover Aluno.\n4.Atualizar Aluno.'.format(20*'-',20*'-')))

        
        
def relatorio_aluno():
    cpf = input('Digite o CPF: ')
    arq = open('relatorio_aluno\{}.txt'.format(cpf),'r')
    x = arq.readlines()
    for i in x:
        print(i)

