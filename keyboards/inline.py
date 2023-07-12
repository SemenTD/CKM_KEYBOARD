from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cats = InlineKeyboardButton(text="котов",cats = InlineKeyboardButton(text='Котов', url='https://ru.wikipedia.org/wiki/Кошка'))
dogs = InlineKeyboardButton(text="собак",dogs = InlineKeyboardButton(text='Собак', url='https://ru.wikipedia.org/wiki/Собака')
)

cats_dogs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [cats,dogs]


])