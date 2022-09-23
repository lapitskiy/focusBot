import logging
from telegram.ext import Updater, RegexHandler
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

from bot_func import *

from bot_class import *

from bot_settings import settings

import tokencfg

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = tokencfg.TOKEN

REQUEST_KWARGS={
    # "USERNAME:PASSWORD@" is optional, if you need authentication:
    'proxy_url': 'http://KEy2hn:YJzsyg@186.65.115.105:9425/',
    'connect_timeout' : 60,
    'read_timeout' : 60
}

# ReplyKeyboardMarkup

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я SlovoNinza Bot! Добро пожаловать, для навигации используй меню и свой мозг, удачи!", reply_markup=get_main_keyboard())
    #context.bot.message.reply_text('Здравствуйте, {}! \nПоговорите со мной {}!'
    #                       .format(bot.message.chat.first_name, smile), reply_markup=get_keyboard())  # отправляем ответ


def echo(update, context):
    ####
    #### ФЯ Меню
    ####
    if update.message.text == 'Описание фокусов':
        print('Вывод ФЯ ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_MENU = True

    if update.message.text == 'Намерение':
        print('Вывод фя намерение ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_1_MENU = True

    if update.message.text == 'Переопредление':
        print('Переопредление ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_2_MENU = True

    if update.message.text == 'Последствие':
        print('Последствие ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_3_MENU = True

    if update.message.text == 'Разделение':
        print('Разделение ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_4_MENU = True

    if update.message.text == 'Объединение':
        print('Объединение ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_5_MENU = True

    if update.message.text == 'Аналогия':
        print('Аналогия ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_6_MENU = True

    if update.message.text == 'ИРФ':
        print('ИРФ ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_7_MENU = True

    if update.message.text == 'Другой результат':
        print('Другой результат ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_8_MENU = True

    if update.message.text == 'Модель мира':
        print('Модель мира ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_9_MENU = True

    if update.message.text == 'Стратегия реальности':
        print('Стратегия реальности ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_10_MENU = True

    if update.message.text == 'Противоположный пример':
        print('Противоположный пример ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_11_MENU = True

    if update.message.text == 'Ирархия критериев':
        print('Ирархия критериев ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_12_MENU = True

    if update.message.text == 'Применение к себе':
        print('Применение к себе ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_13_MENU = True

    if update.message.text == 'Метафрейм':
        print('Метафрейм ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_14_MENU = True


    ####
    #### Способы применения
    ####

    if update.message.text == 'Способы применения':
        print('Вывод ФЯ ', update)
        thread.bot_updater(update, context)
        settings.SHOW_SPOSOB_MENU = True

    if update.message.text == 'Гуманистическое':
        print('Гуманистическое ', update)
        thread.bot_updater(update, context)
        settings.SHOW_SPOSOB_GUM_MENU = True

    if update.message.text == 'Гуру':
        print('Гуру ', update)
        thread.bot_updater(update, context)
        settings.SHOW_SPOSOB_GYRY_MENU = True

    if update.message.text == 'Провокативное':
        print('Провокативное ', update)
        thread.bot_updater(update, context)
        settings.SHOW_SPOSOB_PROV_MENU = True

    if update.message.text == 'Боевое':
        print('Боевое ', update)
        thread.bot_updater(update, context)
        settings.SHOW_SPOSOB_BOE_MENU = True

    ####
    #### Игра по фя
    ####

    if update.message.text == 'Игра по фя':
        thread.bot_updater(update, context)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Раздел в разработке")

    ####
    #### Убеждения
    ####

    if update.message.text == 'Убеждения':
        thread.bot_updater(update, context)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Раздел в разработке")

    if update.message.text == 'Назад к списку ФЯ':
        print('Список ФЯ ', update)
        thread.bot_updater(update, context)
        settings.SHOW_FY_MENU = True

    if update.message.text == 'Назад на главную':
        print('Главное меню ', update)
        thread.bot_updater(update, context)
        settings.SHOW_MAIN_MENU = True


def last_data(update, context):
    text = 'Последние данные'
    print(text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)




if __name__ == '__main__':

    # запускаем поток для обработки свежих данных с основной программы
    thread = ThreadData()
    thread.start()

    # бот телега
    # updater = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS, use_context=True)
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
