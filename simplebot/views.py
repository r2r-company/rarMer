from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler, Dispatcher
import json

TOKEN = '7451278791:AAG7UXvPEJeMJENhhasiaxYnv8oaS8mPCRo'

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        update = Update.de_json(json.loads(request.body), None)
        dispatcher.process_update(update)
        return JsonResponse({"status": "ok"})
    return JsonResponse({"error": "Invalid request method"}, status=405)

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Say Hi", callback_data='hi')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome! Click the button below:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'hi':
        query.edit_message_text(text="Привіт!")

dispatcher = Dispatcher(None, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button))
