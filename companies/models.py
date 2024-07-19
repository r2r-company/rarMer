from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва компанії")
    address = models.CharField(max_length=255, verbose_name="Адреса")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компанія"
        verbose_name_plural = "Компанії"

class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE, verbose_name="Компанія")
    name = models.CharField(max_length=255, verbose_name="Назва підрозділу")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)

    def __str__(self):
        return f'{self.name} ({self.company.name})'

    class Meta:
        verbose_name = "Підрозділ"
        verbose_name_plural = "Підрозділи"


