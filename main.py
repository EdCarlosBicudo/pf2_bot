import tokens
import telebot
import logging
import pretty_errors
from view import bot_view
from util import constants as c
from log import log

bot = telebot.AsyncTeleBot(tokens.BOT_TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    """Responde a com uma mensagem de boas vindas e uma descrição da usabilidade.

    Args:
        message (Message): Mensagem recebida do usuário.
    """

    log.add_known_user(message.chat.id)

    text = ("Este é um bot para consultas sobre o sistema Pathfinder Segunda Edição\n"
            "Este projeto ainda está em desenvolvimento.\n"
            "Funções implementadas até o momento:\n"
            "/talento: Pesquisa os talentos do sistema.\n"
            "/talentos: Pesquisa os talentos do sistema por traço.\n"
            "/licenca: Informações sobre a Licença de Uso da Paizo.\n"
            "\nDesenvolvido por: Ed Carlos Bicudo."
            "\ned.carlos.bicudo@pm.me"
            "\nhttps://github.com/EdCarlosBicudo/pf2_bot")

    bot.reply_to(message, text).wait()


@bot.message_handler(commands=["licenca"])
def exibe_license(message):
    """Exibe a licença de uso da Paizo

    Args:
        message (Message): Mensagem recebida do usuário.
    """
    log.log_access(message.chat.id, message.text)

    text = ("Para informações sobre a licensa acesse: "
            "[https://bitbucket.org/EdCarlosBicudo/pf2_bot/wiki/license]"
            "(https://bitbucket.org/EdCarlosBicudo/pf2_bot/wiki/license)")
    bot.reply_to(message, text, parse_mode="Markdown")


@bot.message_handler(commands=["talento"])
def pesquisa_talentos(message):
    """Pesquisa o talento de acordo com a pesquisa do usuário
    e responde.

    Args:
        message (Message): Mensagem recebida do usuário.
    """

    log.log_access(message.chat.id, message.text)

    pesquisa = message.text.split(" ")[1]
    resposta = bot_view.pesquisa_talento(pesquisa)
    bot.reply_to(message, parse_mode="Markdown", **resposta).wait()


@bot.message_handler(commands=["talentos"])
def pesquisa_talento_por_traco(message):
    """Pesquisa o talento por tracos de acordo com os tracos
    passados pelo usuário e responde.

    Args:
    message (Message): Mensagem recebida do usuário.
    """

    log.log_access(message.chat.id, message.text)

    pesquisa = message.text.split(" ")[1:]
    resposta = bot_view.pesquisa_talento_por_traco(pesquisa)
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

#    while True:
    try:
        bot.polling()
    except Exception as error:
        log.ERROR_LOGGER.error("MAIN:bot_caiu: " + str(error))
