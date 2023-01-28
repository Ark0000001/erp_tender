import datetime
# import re
# from time import timezone
# # from datetime import datetime
from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
import time
from telebot import types
from tender.models import Tab
# import pytz
# import sys
# from translate import Translator


# import wikipedia as wiki
# wiki.set_lang("ru")
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)
# def wiki_bot(word):
#     info=wiki.summary(word)
#     return info

# Название класса обязательно - "Command"
# class Command(BaseCommand):
#     # Используется как описание команды обычно
#     help = 'Телеграм-бот'
#
#     def handle(self, *args, **kwargs):
#
#
#         @bot.message_handler(commands=['rent'])
#         def start(message):
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             btn1 = types.KeyboardButton("Узнать СС")
#             btn2 = types.KeyboardButton("Узнать R%")
#
#
#             markup.add(btn1, btn2)
#             bot.send_message(message.chat.id, text="Рассчитаем СС или R%", reply_markup=markup)
#         @bot.message_handler(func=lambda m: True)
#         def func1(message):
#
#
#             if (message.text == "Узнать СС"):
#                 bot.reply_to(message, "Введи через пробел - выручку и рентабельность : ")
#                 bot.register_next_step_handler(message, plus_one)
#
#             elif (message.text == "Узнать R%"):
#                 bot.reply_to(message, "Введи через пробел - выручку и cc : ")
#                 bot.register_next_step_handler(message, minus_one)
#
#
#         def plus_one(message):
#             p = message.text
#             # b=p.split(' ')
#             # n,m=b
#             # ss1=int(n)+int(m)
#             b = p.split(' ')
#
#
#             n, m = b
#             a, b = n.replace(',', '.'), m.replace(',', '.')
#             v = float(a)
#             r = float(b)
#
#             p = v * r / 100
#             ss1 = v - p
#             bot.reply_to(message, f"Ответ: {ss1:.2f}")
#
#         def minus_one(message):
#             p = message.text
#             b = p.split(' ')
#             print(b)
#             n, m = b
#
#             p = int(n) - int(m)
#             ss2 = p / int(n) * 100
#             bot.reply_to(message, f"Ответ: {ss2:.2f}")

        # @bot.message_handler(commands=['задачи'])
        # def start(message):
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     btn1 = types.KeyboardButton("Просроченные")
        #     btn2 = types.KeyboardButton("Текущие")
        #     markup.add(btn1, btn2)
        #     bot.send_message(message.chat.id,
        #                      text=f"Задачи!", reply_markup=markup)
        # @bot.message_handler(content_types=['text'])
        #
        # def func1(message):
        #     if (message.text == "Просроченные"):
        #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #         btn1 = types.KeyboardButton("Кальницкий")
        #         btn2 = types.KeyboardButton("Ситник")
        #         btn3 = types.KeyboardButton("Муромцева")
        #         btn4 = types.KeyboardButton("Скоробогатая")
        #         btn5 = types.KeyboardButton("Мирончик")
        #         btn6 = types.KeyboardButton("Евтеев")
        #         markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        #         bot.send_message(message.chat.id, text=f"ПРОСРОЧЕННЫЕ ЗАДАЧИ!", reply_markup=markup)
        #
        #
        #     elif (message.text == "Кальницкий"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                                   data2__lte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет просроченных задач!''')
        #
        #     # elif (message.text == "Os"):
        #     #     bot.send_message(message.chat.id, text=f"Твоя операционная система: {ossys}")
        #
        #     elif (message.text == "Ситник"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                                   data2__lte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет просроченных задач!''')
        #     elif (message.text == "Муромцева"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                                   data2__lte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет просроченных задач!''')
        #     elif (message.text == "Скоробогатая"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                                   data2__lte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет просроченных задач!''')
        #     elif (message.text == "Мирончик"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                                   data2__lte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет просроченных задач!''')
        #     elif (message.text == "Евтеев"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                                   data2__lte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет просроченных задач!''')
        #
        #     elif (message.text == "Текущие"):
        #         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #         btn1 = types.KeyboardButton("1Кальницкий")
        #         btn2 = types.KeyboardButton("2Ситник")
        #         btn3 = types.KeyboardButton("3Муромцева")
        #         btn4 = types.KeyboardButton("4Скоробогатая")
        #         btn5 = types.KeyboardButton("5Мирончик")
        #         btn6 = types.KeyboardButton("6Евтеев")
        #         markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        #         bot.send_message(message.chat.id, text=f"ТЕКУЩИЕ ЗАДАЧИ!", reply_markup=markup)
        #
        #     elif (message.text == "1Кальницкий"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:],
        #                                   data2__gte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:])
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Текущие ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет задач!''')
        #     elif (message.text == "2Ситник"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:],
        #                                   data2__gte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:])
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Текущие ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} -Нет задач!''')
        #     elif (message.text == "3Муромцева"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:],
        #                                   data2__gte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:])
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Текущие ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет задач!''')
        #     elif (message.text == "4Скоробогатая"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:],
        #                                   data2__gte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:])
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Текущие ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет задач!''')
        #     elif (message.text == "5Мирончик"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:],
        #                                   data2__gte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:])
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Текущие ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет задач!''')
        #     elif (message.text == "6Евтеев"):
        #         tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:],
        #                                   data2__gte=datetime.date.today()).order_by('data2')
        #         tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text[1:])
        #         if len(tabs) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Текущие ({len(tabs)}) задачи!''')
        #             for tab in tabs:
        #                 bot.send_message(message.chat.id, f'''
        #                             {tab.staffer}
        #                             {tab.data2.strftime("%Y-%m-%d")}
        #                             {str(tab.task_info)[0:140]}...''')
        #
        #         elif len(tabs2) > 0:
        #             bot.send_message(message.chat.id, f'''
        #                             {message.text} - Нет задач!''')

        # @bot.message_handler(content_types=['text'])
        # def message_handler(message: telebot.types.Message):
        #     tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                               data2__lte=datetime.date.today()).order_by('data2')
        #     tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #     if len(tabs) > 0:
        #         bot.send_message(message.chat.id, f'''
        #             {message.text} - Проанализируй пжл свои ({len(tabs)}) задачи!
        #             Ваш любимый БОТ!)''')
        #         for tab in tabs:
        #             bot.send_message(message.chat.id, f'''
        #             {tab.staffer}
        #             {tab.data2.strftime("%Y-%m-%d")}
        #             {str(tab.task_info)[0:40]}...''')
        #
        #     elif len(tabs2) > 0:
        #         bot.send_message(message.chat.id, f'''
        #             {message.text} - КрасАУЧЕГ!
        #             Нет просроченных задач!''')



        #         else:
        #             bot.send_message(message.chat.id, text=f"""
        #                                          Мой Господин - {message.from_user.first_name}!
        #                                          На текущий день нет задач!""", reply_markup=markup)
        #
        #         @bot.message_handler(content_types=['text'])
        #         def message_handler(message: telebot.types.Message):
        #
        #             # try:
        #             #     bot.send_message(message.chat.id, wiki_bot(message.text))
        #             #
        #             # except:
        #             #     bot.send_message(message.chat.id, 'По запросу ничего не найдено!')
        #             # zap = [i for i in re.split(r'\W+',message.text) if i]
        #
        #

        #
        #     elif (message.text == "❓ Задать вопрос"):
        #
        # @bot.message_handler(commands=['сегодня'])  # создаем команду
        # def start2(message):
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #     btn1 = types.KeyboardButton("Кальницкий")
        #     btn2 = types.KeyboardButton("Ситник")
        #     btn3 = types.KeyboardButton("Муромцева")
        #     btn4 = types.KeyboardButton("Скоробогатая")
        #     btn5 = types.KeyboardButton("Мирончик")
        #     btn6 = types.KeyboardButton("Евтеев")
        #     markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        #     bot.send_message(message.chat.id,
        #                      text=f"""
        #                      Мой Господин - {message.from_user.first_name}!
        #                      На текущий день нет задач!""", reply_markup=markup)
        #
        # @bot.message_handler(content_types=['text'])
        # def message_handler2(message: telebot.types.Message):
        #
        #
        #     tabs = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text,
        #                               data2=datetime.date.today()).order_by('data2')
        #     tabs2 = Tab.objects.filter(is_active=False, staffer__name__istartswith=message.text)
        #
        #
        #     if len(tabs) > 0:
        #         bot.send_message(message.chat.id, f'''
        #     {message.text} - Текущие ({len(tabs)}) задачи!
        #     Ваш любимый БОТ!)''')
        #         for tab in tabs:
        #             bot.send_message(message.chat.id, f'''
        #     {tab.staffer}
        #     {tab.data2.strftime("%Y-%m-%d")}
        #     {str(tab.task_info)[0:40]}...''')
        #
        #     elif len(tabs2) > 0:
        #         bot.send_message(message.chat.id, f'''
        #     {message.text} - Срочно создай задачу!''')





        # bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        # bot.load_next_step_handlers()								# Загрузка обработчиков
        # bot.infinity_polling()											# Бесконечный цикл бота

# https://t.me/+Y_KnBhP1EeplNjYy

task=Tab.objects.filter(is_active=False).order_by('data2')
d1=datetime.datetime.today().strftime('%Y-%m-%d')

tasks=[]
for t in task:
    d2=t.data2.strftime('%Y-%m-%d')
    if d2<d1:


        tasks.append((t.staffer,t.task_info))






for i in tasks:
    for k,z in i:
        if int(datetime.datetime.today().strftime('%H'))>18 and int(datetime.datetime.today().strftime('%H'))<19:
            bot.send_message('https://t.me/+Y_KnBhP1EeplNjYy', str(k+' : ' +z))


