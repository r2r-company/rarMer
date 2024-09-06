from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    tariff_plan = models.ForeignKey('TariffPlan', on_delete=models.SET_NULL, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        # Повертає назву сайту як представлення об'єкта
        return self.name

class TariffPlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField(null=True, blank=True)

class Payment(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
