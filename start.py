from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def start(message: types.Message, state: FSMContext):
    keyboard = InlineKeyboardMarkup()
    Latin = InlineKeyboardButton("Латиница", callback_data='Latin')
    Cyrillic = InlineKeyboardButton('Кириллица', callback_data='Cyrillic')
    keyboard.add(Latin, Cyrillic)
    await message.answer("Привет! Я бот который может перевести текст в азбука морзу. Выберите пожалуйста язык, который хотите перевести на азбука морзу", reply_markup=keyboard)