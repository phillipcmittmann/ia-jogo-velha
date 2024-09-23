import sys
import numpy
from knntictactoe import retorna_previsao_knn, inicia_algoritmo_knn
from mlptictactoe import retorna_previsao_mlp, inicia_algoritmo_mlp
from treetictactoe import retorna_previsao_tree, inicia_algoritmo_tree

def initialize_board():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

def display_board(tabuleiro_front):
    tabuleiro_display = tabuleiro_front.copy()

    for linha in tabuleiro_display:
        for index, caracter in enumerate(linha):
            if (caracter == 1):
                linha[index] = 'X'
            elif (caracter == 0):
                linha[index] = 'O'
            else:
                linha[index] = ' '
        print("|".join(linha))
        print("-----")

def get_player_move():
    linha = int(input("Digite a linha (0, 1, or 2): "))
    coluna = int(input("Digite a coluna (0, 1, or 2): "))
    return linha, coluna

def is_valid_move(tabuleiro_front, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro_front[linha][coluna] == ' '

def make_move(tabuleiro_front, player, linha, coluna, algoritmo_escolhido, knn, mlp, tree):
    tabuleiro_front[linha][coluna] = player
    tabuleiro_formatado = process_data(tabuleiro_front)
    tabuleiro_formatado = numpy.reshape(tabuleiro_formatado, (-1, 10))

    if (algoritmo_escolhido == 1):
        return retorna_previsao_knn(tabuleiro_formatado, knn)
    elif (algoritmo_escolhido == 2):
        return retorna_previsao_mlp(tabuleiro_formatado, mlp)
    elif (algoritmo_escolhido == 3):
        return retorna_previsao_tree(tabuleiro_formatado, tree)


def check_winner(tabuleiro_front, player):
    # Check rows, columns, and diagonals
    return any(all(celula == player for celula in linha) for linha in tabuleiro_front) or \
           any(all(linha[i] == player for linha in tabuleiro_front) for i in range(3)) or \
           all(tabuleiro_front[i][i] == player for i in range(3)) or \
           all(tabuleiro_front[i][2 - i] == player for i in range(3))

def is_board_full(tabuleiro_front):
    return all(celula != ' ' for linha in tabuleiro_front for celula in linha)

def play_tic_tac_toe(algoritmo_escolhido, knn, mlp, tree):
    jogador_atual = 'X'
    tabuleiro = initialize_board()

    while True:
        display_board(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")

        movimento = get_player_move()
        if is_valid_move(tabuleiro, movimento[0], movimento[1]):
            estado = make_move(tabuleiro, 
                               jogador_atual, 
                               movimento[0], 
                               movimento[1], 
                               algoritmo_escolhido,
                               knn, mlp, tree)

            if (estado == 0 or estado == 1):
                print(f"Jogador {jogador_atual} venceu!")
                break
            elif estado == 2:
                print("Acabou em empate!")
                break
            else:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Movimento inválido. Tente novamente.")

def process_data(tabuleiro):
    novo_array = []

    for linha in tabuleiro:
        for index, caracter in enumerate(linha):
            if (caracter == 'X'):
                linha[index] = 1
            elif (caracter == 'O'):
                linha[index] = 0
            else:
                linha[index] = 2
            novo_array.append(linha[index])
    novo_array.append(3)

    return novo_array
    

def escolher_algoritmo():
    escolha = int(input("Escolha o algoritmo a ser utilizado: 1-KNN, 2-MLP, 3-Árvores: "))

    algoritmo_escolhido = None
    knn = inicia_algoritmo_knn()
    mlp = inicia_algoritmo_mlp()
    tree = inicia_algoritmo_tree()

    if (escolha == 1):
        # algoritmo knn
        algoritmo_escolhido = 1
    elif (escolha == 2): 
        # algoritmo mlp
        algoritmo_escolhido = 2
    elif (escolha == 3):
        # algoritmo arvore
        algoritmo_escolhido = 3
    else:
        sys.exit()

    play_tic_tac_toe(algoritmo_escolhido, knn, mlp, tree)
    
escolher_algoritmo()