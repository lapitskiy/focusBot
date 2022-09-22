from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton

# функция создает клавиатуру и ее разметку
def get_main_keyboard():
    CALLBACK_BUTTON_DATA = "Описание фокусов"
    CALLBACK_BUTTON_DATA_EXIT = "Способы применения"
    CALLBACK_BUTTON_EXIT_BIRGA = "Игра по фя"
    CALLBACK_BUTTON_EXIT_MARGA = "Убеждения"
    #contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    #location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([[CALLBACK_BUTTON_DATA,CALLBACK_BUTTON_DATA_EXIT],
                                       [CALLBACK_BUTTON_EXIT_BIRGA, CALLBACK_BUTTON_EXIT_MARGA],
                                       ], resize_keyboard=True)  # добавляем кнопки
    return my_keyboard

# функция создает клавиатуру и ее разметку
def get_fy_keyboard():
    CALLBACK_BUTTON_1 = "Намерение"
    CALLBACK_BUTTON_2 = "Переопредление"
    CALLBACK_BUTTON_3 = "Последствие"
    CALLBACK_BUTTON_4 = "Разделение"
    CALLBACK_BUTTON_5 = "Объединение"
    CALLBACK_BUTTON_6 = "Аналогия"
    CALLBACK_BUTTON_7 = "ИРФ"
    CALLBACK_BUTTON_8 = "Другой результат"
    CALLBACK_BUTTON_9 = "Модель мира"
    CALLBACK_BUTTON_10 = "Стратегия реальности"
    CALLBACK_BUTTON_11 = "Противоположный пример"
    CALLBACK_BUTTON_12 = "Ирархия критериев"
    CALLBACK_BUTTON_13 = "Применение к себе"
    CALLBACK_BUTTON_14 = "Метафрейм"
    CALLBACK_BUTTON_15 = "Назад на главную"


    # contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    # location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([[CALLBACK_BUTTON_1, CALLBACK_BUTTON_2],
                                       [CALLBACK_BUTTON_3, CALLBACK_BUTTON_4],
                                       [CALLBACK_BUTTON_5, CALLBACK_BUTTON_6],
                                       [CALLBACK_BUTTON_7, CALLBACK_BUTTON_8],
                                       [CALLBACK_BUTTON_9, CALLBACK_BUTTON_10],
                                       [CALLBACK_BUTTON_11, CALLBACK_BUTTON_12],
                                       [CALLBACK_BUTTON_13, CALLBACK_BUTTON_14],
                                       [CALLBACK_BUTTON_15],
                                       ], resize_keyboard=True)  # добавляем кнопки
    return my_keyboard



# функция создает клавиатуру и ее разметку
def get_fy_1_keyboard():
    CALLBACK_BUTTON_1 = "Назад к списку ФЯ"
    CALLBACK_BUTTON_2 = "Назад на главную"

    # contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    # location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([[CALLBACK_BUTTON_1, CALLBACK_BUTTON_2],
                                       ], resize_keyboard=True)  # добавляем кнопки
    return my_keyboard


# функция создает клавиатуру для способов приминения
def get_spos_keyboard():
    CALLBACK_BUTTON_1 = "Гуманистическое"
    CALLBACK_BUTTON_2 = "Гуру"
    CALLBACK_BUTTON_3 = "Провокативное"
    CALLBACK_BUTTON_4 = "Боевое"
    CALLBACK_BUTTON_15 = "Назад на главную"


    # contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    # location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([[CALLBACK_BUTTON_1, CALLBACK_BUTTON_2],
                                       [CALLBACK_BUTTON_3, CALLBACK_BUTTON_4],
                                       [CALLBACK_BUTTON_15],
                                       ], resize_keyboard=True)  # добавляем кнопки
    return my_keyboard
