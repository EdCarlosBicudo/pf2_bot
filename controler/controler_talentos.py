from dao import dao_talento


def pesquisa(pesquisa):
    retorno = dao_talento.pesquisa(pesquisa)
    return retorno
