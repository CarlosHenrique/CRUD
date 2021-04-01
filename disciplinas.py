def inserir_discip():
    arq = open('disciplinas.txt','a')
    arq.write(input('Código da disciplina: '))
    arq.write(' | ')
    arq = open('disciplinas.txt','a')
    arq.write(input('Nome da disciplina: '))
    arq.write(' | ')
    arq.write('\n')
    arq.close()


def mostrar_discip():
    x=1
    arq = open('disciplinas.txt','r')
    for linha in arq.readlines():
        print(x,'-',linha)
        x+=1
        arq.close()

def mudar_discip():
    arq = open('disciplinas.txt', 'r')#abre o arquivo alunos.txt em modo leitura.
    dic = {}
    lista1 = arq.readlines()#cria uma lista temporaria.
    codd = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(codd) < 5:
                codd += c
        dic[i] = codd
        codd = ''
    arq.close()
    coddinput = input('Digite aqui o codigo da disciplina: ')# pega o codigo da disciplina para encontra-lo na lista.
    if coddinput in dic.values():
        nome = input('Nome da disciplina: ')  # pega informacao atualizada
        codd1 = input('Codigo da disciplina: ')  # informacao atualizada
        arq = open('muda.txt', 'w')  # abre arquivo auxiliar
        arq.write(codd1)
        arq.write(' | ')
        arq.write(nome)
        arq.write('\n')
        arq.close()
        arq = open('muda.txt', 'r')
        aux = arq.readlines()
        arq.close()
        for i in lista1:
            if coddinput == dic[i]:
                pos = lista1.index(i)
                lista1.pop(pos)
                lista1.insert(pos, aux[0])
        arq = open('disciplinas.txt', 'w')
        for i in lista1:
            arq.write(i)
        arq.close()
    else:
        print('Disciplina não encontrada.')
        
def apagar_discip():
    arq = open('disciplinas.txt', 'r')#abre o arquivo alunos.txt em modo leitura.
    dic = {}
    lista1 = arq.readlines()#cria uma lista temporaria.
    codd = ''
    for i in lista1:
        for c in i:
            if c.isnumeric() and len(codd) < 5:
                codd += c
        dic[i] = codd
        codd = ''
    arq.close()
    coddinput = input('Digite aqui o codigo da disciplina: ')# pega o codigo da disciplina para encontra-lo na lista.
    if coddinput in dic.values():
        for i in lista1:
            if coddinput == dic[i]:
                pos = lista1.index(i)
                lista1.pop(pos)
        arq = open('disciplinas.txt', 'w')
        for i in lista1:
            arq.write(i)
        arq.close()
    else:
        print('Disciplina não encontrada.')


def menu_disciplinas():
    while True:
        opcao = int(input('> Menu de Disciplinar <\n[1] - Inserir disciplina no sistema\n[2] - Mostrar disciplina do sistema\n[3] - Apagar dados de uma disciplina\n[4] - Atualizar os dados de uma Disciplina/n[0] - Voltar Menu Principal'))
        if opcao == 0:
            break
        elif opcao == 1:
            inserir_discip()
        elif opcao == 2:
            mostrar_discip()
        elif opcao == 3:
            excluir_discip()
        elif opcao == 4:
            mudar_discip()
        else:
            print('Opção inválida')
            
