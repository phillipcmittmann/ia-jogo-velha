import pandas as pd
import csv
from sklearn.model_selection import train_test_split

##################################################################################################

def replace_chars_in_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            modified_row = []
            for cell in row:
                # Checa se a celula possui a palavra "positive"
                if "positive" in cell:
                    modified_row.append(cell)  # Mantem a celula original
                else:
                    # Muda 'x' com '1' e 'o' com '0'
                    modified_row.append(cell.replace('x', '1').replace('o', '0').replace('b', '2'))
            writer.writerow(modified_row)

input_csv = './tic-tac-toe.data'  # Arquivo a ser lido
output_csv = './tic-tac-toe-no-classes.data'  # Nome do arquivo criado
    
replace_chars_in_csv(input_csv, output_csv)

##################################################################################################

# Função para verificar o resultado do jogo
def verificar_resultado(linha):
    # Linhas e colunas do tabuleiro de jogo
    tabuleiro = [
        [linha['top-left-square'], linha['top-middle-square'], linha['top-right-square']],
        [linha['middle-left-square'], linha['middle-middle-square'], linha['middle-right-square']],
        [linha['bottom-left-square'], linha['bottom-middle-square'], linha['bottom-right-square']]
    ]
    
    # Verificar se "O" ganhou
    if (any([linha == (0, 0, 0) for linha in tabuleiro]) or  # Linhas
        any([coluna == (0, 0, 0) for coluna in zip(*tabuleiro)]) or  # Colunas
        [tabuleiro[i][i] for i in range(3)] == (0, 0, 0) or  # Diagonal principal
        [tabuleiro[i][2-i] for i in range(3)] == (0, 0, 0)):  # Diagonal secundária
        return 0  # X perdeu (O ganhou)
    

    # Verificar se "X" ganhou
    if (any([linha == (1, 1, 1) for linha in tabuleiro]) or  # Linhas
        any([coluna == (1, 1, 1) for coluna in zip(*tabuleiro)]) or  # Colunas
        [tabuleiro[i][i] for i in range(3)] == (1, 1, 1) or  # Diagonal principal
        [tabuleiro[i][2-i] for i in range(3)] == (1, 1, 1)):  # Diagonal secundária
        return 1  # X ganhou
    
    # Verificar se há espaços vazios
    if any(2 in linha for linha in tabuleiro):
        return 3  # Ainda tem jogo
    
    # Se nenhuma condição anterior for atendida, é um empate
    return 2  # Empate

# Ler o arquivo CSV
df = pd.read_csv('tic-tac-toe-no-classes.data', header=None)

df.columns = ['top-left-square', 'top-middle-square', 'top-right-square',
              'middle-left-square', 'middle-middle-square', 'middle-right-square',
              'bottom-left-square', 'bottom-middle-square', 'bottom-right-square', 'result']

# Atualizar a última coluna com base no resultado do jogo
df['result'] = df.apply(verificar_resultado, axis=1)

# Salvar o DataFrame atualizado em um novo arquivo
df.to_csv('tic-tac-toe-processed.data', index=False)

##################################################################################################

X = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)
y = pd.read_csv('./tic-tac-toe-processed.data', sep=',', header=0)

gb_X = X.groupby('result')

o_ganhou_X = gb_X.get_group(0)
o_ganhou_X = o_ganhou_X.drop(o_ganhou_X.columns[9], axis=1)

x_ganhou_X = gb_X.get_group(1)
x_ganhou_X = x_ganhou_X.drop(x_ganhou_X.columns[9], axis=1)

empate_X = gb_X.get_group(2)
empate_X = empate_X.drop(empate_X.columns[9], axis=1)

tem_jogo_X = gb_X.get_group(3)
tem_jogo_X = tem_jogo_X.drop(tem_jogo_X.columns[9], axis=1)

gb_y = y.groupby('result')

o_ganhou_y = gb_y.get_group(0)
o_ganhou_y = o_ganhou_y.drop(o_ganhou_y.columns[:9], axis=1)

x_ganhou_y = gb_y.get_group(1)
x_ganhou_y = x_ganhou_y.drop(x_ganhou_y.columns[:9], axis=1)

empate_y = gb_y.get_group(2)
empate_y = empate_y.drop(empate_y.columns[:9], axis=1)

tem_jogo_y = gb_y.get_group(3)
tem_jogo_y = tem_jogo_y.drop(tem_jogo_y.columns[:9], axis=1)

o_ganhou_X_train, o_ganhou_X_test, o_ganhou_y_train, o_ganhou_y_test = train_test_split(o_ganhou_X, o_ganhou_y, test_size=0.30)
x_ganhou_X_train, x_ganhou_X_test, x_ganhou_y_train, x_ganhou_y_test = train_test_split(x_ganhou_X, x_ganhou_y, test_size=0.30)
empate_X_train, empate_X_test, empate_y_train, empate_y_test = train_test_split(empate_X, empate_y, test_size=0.30)
tem_jogo_X_train, tem_jogo_X_test, tem_jogo_y_train, tem_jogo_y_test = train_test_split(tem_jogo_X, tem_jogo_y, test_size=0.30)

X_train_concat = pd.concat([o_ganhou_X_train, x_ganhou_X_train, tem_jogo_X_train, empate_X_train])
y_train_concat = pd.concat([o_ganhou_y_train, x_ganhou_y_train, tem_jogo_y_train, empate_y_train])

X_train_concat.to_csv('./tic-tac-toe-X-train.data', index=False)
y_train_concat.to_csv('./tic-tac-toe-y-train.data', index=False)

X_test_concat = pd.concat([o_ganhou_X_test, x_ganhou_X_test, tem_jogo_X_test, empate_X_test])
y_test_concat = pd.concat([o_ganhou_y_test, x_ganhou_y_test, tem_jogo_y_test, empate_y_test])

X_test_concat.to_csv('./tic-tac-toe-X-test.data', index=False)
y_test_concat.to_csv('./tic-tac-toe-y-test.data', index=False)

print("Limpeza dos dados realizada com sucesso.")
