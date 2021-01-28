import tokens
import telebot
import logging
import pretty_errors
from view import bot_view

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
    bot.reply_to(message, **resposta).wait()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    bot.polling()
