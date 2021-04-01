
def inserir_turma():
    codt = input('Código da turma: ') # pega o codigo da turma que deseja criar
    arq = open('turmas/turma {}.txt'.format(codt),'w') #cria um arquivo para turma que deseja criar
    arq.write('Código da turma: {}'.format(codt))
    arq.write(' | ')
    per = input('Período: ')
    arq.write(str(per))
    arq.write(' | ')
    codd = input('Código da disciplina: ')
    arq.write('Código da disciplina: {}'.format(codd))
    arq.write(' | ')
    arq.write('\n')
    arq.close()
    quant1 = int(input('Informe o número de professores que deseja cadastrar: ')) # numero de cadastros de professores
    for i in range(quant1):
        while True:
            cpfp = input('Digite o CPF do Professor(a): ')
            if cpfp.isnumeric and len(cpfp) == 11:
                arq = open('turmas/turma {}.txt'.format(codt),'a')
                arq.write('{} | Professor(a)'.format(cpfp))
                arq.write(' | ')
                arq.write('\n')
                arq.close()
                
            else:
                print('CPF inválido. Tente novamente.')
                
    quant2= int(input('Informe o número de alunos que deseja cadastrar: '))
    for c in range(quant2):
        while True:
            cpfa = input('Digite o CPF do Aluno(a): ')
            if cpfa.isnumeric and len(cpfa)==11:
                arq = open('turmas/turma {}.txt'.format(codt),'a')
                arq.write('{} |'.format(cpfa))
                arq.write('\n')
                arq.close()
                break
            else:
                print('CPF inválido. Tente novamente.')
        arq.close()


def mostrar_turma():
    turma = input('Digite o código da turma que deseja consultar: ')
    arq = open('turmas/turma {}.txt'.format(turma),'r')
    x = arq.readlines()
    for i in x:
        print(i)
    arq.close()

def mudar_turma():
    turma = input('Digite o código da turma que deseja atualizar: ') # pega o co da turma que deseja atualizar
    opcao_att = int(input('1.Professores\n2.Alunos\n3.Periodo e Disciplina\nInsira a informação que deseja atualizar:')) # o tipo e informaçao que deseja atualizar
    if opcao_att == 3:
        per = input('Período: ') # pega as novas informações
        codd = input('Código da disciplina: ')
        arq = open('turmas/turma {}.txt'.format(turma),'r') # abre o arquivo referente a turma
        lista1 = arq.readlines()# cria uma variavel com todas as linhas do arquivo da turma
        arq.close()
        arq = open('att.txt','w') # abre o arquivo de atualização
        arq.write('Código da turma: {}'.format(turma)) #escreve os novos dados
        arq.write(' | ')
        arq.write('Periodo: {}'.format(per))
        arq.write(' | ')
        arq.write('Código da disciplina: {}'.format(codd))
        arq.write('\n')
        arq.close()
        arq = open('att.txt','r') # abre ele em modo leitura
        att = arq.readlines() # cria uma variavel c todas as linhas do arquivo de atualizaçao
        arq.close()
        for i in lista1:
            if lista1.index(i) == 0: # pega a primeira linha da lista 1
                pos = lista1.index(i) 
                lista1.pop(pos) # remove a primeira linha
                lista1.insert(pos,att[0]) # acrescenta as informaçoes do arquivo de atualização
        arq = open('turmas/turma {}.txt'.format(turma),'w') # abre o arquivo da turma
        for i in lista1: # reescreve as informações atualizadas
            arq.write(i)
        arq.close()

    elif opcao_att == 2:
        arq = open('turmas/turma {}.txt'.format(turma),'r')
        dic = {}
        lista1 = arq.readlines()
        cpfaluno = ''
        for i in lista1:
            for c in i:
                if c.isnumeric and len(cpfaluno) < 11:
                    cpfaluno += c
            dic[i] = cpfaluno
            cpfaluno = ''
        arq.close()
        cpf_busca = input('Digite aqui o CPF que deseja atualizar: ') 
        if cpf_busca in dic.values():
            arq = open('att.txt', 'w')
            cpf_att = input('Digite o novo CPF: ')
            arq.write('{} | ALUNO(A)'.format(cpf_att))
            arq.write('\n')
            arq.close()
            arq = open('att.txt','r')
            aux = arq.readlines()
            arq.close()
            for i in lista1:
                if cpf_busca == dic[i]:
                    pos = lista1.index(i)
                    lista1.pop(pos)
                    lista1.insert(pos,aux[0])
            arq = open('turmas/turma {}.txt'.format(turma),'w')
            for i in lista1:
                arq.write(i)
            arq.close()
            arq = open('relatorio_aluno/{}.txt'.format(cpf_att),'w')
            arq.write(codd)
            print('Atualizado com sucesso.')
        else:
            print('CPF inválido. Tente novamente')
            
    elif opcao_att == 1:
        arq = open('turmas/turma {}.txt'.format(turma),'r')
        dic = {}
        lista1 = arq.readlines()
        cpfprof = ''
        for i in lista1:
            for c in i:
                if c.isnumeric and len(cpfprof) < 11:
                    cpfprof += c
            dic[i] = cpfprof
            cpfprof = ''
        arq.close()
        cpf_busca = input('Digite aqui o CPF que deseja atualizar: ') 
        if cpf_busca in dic.values():
            arq = open('att.txt', 'w')
            cpf_att = input('Digite o novo CPF: ')
            arq.write('{} | PROFESSOR(A)'.format(cpf_att))
            arq.write('\n')
            arq.close()
            arq = open('att.txt','r')
            aux = arq.readlines()
            arq.close()
            for i in lista1:
                if cpf_busca == dic[i]:
                    pos = lista1.index(i)
                    lista1.pop(pos)
                    lista1.insert(pos,aux[0])
            arq = open('turmas/turma {}.txt'.format(turma),'w')
            for i in lista1:
                arq.write(i)
            arq.close()
            print('Atualizado com sucesso.')
        else:
            print('CPF inválido. Tente novamente')
    
      
        
      
        
            
            
def ata_turma():
    turma = input('Digite o código da turma para gerar a ata : ')
    arq = open('turmas/turma {}.txt'.format(turma),'r')
    x = arq.readlines()
    for i in x:
        print(i)
    arq.close()
   
        
       
        
    
def apagar_turma():
    turma = input('Digite o código da turma que deseja deletar: ')
    arq = open('turmas/turma {}.txt'.format(turma),'w')
    arq.close()
    


def menu_disciplinas():
    while True:
        opcao = int(input('> Menu de Disciplinar <\n[1] - Inserir disciplina no sistema\n[2] - Mostrar disciplina do sistema\n[3] - Apagar dados de uma disciplina\n[4] - Atualizar os dados de uma Disciplina\n[5] - Mostrar ata de uma turma \n[0] - Voltar Menu Principal'))
        if opcao == 0:
            break
        elif opcao == 1:
            inserir_discip()
        elif opcao == 2:
            mostrar_discip()
        elif opcao == 3:
            apagar_discip()
        elif opcao == 4:
            mudar_discip()
        elif opcao == 5:
            ata_turma()
        else:
            print('Opção inválida')
            
   
 


