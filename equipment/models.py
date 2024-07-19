from django.db import models
from companies.models import Company, Department
from nomenklatyra.models import Product
from workers.models import Worker
from django.apps import apps  # Додати імпорт apps

class EquipmentReceipt(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Номенклатура')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компанія')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Підрозділ')
    employee = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Працівник')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата приходу')
    task = models.ForeignKey('tasks.Task', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='На основі задачі', limit_choices_to={'status': 'В процесі'})

    def __str__(self):
        return f"{self.item.name} (ID: {self.item.id}) from {self.company.name} at {self.date.strftime('%Y-%m-%d')}"

    def get_department_name(self):
        return self.department.name if self.department else 'Без підрозділу'

    def get_employee_username(self):
        return self.employee.user.username if self.employee else 'Без працівника'

    class Meta:
        verbose_name = 'Прихід обладнання'
        verbose_name_plural = 'Приходи обладнання'


class EquipmentInventory(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Номенклатура')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компанія')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Підрозділ')
    employee = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Працівник')
    status = models.CharField(max_length=50, default='Прихід товару', verbose_name='Статус')

    def __str__(self):
        return f'{self.item.name} (ID: {self.item.id}) - {self.department.name if self.department else "Без підрозділу"}: {self.status}'

    def get_department_name(self):
        return self.department.name if self.department else 'Без підрозділу'

    def get_employee_username(self):
        return self.employee.user.username if self.employee else 'Без працівника'

    class Meta:
        verbose_name = 'Запас обладнання'
        verbose_name_plural = 'Запаси обладнання'


class EquipmentTransfer(models.Model):
    inventory = models.ForeignKey(EquipmentInventory, on_delete=models.CASCADE, verbose_name='Запас')
    to_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Новий підрозділ')
    to_employee = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Новий працівник')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата переміщення')
    task = models.ForeignKey('tasks.Task', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='На основі задачі', limit_choices_to={'status': 'В процесі'})

    def __str__(self):
        return f"Переміщення {self.inventory.item.name} (ID: {self.inventory.item.id}) до {self.get_to_department_name()}"

    def get_to_department_name(self):
        return self.to_department.name if self.to_department else 'Без підрозділу'

    def get_to_employee_username(self):
        return self.to_employee.user.username if self.to_employee else 'Без працівника'

    class Meta:
        verbose_name = 'Переміщення обладнання'
        verbose_name_plural = 'Переміщення обладнання'


class EquipmentWriteOff(models.Model):
    inventory = models.ForeignKey(EquipmentInventory, on_delete=models.CASCADE, verbose_name='Запас')
    reason = models.TextField(verbose_name='Причина списання')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата списання')
    task = models.ForeignKey('tasks.Task', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='На основі задачі', limit_choices_to={'status': 'В процесі'})

    def __str__(self):
        return f"Списання {self.inventory.item.name} (ID: {self.inventory.item.id}) через {self.reason}"

    def get_department_name(self):
        return self.inventory.department.name if self.inventory.department else 'Без підрозділу'

    def get_employee_username(self):
        return self.inventory.employee.user.username if self.inventory.employee else 'Без працівника'

    class Meta:
        verbose_name = 'Списання обладнання'
        verbose_name_plural = 'Списання обладнання'
