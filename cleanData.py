import pandas as pd

'''
classes = [
    'top-left-square', 
    'top-middle-square', 
    'top-right-square',
    'middle-left-square',  
    'middle-middle-square', 
    'middle-right-square', 
    'bottom-left-square', 
    'bottom-middle-square', 
    'bottom-right-square',
    'x-won'
    ]

df = pd.read_csv('tic-tac-toe.data', names=classes)
'''

##################################################################################################

# Função para verificar o resultado do jogo
def verificar_resultado(linha):
    # Linhas e colunas do tabuleiro de jogo
    tabuleiro = [
        [linha['top-left-square'], linha['top-middle-square'], linha['top-right-square']],
        [linha['middle-left-square'], linha['middle-middle-square'], linha['middle-right-square']],
        [linha['bottom-left-square'], linha['bottom-middle-square'], linha['bottom-right-square']]
    ]
    
    # Verificar se "X" ganhou
    if (any([linha == ['x', 'x', 'x'] for linha in tabuleiro]) or  # Linhas
        any([coluna == ['x', 'x', 'x'] for coluna in zip(*tabuleiro)]) or  # Colunas
        [tabuleiro[i][i] for i in range(3)] == ['x', 'x', 'x'] or  # Diagonal principal
        [tabuleiro[i][2-i] for i in range(3)] == ['x', 'x', 'x']):  # Diagonal secundária
        return 1  # X ganhou
    
    # Verificar se "O" ganhou
    if (any([linha == ['o', 'o', 'o'] for linha in tabuleiro]) or  # Linhas
        any([coluna == ['o', 'o', 'o'] for coluna in zip(*tabuleiro)]) or  # Colunas
        [tabuleiro[i][i] for i in range(3)] == ['o', 'o', 'o'] or  # Diagonal principal
        [tabuleiro[i][2-i] for i in range(3)] == ['o', 'o', 'o']):  # Diagonal secundária
        return 2  # X perdeu (O ganhou)
    
    # Verificar se há espaços vazios
    if any('b' in linha for linha in tabuleiro):
        return 4  # Ainda tem jogo
    
    # Se nenhuma condição anterior for atendida, é um empate
    return 3  # Empate

# Ler o arquivo CSV
df = pd.read_csv('tic-tac-toe.data', header=None)

df.columns = ['top-left-square', 'top-middle-square', 'top-right-square',
              'middle-left-square', 'middle-middle-square', 'middle-right-square',
              'bottom-left-square', 'bottom-middle-square', 'bottom-right-square', 'result']

# Atualizar a última coluna com base no resultado do jogo
df['result'] = df.apply(verificar_resultado, axis=1)

# Salvar o DataFrame atualizado em um novo arquivo
df.to_csv('tic-tac-toe-processed.data', index=False)

print("Última coluna atualizada com os resultados.")
