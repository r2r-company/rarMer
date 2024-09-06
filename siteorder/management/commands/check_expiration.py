from django.core.management.base import BaseCommand
from django.utils import timezone
from siteorder.models import Site
from siteorder.second_telegram_bot import notify_users_second_bot  # Використайте вашу функцію для надсилання повідомлень

class Command(BaseCommand):
    help = 'Перевіряє дати закінчення сайтів і надсилає сповіщення, якщо залишилось менше 7 днів'

    def handle(self, *args, **kwargs):
        today = timezone.now().date()
        warning_date = today + timezone.timedelta(days=7)

        # Отримати всі сайти, термін дії яких підходить до завершення
        sites_to_notify = Site.objects.filter(expiration_date__lte=warning_date)

        for site in sites_to_notify:
            days_left = (site.expiration_date - today).days
            message = f"Сайт {site.name} ({site.url}) завершується через {days_left} днів. Будь ласка, оновіть тарифний план."
            notify_users_second_bot(message)

        self.stdout.write(self.style.SUCCESS('Перевірка дати закінчення завершена'))
