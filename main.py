from config import key
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from start import start
import input
import translate

API_TOKEN = key


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
class ABCMorse(StatesGroup):
    CyrillicST = State()
    LatinST = State()

@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    await start(message, state=None)
@dp.callback_query_handler(text = 'Cyrillic')
async def cyr(callback_query: types.CallbackQuery, state: FSMContext):
    await input.Cyrillic(callback_query, state)
@dp.callback_query_handler(text = 'Latin')
async def lat(callback_query: types.CallbackQuery, state: FSMContext):
    await input.Latin(callback_query, state)
@dp.message_handler(content_types=types.ContentType.TEXT, state=ABCMorse.CyrillicST)
async def CyrTranslate(message: types.Message, state: FSMContext):
    await translate.ABCMorseCResult(message, state)
@dp.message_handler(content_types=types.ContentType.TEXT, state=ABCMorse.LatinST)
async def LatTranslate(message: types.Message, state: FSMContext):
    await translate.ABCMorseLResult(message, state)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)