from aiogram import types, Dispatcher

async def start(message: types.Message):
    await message.answer("Hello! This is a test bot.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
