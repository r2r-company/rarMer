from companies.models import Company, Department
from django import forms
from tasks.models import Task
from workers.models import Worker

from .models import EquipmentInventory, EquipmentReceipt, EquipmentTransfer, EquipmentWriteOff

class EquipmentInventoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentInventory
        fields = ['item', 'company', 'department', 'employee', 'status']


class EquipmentReceiptForm(forms.ModelForm):
    class Meta:
        model = EquipmentReceipt
        fields = ['item', 'company', 'department', 'employee', 'task']
        labels = {
            'item': 'Номенклатура',
            'company': 'Компанія',
            'department': 'Підрозділ',
            'employee': 'Працівник',
            'task': 'На основі задачі',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task'].queryset = self.fields['task'].queryset.filter(status='В процесі')
        self.fields['task'].label_from_instance = lambda obj: obj.task_display()
        self.fields['department'].queryset = Department.objects.none()
        self.fields['employee'].queryset = Worker.objects.none()

        if 'company' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['department'].queryset = Department.objects.filter(company_id=company_id)
            except (ValueError, TypeError):
                pass

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['employee'].queryset = Worker.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass

        if self.instance.pk:
            self.fields['department'].queryset = self.instance.company.department_set.all()
            self.fields['employee'].queryset = self.instance.department.worker_set.all()

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task'].queryset = self.fields['task'].queryset.filter(status='В процесі')
        self.fields['task'].label_from_instance = lambda obj: obj.task_display()

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
            'reason': 'Причина списання',
            'task': 'На основі задачі',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task'].queryset = self.fields['task'].queryset.filter(status='В процесі')
        self.fields['task'].label_from_instance = lambda obj: obj.task_display()


class ReportFilterForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), required=False, label='Компанія')
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=False, label='Підрозділ')
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата з')
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата по')