from controler import controler_talentos


def test_pesquisa_talento_com_resultado():
    pesquisa = "artista"
    retorno = controler_talentos.pesquisa(pesquisa)
    assert len(retorno) > 0


def test_pesquisa_talento_sem_resultado():
    pesquisa = "nao_existe"
    retorno = controler_talentos.pesquisa(pesquisa)
    assert len(retorno) == 0


def test_pesquisa_talento_por_id_com_resultado():
    pesquisa = 1
    retorno = controler_talentos.pesquisa_por_id(pesquisa)
    assert len(retorno) == 1


def test_pesquisa_talento_por_id_sem_resultado():
    pesquisa = -1
    retorno = controler_talentos.pesquisa_por_id(pesquisa)
    assert len(retorno) == 0


def test_pesquisa_talento_por_traco_com_resultado():
    pesquisa = ["GERAL"]
    retorno = controler_talentos.pesquisa_por_traco(pesquisa)
    assert len(retorno) > 0


def test_pesquisa_talento_por_traco_sem_resultado():
    pesquisa = ["nao_existe"]
    retorno = controler_talentos.pesquisa_por_traco(pesquisa)
    assert len(retorno) == 0
