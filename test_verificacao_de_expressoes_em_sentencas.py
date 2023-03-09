from verificacao_de_expressoes_em_sentencas import verificar_expressao, obter_tokens

def test_obter_tokens():
    sentenca = " "
    tokens = obter_tokens(sentenca)

    assert tokens == []

def test_verificar_expressao():
    expressao = verificar_expressao()

    assert expressao == [{
        
    }]