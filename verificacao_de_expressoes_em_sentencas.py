import json

# 1 -ler o arquivo de expressões e guardar o resultado em uma lista
with open('expressoes.txt', 'r') as expressoes_arquivo:
        expressoes = expressoes_arquivo.readlines()

# 2- ler o arquivo de entrada (textos.json) e guardar o conteúdo em uma variável usando a funçâo "json.loads"
with open('textos.json') as entrada_textos:
    conteudo = entrada_textos.read().replace('\n', '')
    textos = eval(conteudo)

output = []

for item in textos:
    texto_id = item['id']
    texto = item['texto']

    # 3- descobre as frases no texto atual
    frases = []
    frase_atual = ''
    for letra in texto:
        frase_atual += letra
        if letra in ('!', '?', '.'):
            frases.append(frase_atual.strip())
            frase_atual = ''

    # 4- iterar nas expressoes e ver se elas estâo nas frases
    sentencas = []
    for frase in frases:
        encontrou_expressao = False

        for expressao in expressoes:
            expressao = expressao.replace('\n', '')
            if expressao.lower() in frase.lower():
                sentenca_dict = {'sentença': frase, 'expressão': expressao}
                sentencas.append(sentenca_dict)
                encontrou_expressao = True
                break

        if not encontrou_expressao:
            sentenca_dict = {'sentença': frase, 'expressão': 'null'}
            sentencas.append(sentenca_dict)

    # 5- montar o dicionario que vai ser gravado no arquivo
    output_dict = {'id': texto_id, 'sentenças': sentencas}
    output.append(output_dict)

# 6 - Salvar a lista de saida em arquivo, usando a funcao "json.dumps"
with open('saida.json', 'w') as saida_resultado:
    json.dump(output, saida_resultado, ensure_ascii=False)

