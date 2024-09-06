from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment, Site, TariffPlan

@receiver(post_save, sender=Payment)
def update_expiration_dates(sender, instance, **kwargs):
    """
    Сигнал для оновлення полів Дата закінчення у таблицях Сайти та Тарифний план
    при збереженні Оплати.
    """
    # Оновлюємо дату закінчення у пов'язаному сайті
    site = instance.site
    site.expiration_date = instance.expiration_date
    site.save()

    # Оновлюємо дату закінчення у пов'язаному тарифному плані
    tariff_plan = site.tariff_plan
    if tariff_plan:
        tariff_plan.expiration_date = instance.expiration_date
        tariff_plan.save()
