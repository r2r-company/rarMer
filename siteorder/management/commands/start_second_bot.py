from django.core.management.base import BaseCommand
from siteorder.second_telegram_bot import main_second_bot

class Command(BaseCommand):
    help = 'Запускає другого Telegram-бота'

    def handle(self, *args, **kwargs):
        print("Запуск другого Telegram-бота...")
        main_second_bot()
