import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import django

# Установіть змінну середовища для налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rarMer.settings')
django.setup()

# Змінні для Telegram бота і URL API вашого Django серверу
BOT_TOKEN = '6773354730:AAE8jlpfanpabHzqyot0iFWYY_7BTrhBOT8'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Say Hi", callback_data="say_hi"))
    await message.reply("Welcome! Click the button below:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'say_hi')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Привіт!')

if __name__ == '__main__':
    start_polling(dp, skip_updates=True)
