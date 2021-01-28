from models.Talento import Talento, Tipo, TipoTalento


def pesquisa(pesquisa):
    retorno = Talento.select().where(Talento.nome.contains(pesquisa))
    return retorno
