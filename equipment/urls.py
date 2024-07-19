# equipment/urls.py
from django.urls import path
from .views import (
    equipment_inventory_list, add_equipment_inventory,
    equipment_receipt_list, add_equipment_receipt,
    equipment_transfer_list, add_equipment_transfer,
    equipment_writeoff_list, add_equipment_writeoff,
    equipment_documents, inventory_report, receipt_report,
    transfer_report, writeoff_report, equipment_documents_view,
    load_departments, load_employees
)

urlpatterns = [
    path('inventory/', equipment_inventory_list, name='equipment_inventory_list'),
    path('inventory/add/', add_equipment_inventory, name='add_equipment_inventory'),
    path('receipt/', equipment_receipt_list, name='equipment_receipt_list'),
    path('receipt/add/', add_equipment_receipt, name='add_equipment_receipt'),
    path('transfer/', equipment_transfer_list, name='equipment_transfer_list'),
    path('transfer/add/', add_equipment_transfer, name='add_equipment_transfer'),
    path('writeoff/', equipment_writeoff_list, name='equipment_writeoff_list'),
    path('writeoff/add/', add_equipment_writeoff, name='add_equipment_writeoff'),
    path('documents/<int:equipment_id>/', equipment_documents, name='equipment_documents'),
    path('report/inventory/', inventory_report, name='inventory_report'),
    path('report/receipt/', receipt_report, name='receipt_report'),
    path('report/transfer/', transfer_report, name='transfer_report'),
    path('report/writeoff/', writeoff_report, name='writeoff_report'),
    path('documents/<int:equipment_id>/', equipment_documents_view, name='equipment_documents'),
    path('load-departments/', load_departments, name='load_departments'),
    path('load-employees/', load_employees, name='load_employees'),
]
