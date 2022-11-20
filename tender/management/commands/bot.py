import datetime
import re
from time import timezone
# from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from tender.models import Tab, DealerTab,IconsDealers,PostavTab, Product
import pytz


import wikipedia as wiki
wiki.set_lang("ru")
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)
def wiki_bot(word):
    info=wiki.summary(word)
    return info

# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Телеграм-бот'

    def handle(self, *args, **kwargs):

        @bot.message_handler(content_types=['text'])
        def message_handler(message: telebot.types.Message):

            # try:
            #     bot.send_message(message.chat.id, wiki_bot(message.text))
            #
            # except:
            #     bot.send_message(message.chat.id, 'По запросу ничего не найдено!')
            zap = [i for i in re.split(r'\W+',message.text) if i]
            print(zap)
            if zap[0] == 'Просроченные':

                tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=zap[-1], data2__lte=datetime.date.today()).order_by('data2')
                for tab in tabs:
                    if tab:
                        bot.send_message(message.chat.id, f'{tab.staffer} {tab.data2.strftime("%Y-%m-%d")}')
                    else:
                        bot.send_message(message.chat.id, f'{zap[-1]} - КрасАУЧЕГ!')

        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()								# Загрузка обработчиков
        bot.infinity_polling()											# Бесконечный цикл бота