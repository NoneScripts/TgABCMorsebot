from aiogram import types
from aiogram.dispatcher import FSMContext
from ABC import Cyrillic_ListMorse, Latin_ListABCMorse

async def ABCMorseCResult(message: types.Message, state: FSMContext):
    translate = message.text
    try:
        result = ' '.join(Cyrillic_ListMorse.get(m.upper()) for m in translate)
        await message.reply(result)
        await state.finish()
    except:
        await message.reply('Это не кириллица! Либо в этом тексте присутствуют не понятные символы')
        await state.finish()

async def ABCMorseLResult(message: types.Message, state: FSMContext):
    translate = message.text
    try:
        result = ' '.join(Latin_ListABCMorse.get(m.upper()) for m in translate)
        await message.reply(result)
        await state.finish()
    except TypeError:
        await message.reply('Это не латыня! Либо в этом тексте присутствуют не понятные символы')
        await state.finish()