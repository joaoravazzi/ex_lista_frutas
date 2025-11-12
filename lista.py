# lista é uma "variável" que suporte muitos dados

frutas = []
#quando eu coloco a lista apenas com [] eu estou dizendo que ela é vazia

# o usuário terá 4 opções:
# - ver a lista
# - adicionar valor a lista
# - excluir a lista
# - sair da lista

print('----- Bem Vindo ao Varejão Gen -----')
print('Suas opções são:')
print('1 - Add fruta \n2 - Excluir fruta \n3 - Ver lista \n4 - sair')

escolha = int(input('Qual opção desejada: '))

if escolha < 1 or escolha > 4:
    print('Escolha nao reconhecida, finalizando sistema')
else:
    while escolha >= 1:
        if escolha == 1: #caso 1: add fruta
            nova_fruta = (input('Qual fruta quer adicionar: '))
            frutas.append(nova_fruta) # para adicionar um elemento na lista eu devo chamar a lista e dar o atributo ".append", anexando assim, o novo valor
            print(f'Fruta {frutas[-1]} adicionada')
            escolha = int(input('Qual opção desejada: '))
        elif escolha == 2: #caso 2: excluir fruta
            for posicao, cada_fruta in enumerate(frutas, start=1):
                print(posicao,' - ', cada_fruta)
            print('Agora você pode excluir um produto')
            posicao_fruta = int(input('Digite o numero da fruta que deseja excluir: '))
            frutas.pop(posicao_fruta - 1) #o comando pop exclui um elemento da lista, baseado em sua posição
            print('Fruta excluída')
            escolha = int(input('Qual opção desejada: '))
        elif escolha == 3: #caso 3: ver a lista
            for posicao, nome_frutas in enumerate(frutas, start = 1):
                print(posicao, '-', nome_frutas)
            escolha = int(input('Qual opção desejada: '))
        else: #caso 4: sair
            print('Obrigado, volte sempre!')    
            break 