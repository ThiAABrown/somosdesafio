from verificacao_de_expressoes_em_sentencas import verificar_expressao, obter_tokens

def test_obter_tokens():
    sentenca = " "
    tokens = obter_tokens(sentenca)

    assert tokens == []

def test_verificar_expressao():
    output = verificar_expressao()
    # __import__('ipdb').set_trace()
    assert output == [
        {
            'id': 1, 
            'sentenças': [
                {
                'sentença': 'Em primeiro lugar, a forma atual de ensino, em que o aluno é obrigado a sentar-se em intervalos determinados pelos superiores, forma os adultos que levam essa forma de produção para o ofício.', 
                'expressão': None
                },
                {
                'sentença': 'Logo, baseado no que foi dito, vale citar o filósofo Pitágoras, que explica que é melhor educar bem as crianças do que ter que reeducá-las como adultos.', 
                'expressão': 'baseado no que foi dito'
                }, 
                {
                'sentença': 'Assim, os maus hábitos adquiridos na infância podem gerar, nos adultos, muitas complicações, já que dentro da sala de aula, a movimentação dos alunos pelo ambiente é repudiada e muitas vezes com consequências.', 
                'expressão': None
                }, 
                {
                'sentença': 'Como consequência, a doutrinação do modelo educacional não atende aos paradigmas de formação de um adulto atento à saúde ocupacional.', 'expressão': 'como consequência'
                }
            ]
        }, 
        {
            'id': 4, 
            'sentenças': 
            [
                {
                'sentença': 'Perante os argumentos citados, é alarmante o número de indivíduos que crescem traumatizados, muitas vezes sem tratamento adequado, durante ou após a infância, desenvolvendo uma realidade de mundo inquietante.', 
                'expressão': 'perante os argumentos citados'
                }, 
                {
                'sentença': 'Por conseguinte, é relevante adicionar que, sendo a cultura - associada às relações e experiências de vida do cidadão - um meio pelo qual se cria a construção da realidade na consciência dos jovens, a realidade que está sendo criada pelas vítimas pode refletir na decadência da sociedade brasileira, em termos de segurança, educação e até cultural.', 
                'expressão': 'é relevante adicionar'
                }
            ]
        }
    ]