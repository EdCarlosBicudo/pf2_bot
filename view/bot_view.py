from controler import controler_talentos


def pesquisa_talento(pesquisa):
    retorno = controler_talentos.pesquisa(pesquisa)

    if retorno.count() == 0:
        return {"text": "Desculpe, não consegui encontrar este Talento."}

    if retorno.count() == 1:
        return {"text": retorno[0]}

    if retorno.count() > 1:
        #TODO fazer o keyboard markup
        return {"text": "O Talento que você está procurando é um desses?"}
