def identificar_repeticao(s1, s2):
    repeticao = 0
    tamanho_s1 = len(s1) 
    tamanho_s2 = len(s2)
    for string in range(tamanho_s1):
        substring = s1[string:string+tamanho_s2]
        if substring == s2:
            repeticao += 1
    
    return repeticao

retorno = identificar_repeticao("banana", "na")
print(retorno)
