from aiogram import types
from main import bot
from main import ABCMorse
from aiogram.dispatcher import FSMContext

async def Cyrillic(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите пожалуйста текст")
    await state.set_state(ABCMorse.CyrillicST)

async def Latin(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите пожалуйста текст")
    await state.set_state(ABCMorse.LatinST)