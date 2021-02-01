from controler import controler_talentos
from markups import inline_keyboard_markups as ikm


def pesquisa_talento(pesquisa):
    retorno = controler_talentos.pesquisa(pesquisa)

    if retorno.count() == 0:
        return {"text": "Desculpe, não consegui encontrar este Talento."}

    if retorno.count() == 1:
        return {"text": retorno[0]}

    if retorno.count() > 1:
        return {"text": "O Talento que você está procurando é um desses?",
                "reply_markup": ikm.talentos_markup(retorno)}


def pesquisa_talento_por_id(id):
    retorno = controler_talentos.by_id(id)

    return {"text": retorno}
