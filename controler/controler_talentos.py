from dao import dao_talento


def pesquisa(pesquisa):
    return dao_talento.pesquisa(pesquisa)


def pesquisa_por_id(id):
    return dao_talento.pesquisa_por_id(id)


def pesquisa_por_traco(pesquisa):
    return dao_talento.pesquisa_por_traco(pesquisa)
