# 1 -ler o arquivo de expressões e guardar o resultado em uma lista

with open('expressoes.txt', 'r') as expressoes_arquivo:
        expressoes = expressoes_arquivo.readlines()
__import__('ipdb').set_trace()

# 2- ler o arquivo de entrada (textos.json) e guardar o conteúdo em uma variável usando a funçâo "json.loads"

# 3 - criar uma lista para armazenar o output 

# 4 - para cada sentença (.?!) do arquivo de entrada, iterar na lista de expressôes e verificar se ela comea com a expressâo. 

# 5 - Criar um dict na lista que armazena o output com a sentenca e se ela possui ou nao a expressao.

# 6 - Salvar a lista de output em arquivo, usando a funcao "json.dumps"

