from identificacao_de_substrings import identificar_repeticao

def test_01():
    retorno = identificar_repeticao("banana", "na")
    # __import__('ipdb').set_trace()
    assert retorno == 2

def test_02():
    retorno = identificar_repeticao("nonono", "no")
    # __import__('ipdb').set_trace()
    assert retorno == 3
