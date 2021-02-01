from telebot.types import InlineKeyboardMarkup
from view import bot_view
from models.Talento import Talento


def test_pesquisa_talento_sem_resultado():
    pesquisa = "nao_existe"
    retorno = bot_view.pesquisa_talento(pesquisa)
    resultado_esperado = {"text": "Desculpe, não consegui encontrar este Talento."}
    assert isinstance(retorno, dict)
    assert resultado_esperado == retorno


def test_pesquisa_talento_com_um_resultado():
    pesquisa = "Aliados Quietos"
    retorno = bot_view.pesquisa_talento(pesquisa)
    assert isinstance(retorno, dict)
    assert retorno == {"text": Talento.get(Talento.nome == pesquisa)}


def test_pesquisa_talento_com_mais_de_um_resultado():
    pesquisa = "Artista"
    retorno = bot_view.pesquisa_talento(pesquisa)
    assert isinstance(retorno, dict)
    assert retorno["text"] == "O Talento que você está procurando é um desses?"
    assert isinstance(retorno["reply_markup"], InlineKeyboardMarkup)


def test_pesquisa_talento_por_id_com_resultado():
    pesquisa = 1
    retorno = bot_view.pesquisa_talento_por_id(pesquisa)
    assert isinstance(retorno, dict)
    assert retorno == {"text": Talento.get(Talento.id == pesquisa)}
