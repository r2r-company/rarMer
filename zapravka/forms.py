from companies.models import Department
from django import forms
from workers.models import Worker

from .models import Cartridge

class CartridgeForm(forms.ModelForm):
    class Meta:
        model = Cartridge
        fields = ['name', 'number', 'status', 'company', 'department', 'worker']
        labels = {
            'name': 'Назва картриджа',
            'number': '№ картриджа',
            'status': 'Статус',
            'company': 'Компанія',
            'department': 'Підрозділ',
            'worker': 'Працівник',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        last_cartridge = Cartridge.objects.all().order_by('number').last()
        if last_cartridge:
            new_number = last_cartridge.number + 1
        else:
            new_number = 1
        self.fields['number'].initial = new_number
        self.fields['number'].widget.attrs['readonly'] = True

        self.fields['department'].queryset = Department.objects.none()
        self.fields['worker'].queryset = Worker.objects.none()

        if 'company' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['department'].queryset = Department.objects.filter(company_id=company_id).order_by('name')
                self.fields['worker'].queryset = Worker.objects.filter(company_id=company_id).order_by('user__last_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.company.department_set.order_by('name')
            self.fields['worker'].queryset = self.instance.department.worker_set.order_by('user__last_name')
