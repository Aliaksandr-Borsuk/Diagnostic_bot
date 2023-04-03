from aiogram import Router
from aiogram.types import Message

router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
# TODO ################################## to English
@router.message()
async def send_echo(message: Message):
    await message.reply(
        f"Unfortunately, I don't understand this message...\n" +\
        "Для отзыва отправьте сообщение со словом feedback в начале. Образец:\n" +\
        "feedback тут текст отзыва."
        )
