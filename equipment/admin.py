from django.contrib import admin
from .models import EquipmentInventory, EquipmentReceipt, EquipmentTransfer, EquipmentWriteOff

@admin.register(EquipmentInventory)
class EquipmentInventoryAdmin(admin.ModelAdmin):
    list_display = ['item', 'company', 'department', 'employee_display', 'status']

    def employee_display(self, obj):
        return obj.employee.user.username if obj.employee else 'No employee assigned'
    employee_display.short_description = 'Assigned to'

@admin.register(EquipmentReceipt)
class EquipmentReceiptAdmin(admin.ModelAdmin):
    list_display = ['item', 'company', 'department', 'employee', 'date']

@admin.register(EquipmentTransfer)
class EquipmentTransferAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'to_department', 'to_employee', 'date']

@admin.register(EquipmentWriteOff)
class EquipmentWriteOffAdmin(admin.ModelAdmin):
    list_display = ['inventory', 'reason', 'date']
