import telebot
from config import token


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def message_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, '- Урра! Отлично сработано, ребятки. Давайте завтра не придем? Возбмем отгул на денек?)))')

bot.infinity_polling()