import telegram
from django.template.loader import render_to_string
from Requests.settings import bot, chat_id


def telega(i):
    message_html = render_to_string('bot/bot.html', {'i': i})
    bot.send_message(chat_id=chat_id, text=message_html, parse_mode=telegram.ParseMode.HTML)

    return i