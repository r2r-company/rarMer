from django.db import models
from django.contrib.auth.models import User
from equipment.models import EquipmentInventory
from django.utils import timezone

class Task(models.Model):
    task_number = models.CharField(max_length=20, unique=True, verbose_name='Номер завдання')
    name = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(verbose_name='Опис')
    status = models.CharField(max_length=50, choices=[('Новий', 'Новий'), ('В процесі', 'В процесі'), ('Завершено', 'Завершено')], default='Новий', verbose_name='Статус')
    due_date = models.DateField(verbose_name='Кінцевий термін', null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Призначено')
    priority = models.CharField(max_length=50, choices=[('Високий', 'Високий'), ('Середній', 'Середній'), ('Низький', 'Низький')], default='Середній', verbose_name='Пріоритет')
    equipment = models.ForeignKey(EquipmentInventory, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Обладнання')
    created_by = models.ForeignKey(User, related_name='created_tasks', on_delete=models.CASCADE, verbose_name='Створено')

    def save(self, *args, **kwargs):
        if not self.task_number:
            self.task_number = self.generate_task_number()
        super().save(*args, **kwargs)

    def generate_task_number(self):
        return f"TASK-{timezone.now().strftime('%Y%m%d%H%M%S')}"

    def task_display(self):
        return f"{self.name} ({self.task_number}) - Поставив: {self.created_by.username}, Виконавець: {self.assigned_to.username}, Дата виконання: {self.due_date}"

    def __str__(self):
        return self.name

class TaskComment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.name}'
