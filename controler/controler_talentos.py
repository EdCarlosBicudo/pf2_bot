from dao import dao_talento


def pesquisa(pesquisa):
    return dao_talento.pesquisa(pesquisa)


def by_id(id):
    return dao_talento.by_id(id)
