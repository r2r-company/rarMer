from django import forms
from .models import Worker

class WorkerForm(forms.ModelForm):
    hire_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Worker
        fields = ['company', 'department', 'hire_date']