from companies.forms import CompanyForm, DepartmentForm
from companies.models import Company, Department
from django.shortcuts import render, redirect, get_object_or_404


def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companies_list')
    else:
        form = CompanyForm()
    return render(request, 'companies/add_company.html', {'form': form})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companies_list')
    else:
        form = DepartmentForm()
    return render(request, 'companies/add_department.html', {'form': form})

def companies_list(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies_list.html', {'companies': companies})

def subdivisions(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    departments = Department.objects.filter(company=company)
    return render(request, 'companies/subdivisions_list.html', {'company': company, 'departments': departments})