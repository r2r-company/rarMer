# zapravka/utils.py
import requests
from django.conf import settings

def send_telegram_message(message):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'  # Додаємо parse_mode для форматування повідомлень
    }
    requests.post(url, data=payload)
