from companies.models import Department, Company
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Access
from .forms import AccessForm
from django.core.exceptions import PermissionDenied




def admin_only(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return function(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)
    return wrap

@admin_only
def access_list(request):
    company_id = request.GET.get('company')
    department_id = request.GET.get('department')
    user_id = request.GET.get('user')

    companies = Company.objects.all()
    departments = Department.objects.filter(company_id=company_id) if company_id else Department.objects.all()
    users = User.objects.filter(userprofile__department_id=department_id) if department_id else User.objects.all()

    accesses = Access.objects.all()
    if user_id:
        accesses = accesses.filter(user_id=user_id)
    elif department_id:
        accesses = accesses.filter(user__userprofile__department_id=department_id)
    elif company_id:
        accesses = accesses.filter(user__userprofile__department__company_id=company_id)

    return render(request, 'access/access_list.html', {
        'accesses': accesses,
        'companies': companies,
        'departments': departments,
        'users': users,
        'selected_company': int(company_id) if company_id else None,
        'selected_department': int(department_id) if department_id else None,
        'selected_user': int(user_id) if user_id else None,
    })

def access_add(request):
    if request.method == 'POST':
        form = AccessForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access_list')
    else:
        form = AccessForm()
    return render(request, 'access/access_form.html', {'form': form})

def access_edit(request, pk):
    access = get_object_or_404(Access, pk=pk)
    if request.method == 'POST':
        form = AccessForm(request.POST, instance=access)
        if form.is_valid():
            form.save()
            return redirect('access_list')
    else:
        form = AccessForm(instance=access)
    return render(request, 'access/access_form.html', {'form': form})

def access_delete(request, pk):
    access = get_object_or_404(Access, pk=pk)
    if request.method == 'POST':
        access.delete()
        return redirect('access_list')
    return render(request, 'access/access_confirm_delete.html', {'access': access})


def get_departments(request):
    company_id = request.GET.get('company')
    departments = Department.objects.filter(company_id=company_id)
    data = {'departments': list(departments.values('id', 'name'))}
    return JsonResponse(data)

def get_users(request):
    department_id = request.GET.get('department')
    users = User.objects.filter(userprofile__department_id=department_id)
    data = {'users': list(users.values('id', 'username'))}
    return JsonResponse(data)