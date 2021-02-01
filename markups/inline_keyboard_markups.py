from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from util import constants as c


def talentos_markup(talentos):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    for talento in talentos:
        markup.add(InlineKeyboardButton(talento.nome,
                   callback_data=f"{c.CALLBACK_TALENTO} {talento.id}"))

    return markup
