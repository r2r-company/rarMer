import os
import django
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rarMer.settings')
django.setup()

from zapravka.models import Cartridge


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = requests.get('http://127.0.0.1:8000/zapravka/list_cartridges/')
        response.raise_for_status()  # Перевіряє, чи запит був успішним
        data = response.json()

        if 'message' in data:
            await update.message.reply_text(data['message'])
        else:
            cartridges = data
            keyboard = [
                [InlineKeyboardButton(f"{cartridge['name']} - {cartridge['number']}",
                                      callback_data=f"confirm_change_{cartridge['id']}")]
                for cartridge in cartridges
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text('Список порожніх картриджів:', reply_markup=reply_markup)
    except requests.exceptions.RequestException as e:
        await update.message.reply_text(f'HTTP Error: {e}')
    except ValueError as e:
        await update.message.reply_text(f'Error decoding JSON: {e}')


async def confirm_change(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    cartridge_id = query.data.split('_')[-1]
    keyboard = [
        [InlineKeyboardButton("Так", callback_data=f"change_status_{cartridge_id}")],
        [InlineKeyboardButton("Ні", callback_data="cancel")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text="Ви впевнені, що хочете змінити статус цього картриджа?",
                                  reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "cancel":
        await query.edit_message_text(text="Зміна статусу скасована.")
    else:
        cartridge_id = query.data.split('_')[-1]
        response = requests.post(f'http://127.0.0.1:8000/zapravka/change_status_from_telegram/{cartridge_id}/')
        if response.json().get('success'):
            await query.edit_message_text(text=f"Статус картриджа {cartridge_id} змінено на 'Заправлений'")
        else:
            await query.edit_message_text(text=f"Не вдалося змінити статус картриджа {cartridge_id}")


app = ApplicationBuilder().token("7451278791:AAG7UXvPEJeMJENhhasiaxYnv8oaS8mPCRo").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(confirm_change, pattern='confirm_change_'))
app.add_handler(CallbackQueryHandler(button, pattern='change_status_'))
app.add_handler(CallbackQueryHandler(button, pattern='cancel'))

app.run_polling()
