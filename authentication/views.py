from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import ldap3
from ldap3.core.exceptions import LDAPException
from rarMer import settings

def login_view(request):
    ad_users = []
    try:
        server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI)
        conn = ldap3.Connection(server, user=settings.AUTH_LDAP_BIND_DN, password=settings.AUTH_LDAP_BIND_PASSWORD, auto_bind=True)
        print("Connected to LDAP server:", conn.bind())
        conn.search(settings.AUTH_LDAP_SEARCH_BASE, '(objectClass=person)', attributes=['sAMAccountName'])
        print("LDAP search response:", conn.response)
        for entry in conn.entries:
            ad_users.append({
                'username': entry.sAMAccountName.value,
            })
        print("AD Users:", ad_users)  # Друк користувачів з AD
    except LDAPException as e:
        print("LDAPException:", str(e))  # Друк повідомлення про помилку

    if request.method == 'POST':
        form = LoginForm(request.POST, ad_users=ad_users)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Змініть на вашу URL назву для домашньої сторінки
            else:
                form.add_error(None, 'Невірні облікові дані')
    else:
        form = LoginForm(ad_users=ad_users)
        print("Form Choices:", form.fields['username'].choices)  # Друк виборів у формі

    print("Rendering form with users:", ad_users)  # Друк користувачів перед рендерингом шаблону
    return render(request, 'registration/login.html', {'form': form, 'ad_users': ad_users})
