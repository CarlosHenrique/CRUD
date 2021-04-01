import profs
import turmas
import disciplinas
import alunos
def main():
    while True:
        print('{} BEM VINDO AO MENU PRINCIPAL {}\n1-Menu de Professores\n2-Menu de Alunos\n3-Menu de Disciplinas\n4-Menu de Turmas\n0-PARAR PROGRAMA'.format(10*'-',10*'-'))
        opcao = int(input('Qual menu deseja acessar: '))
        if opcao == 0:
            break
        elif opcao ==1:
            profs.menu_prof()
        elif opcao == 2:
            alunos.menu_aluno()
        elif opcao == 3:
            disciplinas.menu_disciplina()
        elif opcao == 4:
            turmas.menu_turma()
        else:
            print('Opção inválida. Tente novamente')
            
        

main()
    
    
