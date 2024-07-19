from django import forms
from equipment.models import EquipmentTransfer, EquipmentWriteOff

from .models import Task, TaskComment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'due_date', 'assigned_to', 'priority']
        labels = {
            'name': 'Назва',
            'description': 'Опис',
            'status': 'Статус',
            'due_date': 'Кінцевий термін',
            'assigned_to': 'Призначено',
            'priority': 'Пріоритет',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        }

class TaskCommentForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['task', 'user', 'comment_text']
        labels = {
            'task': 'Завдання',
            'user': 'Користувач',
            'comment_text': 'Текст коментаря',
        }


class EquipmentTransferForm(forms.ModelForm):
    task = forms.ModelChoiceField(
        queryset=Task.objects.filter(status='В процесі'),
        required=False,
        label='На основі задачі'
    )

    class Meta:
        model = EquipmentTransfer
        fields = ['inventory', 'to_department', 'to_employee', 'task']
        labels = {
            'inventory': 'Запас',
            'to_department': 'Новий підрозділ',
            'to_employee': 'Новий працівник',
            'task': 'На основі задачі',
        }


class EquipmentWriteOffForm(forms.ModelForm):
    task = forms.ModelChoiceField(
        queryset=Task.objects.filter(status='В процесі'),
        required=False,
        label='На основі задачі'
    )

    class Meta:
        model = EquipmentWriteOff
        fields = ['inventory', 'reason', 'task']
        labels = {
            'inventory': 'Запас',
            'reason': 'Причина',
            'task': 'На основі задачі',
        }


