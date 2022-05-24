tabela = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
jogador = True
conta = 0
def printtab(tabela):
    for l in range(0, 3):
        for c in range(0, 3):
            print(f'[{tabela[l][c]}]', end='')
        print()

def fazerlinha():
    print('-=' * 29)

def adiciona(jogo, tabela, jogadoratu):
    linha = jogo[0]
    coluna = jogo[1]
    tabela[linha][coluna] = jogadoratu

    
def verifica(jogo, tabela):
    linha = jogo[0]
    coluna = jogo[1]
    if tabela[linha][coluna] != '_':
        print('Posição ocupada')
        return True
    else:
        return False
        
def troca(jogador):
    if jogador:
        return 'X'
    else:
        return 'O'

def posicao(jogada):
    linha = int(jogada / 3)
    coluna = jogada
    if coluna > 2:
        coluna = int(coluna % 3)
    return (linha, coluna)

def sair(jogada):
    if jogada == 'sair': return True
    else: return False

def olhacoluna(jogador, tabela):
    if tabela[0][0] == jogador and tabela[1][0] == jogador and tabela[2][0] == jogador:
        return True
    elif tabela[0][1] == jogador and tabela[1][1] == jogador and tabela[2][1] == jogador:
        return True
    elif tabela[0][2] == jogador and tabela[1][2] == jogador and tabela[2][2] == jogador:
        return True
    else:
        return False
    

def olhalinha(jogador, tabela):
    if tabela[0][0] == jogador and tabela[0][1] == jogador and tabela[0][2] == jogador:
        return True
    elif tabela[1][0] == jogador and tabela[1][1] == jogador and tabela[1][2] == jogador:
        return True
    elif tabela[2][0] == jogador and tabela[2][1] == jogador and tabela[2][2] == jogador:
        return True
    else:
        return False


def olhadiagonal(jogador, tabela):
    if tabela[0][0] == jogador and tabela[1][1] == jogador and tabela[2][2] == jogador:
        return True
    elif tabela[0][2] == jogador and tabela[1][1] == jogador and tabela[2][0] == jogador:
        return True
    else:
        return False

def vitoria(jogador, tabela):
    if olhalinha(jogador, tabela):
        return True
    if olhacoluna(jogador, tabela):
        return True
    if olhadiagonal(jogador, tabela):
        return True
    return False
 

while conta < 9:
    jogadoratu = troca(jogador)
    fazerlinha()
    print('            Esse é o tabuleiro, faça sua jogada')
    fazerlinha()
    printtab(tabela)
    fazerlinha()
    jogada = input('Jogada: ')
    fazerlinha()
    if sair(jogada):
         break
    jogada = int(jogada) -1
    jogo = posicao(jogada)
    if verifica(jogo, tabela):
        print('Tente novamente')
        continue
    adiciona(jogo, tabela, jogadoratu)
    if vitoria(jogadoratu, tabela):
        printtab(tabela)
        print(f'{jogadoratu} Voce ganhou!')
        break
    conta += 1
    if conta == 9:
        print(' Deu Empate')
    jogador = not jogador