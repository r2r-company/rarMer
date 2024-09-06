from asgiref.sync import sync_to_async
from telegram.ext import Application, CommandHandler
from django.conf import settings
from siteorder.models import Site

async def start(update, context):
    """Асинхронний обробник команди /start для другого бота"""

    # Отримуємо всі сайти, відсортовані за датою закінчення (від найближчої дати до найбільш віддаленої)
    sites = await sync_to_async(list)(Site.objects.filter(expiration_date__isnull=False).order_by('expiration_date'))

    # Формуємо повідомлення з інформацією про всі сайти
    message = "Список сайтів за датою закінчення:\n"
    for site in sites:
        if site.expiration_date:
            message += f"{site.name} ({site.url}) - закінчення {site.expiration_date}\n"
        else:
            message += f"{site.name} ({site.url}) - дата закінчення не встановлена\n"

    # Надсилаємо повідомлення
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def notify_users_second_bot(message):
    """Функція для надсилання повідомлень користувачам від другого бота"""
    chat_id = '5904757949'  # Вкажіть chat ID користувача або групи
    await application.bot.send_message(chat_id=chat_id, text=message)

def main_second_bot():
    """Головна функція для запуску другого бота"""
    global application
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN_SECOND).build()

    # Додайте асинхронний обробник команд для другого бота
    application.add_handler(CommandHandler('start', start))

    # Запуск бота
    application.run_polling()
