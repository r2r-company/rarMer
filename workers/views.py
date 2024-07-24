import ldap3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from equipment.models import EquipmentInventory
from ldap3.core.exceptions import LDAPException
from rarMer import settings
from workers.form import WorkerForm
from django import forms

from .models import Worker
from django.shortcuts import render
from django.core.exceptions import PermissionDenied


def admin_only(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)
    return wrap

def worker_list(request):
    workers = Worker.objects.all()

    context = {
        'workers': workers,
    }
    return render(request, 'worker/worker_list.html', context)

@login_required
def profile_view(request):
    try:
        worker = Worker.objects.get(user=request.user)
        equipment_list = EquipmentInventory.objects.filter(employee=worker)

        context = {
            'worker': worker,
            'equipment_list': equipment_list,
        }

        return render(request, 'worker/profile.html', context)
    except Worker.DoesNotExist:
        return redirect('create_profile')  # Замість 'create_profile' вкажіть вашу URL назву для створення профілю
@admin_only
def get_ad_users(request):
    try:
        server = ldap3.Server(settings.AUTH_LDAP_SERVER_URI)
        conn = ldap3.Connection(server, user=settings.AUTH_LDAP_BIND_DN, password=settings.AUTH_LDAP_BIND_PASSWORD, auto_bind=True)
        conn.search(settings.AUTH_LDAP_SEARCH_BASE, '(objectClass=person)', attributes=['sAMAccountName', 'givenName', 'sn', 'mail'])

        users = []
        for entry in conn.entries:
            users.append({
                'username': entry.sAMAccountName.value,
                'first_name': entry.givenName.value,
                'last_name': entry.sn.value,
                'email': entry.mail.value,
            })

        return render(request, 'worker/ad_users.html', {'users': users, 'error': None})

    except LDAPException as e:
        error_message = "Немає з'єднання з Active Directory"
        return render(request, 'worker/ad_users.html', {'users': [], 'error': error_message})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user
            worker.save()
            return redirect('profile')
    else:
        form = WorkerForm()

    return render(request, 'worker/create_profile.html', {'form': form})
