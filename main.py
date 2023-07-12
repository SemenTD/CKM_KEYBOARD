import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message ,CallbackQuery, ContentType  # Тип сообщения
from keyboards.inline import cats_dogs_keyboard


from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!Кого ты больше любишь?:", reply_markup=cats_dogs_keyboard)  # Отвечаем на полученное сообщени
@dp.callback_query()
async def handle_cats(query:CallbackQuery):
    await query.answer(f"Вы нажали кнопку с callblak-data:{query.data}")

@dp.message()
async def echo_all(message:Message):
    await message.send_copy(message.chat.id)

async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
