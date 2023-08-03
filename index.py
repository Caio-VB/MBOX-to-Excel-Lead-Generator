import csv

# Abrindo o arquivo de texto
with open('INBOX.txt', 'r', encoding='utf-8') as arquivo_txt:
    # Lendo todo o conteúdo do arquivo de texto
    conteudo = arquivo_txt.read()
    
    # Separando o conteúdo em linhas
    linhas = conteudo.split('\n')
    
    # Inicializando a matriz
    matriz = []
    
    # Inicializando as variáveis para armazenar os valores de cada conjunto
    nome = ''
    telefone = ''
    especialidade = ''
    unidade = ''
    data = ''
    
    # Iterando sobre as linhas do arquivo de texto
    for linha in linhas:
        if linha.startswith('Nome:'):
            nome = linha[len('Nome: '):]  # Removendo a string "Nome: " da linha
        elif linha.startswith('Telefone:'):
            telefone = linha[len('Telefone: '):]  # Removendo a string "Telefone: " da linha
        elif linha.startswith('Especialidade:'):
            especialidade = linha[len('Especialidade: '):]  # Removendo a string "Especialidade: " da linha
        elif linha.startswith('Unidade:'):
            unidade = linha[len('Unidade: '):]  # Removendo a string "Unidade: " da linha
        elif linha.startswith('Este e-mail foi enviado em'):
            data = linha[len('Este e-mail foi enviado em '):]  # Removendo a string "Este e\-mail foi enviado em " da linha
            # Adicionando os valores separados na matriz
            matriz.append([nome, telefone, especialidade, unidade, data])
    

    # Adicionando a primeira linha com os nomes das colunas
    matriz.insert(0, ['Nome', 'Telefone', 'Especialidade', 'Unidade', 'Data e Hora'])
            
    # Escrevendo a matriz em um arquivo CSV
    with open('arquivo.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(matriz)
