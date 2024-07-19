from companies.models import Department
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from workers.models import Worker

from .models import EquipmentInventory, EquipmentReceipt, EquipmentTransfer, EquipmentWriteOff
from .forms import EquipmentInventoryForm, EquipmentReceiptForm, EquipmentTransferForm, EquipmentWriteOffForm, \
    ReportFilterForm


def equipment_inventory_list(request):
    inventory_items = EquipmentInventory.objects.all()
    return render(request, 'equipment/inventory_list.html', {'inventory_items': inventory_items})

def add_equipment_inventory(request):
    if request.method == 'POST':
        form = EquipmentInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_inventory_list')
    else:
        form = EquipmentInventoryForm()
    return render(request, 'equipment/add_inventory.html', {'form': form})

def equipment_receipt_list(request):
    receipt_items = EquipmentReceipt.objects.all()
    return render(request, 'equipment/receipt_list.html', {'receipt_items': receipt_items})

def add_equipment_receipt(request):
    if request.method == 'POST':
        form = EquipmentReceiptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_receipt_list')
    else:
        form = EquipmentReceiptForm()
    return render(request, 'equipment/add_receipt.html', {'form': form})

def equipment_transfer_list(request):
    transfer_items = EquipmentTransfer.objects.all()
    return render(request, 'equipment/transfer_list.html', {'transfer_items': transfer_items})

def add_equipment_transfer(request):
    if request.method == 'POST':
        form = EquipmentTransferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_transfer_list')
    else:
        form = EquipmentTransferForm()
    return render(request, 'equipment/add_transfer.html', {'form': form})

def equipment_writeoff_list(request):
    writeoff_items = EquipmentWriteOff.objects.all()
    return render(request, 'equipment/writeoff_list.html', {'writeoff_items': writeoff_items})

def add_equipment_writeoff(request):
    if request.method == 'POST':
        form = EquipmentWriteOffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_writeoff_list')
    else:
        form = EquipmentWriteOffForm()
    return render(request, 'equipment/add_writeoff.html', {'form': form})



def receipt_report_view(request):
    filter_form = ReportFilterForm(request.GET or None)
    receipts = EquipmentReceipt.objects.all()

    if filter_form.is_valid():
        if filter_form.cleaned_data.get('company'):
            receipts = receipts.filter(company=filter_form.cleaned_data['company'])
        if filter_form.cleaned_data.get('department'):
            receipts = receipts.filter(department=filter_form.cleaned_data['department'])
        if filter_form.cleaned_data.get('date_from'):
            receipts = receipts.filter(date__gte=filter_form.cleaned_data['date_from'])
        if filter_form.cleaned_data.get('date_to'):
            receipts = receipts.filter(date__lte=filter_form.cleaned_data['date_to'])

    return render(request, 'equipment/receipt_report.html', {
        'filter_form': filter_form,
        'receipts': receipts,
    })


def transfer_report_view(request):
    filter_form = ReportFilterForm(request.GET or None)
    transfers = EquipmentTransfer.objects.all()

    if filter_form.is_valid():
        if filter_form.cleaned_data.get('company'):
            transfers = transfers.filter(inventory__company=filter_form.cleaned_data['company'])
        if filter_form.cleaned_data.get('department'):
            transfers = transfers.filter(inventory__department=filter_form.cleaned_data['department'])
        if filter_form.cleaned_data.get('date_from'):
            transfers = transfers.filter(date__gte=filter_form.cleaned_data['date_from'])
        if filter_form.cleaned_data.get('date_to'):
            transfers = transfers.filter(date__lte=filter_form.cleaned_data['date_to'])

    return render(request, 'equipment/transfer_report.html', {
        'filter_form': filter_form,
        'transfers': transfers,
    })


def writeoff_report_view(request):
    filter_form = ReportFilterForm(request.GET or None)
    writeoffs = EquipmentWriteOff.objects.all()

    if filter_form.is_valid():
        if filter_form.cleaned_data.get('company'):
            writeoffs = writeoffs.filter(inventory__company=filter_form.cleaned_data['company'])
        if filter_form.cleaned_data.get('department'):
            writeoffs = writeoffs.filter(inventory__department=filter_form.cleaned_data['department'])
        if filter_form.cleaned_data.get('date_from'):
            writeoffs = writeoffs.filter(date__gte=filter_form.cleaned_data['date_from'])
        if filter_form.cleaned_data.get('date_to'):
            writeoffs = writeoffs.filter(date__lte=filter_form.cleaned_data['date_to'])

    return render(request, 'equipment/writeoff_report.html', {
        'filter_form': filter_form,
        'writeoffs': writeoffs,
    })


def inventory_report_view(request):
    filter_form = ReportFilterForm(request.GET or None)
    inventories = EquipmentInventory.objects.all()

    if filter_form.is_valid():
        if filter_form.cleaned_data.get('company'):
            inventories = inventories.filter(company=filter_form.cleaned_data['company'])
        if filter_form.cleaned_data.get('department'):
            inventories = inventories.filter(department=filter_form.cleaned_data['department'])

    return render(request, 'equipment/inventory_report.html', {
        'filter_form': filter_form,
        'inventories': inventories,
    })


def equipment_documents(request, equipment_id):
    equipment = get_object_or_404(EquipmentInventory, pk=equipment_id)
    receipts = EquipmentReceipt.objects.filter(item=equipment.item)
    transfers = EquipmentTransfer.objects.filter(inventory=equipment)
    writeoffs = EquipmentWriteOff.objects.filter(inventory=equipment)

    context = {
        'equipment': equipment,
        'receipts': receipts,
        'transfers': transfers,
        'writeoffs': writeoffs
    }

    return render(request, 'equipment/equipment_documents.html', context)

def inventory_report(request):
    inventory_items = EquipmentInventory.objects.all()
    context = {'inventory_items': inventory_items}
    return render(request, 'equipment/inventory_report.html', context)


def receipt_report(request):
    receipts = EquipmentReceipt.objects.all()
    context = {'receipts': receipts}
    return render(request, 'equipment/receipt_report.html', context)

def transfer_report(request):
    transfers = EquipmentTransfer.objects.all()
    context = {'transfers': transfers}
    return render(request, 'equipment/transfer_report.html', context)

def writeoff_report(request):
    writeoffs = EquipmentWriteOff.objects.all()
    context = {'writeoffs': writeoffs}
    return render(request, 'equipment/writeoff_report.html', context)

def equipment_documents_view(request, equipment_id):
    equipment = get_object_or_404(EquipmentInventory, id=equipment_id)
    receipts = EquipmentReceipt.objects.filter(item=equipment.item, company=equipment.company)
    transfers = EquipmentTransfer.objects.filter(inventory=equipment)
    writeoffs = EquipmentWriteOff.objects.filter(inventory=equipment)
    context = {
        'equipment': equipment,
        'receipts': receipts,
        'transfers': transfers,
        'writeoffs': writeoffs,
    }
    return render(request, 'equipment/equipment_documents.html', context)


@csrf_exempt
def load_departments(request):
    company_id = request.GET.get('company_id')
    departments = Department.objects.filter(company_id=company_id).all()
    return JsonResponse(list(departments.values('id', 'name')), safe=False)

@csrf_exempt
def load_employees(request):
    department_id = request.GET.get('department_id')
    employees = Worker.objects.filter(department_id=department_id).all()
    return JsonResponse(list(employees.values('id', 'user__first_name', 'user__last_name')), safe=False)