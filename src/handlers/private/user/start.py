from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command(commands=['start']))
async def on_start(message: types.Message):
    text = 'Привет пользователь'
    await message.answer(text)
