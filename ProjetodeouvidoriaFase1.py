lista = []
opcao = 0
while opcao != 6:
    print('==== PROJETO DE OUVIDORIA ====')
    print("[ 1 ] Listar Reclamacao")
    print("[ 2 ] Adicionar Reclamacao")
    print("[ 3 ] Pesquisar Reclamacao")
    print("[ 4 ] Remover Reclamacao")
    print("[ 5 ] Alterar Reclamacao")
    print("[ 6 ] Sair")
    print('='*30)
    opcao = int(input('Digite uma opcao: '))
    if opcao not in range(1,7):
        print('Opcao invalida, Digite uma opcao de 1 a 6')
    else:
        if opcao == 1 and lista == []: # Caso a lista esteja vazia
            print('Nenhuma reclamacao na lista, caso desejar adicionar tecle [2]')
            print()
            
        elif opcao == 1: 
            for item in range(len(lista)):
                print(item,'-', lista[item])
                
        elif opcao == 2: 
            novaReclamacao = str(input('Digite uma nova reclamacao: '))
            lista.append(novaReclamacao)
            print('Reclamacao adicionada com sucesso!!!')
            
        elif opcao == 3: 
            for item in range(len(lista)):
                print(item,'-',lista[item])
            pesquisar = int(input('Digite qual o numero da reclamacao: '))
            escolha = int(input('Voce deseja [4] Remover ou [5] Alterar: '))
            
            if escolha == 4:
                remover = lista.pop(pesquisar)
                print('Reclamacao removida com sucesso!!!')
                
            elif escolha == 5:
                #alterar = int(input('Qual a reclamacao que voce quer alterar: '))
                newAlterar = str(input('DIGITE A NOVA RECLAMACAO PARA ALTERAR: '))
                lista[pesquisar] = newAlterar
                print('Reclamacao alterada com sucesso!!!')
                
        elif opcao == 4:
            if opcao == 4 and lista == []:
                print('Nenhuma reclamacao na lista, caso desejar adicionar tecle [2]')
                print()
            elif opcao == 4:
                for item in range(len(lista)):
                    print(item,'-',lista[item])
                op1 = input('Deseja remover tudo na lista? [S/N]')
                if op1 in 'Ss':
                    lista.clear()
                    print('Toda a lista foi removida')
                elif op1 in 'Nn':
                    op = int(input('Qual o opcao voce deseja remover: '))
                    remover = lista.pop(op)
                    print('Reclamacao removida com sucesso!!!!')
            
        elif opcao == 5:
            if opcao == 5 and lista == []:
                print('Nenhuma reclamacao na lista, caso desejar adicionar tecle [2]')
                print()
            else:
                for item in range(len(lista)):
                    print(item,"-",lista[item])
                op = int(input('Qual opcao voce deseja alterar: '))
                newAlterar = str(input('DIGITE A NOVA RECLAMACAO PARA ALTERAR: '))
                lista[op] = newAlterar
        
print('Obrigado por usar no progama de ouvidoria :), Volte sempre!!!')