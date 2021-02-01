import tokens
import telebot
import logging
import pretty_errors
from view import bot_view
from util import constants as c

bot = telebot.AsyncTeleBot(tokens.BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    """Responde a com uma mensagem de boas vindas e uma descrição da usabilidade.
    """

    bot.reply_to(message, "Seu bot iniciou!").wait()


@bot.message_handler(commands=["talento", "talentos"])
def pesquisa_talentos(message):
    """Pesquisa o talento de acordo com a pesquisa do usuário
    e responde.

    Args:
        message (Message): Mensagem recebida do usuário.
    """
    pesquisa = message.text.split(" ")[1]
    resposta = bot_view.pesquisa_talento(pesquisa)
    bot.reply_to(message, parse_mode="Markdown", **resposta).wait()


@bot.callback_query_handler(func=lambda message:
                            c.CALLBACK_TALENTO in message.data)
def callback_pesquisa_talento(message):
    """Retorna o Talento escolhido pelo usuário
    dentro das opções

    Args:
        message (Message): Mensagem recebida do usuário.
    """
    id = message.data.split(" ")[1]
    resposta = bot_view.pesquisa_talento_por_id(id)
    bot.send_message(message.message.chat.id,
                     parse_mode="Markdown",
                     **resposta).wait()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    bot.polling()
