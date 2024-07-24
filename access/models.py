from django.contrib.auth.models import User
from django.db import models

class Access(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва")
    ip = models.GenericIPAddressField(verbose_name="IP", blank=True, null=True)
    gw = models.GenericIPAddressField(verbose_name="GW", blank=True, null=True)
    mask = models.GenericIPAddressField(verbose_name="Mask", blank=True, null=True)
    dns = models.GenericIPAddressField(verbose_name="DNS", blank=True, null=True)
    login = models.CharField(max_length=255, verbose_name="Логін", blank=True, null=True)
    password = models.CharField(max_length=255, verbose_name="Пароль", blank=True, null=True)
    ipsec = models.CharField(max_length=255, verbose_name="IPsec", blank=True, null=True)
    site = models.CharField(max_length=255, verbose_name="Site", blank=True, null=True)
    additional_info = models.TextField(verbose_name="Додатково", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Доступ"
        verbose_name_plural = "Доступи"