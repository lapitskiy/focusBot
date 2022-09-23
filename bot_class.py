#
# поток связанный с ботом
#
from bot_settings import settings
import threading
from bot_func import *



class ThreadData(threading.Thread):
    """StartTrade"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.update = None
        self.context = None


    def run(self):
        self.start_thread()

    def start_thread(self):
        while True:
            if settings.SHOW_MAIN_MENU: # меню ФЯ
                settings.SHOW_MAIN_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Я SlovoNinza Bot! Главное меню!",
                                         reply_markup=get_main_keyboard())


            if settings.SHOW_FY_MENU: # меню ФЯ
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Я SlovoNinza Bot! Выберете ФЯ для изучения!",
                                         reply_markup=get_fy_keyboard())
                settings.SHOW_FY_MENU = False

            if settings.SHOW_FY_1_MENU: # меню ФЯ намерение
                settings.SHOW_FY_1_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю намерение...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy1.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_2_MENU: # меню ФЯ 2
                settings.SHOW_FY_2_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю переопределение...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy2.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_3_MENU: # меню ФЯ 3
                settings.SHOW_FY_3_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю последствие...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy3.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_4_MENU: # меню ФЯ 4
                settings.SHOW_FY_4_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю разделение...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy4.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_5_MENU: # меню ФЯ 5
                settings.SHOW_FY_5_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю объединение...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy5.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_6_MENU: # меню ФЯ 6
                settings.SHOW_FY_6_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю аналогию...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy6.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_7_MENU: # меню ФЯ 7
                settings.SHOW_FY_7_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю ирф...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy7.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_8_MENU: # меню ФЯ 7
                settings.SHOW_FY_8_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю др...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy8.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_9_MENU: # меню ФЯ 9
                settings.SHOW_FY_9_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю мм...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy9.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_10_MENU: # меню ФЯ 10
                settings.SHOW_FY_10_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю ср...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy10.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_11_MENU: # меню ФЯ 11
                settings.SHOW_FY_11_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю пп...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy11.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_12_MENU: # меню ФЯ 12
                settings.SHOW_FY_12_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю ик...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy12.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_13_MENU: # меню ФЯ 13
                settings.SHOW_FY_13_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю пс...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy13.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_FY_14_MENU: # меню ФЯ 14
                settings.SHOW_FY_14_MENU = False
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Загружаю мф...",
                                         reply_markup=get_fy_1_keyboard())
                with open('data/fy14.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            ###
            ###  СПОСОБЫ ПРИМЕНЕНИЯ
            ###
            if settings.SHOW_SPOSOB_MENU:
                self.context.bot.send_message(chat_id=self.update.effective_chat.id, text="Я SlovoNinza Bot! Выберете способ приминения!",
                                         reply_markup=get_spos_keyboard())
                settings.SHOW_SPOSOB_MENU = False

            if settings.SHOW_SPOSOB_GUM_MENU:
                settings.SHOW_SPOSOB_GUM_MENU = False
                with open('data/spos/gum.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')


            if settings.SHOW_SPOSOB_GYRY_MENU:
                settings.SHOW_SPOSOB_GYRY_MENU = False
                with open('data/spos/gyry.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_SPOSOB_PROV_MENU:
                settings.SHOW_SPOSOB_PROV_MENU = False
                with open('data/spos/prov.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')

            if settings.SHOW_SPOSOB_BOE_MENU:
                with open('data/spos/boe.txt', 'r', encoding='utf-8') as file:
                    content = file.read()

                if len(content) > 4096:
                    for x in range(0, len(content), 4096):
                        self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content[x:x + 4096], parse_mode='html')
                else:
                    self.context.bot.send_message(chat_id=self.update.effective_chat.id, text=content, parse_mode='html')
                settings.SHOW_SPOSOB_BOE_MENU = False


    def bot_updater(self, update, context):
        self.update = update
        self.context = context

