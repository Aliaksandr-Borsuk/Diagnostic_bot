from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_en import LEXICON


def create_symptoms_keyboard(*args: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons = [InlineKeyboardButton(
            text=f"{button.replace('_', ' ')} ",
            callback_data=str(button)) for button in args]
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=2)

    # Добавляем в билдер ряд с кнопками
    kb_builder.row(
        InlineKeyboardButton(
                text=LEXICON['backward'], callback_data='backward'
                ),
        # InlineKeyboardButton(
        #         text=LEXICON['show_symptoms'], callback_data='show_symptoms'
        #         ),
        InlineKeyboardButton(
                text=LEXICON['forward'], callback_data='forward'
                ),
        )

    # Добавляем в клавиатуру в конце кнопку "get_diagnosis"
    kb_builder.row(InlineKeyboardButton(
                        text=LEXICON['get_diagnosis'],
                        callback_data='get_diagnosis'))

    return kb_builder.as_markup()


# Создаем объект инлайн-клавиатуры к сообщению с диагнозами
def create_diagnosis_keyboard(*args: list[list[str]]) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons = [InlineKeyboardButton(
            text = diagn [0] + "   " + diagn[1],
            callback_data = diagn[0]
            ) for diagn  in args]
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=1)
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(
        InlineKeyboardButton(
                text=LEXICON['return_to_symptoms'],
                callback_data='return_to_symptoms'
                ),
        InlineKeyboardButton(
                text=LEXICON['repeat_diagnostic'],
                callback_data='repeat_diagnostic'
                ),
        )
    return kb_builder.as_markup()
