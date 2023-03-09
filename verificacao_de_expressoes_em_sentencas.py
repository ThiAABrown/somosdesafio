import json



def obter_tokens(sentenca):
    pontuacoes = [",", ".", "!", "?", ";", ":", "(", ")", "[", "]", "{", "}", "-", "/", "\\", "'", '"']

    palavra = ""
    tokens = []
    for posicao in range(len(sentenca)):
        if sentenca[posicao] not in pontuacoes and sentenca[posicao] != " ":
            palavra += sentenca[posicao]
        else:
            if palavra:
                tokens.append(palavra)
                palavra = ""
            if sentenca[posicao] in pontuacoes:
                tokens.append(sentenca[posicao])

    # Adicionar a última palavra à lista de tokens
    if palavra:
        tokens.append(palavra)

    return tokens

def verificar_expressao():
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
                    tokens = obter_tokens(frase.lower())
                    primeira_palavra_expressao = expressao.split()[0]
                    primeiros_tokens = tokens[:3]
                    
                    if primeira_palavra_expressao in primeiros_tokens:
                        sentenca_dict = {'sentença': frase, 'expressão': expressao}
                        sentencas.append(sentenca_dict)
                        encontrou_expressao = True
                        break

            if not encontrou_expressao:
                sentenca_dict = {'sentença': frase, 'expressão': None}
                sentencas.append(sentenca_dict)

        # 5- montar o dicionario que vai ser gravado no arquivo
        output_dict = {'id': texto_id, 'sentenças': sentencas}
        output.append(output_dict)
    return output

def converter_para_null(value):
    return "null" if value is None else value

output = verificar_expressao()

# 6 - Salvar a lista de saida em arquivo, usando a funcao "json.dumps"
with open('saida.json', 'w') as saida_resultado:
    json.dump(output, saida_resultado, ensure_ascii=False, default=converter_para_null)
