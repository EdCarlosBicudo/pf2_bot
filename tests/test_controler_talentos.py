from controler import controler_talentos


def test_pesquisa_talento_com_resultado():
    pesquisa = "artista"
    retorno = controler_talentos.pesquisa(pesquisa)
    assert len(retorno) > 0


def test_pesquisa_talento_sem_resultado():
    pesquisa = "nao_existe"
    retorno = controler_talentos.pesquisa(pesquisa)
    assert len(retorno) == 0
