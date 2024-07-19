from companies.models import Company, Department
from django import forms

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['company', 'name']

