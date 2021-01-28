from dao import dao_talento


def test_pesquisa_talento_com_resultado():
    pesquisa = "artista"
    retorno = dao_talento.pesquisa(pesquisa)
    assert len(retorno) > 0


def test_pesquisa_talento_sem_resultado():
    pesquisa = "nao_existe"
    retorno = dao_talento.pesquisa(pesquisa)
    assert len(retorno) == 0
