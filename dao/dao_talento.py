from models.Talento import Talento, Traco, TracoTalento


def pesquisa(pesquisa):
    retorno = Talento.select().where(Talento.nome.contains(pesquisa))
    return retorno


def pesquisa_por_id(id):
    retorno = Talento.select().where(Talento.id == id)
    return retorno


def pesquisa_por_traco(pesquisa):
    query = (Talento
             .select(Talento, Traco)
             .join(TracoTalento)
             .join(Traco)
             .where(Traco.nome.in_(pesquisa))
             )
    retorno = []

    for talento in query:
        add = True
        for p in pesquisa:
            aux = []
            for traco in talento.tracos:
                aux.append(traco.traco.nome)
            if p not in aux:
                add = False
        if add:
            retorno.append(talento)
    return retorno
