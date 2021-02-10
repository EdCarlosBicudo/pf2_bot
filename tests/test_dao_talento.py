from dao import dao_talento


def test_pesquisa_talento_com_resultado():
    pesquisa = "artista"
    retorno = dao_talento.pesquisa(pesquisa)
    assert len(retorno) > 0


def test_pesquisa_talento_sem_resultado():
    pesquisa = "nao_existe"
    retorno = dao_talento.pesquisa(pesquisa)
    assert len(retorno) == 0


def test_pesquisa_talento_por_id_com_resultado():
    pesquisa = 1
    retorno = dao_talento.pesquisa_por_id(pesquisa)
    assert len(retorno) == 1


def test_pesquisa_talento_por_id_sem_resultado():
    pesquisa = -1
    retorno = dao_talento.pesquisa_por_id(pesquisa)
    assert len(retorno) == 0


def test_pesquisa_talento_por_traco_com_resultado():
    pesquisa = ["GERAL"]
    retorno = dao_talento.pesquisa_por_traco(pesquisa)
    assert len(retorno) > 1


def test_pesquisa_talento_por_traco_sem_resultado():
    pesquisa = ["nao_existe"]
    retorno = dao_talento.pesquisa_por_traco(pesquisa)
    assert len(retorno) == 0
