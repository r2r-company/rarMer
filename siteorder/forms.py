from django import forms
from .models import Site, TariffPlan, Payment

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url', 'login', 'password', 'email', 'tariff_plan', 'expiration_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'login': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tariff_plan': forms.Select(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'name': 'Назва сайту',
            'url': 'Посилання',
            'login': 'Логін',
            'password': 'Пароль',
            'email': 'Електронна пошта',
            'tariff_plan': 'Тарифний план',
            'expiration_date': 'Дата закінчення',
        }


class TariffPlanForm(forms.ModelForm):
    class Meta:
        model = TariffPlan
        fields = ['name', 'price', 'expiration_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['site', 'payment_date', 'amount', 'expiration_date']
        widgets = {
            'site': forms.Select(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'site': 'Сайт',
            'payment_date': 'Дата оплати',
            'amount': 'Сума',
            'expiration_date': 'Дата закінчення',
        }
