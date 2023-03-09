from validacao_de_sequencia_de_caracteres import validar_caracteres

def teste_01():
    retorno = validar_caracteres("{[()]}")
    print(retorno)
    assert retorno == True

def teste_02():
    retorno = validar_caracteres("()[]{}")
    print(retorno)
    assert retorno == True

def teste_03():
    retorno = validar_caracteres("([])")
    print(retorno)
    assert retorno == True

def teste_04():
    retorno = validar_caracteres("{{[[(())]]}}")
    print(retorno)
    assert retorno == True

def teste_05():
    retorno = validar_caracteres("{[()([])]}")
    print(retorno)
    assert retorno == True

def teste_06():
    retorno = validar_caracteres("([]")
    print(retorno)
    assert retorno == False

def teste_07():
    retorno = validar_caracteres("[({)}]")
    print(retorno)
    assert retorno == False

def teste_08():
    retorno = validar_caracteres(")(")
    print(retorno)
    assert retorno == False

def teste_09():
    retorno = validar_caracteres("(([{()}])))")
    print(retorno)
    assert retorno == False