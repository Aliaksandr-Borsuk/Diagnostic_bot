from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from lexicon.lexicon_en import LEXICON


# Создаем объекты инлайн-кнопок
big_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Start of diagnostics',
    callback_data='go_diagnostic')


# Создаем объект инлайн-клавиатуры
start_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1]])


# Создаем объекты инлайн-кнопок
button_return_skb: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['return_to_symptoms'],
    callback_data='return_to_symptoms')

button_diagnosis: InlineKeyboardButton = InlineKeyboardButton(
    text='Get diagnosis',
    callback_data='get_diagnosis')

button_return_diagnoses: InlineKeyboardButton = InlineKeyboardButton(
                        text=LEXICON['return_to_diagnoses'],
                        callback_data='get_diagnosis')

# Создаем объект инлайн-клавиатуры для возврата к диагнозам
return_diagnoses_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_return_diagnoses]]
                    )


button_repeat_diagnostic: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['repeat_diagnostic'],
    callback_data='repeat_diagnostic')


# Создаем объекты кнопок
bottom_button_1: KeyboardButton = KeyboardButton(text='/run_diagnostics')
bottom_button_2: KeyboardButton = KeyboardButton(text='/help')

# Создаем объект клавиатуры, добавляя в него кнопки
bottom_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[bottom_button_1]],
                                    resize_keyboard=True,
                                    one_time_keyboard=True
                                    )


