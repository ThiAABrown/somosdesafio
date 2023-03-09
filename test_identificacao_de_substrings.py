from identificacao_de_substrings import identificar_repeticao

def test_01():
    retorno = identificar_repeticao("banana", "na")
    assert retorno == 2

def test_02():
    retorno = identificar_repeticao("nonono", "no")
    assert retorno == 3

def test_03():
    retorno = identificar_repeticao("ABCDCDC", "CDC")
    assert retorno == 2

def test_04():
    retorno = identificar_repeticao("banana", "no")
    assert retorno == 0

def test_05():
    retorno = identificar_repeticao("nonono", "na")
    assert retorno == 0

def test_06():
    retorno = identificar_repeticao("ABCDCDC", "FGH")
    assert retorno == 0