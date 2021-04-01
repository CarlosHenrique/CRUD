# def de professores
def cadastrar_prof():
    arq = open('prof.txt', 'a')
    arq.write(input('Nome:'))
    arq.write(' | ')
    while True:
        cpf = input('CPF:')
        if cpf.isnumeric() and len(cpf) == 11:
            arq.write(cpf)
            arq = open('relatorio_prof/{}.txt'.format(cpf),'w')
            break
        else:
            print('Digite um CPF valido.')
    arq = open('prof.txt', 'a')
    arq.write(' | ')
    arq.write(input('Departamento:'))
    arq.write(' | ')
    arq.write('\n')
    arq.close()

def consultar_prof():
    x=1
    arq = open('prof.txt', 'r')
    for linha in arq.readlines():
        print(x,'-',linha)
        x+=1
        arq.close()

def atualizar_prof():
    arq = open('prof.txt','r') #abrir arquivo dos professores
    dic = {}
    lista1 = arq.readlines() #lista temporaria
    cpfprof = '' #string vazia
    for i in lista1:#percorre a lista
        for n in i:# percorre cada caractere da lista
            if n.isnumeric() and len(cpfprof)<11:
                cpfprof+=n
        dic[i] = cpfprof
        cpfprof = ''
    arq.close()
    inputcpf = input('Digite aqui o CPF: ') #pega o cpf do professor e busca na lista
    if inputcpf in dic.values():
        nome = input('Nome: ') # informacoes atualizadas
        cpf = input('CPF: ')
        dept = input('Departamento: ')
        arq = open('att.txt','w') #abre arquivo pra auxiliar na att e escreve os dados
        arq.write(nome)
        arq.write(' | ')
        arq.write(cpf)
        arq.write(' | ')
        arq.write(dept)
        arq.write('\n')
        arq.close()
        arq = open('att.txt','r')
        aux = arq.readlines() # escreve os dados numa variavel auxiliar
        arq.close()
        for i in lista1: # percorre a lista temporaria
            if inputcpf == dic[i]: # se o cpf  que deseja atualizar for igual a algum do dicionario
                posi = lista1.index(i) # variavel pega a posicao 
                lista1.pop(posi) # apaga o dado naquela posicao 
                lista1.insert(posi,aux[0]) # adiciona os dados naquela posção
        arq = open('prof.txt','w') # abre o arquivo de prof
        for i in lista1: # percorre a lista 1 reescrevendo os dados atualizados
            arq.write(i)
        arq.close()
        print('Atualizado com sucesso')
    else:
        print('CPF inválido')
                
def remover_prof():
    arq = open('prof.txt', 'r')#abre o arquivo alunos.txt em modo leitura.
    dic = {}
    lista1 = arq.readlines()#cria uma lista temporaria.
    cpfprof = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(cpfprof) < 11:
                cpfprof += c
        dic[i] = cpfprof
        cpfprof = ''
    arq.close()
    inputcpf = input('Digite aqui seu CPF: ')# recebe o cpf do professor para encontra-lo na lista.
    if inputcpf in dic.values(): # se o cpf estiver no dicionario
        for i in lista1: # percorre a lista1 
            if inputcpf == dic[i]: # se o cpf do professor for igual ao cpf do dicionario
                posi = lista1.index(i) # variavel recebe a posicao  na lista1
                lista1.pop(posi) 
        arq = open('prof.txt', 'w')
        for i in lista1:
            arq.write(i)
        arq.close()
        print('Removido com sucesso')
    else:
        print('CPF inválido.')

def menu_prof():
    while True:
        opcao = int(input('{}MENU PROFESSORES {}\n0.Voltar para o menu principal\n1.Cadastrar Professor\n2.Consultar Professor\n3.Remover Professor\n4.Atualizar Professor\n5.Relatório Professores\n'.format(10*'-',10*'-')))
        if opcao == 0:
            break
        elif opcao == 1:
            cadastrar_prof()
        elif opcao == 2:
           consultar_prof()
        elif opcao == 3:
            remover_prof()
        elif opcao == 4:
            atualizar_prof()
        elif opcao == 5:
            relatorio_prof()
        else:
            print('Opção inválida. Tente novamente.')
            



