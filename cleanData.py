import pandas as pd
import csv

##################################################################################################

# Função de leitura do csv
def substitui_caracteres_csv(arquivo_input, arquivo_output):
    with open(arquivo_input, mode='r', newline='', encoding='utf-8') as infile, \
         open(arquivo_output, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for linha in reader:
            linha_modificada = []
            for celula in linha:
                # Verifica se a celula contém a palavra "positive"
                if "positive" in celula:
                    linha_modificada.append(celula)  # Mantém a celula original
                else:
                    # Substitui 'x' com '1' e 'o' com '0'
                    linha.append(celula.replace('x', '1').replace('o', '0').replace('b', '2'))
            writer.writerow(linha_modificada)

input_csv = './tic-tac-toe.data'  # Nome do dataset original
output_csv = './tic-tac-toe-no-classes.data'  # Nome do dataset alterado, a ser trabalhado
    
substitui_caracteres_csv(input_csv, output_csv)

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
        return 0  # O ganhou
    

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

print("Última coluna atualizada com os resultados.")
