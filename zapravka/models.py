from django.db import models
from companies.models import Company, Department
from workers.models import Worker

class Cartridge(models.Model):
    STATUS_CHOICES = [
        ('Заправлений', 'Заправлений'),
        ('Порожній', 'Порожній'),
    ]

    name = models.CharField(max_length=255, verbose_name='Назва картриджа')
    number = models.IntegerField(verbose_name='№ картриджа')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Заправлений', verbose_name='Статус')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компанія')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Підрозділ')
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Працівник')

    def __str__(self):
        return f'{self.name} ({self.number}) - {self.status}'
