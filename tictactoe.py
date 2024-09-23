def initialize_board():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

def display_board(tabuleiro_front):
    for linha in tabuleiro_front:
        print("|".join(linha))
        print("-----")

def get_player_move():
    linha = int(input("Digite a linha (0, 1, or 2): "))
    coluna = int(input("Digite a coluna (0, 1, or 2): "))
    return linha, coluna

def is_valid_move(tabuleiro_front, linha, coluna):
    return 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro_front[linha][coluna] == ' '

def make_move(tabuleiro_front, player, linha, coluna):
    tabuleiro_front[linha][coluna] = player

def check_winner(tabuleiro_front, player):
    # Check rows, columns, and diagonals
    return any(all(celula == player for celula in linha) for linha in tabuleiro_front) or \
           any(all(linha[i] == player for linha in tabuleiro_front) for i in range(3)) or \
           all(tabuleiro_front[i][i] == player for i in range(3)) or \
           all(tabuleiro_front[i][2 - i] == player for i in range(3))

def is_board_full(tabuleiro_front):
    return all(celula != ' ' for linha in tabuleiro_front for celula in linha)

def play_tic_tac_toe():
    jogador_atual = 'X'
    tabuleiro = initialize_board()

    while True:
        display_board(tabuleiro)
        print(f"Vez do jogador {jogador_atual}.")

        movimento = get_player_move()
        if is_valid_move(tabuleiro, movimento[0], movimento[1]):
            make_move(tabuleiro, jogador_atual, movimento[0], movimento[1])

            if check_winner(tabuleiro, jogador_atual):
                print(f"Player {jogador_atual} wins!")
                process_data(tabuleiro)
                break
            elif is_board_full(tabuleiro):
                print("The game ends in a tie!")
                break
            else:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Movimento. Tente novamente.")

def process_data(tabuleiro):
    for linha in tabuleiro:
        for index, caracter in enumerate(linha):
            if (caracter == 'X'):
                linha[index] = 1
            elif (caracter == 'O'):
                linha[index] = 0
            else:
                linha[index] = 2

def escolher_algoritmo():
    escolha = int(input("Escolha o algoritmo a ser utilizado: 1-KNN, 2-MLP, 3-Árvores: "))

    if (escolha == 1):
        # algoritmo knn
        return 0
    elif (escolha == 2): 
        # algoritmo mlp
        return 0
    elif (escolha == 3):
        # algoritmo arvore
        return 0

# Run the game
play_tic_tac_toe()