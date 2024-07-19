from companies.models import Company, Department
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from nomenklatyra.models import Product


class Worker(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Користувач")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компанія")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Підрозділ")
    position = models.CharField(max_length=100, verbose_name="Позиція")  # Додаємо позицію
    hire_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.department.name if self.department else 'Немає підрозділу'}"


class Equipment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва обладнання")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, related_name='equipment', verbose_name="Працівник")

    def __str__(self):
        return self.name