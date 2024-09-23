import random
import numpy
from knntictactoe import inicia_algoritmo as init_knn
from mlptictactoe import inicia_algoritmo as init_mlp
from treetictactoe import inicia_algoritmo as init_tree

def print_board(board):
    print("\n    1   2   3 \n")
    print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")


def check_row(board, row):
    return (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ")


def check_column(board, col):
    return (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " ")


def check_diagonals(board):
    return (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ") or\
            (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ")


def check_winner(board):
    for i in range(3):
        if check_row(board, i):
            return True
        if check_column(board, i):
            return True
    if check_diagonals(board):
        return True
    return False


def is_board_full(board):
    for item in board:
        if " " in item:
            return False
    return True


def play(board):
    while True:
        row = input("Enter row number: ")
        while not row.isdigit() or int(row) < 1 or int(row) > 3:
            row = input("Enter row number between 1-3: ")

        row = int(row)
        
        col = input("Enter column number: ")
        
        while not col.isdigit() or int(col) < 1 or int(col) > 3:
            col = input("Enter column number between 1-3: ")
        
        col = int(col)
        
        if board[row-1][col-1] != " ":
            print("Pick an empty box!")
        else:
            return (row-1, col-1)
        


def play_random(board):
    possible_moves = []

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                possible_moves.append((row, col))
    
    return possible_moves[random.randrange(len(possible_moves))]


def main():
    random.seed()
    
    # Create an empty board
    board = [ 
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Create 2 players
    players = ["X", "O"]
    # Player X plays first
    turn = 0

    while not is_board_full(board):
        print_board(board)

        if turn == 0:
            # User input
            print("You play!")
            row, col = play(board)
            board[row][col] = players[turn]
        else:
            # Compuuter plays
            print("Computer plays!")
            row, col = play_random(board)
            board[row][col] = players[turn]
            
        copia_board = numpy.array(board).flatten()

        copia_board[copia_board == 'O'] = 0
        copia_board[copia_board == 'X'] = 1
        copia_board[copia_board == ' '] = 2

        copia_board = [int(numeric_string) for numeric_string in copia_board]
        copia_board = numpy.array(copia_board)

        if (algoritmo_escolhido == 1):
            predicao = knn.predict(copia_board.reshape(1, -1))
            pass
        if (algoritmo_escolhido == 2):
            predicao = mlp.predict(copia_board.reshape(1, -1))
            pass
        if (algoritmo_escolhido == 3):
            predicao = tree.predict(copia_board.reshape(1, -1))
            pass

        print("Predição: " + str(predicao[0]))

        if (predicao[0] == 0):
            print_board(board)
            print("O ganhou!")
            break
        elif (predicao[0] == 1):
            print_board(board)
            print("X ganhou!")
            break
        elif (predicao[0] == 2):
            print_board(board)
            print("Empate!")
            break
        else:
            print("Ainda tem jogo...")
        
        # Select the next player
        turn = 1 - turn


def escolher_algoritmo():
    escolha = int(input("Escolha o algoritmo a ser utilizado: 1-KNN, 2-MLP, 3-Árvores: "))

    if (escolha == 1):
        # algoritmo knn
        return 1
    elif (escolha == 2): 
        # algoritmo mlp
        return 2
    elif (escolha == 3):
        # algoritmo arvore
        return 3
    

knn = init_knn()
mlp = init_mlp()
tree = init_tree()

algoritmo_escolhido = escolher_algoritmo()

main()