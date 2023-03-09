def validar_caracteres(string):
    lista = []
    for caracter in string:
        if caracter in "({[":
            lista.append(caracter)
        elif caracter in ")}]":
            if len(lista) == 0:
                return False
            abertura = lista.pop()
            if (abertura == "(" and caracter != ")") or \
                (abertura == "{" and caracter != "}") or \
                (abertura == "[" and caracter != "]"):
                return False
    
    return len(lista) == 0