from django import forms

class LoginForm(forms.Form):
    username = forms.ChoiceField(label="Ім'я користувача", widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Пароль")

    def __init__(self, *args, **kwargs):
        ad_users = kwargs.pop('ad_users', [])
        super().__init__(*args, **kwargs)
        self.fields['username'].choices = [(user['username'], user['username']) for user in ad_users]
